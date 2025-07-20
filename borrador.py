

import time     #importa la biblioteca para manjeo del tiempo 
import os       #importa la biblioteca de manejo del sistema operativo

BORRAR = 'clear'        #crea una constante con comando de borrado de consola en linux
OCULTAR_CURSOR = '\033[?025l' #crea una constante para ocultar el cursor de la consola
MOSTRAR_CURSOR = '\033[?025h' #crea una constante para mostrar el cursor en la consola
UN_SEGUNDO = 1      #crea variable para manejo del tiempo en segundos

print(OCULTAR_CURSOR,end='')      #ocualta el cursor de la consola de linux y mantenerlo en la misma posición
os.system(BORRAR)       #borra toda la pantalla ('clear' en consolas unix y 'cls' en windows)



UNICODE_CORAZON = 0X2764    #crear una constante para el unicode del caracter corazón
UNICODE_COLOR_ROJO = 0XFE0F     #crear una constante para el unicode del atributo color rojo del corazón
UNICODE_CUADRADO_BLANCO = 11036     #crea una constante para almacenar UNICODE de cuadrado blanco (11036)

CORAZON = chr(UNICODE_CORAZON)       #convierte UNICODE del corazón a caracter de cadena
ROJO = chr(UNICODE_COLOR_ROJO)      #convierte unicode del color rojo del corazón a caracter de cadena


#---------------------------------------------------------------------------
input()

for item in range(3):           #contruye una fila de 3 cuadrados marrones 
    print("🟫", end='')
print('')
input()
os.system(BORRAR)

for item in range(2):            #contruye un bloque de 2x2 cuadrados marrones 
    for item in range(2):
        print("🟫", end='')
    print('')
                #construye un techo de longitud de 30 bloques de 2x2 con una separación de un espacio 
input()         #si tu pantalla no es muy grande reduce la cantidad de bloques
os.system(BORRAR)

for item in range(2):
    for item in range(30):
        for item in range(2):
            print("🟫", end='')
            print('',end='') 
        print('', end='')
    print('')


for item in range(7):       #construye un muro de 5 x 7 cuadriculas a 15 espacios desdde el inicio de la linea
    for item in range(15):       #crea 15 espacios seguidos en la misma linea 
        print(" ", end='')
    print("🟫"*5, end='')
    for item in range(15):
        print(' ', end='')
    print("🟫"*3)

for item in range(5):
    for item in range(40):
        print(" ", end='')
    print("🟫"*3)

#crea un esṕacio de 5 print
for item in range(5):
    print('')
    
#construye un bloque de  5x20 a una distancia de 20 espaciosd esde el inicio
for item in range(5):
    for item in range(20):
        print(" ", end='')
    print("🟫"*20)

#construye un piso de 30 bloques de 2x2

for item in range(2):
    for item in range(60):
        print("🟫",end='')
    print('')
input()
print(MOSTRAR_CURSOR)