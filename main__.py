#############################################################################################
# RoboCore - Primeiros Passos com a Raspberry Pi Pico com Python
# Faz o LED conectado ao GPIO 25 (LED interno da placa) piscar de 1 em 1 segundo.
#############################################################################################

#adiciona a instancia "Pin" da biblioteca "machine" ao codigo
from machine import Pin

#adiciona a funcao "sleep" da biblioteca "time" ao codigo
from time import sleep

from Devices import Device

#configura o pino conectado ao LED da placa como uma saida
led = Pin(25, Pin.OUT)

device = Device()
device.executa()


#executa infinitamente
while True:
    led.high() #acende o LED
    sleep(0.2) #aguarda 1 segundo
    led.low() #apaga o LED
    sleep(0.2) #aguarda 1 segundo
    
    print('Katia Cilene')