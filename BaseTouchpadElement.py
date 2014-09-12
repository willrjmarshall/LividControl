from BaseButtonElement import BaseButtonElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from Skins import touchpad_skin
from Map import * 


class BaseTouchpadElement(BaseButtonElement):
  """ Variant for touch buttons """
  default_states = {True: 'On',
   False: 'Off'}

  def __init__(self, identifier, skin = touchpad_skin(), *a, **k):
    super(BaseButtonElement, self).__init__(True, MIDI_NOTE_TYPE, 
        CHANNEL, identifier, is_rgb = True, skin = skin,
        *a, **k)
