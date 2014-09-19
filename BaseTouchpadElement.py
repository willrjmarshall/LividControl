from BaseButtonElement import BaseButtonElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from Skins import touchpad_skin
from Map import * 
from MatrixMaps import PAD_FEEDBACK_CHANNEL


class BaseTouchpadElement(BaseButtonElement):
  """ Variant for touch buttons """
  default_states = {True: 'On',
   False: 'Off'}

  def __init__(self, identifier, skin = touchpad_skin(), channel = CHANNEL, *a, **k):
    super(BaseButtonElement, self).__init__(True, MIDI_NOTE_TYPE, 
        channel, identifier, is_rgb = True, skin = skin,
        *a, **k)
