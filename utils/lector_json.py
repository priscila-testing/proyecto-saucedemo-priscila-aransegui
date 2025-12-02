import json
from pathlib import Path

def leer_jason_productos(ruta_archivo):
    ruta = Path(ruta_archivo)

    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    nombres = [producto["nombre"] for producto in productos]
    return nombres