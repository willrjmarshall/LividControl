from _Framework.ComboElement import ComboElement
from _Framework.Dependency import dependency

class BaseMessenger(object):
  """ Interface for components that provide global controls, 
  e.g. control_surface, log_message, with_session, with_sequence """

  log_message = dependency(log_message=None)
  control_surface = dependency(control_surface=None)
  utility_buttons = dependency(utility_buttons=None)

