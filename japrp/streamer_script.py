import sys
sys.path.append("../")
from japrp.streamer import UrlStreamer
#URL = "http://bob.hoerradar.de/radiobob-hartesaite-mp3-hq?sABC=6020sp0s%230%23r731s0685son37qn82q119rrn30n0ss5%23zrqvncynlre&=&amsparams=playerid:mediaplayer;skey:1612774415"  # BBC
#URL = 'http://s5-webradio.rockantenne.de/rockantenne'
URL = "http://mp3-live.swr3.de/swr3_m.m3u"

stream = UrlStreamer(URL)
stream.play()
