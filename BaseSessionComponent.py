from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.Layer import Layer
from _Framework.ComboElement import ComboElement
from _Framework.SubjectSlot import subject_slot
from BaseMessenger import BaseMessenger

from _Tools.re import *
import Colors

class BaseSessionComponent(SessionComponent, BaseMessenger):
  """ A customized session component for the Livid Base 
      Self-initializes to keep things isolated 
  """

  def __init__(self, matrix = None, *a, **k):
    super(BaseSessionComponent, self).__init__(enable_skinning=True, 
        is_enabled=False, 
        layer = self._create_session_layer(matrix),
        auto_name=True, *a, **k)
    self.set_rgb_mode(Colors.CLIP_COLOR_TABLE, Colors.RGB_COLOR_TABLE, clip_slots_only=True)

  def _create_session_layer(self, matrix):
    return Layer(clip_launch_buttons=matrix,
        track_bank_right_button = self.control_surface.with_session(self.utility_buttons[6]),
        scene_bank_up_button = self.utility_buttons[6],
        scene_bank_down_button = self.utility_buttons[7])

  def set_clip_launch_buttons(self, buttons):
      if buttons:
          buttons.reset()
      super(BaseSessionComponent, self).set_clip_launch_buttons(buttons)

