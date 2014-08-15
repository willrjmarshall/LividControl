from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ModesComponent import LazyComponentMode, ModesComponent
from _Framework.Layer import Layer
from _Framework.ButtonMatrixElement import ButtonMatrixElement

from BaseButtonElement import BaseButtonElement
from BaseSessionComponent import BaseSessionComponent
from Map import * 
NUM_TRACKS = 8
NUM_SCENES = 4

class PadModes(ModesComponent):
  """ Switcheds pads between session control, keyboard and sequencer mode """

  def __init__(self, parent):
    super(PadModes, self).__init__()
    self.parent = parent
    self._session_mode = LazyComponentMode(self._create_session)
    self.add_mode('session', self._create_session_mode())
    self.selected_mode = "session"

  def _create_session_mode(self):
    return [self._session_mode]

  def _create_session_layer(self):
    return Layer(clip_launch_buttons=self._create_matrix())

  def _create_session(self):
    session = BaseSessionComponent(self.parent, num_tracks = NUM_TRACKS, num_scenes = NUM_SCENES, layer = self._create_session_layer())
    self.parent.set_highlighting_session_component(session)
    return session

  def _create_matrix(self):
    self._matrix = ButtonMatrixElement(name='Button_Matrix')
    pads = self._create_pads()
    for index in range(NUM_SCENES):
      self._matrix.add_row(pads[(index*NUM_TRACKS):(index*NUM_TRACKS)+NUM_TRACKS])
    return self._matrix
  
  def _create_pads(self):
    self._pads = [BaseButtonElement(CHANNEL, pad) for pad in BASE_PADS]
    return self._pads

  def _create_zooming(self):
    pass
