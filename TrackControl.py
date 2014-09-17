from _Framework.MixerComponent import MixerComponent
NUM_TRACKS = 8

class TrackControl(MixerComponent):
  """ Uses a pad matrix and LED colors to control
  mutes, solos, arms, xfader assigns for 8 channels """

  def __init__(self):
    super(TrackControl, self).__init__(NUM_TRACKS)
