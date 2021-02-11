import logging
from abc import ABC
import requests


class AudiostreamBackend(ABC):
    """
    Abstract base class that is a blueprint for bindings to different libraries that can play audio from a web source,
    because the streaming backend is only intended for audio streaming (i.e. from a webadress), no next or previous
    functions are implemented, as they carry no relevance for streams.
    """
    def __init__(self):
        self._PLAYLIST_FORMATS = {"psu", "m3u", "m3u8"}
        self.media_player = None
        self.media = None

    def play(self):
        """
        Call the play function of the bound backend
        """
        raise NotImplementedError

    def pause(self):
        """
        Call the pause function of the bound backend
        """
        raise NotImplementedError

    def stop(self):
        """
        Call the stop function of the bound backend
        """
        raise NotImplementedError

    def set_media(self, url, media_type: str = None):
        """
        Bind media to backend.

        :param url: url = media that should be bound
        :param media_type: used to specify syntax that must be used for different media formats
        """
        raise NotImplementedError

    @staticmethod
    def _check_url(url: str) -> None:
        """
        Check if a provided url is valid using requests. This should be called everytime before setting a media,
        therefore it must be implemented in the sublass

        :param url: webadress of an audiostream
        """
        try:
            r = requests.get(url, stream=True)
            if r.ok:
                pass
            else:
                raise ValueError(f"Url is not ok {r.status_code}")
        except Exception as e:
            logging.getLogger('failed to get stream: {e}'.format(e=e))
            raise

    @staticmethod
    def _infer_url_type(url: str):
        """
        Can be used to infer the type of a audiostream url (acc, mp3, m3u, ...). It checks if the last element of the url
        is equal to one of the known types of webstreams

        :param url: audiostream url
        """
        ending = url.split(".")[-1]
        res = None
        if ending == "m3u":
            res = "m3u"
        elif ending == "m3u8":
            res = "m3u8"
        elif ending == "psu":
            res = "psu"
        elif ending == "mp3":
            res = "mp3"
        elif ending == "acc":
            res = "acc"
        return res

if __name__ == "__main__":
    import time
    #URL = "http://bob.hoerradar.de/radiobob-hartesaite-mp3-hq?sABC=6020sp0s%230%23r731s0685son37qn82q119rrn30n0ss5%23zrqvncynlre&=&amsparams=playerid:mediaplayer;skey:1612774415"  # BBC
    #URL = 'http://swr-swr3-live.cast.addradio.de/swr/swr3/live/mp3/128/stream.mp3'
    URL = "http://mp3-live.swr3.de/swr3_m.m3u"
    #WRONG_URL = "NO URL"
    #WRONG_URL2 = "http://WRONG_SITE_NOT_EXISTIERING"
    #player = QtMediaPlayerWrapper()
    #player.set_media(URL)
    #player.play()
    #time.sleep(10)
    #player.stop()