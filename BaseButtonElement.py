from _Framework.InputControlElement import MIDI_NOTE_TYPE
from Push.ConfigurableButtonElement import ConfigurableButtonElement
from _Framework.Skin import Skin

from Skins import make_pad_skin, Colors
from Colors import Rgb

class BaseButtonElement(ConfigurableButtonElement):
  """ Custom self-initing button element for Livid Base """

  default_states = {True: 'Session.ClipStarted',
   False: 'Session.StoppedClip'}
  num_delayed_messages = 2
  send_depends_on_forwarding = False

  def __init__(self, channel, identifier, *a, **k):
    super(BaseButtonElement, self).__init__(True, MIDI_NOTE_TYPE, 
        channel, identifier, skin = make_pad_skin(), is_rgb = True,
        *a, **k)
