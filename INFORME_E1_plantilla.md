# Plantilla del informe — Proyecto 1

Completar y adaptar en procesador de texto. La consigna exige PDF, formato IEEE, 5–8 páginas. Reemplaza las indicaciones entre corchetes; esta plantilla no es un informe final listo para entregar.

## Portada y registro

**Rutas óptimas en la red vial del Alto Magdalena**  
Asignatura: Estructura de Datos · Proyecto 1  
Integrantes: [nombres del grupo de 2–3]  
Docente: Ing. Edicson Pineda Cadena  
Universidad Piloto de Colombia, Seccional del Alto Magdalena  
Fecha: [fecha efectiva]

## Resumen

[Problema, modelo, algoritmo y resultado principal en 100–150 palabras.]

## 1. Contexto y modelado

Se modela la red vial como `G=(V,E)`. Cada vértice representa [intersección/municipio definido]; cada arco dirigido `u→v` representa un tramo transitable desde `u` hasta `v`; el peso `w(u,v)` es [tiempo en minutos, fuente y criterio]. Los pesos son no negativos, condición necesaria para Dijkstra.

**Supuestos y delimitaciones:** [qué se considera intersección; sentidos únicos; condición de tráfico; datos omitidos].  
**Fuente y fecha de los datos:** [mapa/servicio, fecha; citar correctamente].

## 2. Instancia de ejemplo

Usa 8–12 vértices y marca si la instancia es didáctica o real.

**Figura 1. Grafo dirigido:** [insertar dibujo con flechas, etiquetas y peso en minutos].  
**Lista de adyacencia:** [cada origen y sus pares (destino,peso)].  
**Matriz:** filas=origen; columnas=destino; `∞` significa que no existe arco; diagonal [definir].  
**Lista de aristas:** `origen | destino | peso (min)`.

## 3. Representaciones

| Representación | Memoria | Consultar arco | Recorrer vecinos de u | Agregar arco |
|---|---:|---:|---:|---:|
| Lista de adyacencia | Θ(V+E) | O(grado(u)) | O(grado(u)) | O(1) amortizado |
| Matriz | Θ(V²) | O(1) | O(V) | O(1) |
| Lista de aristas | Θ(E) | O(E) | O(E) | O(1) amortizado |

**Elección para Dijkstra:** [justificar según dispersidad, memoria y recorrido de vecinos].

## 4. TAD y UML

Inserta UML coherente con `src/`. Para cada método especifica firma, propósito, precondición, postcondición, excepción y costo.

| TAD | Operación | Precondición | Postcondición | Excepción | Costo |
|---|---|---|---|---|---|
| Grafo | `agregar_arista(u,v,w)` | peso ≥ 0 | registra arco dirigido | `ValueError` si peso negativo | O(1) amortizado |
| Grafo | `vecinos(u)` | u existe | retorna arcos salientes | `KeyError` si falta u | O(1) para acceder a lista |
| Montículo | `insertar(p,d)` | — | agrega entrada y conserva propiedad heap | — | O(log n) |
| Montículo | `extraer()` | no vacío | retorna/elimina mínima prioridad | `IndexError` vacío | O(log n) |
| Cola | `encolar(x)` | — | agrega al final | — | O(1) |
| Cola | `desencolar()` | no vacía | retorna/elimina frente | `IndexError` vacía | O(1) |
| Pila | `push(x)` / `pop()` | para pop: no vacía | LIFO | `IndexError` pop vacía | O(1) |

## 5. Traza manual de Dijkstra

Origen: [s]. Destino: [t].

| Paso | Mínimo extraído | Montículo (arreglo) | Distancias | Predecesores | Relajaciones |
|---:|---|---|---|---|---|
| 0 | — | `[(0,s)]` | s:0; demás:∞ | — | inicialización |
| 1 | [completar] | [completar] | [completar] | [completar] | [completar] |

Ruta final: [secuencia]. Tiempo total: [suma] minutos. Las entradas `(d,u)` con `d > dist[u]` se descartan como obsoletas.

## 6. Complejidad

| Operación/algoritmo | Complejidad | Supuestos |
|---|---:|---|
| Montículo insertar/extract-min | O(log n) | n entradas actuales |
| Dijkstra con montículo lazy | O((V+E) log E), típicamente O((V+E) log V) | listas, grafo simple |
| Dijkstra con lista no ordenada | O(V²+E), típicamente O(V²) | selección lineal del mínimo |
| Memoria adicional Dijkstra | O(V+E) en peor caso | duplicados pueden llegar a E |

## 7. Repositorio, referencias y uso de IA

URL GitHub: [pegar URL pública]. El repo incluye código, README, datos y evidencia reproducible. Cita libros, documentación, mapa, datasets y código externo. Declara herramienta de IA, alcance de asistencia y revisión humana.
