from __future__ import with_statement
import Live
import math
import sys
from _Tools.re import *
from itertools import imap, chain, starmap

from _Framework.ControlSurface import OptimizedControlSurface
from _Framework.Layer import Layer

from MatrixMaps import PAD_TRANSLATIONS, FEEDBACK_CHANNELS


from ControlElementFactory import create_modifier_button, create_button
from PadModes import PadModes
from FaderModes import FaderModes
from UtilityModes import UtilityModes
from LCDDisplay import LCDDisplay
from PPMeter import PPMeter
from BaseFaderElement import BaseFaderElement
from Map import *
from Skins import button_skin_2, button_skin_1
from Push.PlayheadElement import PlayheadElement

STREAMINGON = (240, 0, 1, 97, 12, 62, 127, 247)

class BaseControl(OptimizedControlSurface, LCDDisplay):
  __module__ = __name__
  __doc__ = " Better Base controller script by Will Marshall"
  def __init__(self, c_instance):
    super(BaseControl, self).__init__(c_instance)
    self.log_message('BaseControl script open')
    with self.component_guard():
      self._playhead = PlayheadElement(self._c_instance.playhead)
      self._playhead.reset()
      self._send_midi(STREAMINGON)
      self._send_midi((191, 122, 64))
      self._create_modifier_buttons()
      self._init_faders()
      self._init_utility()
      self._init_pads()
      self._init_ppm()
      
      self.set_pad_translations(PAD_TRANSLATIONS)
      self.set_feedback_channels(FEEDBACK_CHANNELS)

  def reset_controlled_track(self):
    self.set_controlled_track(self.song().view.selected_track)

  def _on_selected_track_changed(self):
    super(BaseControl, self)._on_selected_track_changed()
    self.reset_controlled_track()

  def update(self):
    super(BaseControl, self).update()
    self.set_feedback_channels(FEEDBACK_CHANNELS)
    self.reset_controlled_track()


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
    self._device_button = self.utility_buttons[2] 
    self._sequence_button = self.utility_buttons[3] 

  def _init_pads(self):
    self._pad_modes = PadModes(self)
    self._pad_modes.layer = Layer(session_button = self._session_button, 
        note_button = self._note_button,
        track_button = self._device_button,
        sequence_button = self._sequence_button)

  def _init_faders(self):
    self._master_fader = BaseFaderElement(BASE_MASTER)
    self._fader_modes = FaderModes(self)
    self._fader_modes.layer = Layer(mixer_button = self._session_button,
        mixer2_button = self._note_button,
        mixer3_button = self._sequence_button,
        device_button = self._device_button)

  def _init_utility(self):
    self._utility_modes = UtilityModes(self)
    self._utility_modes.layer = Layer(session_button = self._session_button, 
        note_button = self._note_button,
        device_button = self._device_button,
        sequence_button = self._sequence_button)

  def _init_ppm(self):
    self._ppm = PPMeter(self, self.song().master_track, self._master_fader)

