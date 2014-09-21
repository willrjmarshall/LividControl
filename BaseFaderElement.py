import Live
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE

from Colors import Rgb
from Map import CHANNEL_16_CC
from BaseMessenger import BaseMessenger
ABSOLUTE_MAP_MODE = Live.MidiMap.MapMode.absolute

class BaseFaderElement(EncoderElement):
  """ Custom fader class for Livid Base faders """

  def __init__(self, cc, channel = 0):
    super(BaseFaderElement, self).__init__(MIDI_CC_TYPE, channel, cc, ABSOLUTE_MAP_MODE)
    self._mapping_feedback_delay = -1
  
  def set_theme(self, color, style):
    config_cc = self._msg_identifier + 9
    config_value = FADER_STYLE[color][style] 
    self._send_midi(tuple([CHANNEL_16_CC, config_cc, config_value]))

FADER_STYLE = {
  Rgb.RED : {
    "walk" :    68,
    "fill" :    69,
    "eq" :      70,
    "spread" :  71},
  Rgb.YELLOW : {
    "walk" :    76,
    "fill" :    77,
    "eq" :      78,
    "spread" :  79},
  Rgb.GREEN : {
    "walk" :    72,
    "fill" :    73,
    "eq" :      74,
    "spread" :  75},
  Rgb.CYAN : {
    "walk" :    88,
    "fill" :    89,
    "eq" :      90,
    "spread" :  91},
  Rgb.BLUE : {
    "walk" :    80,
    "fill" :    81,
    "eq" :      82,
    "spread" :  83},
  Rgb.MAGENTA : {
    "walk" :    84,
    "fill" :    85,
    "eq" :      86,
    "spread" :  87},
  Rgb.WHITE : {
    "walk" :    92,
    "fill" :    93,
    "eq" :      94,
    "spread" :  95},
}
