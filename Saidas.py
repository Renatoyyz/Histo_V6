import RPi.GPIO as GPIO

class Saidas:
    def __init__(self):
        self.PINO_PORTA = 40 
        
        self.PINO_BUZZER = 37
        self.PINO_WATCHDOG = 12
        self.PINO_MAG = 32
        self.PINO_VENT = 33
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        
        GPIO.setup(self.PINO_PORTA, GPIO.IN)
        
        GPIO.setup(self.PINO_BUZZER, GPIO.OUT)
        GPIO.setup(self.PINO_WATCHDOG, GPIO.OUT)
        GPIO.setup(self.PINO_MAG, GPIO.OUT)
        GPIO.setup(self.PINO_VENT, GPIO.OUT)
        
        GPIO.output(self.PINO_BUZZER, 0)
        GPIO.output(self.PINO_WATCHDOG, 0)
        GPIO.output(self.PINO_MAG, 0)
        GPIO.output(self.PINO_VENT, 0)

    @property
    def porta_in(self):
        return GPIO.input(self.PINO_PORTA)
        
    def buzzer(self, estado):
        if estado == 1:
            GPIO.output(self.PINO_BUZZER, 1)
        else:
            GPIO.output(self.PINO_BUZZER, 0)
            
    def watchdog(self, estado):
        if estado == 1:
            GPIO.output(self.PINO_WATCHDOG, 1)
        else:
            GPIO.output(self.PINO_WATCHDOG, 0)
            
    def magnetron(self, estado):
        if estado == 1:
            GPIO.output(self.PINO_MAG, 1)
        else:
            GPIO.output(self.PINO_MAG, 0)
            
    def ventilador(self, estado):
        if estado == 1:
            GPIO.output(self.PINO_VENT, 1)
        else:
            GPIO.output(self.PINO_VENT, 0)
            