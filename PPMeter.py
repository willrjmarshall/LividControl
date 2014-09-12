import Live
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.SubjectSlot import subject_slot
from _Framework.SessionComponent import SessionComponent 
import math

#MASTER_SCALE_MAX = 1.0
#MASTER_SCALE_MIN = 0.2
MASTER_SCALE_MAX = 0.9
MASTER_SCALE_MIN = 0.4

class PPMeter(ControlSurfaceComponent):
  'represents a single PPM with source and target' 

  def __init__(self, control_surface, track, target):
    super(PPMeter, self).__init__() 
    self.control_surface = control_surface
    self.track = track 
    self.target = target
    self.prev_mean_peak = 0.0
    self._on_output_meter.subject = self.track

  @subject_slot('output_meter_left')
  def _on_output_meter(self):
    self.target.send_value(self.scale(self.mean_peak), True)

  def scale(self, value):
    if (value > MASTER_SCALE_MAX):
      value =MASTER_SCALE_MAX 
    elif (value < MASTER_SCALE_MIN):
      value = MASTER_SCALE_MIN 
    value = value - MASTER_SCALE_MIN
    value = value * 2 * 127
    return int(round(value))

  @property
  def mean_peak(self):
    return (self.track.output_meter_left + self.track.output_meter_right) / 2
