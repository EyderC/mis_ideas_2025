from pathlib import Path

archivo = Path("ejercicios.txt")


cargas_inciales = []
tipo_ejercicio = {
    'ejercicio':'press plano',
    'carga': 70,
    'repeticiones': 12
}

archivo.write_text(str(tipo_ejercicio['carga']))
