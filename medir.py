"""Benchmark reproducible de Dijkstra propio, lista no ordenada y heapq."""
import csv
import heapq
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.algoritmos import dijkstra, dijkstra_lista
from src.generador import grafo_aleatorio, cantidad_aristas_dispersa


def dijkstra_heapq(g, origen):
    """Referencia de biblioteca; no se usa en la implementación de producción."""
    dist = {u: float("inf") for u in g.vertices()}
    prev = {}
    dist[origen] = 0.0
    pq = [(0.0, origen)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g.vecinos(u):
            nueva = d + w
            if nueva < dist[v]:
                dist[v], prev[v] = nueva, u
                heapq.heappush(pq, (nueva, v))
    return dist, prev


def medir(funcion, *args, repeticiones=5):
    funcion(*args)  # calentamiento no contabilizado
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion(*args)
        tiempos.append(time.perf_counter() - inicio)
    media = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos) if len(tiempos) > 1 else 0.0
    return media, desviacion


def ejecutar(tamanos=(100, 300, 1000, 3000, 10000), repeticiones=5,
             grado_medio=3, semilla=2026, incluir_lista_hasta=3000):
    salida = Path(__file__).resolve().parent / "resultados.csv"
    filas = []
    for n in tamanos:
        m = cantidad_aristas_dispersa(n, grado_medio, dirigido=True)
        g = grafo_aleatorio(n, m, dirigido=True, semilla=semilla + n)
        origen = "0"
        propio, _prev, _ops = dijkstra(g, origen)
        referencia, _ = dijkstra_heapq(g, origen)
        if propio != referencia:
            raise AssertionError(f"Distancias distintas para n={n}")
        metodos = [("monticulo_propio", dijkstra)]
        if n <= incluir_lista_hasta:
            metodos.append(("lista_no_ordenada", dijkstra_lista))
        metodos.append(("heapq", lambda grafo, s: (*dijkstra_heapq(grafo, s), 0)))
        for nombre, funcion in metodos:
            media, desv = medir(funcion, g, origen, repeticiones=repeticiones)
            filas.append({"n": n, "m": m, "semilla": semilla + n,
                          "metodo": nombre, "repeticiones": repeticiones,
                          "media_segundos": f"{media:.9f}",
                          "desviacion_segundos": f"{desv:.9f}"})
            print(f"n={n:5} m={m:6} {nombre:20} media={media:.6f}s desv={desv:.6f}s")
    with salida.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=filas[0].keys())
        escritor.writeheader()
        escritor.writerows(filas)
    print(f"Resultados guardados en {salida}")


if __name__ == "__main__":
    ejecutar()
