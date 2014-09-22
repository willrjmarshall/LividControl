from _Framework.ChannelStripComponent import ChannelStripComponent
from BaseMessenger import BaseMessenger

class BaseChannelStripComponent(ChannelStripComponent, BaseMessenger):
  """ Calls reset on some buttons when they're assigned.
  
  This clears out changes to pad enabled, channel and note made by
  the Step Sequencer or Melodic Components. This is because we're using 
  buttons from the Matrix for these controls, which are prone to being fucked with
  """

  def set_arm_button(self, button):
    if button:
      button.reset()
      button.set_on_off_values('MixerButton.Arm', 'Button.Off')
    super(BaseChannelStripComponent, self).set_arm_button(button)
    self.update()

  def set_solo_button(self, button):
    if button:
      button.reset()
      button.set_on_off_values('MixerButton.Solo', 'Button.Off')
    super(BaseChannelStripComponent, self).set_solo_button(button)
    self.update()

  def set_mute_button(self, button):
    if button:
      button.reset()
      button.set_on_off_values('MixerButton.Mute', 'Button.Off')
    super(BaseChannelStripComponent, self).set_mute_button(button)
    self.update()
