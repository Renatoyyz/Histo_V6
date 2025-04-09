import threading
import time
from Saidas import Saidas
from Dados import Dado

class ControleProporcional(threading.Thread):
    def __init__(self, dado, saida):
        threading.Thread.__init__(self)
        self.out = saida
        self._dado = dado
        self.Et=0.0
        self.Mv=0.0
        self.Pb=0.0
        self.ton_pwm = 0.0
        self.toff_pwm = 0.0
            
    def run(self):
        while True:
            if self._dado.controle_estah_acionado == True and self.out.porta_in == 0:
                self.Et = self._dado.temperatura_set_point - self._dado.temperatura_sistema
                self.Pb = self._dado.ganho_poporcional_sistema

                if self.Pb < 0.2:
                    self.Pb = 0.2
                
                self.Mv = ( 100 / (self.Pb) ) * self.Et
                if self.Mv < 10:
                    self.Mv = 0
                if self.Mv > 100:
                    self.Mv = 100

                self.aciona_pwm(self.Mv)
                
                self.out.ventilador(1)
                self.out.magnetron(1)
                time.sleep(self.ton_pwm)
                self.out.magnetron(0)
                time.sleep(self.toff_pwm)

                # print(self.Et)
                # print(self.Pb)
                print(self.Mv)


            else:
                self.out.magnetron(0)
                self.out.ventilador(0)
                time.sleep(1)

    def aciona_pwm(self, porcento):
        self.ton_pwm = (porcento * self._dado.PERIODO_PWM)/100
        self.toff_pwm = self._dado.PERIODO_PWM - self.ton_pwm

if __name__ == '__main__':
    from Watchdog import Watchdog
    dado = Dado()
    dado.set_tamanho_da_amostra(dado.TAMANHO_ESPECIAL)
 
    saidas = Saidas()
    wtd = Watchdog()

    dado.controle_estah_acionado = True
    dado.set_temperatura_sistema(20)
    dado.set_temperatura_set_point(40)
    dado.set_ganho_poporcional_sistema(6)

    controle = ControleProporcional(dado,saidas)

    controle.start()
    wtd.start()

    time.sleep(5)
    dado.set_temperatura_sistema(34.5)
    time.sleep(5)
    dado.set_temperatura_sistema(34.8)
    time.sleep(5)
    dado.set_temperatura_sistema(36)
    time.sleep(5)
    dado.controle_estah_acionado = False
