from Push.InstrumentComponent import InstrumentComponent, InstrumentScalesComponent

from _Framework.Util import recursive_map, index_if, forward_property, first
from itertools import ifilter
from functools import partial
from MatrixMaps import NON_FEEDBACK_CHANNEL
from BaseMessenger import BaseMessenger

class BaseInstrumentComponent(InstrumentComponent, BaseMessenger):
  """ Some methods overriden for Base """

  def _setup_instrument_mode(self):
    if self.is_enabled() and self._matrix:
      self._matrix.reset()
      pattern = self._pattern
      
      # This is incorrectly using matrix.width() in Push script.
      # Since it's an 8x8 grid things still work, but our
      # grid is 8x4 so it breaks
      max_j = self._matrix.height() - 1

      for button, (i, j) in ifilter(first, self._matrix.iterbuttons()):
        profile = 'default' if self._takeover_pads else 'instrument'
        button.sensitivity_profile = profile
        note_info = pattern.note(i, max_j - j)
        if note_info.index != None:
          button.set_on_off_values('Instrument.NoteAction', 'Instrument.' + note_info.color)
          button.turn_off()
          button.set_enabled(self._takeover_pads)
          button.set_channel(note_info.channel)
          button.set_identifier(note_info.index)
        else:
          button.set_channel(NON_FEEDBACK_CHANNEL)
          button.set_light('Instrument.' + note_info.color)
          button.set_enabled(True)
    return
