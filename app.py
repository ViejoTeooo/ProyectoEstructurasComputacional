"""Menú de consola para consultar rutas óptimas del dataset CSV."""
from pathlib import Path
from .persistencia import cargar_csv
from .algoritmos import dijkstra, ruta


def ejecutar(ruta_csv):
    g = cargar_csv(ruta_csv, dirigido=True)
    vertices = g.vertices()
    print(f"Red cargada: {len(vertices)} vértices, {g.num_aristas()} arcos")
    print("Vértices:", ", ".join(vertices))
    while True:
        print("\n1. Calcular ruta óptima\n2. Listar vértices\n0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            return
        if opcion == "2":
            for v in vertices:
                print(f"- {v}: {len(g.vecinos(v))} salidas")
            continue
        if opcion != "1":
            print("Opción no válida.")
            continue
        origen = input("Origen (exacto): ").strip()
        destino = input("Destino (exacto): ").strip()
        if origen not in g.adj or destino not in g.adj:
            print("Origen o destino no existe en el CSV.")
            continue
        dist, prev, relajaciones = dijkstra(g, origen)
        camino = ruta(prev, origen, destino)
        if not camino:
            print(f"No existe ruta dirigida de {origen} a {destino}.")
            continue
        print("Ruta:", " -> ".join(camino))
        print(f"Tiempo mínimo: {dist[destino]:g} minutos")
        print(f"Arcos examinados: {relajaciones}")


if __name__ == "__main__":
    archivo = Path(__file__).resolve().parent.parent / "datos" / "red_ejemplo.csv"
    ejecutar(input(f"CSV [{archivo}]: ").strip() or archivo)
