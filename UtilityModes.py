from _Framework.ModesComponent import ModesComponent, LazyComponentMode
from _Framework.SubjectSlot import subject_slot
from _Framework.Layer import Layer
from BaseTransportComponent import BaseTransportComponent
from BaseMessenger import BaseMessenger
from Colors import Rgb
from Skins import mode_colors

class UtilityModes(ModesComponent, BaseMessenger):
  """ Switches out the utility buttons. 
  Some modes are blank: this means control is delegated to a PadMode or FaderMode """

  def __init__(self, control_surface, buttons = []):
    self.control_surface = control_surface
    super(UtilityModes, self).__init__()
    self.add_mode("session", LazyComponentMode(self._transport))
    self.add_mode("note", [])
    self.add_mode("device", [])
    self.add_mode("sequence", [])
    self._on_selected_mode.subject = self
    self.selected_mode = "session"

  def _transport(self):
    return BaseTransportComponent(is_enabled = False,
        layer = Layer(tempo_decrease_button = self.control_surface.utility_buttons[4], tempo_increase_button = self.control_surface.utility_buttons[5]))

  @subject_slot('selected_mode')
  def _on_selected_mode(self, mode):
    """ Light the additional LED on the selected mode
    and change the fader colors """
    mode_index = self._mode_list.index(mode)
    for led in self.control_surface.utility_button_lights:
      led.turn_off()
    for index, fader in enumerate(self.control_surface.fader_elements):
      fader.set_theme(mode_colors[mode_index] , "fill")
    self.control_surface.utility_button_lights[mode_index].turn_on()
