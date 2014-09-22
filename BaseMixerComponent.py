from _Framework.MixerComponent import MixerComponent

from BaseChannelStripComponent import BaseChannelStripComponent
from BaseMessenger import BaseMessenger

class BaseMixerComponent(MixerComponent, BaseMessenger):
  def _create_strip(self):
    return BaseChannelStripComponent()
