import csv
from .grafo import Grafo


def cargar_csv(ruta, dirigido=True):
    g = Grafo(dirigido=dirigido)
    with open(ruta, newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        requeridas = {"origen", "destino", "peso"}
        if not lector.fieldnames or not requeridas.issubset(lector.fieldnames):
            raise ValueError("CSV debe tener columnas origen,destino,peso")
        for numero, fila in enumerate(lector, start=2):
            try:
                peso = float(fila["peso"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Peso inválido en fila {numero}") from exc
            g.agregar_arista(fila["origen"].strip(), fila["destino"].strip(), peso)
    return g
