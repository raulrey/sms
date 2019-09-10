#ENCIENDE MODULO A6
import RPi.GPIO as gpio
import time
#BCM respeta la nomenclatura de la raspberry
#BOARD numeracion por la posicion que se encentran, pares los de afuera impares los de adentro
gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)  #RESET
gpio.setup(24, gpio.OUT)  #POWER
print("enciende")
gpio.output(24, True) # encendido
time.sleep(2)
gpio.output(24, False)
print("espera")
time.sleep(15)
print("Apaga")
gpio.output(23, False)
time.sleep(1)
gpio.output(23, True)
gpio.cleanup() #gpio.cleanup(23) EN CASO DE LIBERAR SOLO UN  PUERTO 
            
  
