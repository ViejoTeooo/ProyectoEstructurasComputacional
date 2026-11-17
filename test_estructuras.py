import heapq
import random
import pytest
from src.estructuras import Cola, Pila, MonticuloMin


def test_pila_lifo_y_vacia():
    p = Pila()
    p.push("a"); p.push("b")
    assert p.peek() == "b"
    assert p.pop() == "b"
    assert p.pop() == "a"
    assert p.vacia()
    with pytest.raises(IndexError):
        p.pop()


def test_cola_fifo_y_vacia():
    c = Cola()
    c.encolar(1); c.encolar(2)
    assert c.desencolar() == 1
    assert c.desencolar() == 2
    assert c.vacia()
    with pytest.raises(IndexError):
        c.desencolar()


def test_monticulo_contra_heapq():
    propio, referencia = MonticuloMin(), []
    rnd = random.Random(17)
    for i in range(1000):
        if rnd.random() < .65 or not referencia:
            prioridad = rnd.randrange(10000) + i / 100000
            propio.insertar(prioridad, i)
            heapq.heappush(referencia, (prioridad, i))
        else:
            assert propio.extraer() == heapq.heappop(referencia)
    while referencia:
        assert propio.extraer() == heapq.heappop(referencia)
    with pytest.raises(IndexError):
        propio.extraer()
