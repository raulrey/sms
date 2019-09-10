import serial
import os
import RPi.GPIO as GPIO
import time
import sys
import keyboard # pip3 install keyboard
import socket
import select

os.system('clear')
print ("SMS Read Server")
# Puerto Serie configuracion
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)
tiempo =0.2




def resetPort():
    print ("Reset Serial Buffer")
    port.flushInput()
    port.flushOutput()
    time.sleep(1)
    port.write(str.encode('AT\r'))
    time.sleep(1)
    port.write(str.encode('AT+CMGF=1\r'))
    time.sleep(1)
    port.write(str.encode('AT+CSQ=?\r'))
    time.sleep(1)
    port.write(str.encode('AT+CMGS=3434800336\r'))
    time.sleep(1)
    port.write(str.encode('INICIO MODULO SMS'+chr(26)))

def readPort():
    message=""
    fin = "True"
    if port.inWaiting() > 0:
        fin = "False"
        r = ""
    while fin == "False":
        if port.inWaiting() > 0:
            r = port.readline().decode()
            message = r
            fin = "True"
    return message

def writePort(numero, dato):
    port.flushInput()
    port.flushOutput()
    time.sleep(1)
    port.write(str.encode('AT\r'))
    time.sleep(1)
    port.write(str.encode('AT+CMGF=1\r'))
    time.sleep(1)
    port.write(str.encode('AT+CSQ=?\r'))
    time.sleep(1)
    port.write(str.encode('AT+CMGS=' + numero + '\r'))
    time.sleep(1)
    port.write(str.encode(dato + chr(26)))

def enviar(mensaje):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("45.162.140.70",8887))
    server_socket.send(mensaje.encode("utf-8"))                      


resetPort()

bucle=True
print ("Iniciado") 
while bucle:
    # SOCKET ESCUCHA
  
            

    # COMANDOS AT
    message = readPort()
    if message != "":
        print (message)

        if message[0:16]=='+CIEV: "MESSAGE"':
            print ("Mensaje de entrada")
            message = readPort()
            print ("Cabecera de mensaje:", message)
            
            message = readPort()
            print ("Mensaje completo: ", message)
            comilla1=message.find('"')
            comilla2=message.find('"',comilla1+1)
            comilla3=message.find('"',comilla2+1)
            comilla4=message.find('"',comilla3+1)

            numero = message[int(comilla1+1): int(comilla2)]
            fecha = message[int(comilla3+1): int(comilla4)]
            print ("Numero")            
            print (numero)
            print ("Fecha")
            print(fecha)

            message = readPort()
            print ("Dato")
            print (message)
            print ("Cabecera de mensaje: ", message[0:3])
            
            message = message + "@numero:" + numero
            print ("Mensaje con numero: ",message)
            
            
            if message[0:3]=="A1@":
                try:
                    enviar(message)
                    print ("Enviando Mensaje por socket: ", message)
                    
                except Exception as e:
                    print ("Error de socket: ", e)
                    writePort(numero, "Sin Servicio")

                    
                    
                

        if message[0:13]=='+CIEV: "CALL"':
            print ("Llamada de entrada")

    if keyboard.is_pressed('q'):
        print ("bye bye")
        time.sleep(1)
        bucle = False
    
