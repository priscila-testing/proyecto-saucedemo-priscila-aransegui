import csv
import os

def leer_csv_login():
    ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "data_login.csv")
    datos = []
    with open(ruta, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            debe_funcionar = fila["debe_funcionar"].strip() == "True"
            datos.append((fila["usuario"], fila["password"], debe_funcionar))
    return datos

# Solo para probar el archivo SOLO (no cuando lo importás)
if __name__ == "__main__":
    print(leer_csv_login())