from _Framework.SessionComponent import SessionComponent
from _Tools.re import *
from _Framework.ButtonMatrixElement import ButtonMatrixElement
import Colors

class BaseSessionComponent(SessionComponent):
  """ A customized session component for the Livid Base 
      Self-initializes to keep things isolated 
  """

  def __init__(self, parent, *a, **k):
    self.parent = parent
    super(BaseSessionComponent, self).__init__(enable_skinning=True, is_enabled=False, auto_name=True, *a, **k)

    self.set_rgb_mode(Colors.CLIP_COLOR_TABLE, Colors.RGB_COLOR_TABLE, clip_slots_only=True)
