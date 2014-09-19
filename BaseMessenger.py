from _Framework.Dependency import dependency
from LCDDisplay import LCDDisplay

class BaseMessenger():
  """ Interface for components that provide global controls, 
  e.g. control_surface, log_message, with_session, with_sequence 
  
  To keep things DRY, we define some shared methods here! Magic!
  """

  log_message = dependency(log_message=None)
  control_surface = dependency(control_surface=None)
  reset_controlled_track = dependency(reset_controlled_track=None)
  with_sequencer = dependency(with_sequencer = None)
  with_session = dependency(with_session = None)
  with_note = dependency(with_note = None)
  display_num = dependency(display_num = None)
  
  @property
  def utility_buttons(self):
    return self.control_surface.utility_buttons
