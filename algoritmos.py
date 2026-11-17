"""Algoritmos del Proyecto 1: BFS, DFS y Dijkstra con estructuras propias."""
from .estructuras import Cola, Pila, MonticuloMin


def bfs(g, origen):
    if origen not in g.adj:
        raise KeyError(f"Origen desconocido: {origen}")
    vistos, orden, cola = {origen}, [], Cola()
    cola.encolar(origen)
    while not cola.vacia():
        u = cola.desencolar()
        orden.append(u)
        for v, _ in g.vecinos(u):
            if v not in vistos:
                vistos.add(v)
                cola.encolar(v)
    return orden


def dfs(g, origen):
    if origen not in g.adj:
        raise KeyError(f"Origen desconocido: {origen}")
    vistos, orden, pila = set(), [], Pila()
    pila.push(origen)
    while not pila.vacia():
        u = pila.pop()
        if u in vistos:
            continue
        vistos.add(u)
        orden.append(u)
        for v, _ in reversed(g.vecinos(u)):
            if v not in vistos:
                pila.push(v)
    return orden


def dijkstra(g, origen):
    """Retorna distancias, predecesores y cantidad de relajaciones examinadas."""
    if origen not in g.adj:
        raise KeyError(f"Origen desconocido: {origen}")
    dist = {u: float("inf") for u in g.vertices()}
    prev, operaciones = {}, 0
    dist[origen] = 0.0
    pq = MonticuloMin()
    pq.insertar(0.0, origen)
    while pq:
        d, u = pq.extraer()
        if d > dist[u]:  # descarta una entrada antigua tras mejorar dist[u]
            continue
        for v, w in g.vecinos(u):
            operaciones += 1
            nueva = d + w
            if nueva < dist[v]:
                dist[v], prev[v] = nueva, u
                pq.insertar(nueva, v)
    return dist, prev, operaciones


def dijkstra_lista(g, origen):
    """Versión de referencia con cola no ordenada para comparar rendimiento."""
    if origen not in g.adj:
        raise KeyError(f"Origen desconocido: {origen}")
    dist = {u: float("inf") for u in g.vertices()}
    prev, pendientes, operaciones = {}, {origen}, 0
    dist[origen] = 0.0
    while pendientes:
        u = min(pendientes, key=dist.__getitem__)
        pendientes.remove(u)
        if dist[u] == float("inf"):
            break
        for v, w in g.vecinos(u):
            operaciones += 1
            nueva = dist[u] + w
            if nueva < dist[v]:
                dist[v], prev[v] = nueva, u
                pendientes.add(v)
    return dist, prev, operaciones


def ruta(prev, origen, destino):
    """Ruta origen-destino; retorna [] si el destino es inalcanzable."""
    if origen == destino:
        return [origen]
    camino, actual = [destino], destino
    while actual != origen:
        if actual not in prev:
            return []
        actual = prev[actual]
        camino.append(actual)
    return list(reversed(camino))
