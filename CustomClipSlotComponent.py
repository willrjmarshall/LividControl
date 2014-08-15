from _Framework.ClipSlotComponent import ClipSlotComponent

class CustomClipSlotComponent(ClipSlotComponent):
  def __init__(self, parent, *a, **k):
    self.parent = parent
    super(CustomClipSlotComponent, self).__init__(*a, **k)

  def _color_value(self, color):
    self.parent.log_message(str(color))
    return super(CustomClipSlotComponent, self)._color_value(color)
