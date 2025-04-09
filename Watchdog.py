import threading
import time
from Saidas import Saidas

class Watchdog(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.out = Saidas()
        
    def run(self):
        while True:
            self.out.watchdog(1)
            time.sleep(0.01)
            self.out.watchdog(0)
            time.sleep(0.01)
