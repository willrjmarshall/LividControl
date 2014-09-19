from __future__ import with_statement
from Push.NoteEditorComponent import NoteEditorComponent
from itertools import chain, imap, ifilter
from functools import partial
from _Framework.Util import sign, product, in_range, clamp, forward_property, first
from _Framework import Task, Defaults
from Push.LoopSelectorComponent import create_clip_in_selected_slot
from Push.MatrixMaps import PAD_FEEDBACK_CHANNEL

class BaseNoteEditorComponent(NoteEditorComponent):
  """ Monkeypatches NoteEditorComponent to support 4 instead of 8 steps """
  def _visible_steps(self):
    first_time = self.page_length * self._page_index
    steps_per_page = self._get_step_count()
    step_length = self._get_step_length()
    indices = range(steps_per_page)
    if self._is_triplet_quantization():
      #indices = filter(lambda k: k % 8 not in (6, 7), indices)
      indices = filter(lambda k: k % 4 != 3, indices)
    return [ (self._time_step(first_time + k * step_length), index) for k, index in enumerate(indices) ]
