# Proyecto 1: Rutas óptimas en la red vial del Alto Magdalena

Implementación académica de rutas de menor tiempo para un grafo vial dirigido. **Los datos de ejemplo son ilustrativos y no deben presentarse como mediciones reales.** Reemplázalos por tiempos verificados en una fuente cartográfica, anota fuente y fecha, y revisa sentidos de circulación antes de entregar.

## Requisitos

- Python 3.11 o superior.
- Instalar dependencias de desarrollo con `python -m pip install -r requirements.txt`.
- La solución implementa sus propias clases `Cola`, `Pila` y `MonticuloMin`; no usa `collections.deque`, `heapq` ni `networkx` en los algoritmos de producción. Esas bibliotecas se reservan para pruebas y comparación.

## Estructura

```text
src/             estructuras, grafos, algoritmos, app y carga CSV
datos/           instancias de demostración y datos reales documentados
tests/           pruebas de estructuras, algoritmos y validación cruzada
rendimiento/     benchmark reproducible y gráficas
docs/            plantilla de informe y especificaciones
```

## Iniciar la aplicación

Desde la carpeta raíz del repositorio:

```bash
python -m src.app
```

El menú permite listar vértices y calcular una ruta por identificadores exactos. Para cargar otro CSV, usa `from src.app import ejecutar; ejecutar("datos/red_real.csv")`.

## Uso desde Python

```python
from src.persistencia import cargar_csv
from src.algoritmos import dijkstra, ruta

g = cargar_csv("datos/red_ejemplo.csv", dirigido=True)
dist, prev, relajaciones = dijkstra(g, "Girardot_Centro")
destino = "Ricaurte_Centro"
print("Tiempo:", dist[destino], "min")
print("Ruta:", ruta(prev, "Girardot_Centro", destino))
```

Los identificadores de vértices deben coincidir exactamente con el CSV. Si la distancia es `inf`, no existe una ruta dirigida desde el origen al destino.

## Pruebas y rendimiento

```bash
pytest -v
python rendimiento/medir.py
python rendimiento/graficar.py
```

Las pruebas comparan el montículo propio con `heapq` y las distancias con NetworkX. Estas bibliotecas se usan solo para validación. El benchmark usa grafos dirigidos dispersos reproducibles y verifica que las distancias coincidan antes de medir. La versión de lista no ordenada se limita por defecto a 3.000 vértices para evitar tiempos excesivos; el umbral se configura en `rendimiento/medir.py`.

Los resultados generados incluyen promedio y desviación; reporta también CPU, versión de Python, semilla, tamaño y repeticiones al presentar el experimento.

## Datos

`datos/red_ejemplo.csv` es una instancia pequeña **ficticia** para practicar la traza. Para la entrega, crea `datos/red_real.csv` con 15–25 puntos de Girardot y municipios vecinos, tiempos en minutos, calles de un solo sentido representadas con arcos y referencia/fecha de consulta. No mezcles ambos conjuntos en las conclusiones.

## Entregas

- **1:** informe IEEE de 5–8 páginas; modelo, instancia dibujada de 8–12 vértices con lista/matriz/aristas, costos, TAD, UML, traza manual de Dijkstra, complejidades y URL del repo con `Nodo` y `Grafo` funcionales.
- **2:** completar/explicar `Grafo`, `MonticuloMin` y Dijkstra; pruebas de montículo contra `heapq` y distancias contra `networkx`; versión funcional con lista no ordenada para la comparación.
- **3:** experimento en tamaños desde `10²` hasta `10⁴` vértices; comparar montículo propio, lista no ordenada y `heapq`; gráficas, discusión del costo y dibujo de la ruta sobre mapa. Usa escalas posibles, repeticiones y semillas documentadas; la lista no ordenada puede volverse muy lenta en 10⁴, así que registra honestamente el límite/tiempo.

## Registro de datos que debe acompañar al CSV real

En el informe indica el servicio cartográfico consultado, fecha, criterio de tiempo (estimado para qué condición si aparece), criterios para convertir intersecciones en nodos, y cómo se decidieron los sentidos. El docente sugiere tiempos tomados de un mapa; cita la fuente según la política académica y no inventes mediciones.

## Honestidad académica

Declara en un anexo el uso de herramientas de IA, conforme a la instrucción del docente. Cada integrante debe poder explicar cada función y los resultados.

## Contenido del repositorio

- `src/estructuras.py`: Nodo, Cola, Pila y MonticuloMin propios.
- `src/grafo.py`: Grafo de listas y GrafoMatriz.
- `src/algoritmos.py`: BFS, DFS, Dijkstra y variante no ordenada.
- `src/persistencia.py`: lectura validada de CSV.
- `src/generador.py`: generador de grafos con semilla.
- `src/app.py`: menú de consola.
- `tests/`: pruebas automatizadas.
- `rendimiento/`: medición y gráfica log-log.
- `docs/`: plantilla de informe para la Entrega 1.
