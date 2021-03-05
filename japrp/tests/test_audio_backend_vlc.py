from japrp.audio_backends import audio_backend_vlc
from time import sleep
import vlc
import pytest
_SLEEP_TIMER = 15
backend_vlc = audio_backend_vlc.VlcBackend()


def helper_play_func(url, media_type, stop_player=True):
    backend_vlc.set_media(url, media_type=media_type)
    backend_vlc.media_player.play()
    sleep(_SLEEP_TIMER)
    try:
        assert backend_vlc.media_player.is_playing() == 1
    except AssertionError:
        raise
    finally:
        if stop_player:
            backend_vlc.stop()
        else:
            backend_vlc.pause()

def test_vlc_spawn_player():
    player = backend_vlc.spawn_player()
    assert isinstance(player, vlc.MediaPlayer)


def test_vlc_spawn_playlist_player():
    player = backend_vlc.spawn_playlist_player()
    assert isinstance(player, vlc.MediaListPlayer)


def test_play_vcl_m3u():
    url = "http://mp3-live.swr3.de/swr3_m.m3u"
    helper_play_func(url, "m3u")


def test_play_vcl_mp3():
    url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    helper_play_func(url, "mp3")


def test_play_vlc_acc():
    url = "https://swr-swr3-live.cast.addradio.de/swr/swr3/live/aac/96/stream.aac"
    helper_play_func(url, "acc")


def test_play_vlc_m3u8():
    url = "https://pehlanashahdlive-lh.akamaihd.net/i/PehlaNashaHDLive_1@335229/master.m3u8"
    helper_play_func(url, "m3u8")


def test_play_vlc_else():
    url = 'http://streams.radiobob.de/bob-christmas/aac-64/mediaplayer/'
    helper_play_func(url, None)


def test_vlc_pause():
    url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    helper_play_func(url, "infer", stop_player=False)
    backend_vlc.pause()
    try:
        assert not backend_vlc.get_is_playing() and bool(backend_vlc.media_player.will_play())
    except AssertionError:
        raise
    finally:
        backend_vlc.stop()


def test_vlc_set_volume_media_player():
    backend_vlc.media_player = backend_vlc.spawn_player()
    backend_vlc.set_volume(1)
    assert backend_vlc.get_volume() == 1


def test_vlc_set_volume_playlist_player():
    backend_vlc.media_player = backend_vlc.spawn_playlist_player()
    backend_vlc._is_playlist = True
    backend_vlc.set_volume(1)
    assert backend_vlc.get_volume() == 1


def test_vlc_stop():
    backend_vlc.media_player = backend_vlc.spawn_player()
    backend_vlc._is_playlist = False
    backend_vlc.media_player.stop()
    assert not (backend_vlc.media_player.will_play())

def test_vlc_set_media():
    url = "http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3"
    pass

