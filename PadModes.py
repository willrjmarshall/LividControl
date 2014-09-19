from _Framework.ModesComponent import ModesComponent, LazyComponentMode
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.Layer import Layer
from _Framework.ComboElement import ComboElement
from _Framework.SubjectSlot import subject_slot
from Push.NoteSettingsComponent import NoteEditorSettingsComponent
from Push.GridResolution import GridResolution
from Push.PlayheadElement import PlayheadElement
from Map import * 
from MatrixMaps import PAD_TRANSLATIONS, FEEDBACK_CHANNELS

from SessionModes import SessionModes
from BaseMelodicComponent import BaseMelodicComponent
from BaseButtonElement import BaseButtonElement
from BasePadElement import BasePadElement
from TrackControl import TrackControl
from BaseSequencer import BaseSequencerComponent
from BaseDrumGroupComponent import BaseDrumGroupComponent 

class PadModes(ModesComponent):
  """ Switcheds pads between session control, keyboard and sequencer mode """

  def __init__(self, control_surface):
    super(PadModes, self).__init__()
    self.control_surface = control_surface
    self.utility_buttons = control_surface.utility_buttons
    self._create_pads()
    self._create_grid()
    self.add_mode('session', self._session().modes())
    self.add_mode('note', LazyComponentMode(self._note_modes))
    self.add_mode('track', LazyComponentMode(self._track_mode))
    self.add_mode('sequence', LazyComponentMode(self._sequencer_mode))
    self.selected_mode = "session"
  
  def _session(self):
    self._session_modes = SessionModes(self)
    return self._session_modes

  def _create_grid(self):
    self._grid = self.register_disconnectable(GridResolution())

  def _note_modes(self):
    return BaseMelodicComponent(self, self._grid)

  def _track_mode(self):
    return TrackControl()

  def _sequencer_mode(self):
    self.control_surface.set_feedback_channels(FEEDBACK_CHANNELS)
    
    self._sequencer = BaseSequencerComponent(self, layer = Layer(
      drum_matrix = self._matrix.submatrix[:4, :4],
      playhead = self.control_surface._playhead,
      select_button = self.control_surface._sequence_button,
      #loop_selector_matrix = self._matrix.submatrix[4:8, :4]))
      button_matrix = self._matrix.submatrix[4:8, :4]))
    self._sequencer._drum_group.__class__ = BaseDrumGroupComponent
    self._sequencer._drum_group.control_surface = self.control_surface
    return self._sequencer 

  def _create_pads(self):
    self._pads = [ [BasePadElement(pad) for pad in row] for row in BASE_PADS ]

  def create_matrix(self):
    self._matrix = ButtonMatrixElement(name='Button_Matrix', rows = self._pads)
    return self._matrix


  def _with_sequencer(self, button):
    return ComboElement(button, modifiers=[self.control_surface._sequence_button])
