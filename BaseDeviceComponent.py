from _Framework.DeviceComponent import DeviceComponent
from Utilities import set_channel

class BaseDeviceComponent(DeviceComponent):
  """ Customized to set the parameter controls to channel 0 """

  def update(self):
    self._update_parameter_controls()
    super(BaseDeviceComponent, self).update()

  def _update_parameter_controls(self):
    set_channel(self._parameter_controls, 0)
