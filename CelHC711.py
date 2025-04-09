from machine import SPI, Pin
import utime
from hx711_gpio import HX711
import _thread

#pin_OUT = 9  
#pin_SCK = 10

class CelHC711():
    def __init__(self, pin_OUT, pin_SCK, scale = 48.36, gain=128, qtd_media=1, adjust_unit=10, casa_decimal=0):
        self.pin_OUT = Pin(pin_OUT, Pin.IN, pull=Pin.PULL_DOWN)
        self.pin_SCK = Pin(pin_SCK, Pin.OUT)
        self.scale = scale
        self.gain = gain
        self.qtd_media = qtd_media
        self.adjust_unit = adjust_unit
        self.casa_decimal = casa_decimal
        
        self.ativa_valor = True
        
        self.hx = HX711(self.pin_SCK, self.pin_OUT, gain=128)
        #hx.set_scale(48.36)
        self.hx.set_scale(self.scale)
        self.hx.tare(50)
        
        self._valor_carga = 0
        
    def set_scale(self, new_scale):
        self.hx.set_scale(new_scale)
        self.scale = new_scale
    def set_media(self, new_media):
        self.qtd_media = new_media
    def set_adjust_unit(self, new_adjust):
        self.adjust_unit = new_adjust
        
    def tara(self, times):
        self.ativa_valor = False
        self.hx.tare(times)
        self.ativa_valor = True
        
    def get_valor(self):
        return self.hx.get_units()
    @property
    def valor_carga(self):
        return self._valor_carga
        
 
    def tread_exec(self):
        while True:
            if self.ativa_valor == True:
                for i in range(self.qtd_media):
                    self._valor_carga += self.hx.get_units()
                self._valor_carga = (self._valor_carga/self.qtd_media)/self.adjust_unit
                if self._valor_carga < 0:
                    self._valor_carga = self.round_loc(0.0000)
                self._valor_carga = self.round_loc(self._valor_carga)
                #print(self._valor_carga)
                #return round(self._valor_carga)
            else:
                utime.sleep(1)
            
    def round_loc(self, valor):
        if self.casa_decimal == 0:
            return round(valor)
        elif self.casa_decimal > 0:
            return round(valor, self.casa_decimal)
        
    def run_cel(self):
        tread_exec = self.tread_exec
        _thread.start_new_thread(self.tread_exec, ())
    
