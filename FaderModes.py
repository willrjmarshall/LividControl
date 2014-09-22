from _Framework.ModesComponent import AddLayerMode, ModesComponent, LazyComponentMode
from _Framework.MixerComponent import MixerComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ComboElement import ComboElement
from _Framework.DeviceComponent import DeviceComponent
from _Framework.Layer import Layer
from _APC.DetailViewCntrlComponent import DetailViewCntrlComponent
from BaseTouchpadElement import BaseTouchpadElement
from BaseMessenger import BaseMessenger
from Map import *

class FaderModes(ModesComponent, BaseMessenger):
  """ Switches between different fader modes """
  def __init__(self):
    super(FaderModes, self).__init__()
    self._init_mixer_layer()
    self.add_mode("mixer", [(self.control_surface.mixer, self._session_volume_layer)])
    self.add_mode("mixer2", [(self.control_surface.mixer, self._session_volume_layer)])
    self.add_mode("device", [(self.control_surface.mixer, self._session_select_layer), 
      LazyComponentMode(self._device_control), LazyComponentMode(self._detail_control)])
    self.add_mode("mixer3", [(self.control_surface.mixer, self._session_volume_layer)])
    self.selected_mode = 'mixer'

  def _device_control(self):
    self._device_component = DeviceComponent(name = 'Device_Component',
        is_enabled = False,
        layer = Layer(parameter_controls = self.control_surface._faders))
    self.control_surface.set_device_component(self._device_component)
    self.control_surface._device_selection_follows_track_selection = True
    return self._device_component

  def _detail_control(self):
    self._detail_view_toggler = DetailViewCntrlComponent(is_enabled = False,
        layer= Layer(device_nav_left_button = self.control_surface.utility_buttons[4], 
          device_nav_right_button = self.control_surface.utility_buttons[5]))
    self._detail_view_toggler.device_nav_right_button._set_color('Alt')
    self._detail_view_toggler.device_nav_left_button._set_color('Alt')
    return self._detail_view_toggler
      
  def _init_mixer_layer(self):
    self._session_volume_layer = Layer(volume_controls = self.control_surface._faders, track_select_buttons = self.control_surface.selects, 
      shift_button = self.control_surface._session_button, 
      prehear_volume_control = self._with_shift(self.control_surface._master_fader))
    self._session_select_layer = Layer(track_select_buttons = self.control_surface.selects)

  def _with_shift(self, button):
    return ComboElement(button, modifiers=[self.control_surface._session_button])

