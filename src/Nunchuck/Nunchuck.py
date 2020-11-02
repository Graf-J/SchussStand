from smbus import SMBus
import RPi.GPIO as rpi
import time as time

bus = 0

class Nunchuck:

  def __init__(self,delay = 0.05):
    self.delay = delay
    if rpi.RPI_REVISION == 1:
      i2c_bus = 0
    elif rpi.RPI_REVISION == 2:
      i2c_bus = 1
    elif rpi.RPI_REVISION == 3:
      i2c_bus = 1
    else:
      print("Unable to determine Raspberry Pi revision.")
      exit
    self.bus = SMBus(i2c_bus)
    self.bus.write_byte_data(0x52,0x40,0x00)
    time.sleep(0.1)

  def read(self):
    self.bus.write_byte(0x52,0x00)
    time.sleep(self.delay)
    temp = [(0x17 + (0x17 ^ self.bus.read_byte(0x52))) for i in range(6)]
    return temp

  def raw(self):
    data = self.read()
    return data

  def joystick(self):
    data = self.read()
    return data[0],data[1]

  def accelerometer(self):
    data = self.read()
    return data[2],data[3],data[4]

  def button_c(self):
    data = self.read()
    butc = (data[5] & 0x02)

    return butc == 0

  def button_z(self):
    try:
      data = self.read()
      butc = (data[5] & 0x01)

      return butc == 0
    except:
      return True

  def joystick_x(self):
    try:
      data = self.read()
      return data[0]
    except:
      return 130

  def joystick_y(self):
    try:
      data = self.read()
      return data[1]
    except:
      return 130

  def accelerometer_x(self):
    data = self.read()
    return data[2]

  def accelerometer_y(self):
    data = self.read()
    return data[3]

  def accelerometer_z(self):
    data = self.read()
    return data[4]
    
  def setdelay(self,delay):
    self.delay = delay


  def scale(self,value,_min,_max,_omin,_omax):
    return (value - _min) * (_omax - _omin) // (_max - _min) + _omin
