"""Generación reproducible de grafos ponderados para rendimiento."""
import random
from .grafo import Grafo


def grafo_aleatorio(n, m, dirigido=True, pmin=1, pmax=100, semilla=None):
    if n <= 0:
        raise ValueError("n debe ser positivo")
    max_aristas = n * (n - 1) if dirigido else n * (n - 1) // 2
    if not 0 <= m <= max_aristas:
        raise ValueError(f"m debe estar entre 0 y {max_aristas}")
    if pmin < 0 or pmax < pmin:
        raise ValueError("Se requieren pesos no negativos y pmax >= pmin")
    rnd = random.Random(semilla)
    g = Grafo(dirigido=dirigido)
    for u in range(n):
        g.agregar_vertice(str(u))
    posibles = [(u, v) for u in range(n) for v in range(n)
                if u != v and (dirigido or u < v)]
    for indice in rnd.sample(range(len(posibles)), m):
        u, v = posibles[indice]
        g.agregar_arista(str(u), str(v), rnd.randint(pmin, pmax))
    return g


def cantidad_aristas_dispersa(n, grado_medio=3, dirigido=True):
    """Devuelve m para grafo disperso, limitado por el máximo simple."""
    maximo = n * (n - 1) if dirigido else n * (n - 1) // 2
    factor = grado_medio if dirigido else grado_medio / 2
    return min(maximo, max(0, int(n * factor)))
