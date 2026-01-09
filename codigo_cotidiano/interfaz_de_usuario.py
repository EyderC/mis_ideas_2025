
print('\nnombres de columnas de la tabla de datos:'.upper())
nombre_columnas = []
columna = input('\t\t- ')
while(columna != 'salir'):
    if columna != 'salir' and columna != '':
        nombre_columnas.append(columna)

    columna = input('\t\t- ')
    

print(nombre_columnas)