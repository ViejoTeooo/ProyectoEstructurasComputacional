import math
import pytest
from src.grafo import Grafo, GrafoMatriz
from src.algoritmos import bfs, dfs, dijkstra, dijkstra_lista, ruta


def grafo_pequeno():
    g = Grafo(dirigido=True)
    for u, v, w in [("A", "B", 4), ("A", "C", 1), ("C", "B", 2),
                    ("B", "D", 1), ("C", "D", 8)]:
        g.agregar_arista(u, v, w)
    g.agregar_vertice("Z")
    return g


def test_dijkstra_y_ruta():
    g = grafo_pequeno()
    dist, prev, ops = dijkstra(g, "A")
    assert dist["D"] == 4
    assert ruta(prev, "A", "D") == ["A", "C", "B", "D"]
    assert math.isinf(dist["Z"])
    assert ruta(prev, "A", "Z") == []
    assert ops > 0


def test_lista_no_ordenada_equivale_al_monticulo():
    g = grafo_pequeno()
    d1, p1, _ = dijkstra(g, "A")
    d2, p2, _ = dijkstra_lista(g, "A")
    assert d1 == d2
    assert ruta(p1, "A", "D") == ruta(p2, "A", "D")


def test_dirigido_matriz_y_validaciones():
    g = Grafo(dirigido=True)
    g.agregar_arista("A", "B", 3)
    assert g.vecinos("B") == []
    m = GrafoMatriz(["A", "B"], dirigido=True)
    m.agregar_arista("A", "B", 3)
    assert m.existe_arista("A", "B")
    assert not m.existe_arista("B", "A")
    with pytest.raises(ValueError):
        g.agregar_arista("B", "A", -1)
    with pytest.raises(KeyError):
        dijkstra(g, "X")


def test_bfs_dfs_alcanzabilidad():
    g = grafo_pequeno()
    assert set(bfs(g, "A")) == {"A", "B", "C", "D"}
    assert set(dfs(g, "A")) == {"A", "B", "C", "D"}
