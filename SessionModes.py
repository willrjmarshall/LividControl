from _Framework.ModesComponent import LazyComponentMode
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionZoomingComponent import SessionZoomingComponent
from _Framework.ComboElement import ComboElement
from _Framework.Layer import Layer
from _Framework.Util import recursive_map 
from Map import * 
NUM_TRACKS = 8
NUM_SCENES = 4

from BaseButtonElement import BaseButtonElement
from BaseSessionComponent import BaseSessionComponent
from BaseMessenger import BaseMessenger

class SessionModes(BaseMessenger):
  """ Encapsulates creation of Session and SessionZooming modes """

  def __init__(self):
    self._session_mode = LazyComponentMode(self._create_session)
    self._zooming_mode = LazyComponentMode(self._create_zooming) 

  def modes(self):
    return [self._zooming_mode, self._session_mode]

  def _create_session(self):
    """ Lazily evaluated the first time session mode is selected """
    session = BaseSessionComponent(num_tracks = (NUM_TRACKS - 2), num_scenes = NUM_SCENES,
        matrix = self.control_surface.matrix)
    self.control_surface.set_highlighting_session_component(session)
    return session

  def _create_zooming(self):
    """ Lazily evaluated the first time session mode is selected """
    return SessionZoomingComponent(session=self._session_mode.component, 
        name='Session_Overview', 
        enable_skinning=True, 
        is_enabled=False, 
        layer=Layer(button_matrix=self._create_shifted_matrix()))

  def _create_shifted_matrix(self):
    self._shifted_matrix = ButtonMatrixElement(name='Shifted_Button_Matrix',
        rows = recursive_map(self._with_session, self.control_surface._pads)) 
    return self._shifted_matrix

  def _with_session(self, button):
    return ComboElement(button, modifiers=[self.control_surface._session_button])
