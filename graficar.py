"""Genera gráfica comparativa desde rendimiento/resultados.csv."""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def graficar(entrada=None, salida=None):
    base = Path(__file__).resolve().parent
    entrada = Path(entrada or base / "resultados.csv")
    salida = Path(salida or base / "tiempos_dijkstra.png")
    datos = defaultdict(list)
    with entrada.open(encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            datos[fila["metodo"]].append((int(fila["n"]), float(fila["media_segundos"])))
    for metodo, puntos in datos.items():
        puntos.sort()
        plt.loglog([x for x, _ in puntos], [y for _, y in puntos], "o-", label=metodo)
    plt.xlabel("Número de vértices (V)")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.title("Comparación de implementaciones de Dijkstra")
    plt.grid(True, which="both", alpha=.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(salida, dpi=160)
    plt.close()
    return salida


if __name__ == "__main__":
    print(graficar())
