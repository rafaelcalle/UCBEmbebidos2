import RPi.GPIO as GPIO # importamos librerias de pines y tiempo
import time

GPIO.cleanup() # limpiamos los pines
GPIO.setmode(GPIO.BOARD) # Definimos la configuracion de los Pines

GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Definimos el pin 3 como entrada y de caracteristica Pullup
GPIO.setup(5,GPIO.OUT) # Definimos el pin 5 como salida
flag = False # Establecemos una bandera
while True: # Iniciamos un While Eterno
	if GPIO.input(3): # leemos el pin
		b = 1 # no se toma en cuenta por ahora
	else:
		flag = not flag # invertimos la bandera
	time.sleep(0.1) # damos una pausa

	if flag: # Preguntamos el estado de la bandera
		GPIO.output(5,1) # Encendemos el led
	else:
		GPIO.output(5,0) # Apagamos el Led
	time.sleep(0.1) # damos una pausa
