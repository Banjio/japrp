from japrp.audio_backends import audio_backend_vlc, audio_backend_pyqt5
from time import sleep
_SLEEP_TIMER = 15
backend = audio_backend_vlc.VlcBackend()
backend_pyqt5 = audio_backend_pyqt5.QtMediaPlayerWrapper()


def test_vcl_m3u():
    url = "http://mp3-live.swr3.de/swr3_m.m3u"
    backend.set_media(url, media_type="m3u")
    backend.media_player.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend.media_player.is_playing() == 1
    except AssertionError:
        raise
    finally:
        backend.media_player.stop()

def test_vcl_mp3():
    url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    #url = "'http://swr-edge-3025-dus-ts-cdn.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3?_art=dj0yJmlwPTg3LjE0OC4xMzYuMTU1JmlkPWljc2N4bC1ienNlMzJsbGImdD0xNjEzMDc1NjE5JnM9Nzg2NmYyOWMjZDlkMzZjNjYxY2QxNjA2MGM1MTc3ZDFiNjNhMGEwZGE'"
    backend.set_media(url, media_type="mp3")
    backend.media_player.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend.media_player.is_playing() == 1
    except AssertionError:
        raise
    finally:
        backend.media_player.stop()

def test_vlc_acc():
    url = "https://swr-swr3-live.cast.addradio.de/swr/swr3/live/aac/96/stream.aac"
    backend.set_media(url, media_type="acc")
    backend.media_player.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend.media_player.is_playing() == 1
    except AssertionError:
        raise
    finally:
        backend.media_player.stop()

def test_vlc_m3u8():
    url = "https://pehlanashahdlive-lh.akamaihd.net/i/PehlaNashaHDLive_1@335229/master.m3u8"
    backend.set_media(url, media_type= 'infer')
    backend.media_player.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend.media_player.is_playing() == 1
    except AssertionError:
        raise
    finally:
        backend.media_player.stop()


def test_vlc_else():
    #url = "http://streams.radiobob.de/bob-hartesaite/mp3-192/mediaplayer"
    url = 'http://streams.radiobob.de/bob-christmas/aac-64/mediaplayer/'
    backend.set_media(url, media_type=None)
    backend.media_player.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend.media_player.is_playing() == 1
    except AssertionError:
        raise
    finally:
        backend.media_player.stop()

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

def test_pyqt5_mediaplayer_else():
    url = 'http://streams.radiobob.de/bob-christmas/aac-64/mediaplayer/'
    backend_pyqt5.set_media(url, media_type=None)
    backend_pyqt5.media_player.play()
    sleep(_SLEEP_TIMER)
    backend_pyqt5.media_player.stop()