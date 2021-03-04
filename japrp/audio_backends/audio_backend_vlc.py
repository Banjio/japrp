from typing import Union
import vlc
from japrp.audio_backends.audio_backends import AudiostreamBackend
import requests
import struct
import re


class VlcBackend(AudiostreamBackend):
    """
    Implement an audio stream backend using the pyton-vlc bindings.
    """

    def __init__(self, cmd: str = ""):
        """
        Initiate an instance of vlc player with no video output and a standard media_player.

        :param cmd: additional command line options, passed to vlc.Instance(), for example -v for a verbose output
        """
        super(VlcBackend, self).__init__()
        self._instance = vlc.Instance("--vout none " + cmd)
        self.media_player = self._instance.media_player_new()
        self._is_playlist = False


    def set_media(self, url: str, media_type: Union[str, None] = 'infer'):
        """
        Bind an audio stream webadress to the vlc media player instance. Depending on the type of the stream another
        player type has to be used.

        :param url: webadress of an audio stream
        :param media_type: type of the stream, e.g. mp3 or m3u
        """
        self._check_url(url)
        self.set_url(url)
        if media_type == 'infer':
            media_type = self._infer_url_type(url)
        if media_type in self._PLAYLIST_FORMATS:
            self.media_player = self._instance.media_list_player_new()
            self.media = self._instance.media_list_new([url])
            self.media_player.set_media_list(self.media)
            self._is_playlist = True
        else:
            self.media_player = self._instance.media_player_new()
            self.media = self._instance.media_new(url)
            self.media.parse()
            self.media_player.set_media(self.media)
            self._is_playlist = False

    def play(self):
        """
        Implement the play method used in vlc.player.play() with additional error handling
        """
        if self.media is None:
            raise ValueError("Media must be set or no media can be played")
        if self.media_player.play() == -1:
            ##TODO: maybe raising an error here is not optimal, compared to doing nothing
            raise TypeError("Error playing stream")
        else:
            self.media_player.play()
            self._is_playing = True

    def pause(self):
        """
        Implement the pause method used in vlc.player.pause()
        """
        if self._is_playing:
            self.media_player.pause()
            self._is_playing = False

    def stop(self):
        self.media = None
        self.media_player.stop()
        self._is_playing = False

    def set_volume(self, value: int):
        if self._is_playlist:
            self.media_player.get_media_player().audio_set_volume(value)
        else:
            self.media_player.audio_set_volume(value)

    def get_volume(self) -> int:
        if self._is_playlist:
            return self.media_player.get_media_player().audio_get_volume()
        else:
            return self.media_player.audio_get_volume()

