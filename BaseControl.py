from __future__ import with_statement
import Live
import math
import sys
from _Tools.re import *
from itertools import imap, chain, starmap

from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from ControlElementFactory import create_modifier_button, create_button

from PadModes import PadModes
from FaderModes import FaderModes
from LCDDisplay import LCDDisplay
from PPMeter import PPMeter
from BaseFaderElement import BaseFaderElement
from BaseTransportComponent import BaseTransportComponent
from Map import *
from Skins import button_skin_2, button_skin_1

class BaseControl(ControlSurface, LCDDisplay):
  __module__ = __name__
  __doc__ = " Better Base controller script by Will Marshall"
  def __init__(self, c_instance):
    super(BaseControl, self).__init__(c_instance)
    self.log_message('BaseControl script open')
    with self.component_guard():
      self._create_modifier_buttons()
      self._init_faders()
      self._init_transport()
      self._init_pads()
      self._init_ppm()
      self._init_switches()
      self._init_misc() # Light flashing, VU meter on master

  def _create_modifier_buttons(self):
    self.utility_buttons = []
    for index in range(8):
      if index < 6:
        skin = button_skin_1() 
      else:
        skin = button_skin_2() 
      self.utility_buttons.append(create_modifier_button(BASE_BUTTONS[index], "BUTTON_" + str(index + 1),
        skin = skin))
    self._session_button = self.utility_buttons[0]
    self._note_button = self.utility_buttons[1] 

  def _init_pads(self):
    self._pad_modes = PadModes(self)
    self._pad_modes.layer = Layer(session_button = self._session_button, note_button = self._note_button)

  def _init_faders(self):
    self._master_fader = BaseFaderElement(BASE_MASTER)
    self._fader_modes = FaderModes(self)
    self._fader_modes.layer = Layer(mixer_button = self._session_button, device_button = self._note_button)

  def _init_transport(self):
    self._transport = BaseTransportComponent()
    self._transport.layer = Layer(tempo_decrease_button = self.utility_buttons[4], tempo_increase_button = self.utility_buttons[5])

  def _init_switches(self):
    pass

  def _init_ppm(self):
    self._ppm = PPMeter(self, self.song().master_track, self._master_fader)

  def _init_misc(self):
    # BPM
    # PPM on master
    pass
