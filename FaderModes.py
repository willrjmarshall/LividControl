from _Framework.ModesComponent import ModesComponent, LazyComponentMode
from _Framework.MixerComponent import MixerComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ComboElement import ComboElement
from _Framework.DeviceComponent import DeviceComponent
from _Framework.Layer import Layer
from _APC.DetailViewCntrlComponent import DetailViewCntrlComponent
from BaseFaderElement import BaseFaderElement
from BaseTouchpadElement import BaseTouchpadElement
from Map import *

class FaderModes(ModesComponent):
  """ Switches between different fader modes """
  def __init__(self, control_surface):
    super(FaderModes, self).__init__()
    self.control_surface = control_surface
    self._init_faders()
    self._init_selects()
    self._init_mixer()
    self.add_mode("mixer", [(self._mixer, self._session_volume_layer)])
    self.add_mode("mixer2", [(self._mixer, self._session_volume_layer)])
    self.add_mode("device", [(self._mixer, self._session_select_layer), LazyComponentMode(self._device_control), LazyComponentMode(self._detail_control)])
    self.add_mode("mixer3", [(self._mixer, self._session_volume_layer)])
    self.selected_mode = 'mixer'

  def _init_faders(self):
    self._faders = ButtonMatrixElement(rows = [[BaseFaderElement(fader) for fader in BASE_TOUCHSTRIPS]])

  def _device_control(self):
    self._device_component = DeviceComponent(name = 'Device_Component',
        is_enabled = False,
        layer = Layer(parameter_controls = self._faders))
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

  def _init_selects(self):
    self._selects = ButtonMatrixElement(rows = [[BaseTouchpadElement(pad) for pad in BASE_TOUCHPADS]])
      
  def _init_mixer(self):
    self._mixer = MixerComponent(len(BASE_TOUCHSTRIPS), auto_name = True, is_enabled = True)
    self._session_volume_layer = Layer(volume_controls = self._faders, track_select_buttons = self._selects, 
      shift_button = self.control_surface._session_button, 
      prehear_volume_control = self._with_shift(self.control_surface._master_fader))
    self._session_select_layer = Layer(track_select_buttons = self._selects)

    # TODO change master volume fader color here
    self._mixer.master_strip().layer = Layer(volume_control=self.control_surface._master_fader)

  def _with_shift(self, button):
    return ComboElement(button, modifiers=[self.control_surface._session_button])

