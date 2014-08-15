from _Framework.SessionComponent import SessionComponent
from _Tools.re import *
from _Framework.ButtonMatrixElement import ButtonMatrixElement
import Colors
from CustomSceneComponent import CustomSceneComponent

class BaseSessionComponent(SessionComponent):
  """ A customized session component for the Livid Base 
      Self-initializes to keep things isolated 
  """

  scene_component_type = CustomSceneComponent

  def __init__(self, parent, *a, **k):
    self.parent = parent
    super(BaseSessionComponent, self).__init__(enable_skinning=True, is_enabled=False, auto_name=True, *a, **k)
    self.set_rgb_mode(Colors.CLIP_COLOR_TABLE, Colors.RGB_COLOR_TABLE, clip_slots_only=True)

  def _create_scene(self):
    return self.scene_component_type(self.parent, num_slots=self._num_tracks, tracks_to_use_callback=self.tracks_to_use)
