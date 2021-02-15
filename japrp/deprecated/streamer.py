import sys
import logging
import queue
import ffmpeg
import sounddevice as sd

module_logger = logging.getLogger(__name__)

class UrlStreamer(object):

    def __init__(self, url, device=None, blocksize=1024, buffersize=20):
        self.url = url
        self.device = device
        self.blocksize = blocksize
        self.buffersize = buffersize

    def play(self):
        q = queue.Queue(self.buffersize)
        module_logger.debug("Getting stream information ...")
        try:
            info = ffmpeg.probe(self.url)
        except ffmpeg.Error as e:
            sys.stderr.buffer.write(e.stderr)
            raise e
        streams = info.get('streams', [])
        if len(streams) != 1:
            raise ValueError("There must be exactly one stream available.")

        stream = streams[0]
        if stream.get('codec_type') != 'audio':
            raise ValueError('The stream must be an audio stream')

        channels = stream['channels']
        samplerate = float(stream['sample_rate'])

        def callback(outdata, frames, time, status):
            assert frames == self.blocksize
            if status.output_underflow:
                print('Output underflow: increase blocksize?', file=sys.stderr)
                raise sd.CallbackAbort
            assert not status
            try:
                data = q.get_nowait()
            except queue.Empty as e:
                print('Buffer is empty: increase buffersize?', file=sys.stderr)
                raise sd.CallbackAbort from e
            assert len(data) == len(outdata)
            outdata[:] = data

        try:
            print('Opening stream ...')
            process = ffmpeg.input(
                self.url
            ).output(
                'pipe:',
                format='f32le',
                acodec='pcm_f32le',
                ac=channels,
                ar=samplerate,
                loglevel='quiet',
            ).run_async(pipe_stdout=True)
            stream = sd.RawOutputStream(
                samplerate=samplerate, blocksize=self.blocksize,
                device=self.device, channels=channels, dtype='float32',
                callback=callback)
            read_size = self.blocksize * channels * stream.samplesize
            print('Buffering ...')
            for _ in range(self.buffersize):
                q.put_nowait(process.stdout.read(read_size))
            print('Starting Playback ...')
            with stream:
                timeout = self.blocksize * self.buffersize / samplerate
                while True:
                    q.put(process.stdout.read(read_size), timeout=timeout)
        except KeyboardInterrupt:
            sys.exit('\nInterrupted by user')
        except queue.Full:
            # A timeout occurred, i.e. there was an error in the callback
            sys.exit(1)
        except Exception as e:
            sys.exit(type(e).__name__ + ': ' + str(e))

