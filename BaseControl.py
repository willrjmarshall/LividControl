from __future__ import with_statement
import Live
import math
import sys
from _Tools.re import *
from itertools import imap, chain, starmap, ifilter
from contextlib import contextmanager

from Push.GridResolution import GridResolution
from Push.AutoArmComponent import AutoArmComponent

from _Framework.ControlSurface import OptimizedControlSurface
from _Framework.ComboElement import ComboElement
from _Framework.SubjectSlot import subject_slot
from _Framework.Layer import Layer
from _Framework.Util import const
from _Framework.Dependency import inject
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.Util import first

from MatrixMaps import PAD_TRANSLATIONS, FEEDBACK_CHANNELS
from ControlElementFactory import create_modifier_button, create_button
from PadModes import PadModes
from FaderModes import FaderModes
from UtilityModes import UtilityModes
from LCDDisplay import LCDDisplay
from PPMeter import PPMeter
from BaseFaderElement import BaseFaderElement
from BasePadElement import BasePadElement
from BaseTouchpadElement import BaseTouchpadElement
from BaseMixerComponent import BaseMixerComponent
from Utilities import wrap_matrix
from Map import *
from Colors import Rgb
from Skins import pad_skin, button_skin, white_button_skin


class BaseControl(OptimizedControlSurface, LCDDisplay):
  __module__ = __name__
  __doc__ = " Better Base controller script by Will Marshall"
  def __init__(self, c_instance):
    super(BaseControl, self).__init__(c_instance)
    self.log_message('BaseControl script open')
    self._utility_buttons = []
    with self.component_guard():
      self._create_shared_controls()
      self._init_mixer()
      self._init_selects()
      self._init_faders()
      self._init_utility()
      self._init_auto_arm()
      self._init_ppm()
      self._init_modes()
      self.set_pad_translations(PAD_TRANSLATIONS)
      self.set_feedback_channels(FEEDBACK_CHANNELS)
      self._device_selection_follows_track_selection = FOLLOW 
      self._suggested_input_port = 'Controls'
      self._suggested_output_port = 'Controls'
      self._on_session_record_changed.subject = self.song()
      self._on_session_record_changed()
      self._send_midi(FADER_FEEDBACK_ON)

  # CREATE stuff 
  def _create_shared_controls(self):
      self._create_modifier_buttons()
      self._create_pads()
      self._create_matrix()
      self._create_grid()

  def _init_mixer(self):
    self._master_fader = BaseFaderElement(BASE_MASTER)
    self.mixer = BaseMixerComponent(len(BASE_TOUCHSTRIPS), auto_name = True, is_enabled = True, invert_mute_feedback = True)
    self.mixer.master_strip().layer = Layer(volume_control=self._master_fader)

  def _init_selects(self):
    selects = [BaseTouchpadElement(pad) for pad in BASE_TOUCHPADS]
    selects_with_session = [self.with_session(pad) for pad in selects]
    self.selects = wrap_matrix(selects) 
    self.selects_with_session = wrap_matrix(selects_with_session)

  def _create_grid(self):
    self.grid = self.register_disconnectable(GridResolution())

  def reset_controlled_track(self):
    self.set_controlled_track(self.song().view.selected_track)

  def update(self):
    super(BaseControl, self).update()
    self.reset_controlled_track()
    self.set_feedback_channels(FEEDBACK_CHANNELS)

  @property
  def utility_buttons(self):
    return self._utility_buttons

  def _create_pads(self):
    self._pads = [ [BasePadElement(pad) for pad in row] for row in BASE_PADS ]
    self._shifted_pads = [ [self.with_sequencer((pad)) for pad in row] for row in self._pads ]

  def _create_matrix(self):
    self.matrix = ButtonMatrixElement(name='Button_Matrix', rows = self._pads)
    self.shifted_matrix = ButtonMatrixElement(name='Button_Matrix', rows = self._shifted_pads)

  def _create_modifier_buttons(self):
    self.utility_button_lights = []
    for index in range(8):
      self.utility_buttons.append(
        create_modifier_button(BASE_BUTTONS[index], 
          "BUTTON_" + str(index + 1),
          skin = button_skin(index)))
      self.utility_button_lights.append(
        create_button(BASE_BUTTON_LIGHTS[index], 
          "BUTTON_LIGHT_" + str(index + 1),
          skin = white_button_skin()))
    self._session_button = self.utility_buttons[0]
    self._note_button = self.utility_buttons[1] 
    self._device_button = self.utility_buttons[2] 
    self._sequence_button = self.utility_buttons[3] 

  def _init_faders(self):
    self.fader_elements = [BaseFaderElement(fader) for fader in BASE_TOUCHSTRIPS]
    self._faders = ButtonMatrixElement(rows = [self.fader_elements])

  def _init_modes(self):
    self._init_fader_modes()
    self._init_pad_modes()

  def _init_fader_modes(self):
    self._fader_modes = FaderModes()
    self._fader_modes.layer = Layer(
        session_button = self._session_button,
        note_button = self._note_button,
        track_button = self._sequence_button,
        sequencer_button = self._device_button)

  def _init_pad_modes(self):
    self._pad_modes = PadModes()
    self._pad_modes.layer = Layer(session_button = self._session_button, 
        note_button = self._note_button,
        track_button = self._device_button,
        sequencer_button = self._sequence_button)

  def _init_utility(self):
    self._utility_modes = UtilityModes(self)
    self._utility_modes.layer = Layer(session_button = self._session_button, 
        note_button = self._note_button,
        track_button = self._device_button,
        sequencer_button = self._sequence_button)

  def _init_auto_arm(self):
    self._auto_arm = AutoArmComponent(is_enabled = True)

  def _init_ppm(self):
    self._ppm = PPMeter(self, self.song().master_track, self._master_fader)

  # Events and callbacks
  def _on_selected_track_changed(self):
    super(BaseControl, self)._on_selected_track_changed()
    self.reset_controlled_track()
    if self._auto_arm.needs_restore_auto_arm:
      self.schedule_message(1, self._auto_arm.restore_auto_arm)

  @subject_slot('session_record')
  def _on_session_record_changed(self):
    status = self.song().session_record
    feedback_color = int(pad_skin()['Instrument.FeedbackRecord'] if status else pad_skin()['Instrument.Feedback'])
    self._c_instance.set_feedback_velocity(feedback_color)

  def with_note(self, button):
    return ComboElement(button, modifiers=[self._note_button])

  def with_session(self, button):
    return ComboElement(button, modifiers=[self._session_button])

  def with_sequencer(self, button):
    return ComboElement(button, modifiers=[self._sequence_button])

  @contextmanager
  def component_guard(self):
    """ Customized to inject additional things """
    with super(BaseControl, self).component_guard():
      with self.make_injector().everywhere():
        yield

  def make_injector(self):
    """ Adds some additional stuff to the injector, used in BaseMessenger """
    return inject(
      control_surface = const(self),
      log_message = const(self.log_message),
      reset_controlled_track = const(self.reset_controlled_track),
      with_note = const(self.with_note),
      with_session = const(self.with_session),
      with_sequencer = const(self.with_sequencer),
      display_num = const(self.display_num),
    ) 
