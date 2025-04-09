import threading
import time
from Saidas import Saidas
from Dados import Dado

class Beep(threading.Thread):
    def __init__(self, dado):
        threading.Thread.__init__(self)
        self.out = Saidas()
        self.dado = dado
        
    def run(self):
        while True:
            if self.dado.aciona_buzzer == True:  
                print(self.out.porta_in)    
                self.out.buzzer(1)
                time.sleep(0.2)
                self.out.buzzer(0)
                time.sleep(0.2)
                self.dado.aciona_buzzer = False
                self.dado.beep_fim_processo = False
            if self.dado.beep_fim_processo == True:
                for i in range(1000):
                    print(i)
                    self.out.buzzer(1)
                    time.sleep(0.4)
                    self.out.buzzer(0)
                    time.sleep(0.4)
                    if self.dado.beep_fim_processo == False:
                        break
                    if self.out.porta_in == 1:
                        self.dado.beep_fim_processo = False
                self.dado.beep_fim_processo = False
            else:
                self.out.buzzer(0)
