from Push.InstrumentComponent import InstrumentComponent
from Push.MelodicComponent import MelodicComponent
from _Framework.Layer import Layer
from _Framework.ComboElement import ComboElement
from _Framework.SubjectSlot import subject_slot
from Skins import pad_skin, Colors
from BaseInstrumentComponent import BaseInstrumentComponent
from BaseMessenger import BaseMessenger
from Map import *

FIRST_NOTE = 35# 7 notes per octave, 5 octaves up from C-2 
NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

class BaseMelodicComponent(MelodicComponent, BaseMessenger):
  """ Switches between note modes : e.g. instrument, drum pad""" 

  def __init__(self):
    super(BaseMelodicComponent, self).__init__(skin=pad_skin(), is_enabled=True, 
        name='Melodic_Component', 
        layer=Layer(),
        grid_resolution = self.control_surface.grid,
        instrument_play_layer = self._create_instrument_layer())
    self._init_scales()
    self._instrument.__class__ = BaseInstrumentComponent
    self._instrument.position = FIRST_NOTE 
    self._on_octave_changed.subject = self._instrument._slider._slideable
    self._on_notes_changed.subject = self._instrument
    self._on_selected_modus.subject = self._instrument.scales._modus_list.scrollable_list
    self.reset_controlled_track()

  def _create_instrument_layer(self):
    return Layer(matrix = self.control_surface.matrix, 
        octave_up_button = self.utility_buttons[4],
        octave_down_button = self.utility_buttons[5],
        scale_up_button = self.utility_buttons[6],
        scale_down_button = self.utility_buttons[7])

  def _init_scales(self):
    # Auto-enable the scales component and assign the modus buttons
    self._instrument._scales_menu.selected_mode = 'enabled'

    # Manually set the colors for the modus up/down ButtonControls using the Alts from our skin
    # This is easier than doing lots of subclassing
    scroller = self._instrument.scales._modus_list._scroller 
    scroller.scroll_up_button.color = "Alt" 
    scroller.scroll_down_button.color = "Alt" 
    scroller.scroll_up_button.disabled_color = "Alt" 
    scroller.scroll_down_button.disabled_color = "Alt" 

    self._instrument.scales.layer = Layer(modus_up_button = self.with_note(self.utility_buttons[7]),
        modus_down_button = self.with_note(self.utility_buttons[6]))
    # Bind _on_selected_modus to changes in scrollable list

  @subject_slot('selected_item')
  def _on_selected_modus(self):
    self.display_num(self.modus_index + 1)

  @subject_slot('position')
  def _on_octave_changed(self):
    self.display_num(str(self.octave_index + 1))

  @subject_slot('position')
  def _on_octave_changed(self):
    self.display_num(str(self.octave_index + 1))

  @subject_slot('position')
  def _on_notes_changed(self):
    self.display_num(str(self.note_index + 1))

  @property
  def modus_index(self):
    return self._instrument._scales._modus_list.scrollable_list.selected_item_index

  @property
  def octave_index(self):
    return int(round(self._instrument._first_note)) / self._instrument.page_length

  @property
  def note_index(self):
    return int(round(self._instrument._first_note)) % self._instrument.page_length
