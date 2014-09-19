from itertools import imap, chain, starmap, izip, ifilter
from _Framework.Util import find_if, first
from Push.StepSeqComponent import StepSeqComponent, DrumGroupFinderComponent
from _Framework.ClipCreator import ClipCreator
from _Framework.SubjectSlot import subject_slot, subject_slot_group
from Push.PlayheadComponent import PlayheadComponent
from Push.PlayheadElement import PlayheadElement
from Skins import pad_skin
from BaseNoteEditorComponent import BaseNoteEditorComponent
from BaseMessenger import BaseMessenger
from MatrixMaps import PAD_FEEDBACK_CHANNEL

class BaseSequencerComponent(StepSeqComponent, BaseMessenger):
  """ Custom step-sequencer for Drum Pads. Keys are handled via Melodic Step Sequencer. """

  def __init__(self, *a, **k):
    super(BaseSequencerComponent, self).__init__(clip_creator = ClipCreator(),
        grid_resolution = self.control_surface.grid,
        is_enabled = False,
        skin = pad_skin(),
        *a, **k)
    self._setup_drum_group_finder()
    self.on_selected_track_changed()
    self.patch_note_editor()
    self.configure_playhead()
    self.update()

  # Set the playhead to use our notes
  # Feedback channel must also be set on ControlSurface
  # Can't be zero, so we're just using 14
  # TODO refactor to pull from Map.py
  def configure_playhead(self):
    self._playhead_component._notes=tuple(chain(*starmap(range, (
         (64, 68),
         (56, 60),
         (48, 52),
         (40, 44)))))
    self._playhead_component._triplet_notes=tuple(chain(*starmap(range, (
         (64, 67),
         (56, 59),
         (48, 51),
         (40, 43)))))

  def set_button_matrix(self, matrix):
    """ This method, as with most set_* methods, is called every time
    This component is enabled """
    self._note_editor_matrix = matrix
    self._update_note_editor_matrix()
    if matrix:
      for button, _ in ifilter(first, matrix.iterbuttons()):
        button.set_channel(PAD_FEEDBACK_CHANNEL)

  def _setup_drum_group_finder(self):
    self._drum_group_finder = DrumGroupFinderComponent()
    self._on_drum_group_changed.subject = self._drum_group_finder
    self._drum_group_finder.update()

  @subject_slot('drum_group')
  def _on_drum_group_changed(self):
    self.set_drum_group_device(self._drum_group_finder.drum_group)

  def on_selected_track_changed(self):
    self.set_drum_group_device(self._drum_group_finder.drum_group)
    self.update()

  def patch_note_editor(self):
    self._note_editor.__class__ = BaseNoteEditorComponent
