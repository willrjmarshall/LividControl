from itertools import imap, chain, starmap
from Push.StepSeqComponent import StepSeqComponent, DrumGroupFinderComponent
from _Framework.ClipCreator import ClipCreator
from _Framework.SubjectSlot import subject_slot, subject_slot_group
from Push.PlayheadComponent import PlayheadComponent
from Push.PlayheadElement import PlayheadElement
from Push.GridResolution import GridResolution
from Skins import pad_skin

class BaseSequencerComponent(StepSeqComponent):
  """ Self-initializing step sequencer """

  def __init__(self, pad_modes, *a, **k):
    self.pad_modes = pad_modes
    super(BaseSequencerComponent, self).__init__(clip_creator = ClipCreator(),
        grid_resolution = pad_modes._grid,
        is_enabled = False,
        skin = pad_skin(),
        *a, **k)
    self.setup_playhead()
    self.setup_drum_group_finder()
    self.on_selected_track_changed()
    self.update()

  def setup_drum_group_finder(self):
    self._drum_group_finder = DrumGroupFinderComponent()
    self._on_drum_group_changed.subject = self._drum_group_finder
    self._drum_group_finder.update()

  @subject_slot('drum_group')
  def _on_drum_group_changed(self):
    self.set_drum_group_device(self._drum_group_finder.drum_group)

  def setup_playhead(self):
    self._playhead_component = self.register_component(PlayheadComponent(grid_resolution=self.pad_modes._grid, 
      paginator=self._paginator, 
      follower=self._loop_selector,
      notes = range(16),
      triplet_notes = chain(*starmap(range, ((0, 3), (4, 7), (8, 11), (12, 15))))))

    self.set_playhead(PlayheadElement(self.pad_modes.control_surface._c_instance.playhead))
    self._playhead.reset()

  def on_selected_track_changed(self):
    self.set_drum_group_device(self._drum_group_finder.drum_group)
    return

    #self._note_editor._visible_steps = self._visible_steps
  #def _visible_steps(self):
		#first_time = self._note_editor.page_length * self._note_editor._page_index
		#steps_per_page = self._note_editor._get_step_count()
		#step_length = self._note_editor._get_step_length()
		#indices = range(steps_per_page)
		#if self._note_editor._is_triplet_quantization():
			#indices = filter(lambda k: k % 4 != 3, indices)
		#return [ (self._note_editor._time_step(first_time + k * step_length), index) for k, index in enumerate(indices) ]
