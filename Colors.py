from itertools import izip, repeat
from _Framework.ButtonElement import Color


class Colors:
  BLACK = 0
  WHITE = 2
  CYAN = 4
  MAGENTA = 8
  RED = 16
  BLUE = 32
  YELLOW = 64
  GREEN = 127

class RgbColor(Color):
    """
    An a RGB color drawable in RGB pads represented.
    """
    _rgb_value = (0, 0, 0)
    def __init__(self, midi_value = None, rgb_value = None, *a, **k):
        super(RgbColor, self).__init__(midi_value=midi_value, *a, **k)
        if rgb_value is not None:
            self._rgb_value = rgb_value
        return

class Rgb:
    """
    Table of RgbColors for main matrix.
    """
    BLACK = RgbColor(Colors.BLACK)
    WHITE = RgbColor(Colors.WHITE)
    CYAN = RgbColor(Colors.CYAN)
    MAGENTA = RgbColor(Colors.MAGENTA)
    RED = RgbColor(Colors.RED)
    BLUE = RgbColor(Colors.BLUE)
    YELLOW = RgbColor(Colors.YELLOW)
    GREEN = RgbColor(Colors.GREEN)

CLIP_COLOR_TABLE = {}
RGB_COLOR_TABLE = ((Colors.BLACK, 0),
    (Colors.WHITE, 16777215),
    (Colors.CYAN, 1090798),
    (Colors.MAGENTA, 12008809),
    (Colors.RED, 16712965),
    (Colors.BLUE, 197631),
    (Colors.YELLOW, 14939139),
    (Colors.GREEN, 5480241))
