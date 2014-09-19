from Push.InstrumentComponent import InstrumentComponent
from Push.MelodicComponent import MelodicComponent
from _Framework.Layer import Layer
from _Framework.ComboElement import ComboElement
from _Framework.SubjectSlot import subject_slot
from Skins import pad_skin, Colors
from Map import *

class BaseMelodicComponent(MelodicComponent):
  """ Switches between note modes : e.g. instrument, drum pad""" 

  def __init__(self, pad_modes, grid_resolution):
    self.pad_modes = pad_modes
    super(BaseMelodicComponent, self).__init__(skin=pad_skin(), is_enabled=True, 
        name='Melodic_Component', 
        layer=Layer(),
        grid_resolution = grid_resolution,
        instrument_play_layer = self._create_instrument_layer())
    self._init_scales()

  def _create_instrument_layer(self):
    return Layer(matrix = self.pad_modes._matrix, 
        octave_up_button = self.pad_modes.utility_buttons[4],
        octave_down_button = self.pad_modes.utility_buttons[5],
        scale_up_button = self.pad_modes.utility_buttons[6],
        scale_down_button = self.pad_modes.utility_buttons[7])

  def _init_scales(self):
    # Auto-enable the scales component and assign the modus buttons
    self._instrument._scales_menu.selected_mode = 'enabled'
    self._instrument.scales.layer = Layer(modus_up_button = self._with_shift(self.pad_modes.utility_buttons[6]),
        modus_down_button = self._with_shift(self.pad_modes.utility_buttons[7]))
    # Bind _on_selected_modus to changes in scrollable list
    self._on_selected_modus.subject = self._instrument.scales._modus_list.scrollable_list

  @subject_slot('selected_item')
  def _on_selected_modus(self):
    self.pad_modes.control_surface._display_num(self.modus_index + 1)

  @property
  def modus_index(self):
    return self._instrument._scales._modus_list.scrollable_list.selected_item_index

  def _with_shift(self, button):
    return ComboElement(button, modifiers=[self.pad_modes.control_surface._note_button])
