
import time     #importa la biblioteca para manjeo del tiempo 
import os       #importa la biblioteca de manejo del sistema operativo

BORRAR = 'clear'        #crea una constante con comando de borrado de consola en linux
OCULTAR_CURSOR = '\033[?025l' #crea una constante para ocultar el cursor de la consola
MOSTRAR_CURSOR = '\033[?025h' #crea una constante para mostrar el cursor en la consola
UN_SEGUNDO = 1      #crea variable para manejo del tiempo en segundos

print(OCULTAR_CURSOR,end='')      #ocualta el cursor de la consola de linux y mantenerlo en la misma posición
os.system(BORRAR)       #borra toda la pantalla ('clear' en consolas unix y 'cls' en windows)

input()     #recibe la tecla enter para avanzar a la siguiente instrucción 

print('¡HOLA MUNDO!'+' hagamos algo genial con python!'.title() )       #imprime el popular hola mundo 
print("👾 Bienvenido a un nuevo universo🧱".title())        #imprime mensaje de bienvenida con emojis       
input()     #recibe la tecla enter para avanzar a la siguiente instrución 


UNICODE_CORAZON = 0X2764    #crear una constante para el unicode del caracter corazón
UNICODE_COLOR_ROJO = 0XFE0F     #crear una constante para el unicode del atributo color rojo del corazón
UNICODE_CUADRADO_BLANCO = 11036     #crea una constante para almacenar UNICODE de cuadrado blanco (11036)

CORAZON = chr(UNICODE_CORAZON)       #convierte UNICODE del corazón a caracter de cadena
ROJO = chr(UNICODE_COLOR_ROJO)      #convierte unicode del color rojo del corazón a caracter de cadena

os.system(BORRAR)       #borra la pantalla 

print(CORAZON + ROJO)     #Imprime un corazón rojo 
time.sleep(UN_SEGUNDO)      #Pausa por un segundo 
os.system(BORRAR)     #Borra el corazón
time.sleep(UN_SEGUNDO)      #Pausa por un segundo

print(CORAZON + ROJO) 
time.sleep(UN_SEGUNDO)
os.system(BORRAR)
time.sleep(UN_SEGUNDO)

print(CORAZON + ROJO)
time.sleep(UN_SEGUNDO)
os.system(BORRAR)
time.sleep(UN_SEGUNDO)

print(CORAZON + ROJO)
time.sleep(UN_SEGUNDO)
os.system(BORRAR)
time.sleep(UN_SEGUNDO)

print(CORAZON + ROJO)
time.sleep(UN_SEGUNDO)
os.system(BORRAR)
time.sleep(UN_SEGUNDO)



# Tiempo aprox. = 30min
#-----------------------------------------------------------------------
input()     #espera hasta que pulses enter
DECIMA_DE_SEGUNDO = 0.1    #crea una constante de tiempo para una decima de segundo

os.system(BORRAR)       #borra la pantalla
print(f"¡programar en python acelera mi corazón! {CORAZON + ROJO}".title())      #imprime un mensaje que acelere tu corazón 
input()     #espera hast que pulses enter
os.system(BORRAR)       #borra la pantalla


for item in range(1500):       #muestra un corazon rojo latiendo 15 veces usando un bucle cada decima de segundo = 0.1
        print(CORAZON + ROJO)
        time.sleep(DECIMA_DE_SEGUNDO)
        os.system(BORRAR)    
        time.sleep(DECIMA_DE_SEGUNDO)

#---------------------------------------------------------------------------

print(MOSTRAR_CURSOR)
