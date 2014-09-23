from _Framework.MixerComponent import MixerComponent

from BaseChannelStripComponent import BaseChannelStripComponent
from BaseMessenger import BaseMessenger
from Utilities import set_channel

class BaseMixerComponent(MixerComponent, BaseMessenger):
  def _create_strip(self):
    return BaseChannelStripComponent()

  def set_user_controls(self, controls):
    self._user_controls = controls
    self._update_user_controls

  def _update_user_controls(self):
      set_channel(self._user_controls, 1)


