from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.Util import nop, recursive_map
from itertools import ifilter

def wrap_matrix(control_list, wrapper = nop):
  return ButtonMatrixElement(rows=[map(wrapper, control_list)])

def set_channel(controls, channel):
    for control in ifilter(None, controls or []):
        control.set_channel(channel)
