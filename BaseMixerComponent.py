from _Framework.MixerComponent import MixerComponent

from BaseChannelStripComponent import BaseChannelStripComponent
from BaseMessenger import BaseMessenger
from Utilities import set_channel

class BaseMixerComponent(MixerComponent, BaseMessenger):
  def _create_strip(self):
    return BaseChannelStripComponent()

  def set_volume_controls(self, controls):
    super(BaseMixerComponent, self).set_volume_controls(controls)
    self._volume_controls = controls
    self._update_volume_controls()

  #def update(self):
    #super(BaseMixerComponent, self).update()

  def _update_volume_controls(self):
      set_channel(self._volume_controls, 1)

