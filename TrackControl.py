from _Framework.MixerComponent import MixerComponent
from _Framework.Layer import Layer
NUM_TRACKS = 8

class TrackControl(MixerComponent, BaseMessenger):
  """ Uses a pad matrix and LED colors to control
  mutes, solos, arms, xfader assigns for 8 channels """

  def __init__(self):
    super(TrackControl, self).__init__(NUM_TRACKS,
      layer = Layer(
        mute_buttons = self.control_surface.fader_elements[0],  
        solo = self.control_surface.fader_elements[2],  
        arm_buttons = self.control_surface.fader_elements[3]  
      )    
    )

