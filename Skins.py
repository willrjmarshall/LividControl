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

    class Zooming:
        Selected = Rgb.MAGENTA
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK

    class Instrument:
      NoteBase = Rgb.CYAN
      NoteScale = Rgb.WHITE
      NoteNotScale = Rgb.BLACK
      NoteInvalid = Rgb.BLACK
      Feedback = Rgb.GREEN
      FeedbackRecord = Rgb.RED
      NoteAction = Rgb.RED

def make_pad_skin():
  return Skin(Colors)

