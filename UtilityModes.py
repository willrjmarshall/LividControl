from _Framework.ModesComponent import ModesComponent, LazyComponentMode
from _Framework.Layer import Layer
from BaseTransportComponent import BaseTransportComponent

class UtilityModes(ModesComponent):
  """ Switches out the utility buttons. 
  Some modes are blank: this means control is delegated to a PadMode or FaderMode """

  def __init__(self, control_surface, buttons = []):
    self.control_surface = control_surface
    super(UtilityModes, self).__init__()
    self.add_mode("session", LazyComponentMode(self._transport))
    self.add_mode("note", [])
    self.add_mode("device", [])
    self.add_mode("sequence", [])
    self.selected_mode = "session"

  def _transport(self):
    return BaseTransportComponent(is_enabled = False,
        layer = Layer(tempo_decrease_button = self.control_surface.utility_buttons[4], tempo_increase_button = self.control_surface.utility_buttons[5]))
