from japrp.audio_backends import audio_backend_vlc, audio_backend_pyqt5, audio_backends
from time import sleep
import pytest
_SLEEP_TIMER = 15
backend_pyqt5 = audio_backend_pyqt5.QtMediaPlayerWrapper()
backend_abstract = audio_backends.AudiostreamBackend()



def test_backend_get_meta():
    url = 'http://streams.radiobob.de/bob-christmas/aac-64/mediaplayer/'
    #url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    title = backend_abstract.get_meta_data_icy(url)
    print(title)

