import Live
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE

ABSOLUTE_MAP_MODE = Live.MidiMap.MapMode.absolute

class BaseFaderElement(EncoderElement):
  """ Custom fader class for Livid Base faders """

  def __init__(self, cc, channel = 0):
    super(BaseFaderElement, self).__init__(MIDI_CC_TYPE, channel, cc, ABSOLUTE_MAP_MODE)
    self._mapping_feedback_delay = -1
  

  # TODO add color-settings here
