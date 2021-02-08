from japrp.streamer import UrlStreamer

def test_play():
    import time
    URL = "http://bob.hoerradar.de/radiobob-hartesaite-mp3-hq?sABC=6020sp0s%230%23r731s0685son37qn82q119rrn30n0ss5%23zrqvncynlre&=&amsparams=playerid:mediaplayer;skey:1612774415"  # BBC
    streamer = UrlStreamer(URL)
    streamer.play()
    # time.sleep(10)
    # del streamer
