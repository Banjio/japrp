from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl
from japrp.audio_backends.audio_backends import AudiostreamBackend


class QtMediaPlayerWrapper(AudiostreamBackend):

    def __init__(self):
        """
        Initiate an instance of pyqt5.MediaPlayer().
        """
        super(QtMediaPlayerWrapper, self).__init__()
        self.media_player = QMediaPlayer()
        self._is_playing = False

    def set_media(self, url, media_type: str = 'infer'):
        """
        Bind an audio stream webadress to the pyqt5 media player instance. Currently no streams of playlist formats
        (m3u, psu, ...) are supported

        :param url: webadress of an audio stream
        :param media_type: type of the stream, e.g. mp3 or m3u or infer to infer the type
        """
        self._check_url(url)
        self.set_url(url)
        if media_type == 'infer':
            media_type = self._infer_url_type(url)
        if media_type in self._PLAYLIST_FORMATS:
            # A possible solution for this problem is here: https://github.com/ivareske/QtInternetRadio
            self.media = QMediaPlaylist()
            self.media.addMedia(QMediaContent(QUrl(url)))
            self.media.setCurrentIndex(1)
            self.media_player.setPlaylist(self.media)
            raise NotImplementedError(
                "Currently QtMediaPlayerWrapper does not support m3u streams natively. Use the vlc backend for this kind of streams")
        elif media_type not in ('mp3', 'acc'):
            raise NotImplementedError(
                "Currently QtMediaPlayerWrapper does not support streams other than mp3 natively, but %s was supplied."
                ". Use the vlc backend for this kind of streams" %media_type)
        else:
            self.media = QMediaContent(QUrl(url))
            self.media_player.setMedia(self.media)

    def play(self):
        """
        call pyqt5.MediaPlayer().play()
        """
        if self.media is None:
            raise ValueError("Media must be set or no media can be played")
        else:
            self.media_player.play()
            self._is_playing = True

    def pause(self):
        """
        call pyqt5.MediaPlayer().pause()
        """
        self.media_player.pause()
        self._is_playing = False

    def stop(self):
        """
        call pyqt5.MediaPlayer().stop()
        """
        self.media = None
        self.media_player.stop()
        self._is_playing = False

    def set_volume(self, value: int):
        """
        call pyqt5.MediaPlayer().setVolume(value)
        """
        self.media_player.setVolume(value)

    def get_volume(self) -> int:
        return self.media_player.volume()

    def get_is_playing(self):
        return self._is_playing
