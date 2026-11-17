"""Estructuras auxiliares propias del proyecto (sin deque ni heapq)."""


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    def __init__(self):
        self._tope = None
        self._n = 0

    def push(self, dato):
        self._tope = Nodo(dato, self._tope)
        self._n += 1

    def pop(self):
        if self._tope is None:
            raise IndexError("pop sobre pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        self._n -= 1
        return dato

    def peek(self):
        if self._tope is None:
            raise IndexError("peek sobre pila vacía")
        return self._tope.dato

    def vacia(self):
        return self._tope is None

    def __len__(self):
        return self._n


class Cola:
    def __init__(self):
        self._frente = self._final = None
        self._n = 0

    def encolar(self, dato):
        nodo = Nodo(dato)
        if self._final is None:
            self._frente = self._final = nodo
        else:
            self._final.siguiente = nodo
            self._final = nodo
        self._n += 1

    def desencolar(self):
        if self._frente is None:
            raise IndexError("desencolar sobre cola vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._n -= 1
        return dato

    def vacia(self):
        return self._frente is None

    def __len__(self):
        return self._n


class MonticuloMin:
    """Montículo binario mínimo propio; almacena pares (prioridad, dato)."""
    def __init__(self):
        self._a = []

    def insertar(self, prioridad, dato):
        self._a.append((prioridad, dato))
        i = len(self._a) - 1
        while i > 0:
            p = (i - 1) // 2
            if self._a[p][0] <= self._a[i][0]:
                break
            self._a[p], self._a[i] = self._a[i], self._a[p]
            i = p

    def extraer(self):
        if not self._a:
            raise IndexError("extraer sobre montículo vacío")
        minimo = self._a[0]
        ultimo = self._a.pop()
        if self._a:
            self._a[0] = ultimo
            i, n = 0, len(self._a)
            while True:
                menor = i
                izq, der = 2 * i + 1, 2 * i + 2
                if izq < n and self._a[izq][0] < self._a[menor][0]:
                    menor = izq
                if der < n and self._a[der][0] < self._a[menor][0]:
                    menor = der
                if menor == i:
                    break
                self._a[i], self._a[menor] = self._a[menor], self._a[i]
                i = menor
        return minimo

    def __len__(self):
        return len(self._a)
