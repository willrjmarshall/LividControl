from _Framework.Skin import Skin
from Push.Colors import Pulse, Blink 

from Colors import Rgb

class Colors:
    On = Rgb.GREEN
    Off = Rgb.BLACK

    class Button:
      On = Rgb.MAGENTA
      Off = Rgb.BLACK
      Pressed = Rgb.GREEN
      Alt = Rgb.YELLOW

    class Button2:
      On = Rgb.GREEN
      Off = Rgb.BLACK
      Pressed = Rgb.YELLOW
    class Touchpad:
      On = Rgb.GREEN
      Off = Rgb.BLACK
      Pressed = Rgb.YELLOW

    class MixerButton:
      Solo = Rgb.CYAN
      Mute = Rgb.GREEN
      Arm = Rgb.RED

    class DrumGroup:
      PadSelected = Rgb.WHITE
      PadSelectedNotSoloed = Rgb.CYAN
      PadFilled = Rgb.YELLOW
      PadEmpty = Rgb.BLACK
      PadMuted = Rgb.RED
      PadMutedSelected = Rgb.BLACK
      PadSoloed = Rgb.BLUE
      PadSoloedSelected = Rgb.BLUE
      PadInvisible = Rgb.BLACK
      PadAction = Rgb.GREEN

    class LoopSelector:
      Playhead = Rgb.GREEN
      PlayheadRecord = Rgb.RED
      SelectedPage = Rgb.YELLOW
      InsideLoopStartBar = Rgb.WHITE
      InsideLoop = Rgb.WHITE
      OutsideLoop = Rgb.BLACK

    class NoteEditor:
      StepSelected = Rgb.WHITE
      StepEmpty = Rgb.BLACK
      StepEmptyBase = Rgb.CYAN
      StepEmptyScale = Rgb.YELLOW
      StepDisabled = Rgb.BLACK
      Playhead = Rgb.GREEN
      PlayheadRecord = Rgb.RED
      QuantizationSelected = Rgb.GREEN
      QuantizationUnselected = Rgb.YELLOW
      NoteBase = Rgb.WHITE
      NoteScale = Rgb.BLUE
      NoteNotScale = Rgb.MAGENTA
      NoteInvalid = Rgb.RED

      class Step:
        Low = Rgb.WHITE
        High = Rgb.CYAN
        Full = Rgb.BLUE
        Muted = Rgb.YELLOW

      class StepEditing:
        Low = Rgb.GREEN
        High = Rgb.YELLOW
        Full = Rgb.RED
        Muted = Rgb.WHITE

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
      NoteBase = Rgb.BLUE
      NoteScale = Rgb.WHITE
      NoteNotScale = Rgb.BLACK
      NoteInvalid = Rgb.BLACK
      Feedback = Rgb.GREEN
      FeedbackRecord = Rgb.RED
      NoteAction = Rgb.YELLOW

def pad_skin():
  return Skin(Colors)

def button_skin(index):
  class Button:
    On = mode_colors[index]
    Off = mode_colors[index]
  return Skin(Button)

def white_button_skin():
  class Button:
    On = Rgb.WHITE
    Off = Rgb.BLACK
  return Skin(Button)

mode_colors = [
  Rgb.MAGENTA,
  Rgb.BLUE,
  Rgb.YELLOW,
  Rgb.RED,
  Rgb.CYAN,
  Rgb.CYAN,
  Rgb.GREEN,
  Rgb.GREEN
]
