


import time
from machine import Pin, UART
led = Pin(2, Pin.OUT)

uart = UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

class Medicion:
  def __init__(self,tds = None,distancia = None,temperatura = None):
      self.tds = tds
      self.distancia = distancia
      self.temperatura = temperatura
      






def Uaart(val):
  byte = b''
  while(1): 
    
    byte = val
    uart.write(byte)
    time.sleep(1)
    if(uart.any() > 0):  
      strigByte = uart.readline()
      time.sleep(1)
      return strigByte







