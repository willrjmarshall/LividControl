from __future__ import with_statement
import Live
import math
import sys
from _Tools.re import *
from itertools import imap, chain, starmap

from _Framework.ControlSurface import ControlSurface

from PadModes import PadModes
from LCDDisplay import LCDDisplay

class BaseControl(ControlSurface, LCDDisplay):
  __module__ = __name__
  __doc__ = " Better Base controller script by Will Marshall"
  def __init__(self, c_instance):
    super(BaseControl, self).__init__(c_instance)
    self.log_message('BaseControl script open')
    with self.component_guard():
      self._init_faders()
      self._init_pads()
      self._init_switches()
      self._init_selectors()
      self._init_misc() # Light flashing, VU meter on master

  def _init_pads(self):
    self._pad_modes = PadModes(self)

  def _init_faders(self):
    pass
  def _init_switches(self):
    pass
  def _init_selectors(self):
    pass
  def _init_misc(self):
    pass
