from machine import Pin
from machine import I2C


class Device:
    def __init__(self):

        self.sda_pin = Pin(0)
        self.scl_pin = Pin(1)
        self.i2c = I2C(0, sda=self.sda_pin, scl=self.scl_pin, freq=400000)
        self.device = 0#i2c.scan()

    def executa(self):
        self.device = self.i2c.scan()
        if bool(self.device):
            print(type(device))
            print("Dispositivo encontrado: ", device)
        else:
            print("Dispositivo não encontrado")
    
