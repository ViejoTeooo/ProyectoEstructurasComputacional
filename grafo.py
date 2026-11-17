"""Grafo dirigido con listas de adyacencia y matriz de adyacencia."""


class Grafo:
    def __init__(self, dirigido=True):
        self.adj = {}
        self.dirigido = dirigido

    def agregar_vertice(self, u):
        self.adj.setdefault(u, [])

    def agregar_arista(self, u, v, peso):
        if peso < 0:
            raise ValueError("Dijkstra requiere pesos no negativos")
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adj[u].append((v, float(peso)))
        if not self.dirigido:
            self.adj[v].append((u, float(peso)))

    def vertices(self):
        return list(self.adj)

    def vecinos(self, u):
        if u not in self.adj:
            raise KeyError(f"Vértice desconocido: {u}")
        return self.adj[u]

    def num_aristas(self):
        m = sum(map(len, self.adj.values()))
        return m if self.dirigido else m // 2


class GrafoMatriz:
    """Usa None para ausencia de arista; los índices corresponden a vertices."""
    def __init__(self, vertices, dirigido=True):
        self.vertices = list(vertices)
        self.indice = {v: i for i, v in enumerate(self.vertices)}
        if len(self.indice) != len(self.vertices):
            raise ValueError("Los vértices deben ser únicos")
        self.dirigido = dirigido
        n = len(self.vertices)
        self.matriz = [[None] * n for _ in range(n)]

    def agregar_arista(self, u, v, peso):
        if peso < 0:
            raise ValueError("Dijkstra requiere pesos no negativos")
        i, j = self.indice[u], self.indice[v]
        self.matriz[i][j] = float(peso)
        if not self.dirigido:
            self.matriz[j][i] = float(peso)

    def existe_arista(self, u, v):
        return self.matriz[self.indice[u]][self.indice[v]] is not None

    def vecinos(self, u):
        i = self.indice[u]
        return [(self.vertices[j], w) for j, w in enumerate(self.matriz[i]) if w is not None]
