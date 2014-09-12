from BaseButtonElement import BaseButtonElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from Skins import pad_skin, Colors
from Map import CHANNEL 

class BasePadElement(BaseButtonElement):
  """ Custom self-initing pad element for Livid Base """

  default_states = {True: 'Session.ClipStarted',
   False: 'Session.StoppedClip'}
  num_delayed_messages = 2
  send_depends_on_forwarding = False

  def __init__(self, identifier, *a, **k):
    super(BaseButtonElement, self).__init__(True, MIDI_NOTE_TYPE, 
        CHANNEL, identifier, skin = pad_skin(), is_rgb = True,
        *a, **k)
