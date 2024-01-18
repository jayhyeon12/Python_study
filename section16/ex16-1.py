class USB:
  def __init__(self, capacity):
    self.capacity = capacity

  def info(self):
    print(f'{self.capacity}GB USB')

usb = USB(128)
# print(usb.capacity)
usb.info()