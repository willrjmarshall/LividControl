from _Framework.SceneComponent import SceneComponent
from CustomClipSlotComponent import CustomClipSlotComponent

class CustomSceneComponent(SceneComponent):
  clip_slot_component_type = CustomClipSlotComponent
  def __init__(self, parent, *a, **k):
    self.parent = parent
    super(CustomSceneComponent, self).__init__(*a, **k)

  def _create_clip_slot(self):
    return self.clip_slot_component_type(self.parent)

