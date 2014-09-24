from _Framework.ModesComponent import AddLayerMode, ModesComponent, LazyComponentMode
from _Framework.MixerComponent import MixerComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ComboElement import ComboElement
from _Framework.Layer import Layer
from _APC.DetailViewCntrlComponent import DetailViewCntrlComponent
from BaseTouchpadElement import BaseTouchpadElement
from BaseDeviceComponent import BaseDeviceComponent
from BaseMessenger import BaseMessenger
from Map import *

class FaderModes(ModesComponent, BaseMessenger):
  """ Switches between different fader modes """
  def __init__(self):
    super(FaderModes, self).__init__()
    self._init_mixer_layer()
    self.add_mode("session", self._mixer_mode())
    self.add_mode("note", [self._simple_mixer_mode(), self._device_mode()])
    self.add_mode("track", [self._simple_mixer_mode(), self._device_mode(), self._detail_mode()])
    self.add_mode("sequencer", [self._simple_mixer_mode(), self._device_mode()])
    self.selected_mode = 'session'

  def _mixer_mode(self):
    """ Full mixer including volume layer """
    return (self.control_surface.mixer, self._session_volume_layer)
  
  def _simple_mixer_mode(self):
    """ Simplified mixer with just selects """
    return (self.control_surface.mixer, self._session_select_layer)

  def _device_mode(self):
    """ Device control and sundries """
    return LazyComponentMode(self._device_control)

  def _detail_mode(self):
    """ Navigation for device control """
    return LazyComponentMode(self._detail_control)

  def _device_control(self):
    self._device_component = BaseDeviceComponent(name = 'Device_Component',
        is_enabled = False,
        layer = Layer(parameter_controls = self.control_surface._faders))
    self.control_surface.set_device_component(self._device_component)
    self.control_surface._device_selection_follows_track_selection = True
    return self._device_component

  def _detail_control(self):
    toggler = DetailViewCntrlComponent(is_enabled = False,
        layer= Layer(device_nav_left_button = self.control_surface.utility_buttons[4], 
          device_nav_right_button = self.control_surface.utility_buttons[5]))
    toggler.device_nav_right_button._set_color('Alt')
    toggler.device_nav_left_button._set_color('Alt')
    return toggler 
      
  def _init_mixer_layer(self):
    self._session_volume_layer = Layer(
        volume_controls = self.control_surface._faders, 
        track_select_buttons = self.control_surface.selects, 
      shift_button = self.control_surface._session_button, 
      prehear_volume_control = self._with_shift(self.control_surface._master_fader))
    self._session_select_layer = Layer(track_select_buttons = self.control_surface.selects)

  def _with_shift(self, button):
    return ComboElement(button, modifiers=[self.control_surface._session_button])

