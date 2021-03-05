from japrp.audio_backends import audio_backend_vlc, audio_backend_pyqt5, audio_backends
from time import sleep
import pytest
_SLEEP_TIMER = 15
backend = audio_backend_vlc.VlcBackend()
backend_pyqt5 = audio_backend_pyqt5.QtMediaPlayerWrapper()
backend_abstract = audio_backends.AudiostreamBackend()



def test_pyqt5_mediaplayer_mp3():
    url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    backend_pyqt5.set_media(url, media_type="mp3")
    backend_pyqt5.media_player.play()
    sleep(_SLEEP_TIMER)
    backend_pyqt5.media_player.stop()

def test_pyqt5_mediaplayer_acc():
    url = "https://swr-swr3-live.cast.addradio.de/swr/swr3/live/aac/96/stream.aac"
    backend_pyqt5.set_media(url, media_type="acc")
    backend_pyqt5.media_player.play()
    sleep(_SLEEP_TIMER)
    backend_pyqt5.media_player.stop()


def test_pyqt5_mediaplayer_m3u():
    url = "https://pehlanashahdlive-lh.akamaihd.net/i/PehlaNashaHDLive_1@335229/master.m3u8"
    with pytest.raises(NotImplementedError):
        backend_pyqt5.set_media(url, media_type='infer')
        backend_pyqt5.media_player.play()
        sleep(_SLEEP_TIMER)
        backend_pyqt5.media_player.stop()

def test_pyqt5_mediaplayer_else():
    url = 'http://streams.radiobob.de/bob-christmas/aac-64/mediaplayer/'
    backend_pyqt5.set_media(url, media_type=None)
    backend_pyqt5.media_player.play()
    sleep(_SLEEP_TIMER)
    backend_pyqt5.media_player.stop()


def test_qt5_set_volume():
    backend_pyqt5.set_volume(2)
    assert backend_pyqt5.get_volume() == 2

def test_backend_get_meta():
    url = 'http://streams.radiobob.de/bob-christmas/aac-64/mediaplayer/'
    #url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    title = backend_abstract.get_meta_data_icy(url)
    print(title)

