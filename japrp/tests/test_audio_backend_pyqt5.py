from japrp.audio_backends import audio_backend_pyqt5
from time import sleep
import pytest
_SLEEP_TIMER = 15
backend_pyqt5 = audio_backend_pyqt5.QtMediaPlayerWrapper()
backend_pyqt5.set_volume(2)

def helper_play_func(url, media_type, stop_player=True):
    backend_pyqt5.set_media(url, media_type=media_type)
    backend_pyqt5.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend_pyqt5.get_is_playing()
    except AssertionError:
        raise
    finally:
        if stop_player:
            backend_pyqt5.stop()
        else:
            backend_pyqt5.pause()


def test_pyqt5_mediaplayer_mp3():
    url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    helper_play_func(url, "mp3")


def test_pyqt5_mediaplayer_acc():
    url = "https://swr-swr3-live.cast.addradio.de/swr/swr3/live/aac/96/stream.aac"
    helper_play_func(url, "acc")


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