from _Framework.ModesComponent import ModesComponent, LazyComponentMode
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from ControlElementFactory import create_modifier_button, create_button
from _Framework.Layer import Layer
from _Framework.SubjectSlot import subject_slot
from Push.GridResolution import GridResolution
from Map import * 

from SessionModes import SessionModes
from BaseMelodicComponent import BaseMelodicComponent
from BaseButtonElement import BaseButtonElement

class PadModes(ModesComponent):
  """ Switcheds pads between session control, keyboard and sequencer mode """

  def __init__(self, control_surface):
    super(PadModes, self).__init__()
    self.control_surface = control_surface
    self._create_pads()
    self.add_mode('session', self._init_session().modes())
    self.add_mode('note', LazyComponentMode(self._note_modes))
    self._create_buttons()
    self.selected_mode = "session"
  
  def _init_session(self):
    self._session_modes = SessionModes(self)
    return self._session_modes

  def _note_modes(self):
    return BaseMelodicComponent(self, self.register_disconnectable(GridResolution()))

  def _create_buttons(self):
    self._session_button = create_modifier_button(BASE_BUTTONS[0], "SESSION_MODE_BUTTON")
    self._note_button = create_modifier_button(BASE_BUTTONS[1], "NOTE_MODE_BUTTON")
    self.layer = Layer(session_button = self._session_button, note_button = self._note_button)

    self._button_5 = create_button(BASE_BUTTONS[4], "BUTTON_5")
    self._button_6 = create_button(BASE_BUTTONS[5], "BUTTON_6")
    self._button_7 = create_button(BASE_BUTTONS[6], "BUTTON_7")
    self._button_8 = create_button(BASE_BUTTONS[7], "BUTTON_8")

  def _create_pads(self):
    self._pads = [ [BaseButtonElement(pad) for pad in row] for row in BASE_PADS ]

  def create_matrix(self):
    self._matrix = ButtonMatrixElement(name='Button_Matrix', rows = self._pads)
    return self._matrix
