from _Framework.Skin import Skin
from Push.Colors import Pulse, Blink 

from Colors import Rgb

class Colors:
    class Button:
      On = Rgb.MAGENTA
      Off = Rgb.BLACK
      Pressed = Rgb.GREEN
    class Button2:
      On = Rgb.GREEN
      Off = Rgb.BLACK
      Pressed = Rgb.YELLOW
    class Touchpad:
      On = Rgb.GREEN
      Off = Rgb.BLACK
      Pressed = Rgb.YELLOW
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

def pad_skin():
  return Skin(Colors)

def button_skin_1():
  return Skin(Colors.Button)

def button_skin_2():
  return Skin(Colors.Button2)

def touchpad_skin():
  return Skin(Colors.Touchpad)
