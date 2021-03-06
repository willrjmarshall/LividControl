from _Framework.InputControlElement import MIDI_NOTE_TYPE
from Push.ConfigurableButtonElement import ConfigurableButtonElement
from BaseMessenger import BaseMessenger
from _Framework.Skin import Skin
from Skins import button_skin, Colors
from Colors import Rgb
from Map import * 

class BaseButtonElement(ConfigurableButtonElement, BaseMessenger):
  """ Custom self-initing button element for Livid Base """

  default_states = {True: 'On',
   False: 'Off',
   'Enabled': 'On', 'Pressed': 'Pressed'}
  num_delayed_messages = 2
  send_depends_on_forwarding = False

  def __init__(self, identifier, skin = button_skin(0), *a, **k):
    super(BaseButtonElement, self).__init__(True, MIDI_NOTE_TYPE, 
        CHANNEL, identifier, is_rgb = True, skin = skin,
        *a, **k)
