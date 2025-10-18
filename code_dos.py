

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
UNICODE_CUADRADO_MARRON = 0X1F7EB
CUADRADO_MARRON = chr(UNICODE_CUADRADO_MARRON)

for item in range(3):           #contruye una fila de 3 cuadrados marrones 
    print("🟫", end='')
print('')
input()
os.system(BORRAR)

for item in range(2):            #contruye un bloque de 2x2 cuadrados marrones 
    for item in range(2):
        print("🟫", end='')
    print('')
                
input()         
os.system(BORRAR)       #borra la pantalla 

for item in range(2):       #construye un techo de longitud de 30 bloques de 2x2 con una separación de un espacio 
    for item in range(30):      #si tu pantalla no es muy grande reduce la cantidad de bloques
        for item in range(2):
            print("🟫", end='')
            print('',end='') 
        print('', end='')
    print('')


for item in range(7):       #construye un muro de 5 x 7 cuadriculas a 25 espacios desdde el inicio de la linea
    for item in range(25):  # y en cada linea a 20 espacios crea una fila de tres cuadriculas   
        print(" ", end='')
    print("🟫"*5, end='')
    for item in range(20):      
        print(' ', end='')
    print("🟫"*3)

for item in range(4):       #a una distancia de 60 espacios crea un bloque de 4x3 para continuar el muro 
    for item in range(55):
        print(" ", end='')
    print("🟫"*3)

#A PARTIR DE AQUI USAR IF PARA INTENTAR CREAR LA ESCALERA DESCENDENTE #

for item in range(28):      #crea una fila de 4 cuadrados a una distancia de 28 espacios
    print(" ", end='')
print("🟫"*4)  
for item in range(28):      #crea una fila de 4 cuadrados a una distancia de 28 espacios
    print(" ", end='')     
print("🟫"*4)

for item in range(24):      #crea una fila de 6 cuadrados a una distancia de 25 espacios
    print(" ", end='')
print("🟫"*6)  
for item in range(24):      #crea una fila de 8 cuadrados a una distancia de 25 espacios
    print(" ", end='')
print("🟫"*6)


    

for item in range(5):       #construye un bloque de  5x20 a una distancia de 24 espacios desde el inicio
    for item in range(24):
        print(" ", end='')
    print("🟫"*20)



for item in range(2):       #construye un piso de 30 bloques de 2x2
    for item in range(60):
        print("🟫",end='')
    print('')
input()
print(MOSTRAR_CURSOR)