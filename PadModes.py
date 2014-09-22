from _Framework.ModesComponent import AddLayerMode, ModesComponent, LazyComponentMode
from _Framework.Layer import Layer
from _Framework.ComboElement import ComboElement
from _Framework.SubjectSlot import subject_slot
from _Framework.Dependency import dependency, depends
from Push.PlayheadElement import PlayheadElement

from itertools import imap, ifilter
from _Framework.Util import find_if, first

from Map import * 
from BaseMessenger import BaseMessenger

from SessionModes import SessionModes
from BaseMelodicComponent import BaseMelodicComponent
from BaseSequencer import BaseSequencerComponent
from BaseDrumGroupComponent import BaseDrumGroupComponent 

class PadModes(ModesComponent, BaseMessenger):
  """ Switcheds pads between session control, keyboard mode, track control mode and sequencer mode """

  def __init__(self):
    super(PadModes, self).__init__()
    self.add_mode('session', self._session().modes())
    self.add_mode('note', LazyComponentMode(self._note_modes))
    self.add_mode('track', AddLayerMode(self.control_surface.mixer, self._track_control_layer()))
    self.add_mode('sequence', LazyComponentMode(self._init_sequencer))
    self.selected_mode = "session"
  
  def _session(self):
    self._session_modes = SessionModes()
    return self._session_modes

  def _note_modes(self):
    return BaseMelodicComponent()

  def _track_control_layer(self):
    return Layer(
      mute_buttons = self.control_surface.matrix.submatrix[:8, :1],
      solo_buttons = self.control_surface.matrix.submatrix[:8, 1:2],
      arm_buttons = self.control_surface.matrix.submatrix[:8, 2:3])

  def _init_sequencer(self):
    self._sequencer = BaseSequencerComponent(layer = Layer(
      drum_matrix = self.control_surface.matrix.submatrix[:4, :4],
      playhead = self._playhead(),
      select_button = self.control_surface._sequence_button,
      loop_selector_matrix = self.control_surface.shifted_matrix.submatrix[4:8, :4],
      button_matrix = self.control_surface.matrix.submatrix[4:8, :4]))
    self._sequencer._drum_group.__class__ = BaseDrumGroupComponent
    return self._sequencer 

  def _playhead(self):
    return PlayheadElement(self.control_surface._c_instance.playhead)

  def _with_sequencer(self, button):
    return ComboElement(button, modifiers=[self.control_surface._sequence_button])


