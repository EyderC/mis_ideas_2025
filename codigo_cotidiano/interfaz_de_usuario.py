import csv


print('\nnombres de columnas de la tabla de datos:'.upper())
encabezado = []
columna = input('\t\t- ')
while(columna != 'salir'):
    if columna != 'salir' and columna != '': #Para que estas dos opciones no se guarden como encabezados 
        encabezado.append(columna)

    columna = input('\t\t- ')

nombre_archivo = input('nombre del archivo para guardar datos: '.title())
nombre_archivo.rstrip()
nombre_archivo.lstrip()
nombre_archivo.lower()

with open(nombre_archivo,'w', newline='', encoding='utf-8') as archivo_csv:
    escribir = csv.writer(archivo_csv)
    escribir.writerow(encabezado)






