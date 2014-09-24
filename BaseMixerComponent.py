from _Framework.MixerComponent import MixerComponent

from BaseChannelStripComponent import BaseChannelStripComponent
from BaseMessenger import BaseMessenger
from Utilities import set_channel

class BaseMixerComponent(MixerComponent, BaseMessenger):
  def _create_strip(self):
    return BaseChannelStripComponent()

  def set_prehear_volume_control(self, control):
    set_channel([control], 0)
    super(BaseMixerComponent, self).set_prehear_volume_control(control)
