from _Framework.Skin import Skin
from Push.Colors import Pulse, Blink 

from Colors import Rgb

class Colors:
    class Session:
        Scene = Rgb.GREEN 
        SceneTriggered = Rgb.GREEN
        NoScene = Rgb.BLACK
        ClipStopped = Rgb.YELLOW
        ClipStarted = Rgb.GREEN
        ClipRecording = Rgb.RED 
        ClipTriggeredPlay = Blink(Rgb.RED, Rgb.BLACK)
        ClipTriggeredRecord = Rgb.RED 
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED
        StopClip = Rgb.RED
        StopClipTriggered = Rgb.RED
        StoppedClip = Rgb.BLACK

def make_pad_skin():
  return Skin(Colors)

