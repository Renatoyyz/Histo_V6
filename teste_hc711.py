from CelHC711 import CelHC711
import utime

cel = CelHC711(9,10, casa_decimal=0)

cel.run_cel()

while True:
    print(cel.valor_carga)
    utime.sleep(0.8)
