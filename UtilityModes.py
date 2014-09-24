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
    self.add_mode("track", [])
    self.add_mode("sequencer", [])
    self._on_selected_mode.subject = self
    self.selected_mode = "session"

  def _transport(self):
    return BaseTransportComponent(is_enabled = False,
        layer = Layer(tempo_decrease_button = self.control_surface.utility_buttons[4], tempo_increase_button = self.control_surface.utility_buttons[5]))

  @subject_slot('selected_mode')
  def _on_selected_mode(self, mode):
    mode_index = self._mode_list.index(mode)
    self._theme_faders(mode_index)
    self._indicate_mode(mode_index)
    self._select_track_if_needed(mode)

  def _select_track_if_needed(self, mode):
    if mode == "note":
      self._select_track_by_name("Instrument")
    elif mode == "sequencer":
      self._select_track_by_name("Drums")

  def _select_track_by_name(self, name):
    for track in self.song().tracks:
      if track.name == name:
        self.song().view.selected_track = track
        break

  def _indicate_mode(self, mode_index):
    """ Light the auxiliary (right) LED on the current mode's button """
    for led in self.control_surface.utility_button_lights:
      led.turn_off()
    self.control_surface.utility_button_lights[mode_index].turn_on()

  def _theme_faders(self, mode_index):
    """ Change the fader colors to indicate mode """
    for index, fader in enumerate(self.control_surface.fader_elements):
      if mode_index > 0:
        fader.set_theme(mode_colors[mode_index], "fill")
      else:
        if index < 4:
          fader.set_theme(mode_colors[mode_index], "spread")
        else:
          fader.set_theme(mode_colors[::-1][mode_index], "fill")
