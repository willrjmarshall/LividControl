from _Framework.TransportComponent import TransportComponent
from _Framework.ScrollComponent import ScrollComponent

class BaseTransportComponent(TransportComponent):
  """ Customized transport with increment and decrement options for tempo """


  def __init__(self, *a, **k):
    super(BaseTransportComponent, self).__init__(*a, **k)
    self._tempo_scrolling = self.register_component(ScrollComponent())
    self._tempo_scrolling.can_scroll_down = self._tempo_can_decrease
    self._tempo_scrolling.can_scroll_up = self._tempo_can_increase
    self._tempo_scrolling.scroll_up = self._increase_tempo
    self._tempo_scrolling.scroll_down = self._decrease_tempo

  def set_tempo_increase_button(self, button):
    self._plus_button = button
    self._tempo_scrolling.set_scroll_up_button(button)

  def set_tempo_decrease_button(self, button):
    self._minus_button = button
    self._tempo_scrolling.set_scroll_down_button(button)
  
  def _tempo_can_decrease(self):
    return self.song().tempo > 0

  def _tempo_can_increase(self):
    return self.song().tempo < 999

  def _increase_tempo(self):
    self.song().tempo = self.song().tempo + 0.5

  def _decrease_tempo(self):
    self.song().tempo = self.song().tempo - 0.5
