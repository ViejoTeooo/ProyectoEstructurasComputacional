"""Validación cruzada opcional con NetworkX, biblioteca solo de pruebas."""
import pytest
nx = pytest.importorskip("networkx")
from src.generador import grafo_aleatorio
from src.algoritmos import dijkstra


@pytest.mark.parametrize("semilla", range(10))
def test_distancias_contra_networkx(semilla):
    g = grafo_aleatorio(25, 80, dirigido=True, semilla=semilla)
    dist, _, _ = dijkstra(g, "0")
    ref = nx.DiGraph()
    ref.add_nodes_from(g.vertices())
    for u in g.vertices():
        for v, w in g.vecinos(u):
            ref.add_edge(u, v, weight=w)
    esperado = nx.single_source_dijkstra_path_length(ref, "0", weight="weight")
    for v in g.vertices():
        assert dist[v] == esperado.get(v, float("inf"))
