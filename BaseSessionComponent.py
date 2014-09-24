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
    self.set_mixer(self.control_surface.mixer)
    self.set_offsets(0, 2)

  def _create_session_layer(self, matrix):
    return Layer(clip_launch_buttons=matrix.submatrix[:6, :4],
        track_bank_right_button = self.control_surface.with_session(self.utility_buttons[6]),
        track_bank_left_button = self.control_surface.with_session(self.utility_buttons[7]),
        stop_track_clip_buttons = self.control_surface.selects_with_session,
        scene_bank_up_button = self.utility_buttons[6],
        scene_bank_down_button = self.utility_buttons[7])

  def set_clip_launch_buttons(self, buttons):
    """ Since we use the matrix as a keyboard, which changes note/channel
    We must reset """
    if buttons:
        buttons.reset()
    super(BaseSessionComponent, self).set_clip_launch_buttons(buttons)
