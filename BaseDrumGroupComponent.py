from itertools import imap, ifilter
from _Framework.Util import find_if, first
from Push.DrumGroupComponent import DrumGroupComponent
from MatrixMaps import PAD_FEEDBACK_CHANNEL
from BaseMessenger import BaseMessenger

class BaseDrumGroupComponent(DrumGroupComponent, BaseMessenger):
  """ Customized to use its own feedback channel """

  def _update_control_from_script(self):
    """ Patched to use our own feedback channel """
    takeover_drums = self._takeover_drums or self._selected_pads
    profile = 'default' if takeover_drums else 'drums'
    if self._drum_matrix:
        for button, _ in ifilter(first, self._drum_matrix.iterbuttons()):
            button.set_channel(PAD_FEEDBACK_CHANNEL)
            button.set_enabled(takeover_drums)
            button.sensitivity_profile = profile
