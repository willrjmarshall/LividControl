from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.Util import nop, recursive_map

def wrap_matrix(control_list, wrapper = nop):
  return ButtonMatrixElement(rows=[map(wrapper, control_list)])
