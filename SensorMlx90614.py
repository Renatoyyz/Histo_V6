from typing import Any
import smbus 
import threading
import time

class MlX90614(threading.Thread):
    
    """ 
    MLX90614_RAWIR1 = 0x04
    MLX90614_RAWIR2 = 0x05
    MLX90614_TA = 0x06
    MLX90614_TOBJ1 = 0x07
    MLX90614_TA = 0x07
    MLX90614_TOBJ1 = 0x06
    MLX90614_TOBJ2 = 0x08
    
    MLX90614_TOMAX = 0x20
    MLX90614_TOMIN = 0x21
    MLX90614_PWMCTRL = 0x22
    MLX90614_TARANGE = 0x23
    MLX90614_EMISS = 0x24
    MLX90614_COFIG = 0x25
    MLX90614_ADDR = 0x0E
    MLX90614_ID1 = 0x3C
    MLX90614_ID2 = 0x3D
    MLX90614_ID3 = 0x3E
    MLX90614_ID4 = 0x3F 
    """
    
    
    def __init__(self, address=0x5A, bus_num=1, arredondamento=2, dado = Any):
        threading.Thread.__init__(self)
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)
        self.arredondamento = arredondamento
        self._dado = dado

        self.VALOR_TEMPERATURA = -1
        
        self.MLX90614_TA = 0x07
    
    def read_reg(self, reg_addr):
        try:
            return self.bus.read_word_data(self.address, reg_addr)
        except:
            print("Erro comunicacao do sensor:")
            return 0
           
    
    def data_to_temp(self, data):
        temp = (data*0.02) - 273.15
        return temp
    
    def get_amb_temp(self):
        data = self.read_reg(self.MLX90614_TA)
        if data == False:
            return self._dado.MLX90614_ERRO
        else:
            return round(self.data_to_temp(data),self.arredondamento)
    
    def get_obj_temp(self):
        data = self.read_reg(self.MLX90614_TOBJ1)
        if data == False:
            return self._dado.MLX90614_ERRO
        else:
            return round(self.data_to_temp(data), self.arredondamento)

    @property
    def valor_temperatura(self):
        return self.VALOR_TEMPERATURA

    def run(self):
        while True:
            time.sleep(1)
            self.VALOR_TEMPERATURA = self.get_amb_temp()
            self._dado.set_temperatura_sistema(self.VALOR_TEMPERATURA)
            #print(self.VALOR_TEMPERATURA)
    
    
    
    
    
    