# Conteo de operaciones por paso

Convención: 1 flop equivale a una operación aritmética elemental (+, -, *, /). Las comparaciones, divisiones de búsqueda de pivote e intercambios se informan aparte.

## Corrida: Sin pivoteo

| Fase | Mult./Div. | Sumas/Restas | Flops | Comparaciones | Div. pivoteo | Intercambios |
|---|---:|---:|---:|---:|---:|---:|
| Eliminación 1 | 143 | 132 | 275 | 0 | 0 | 0 |
| Actualización de b 1 | 11 | 11 | 22 | 0 | 0 | 0 |
| Eliminación 2 | 120 | 110 | 230 | 0 | 0 | 0 |
| Actualización de b 2 | 10 | 10 | 20 | 0 | 0 | 0 |
| Eliminación 3 | 99 | 90 | 189 | 0 | 0 | 0 |
| Actualización de b 3 | 9 | 9 | 18 | 0 | 0 | 0 |
| Eliminación 4 | 80 | 72 | 152 | 0 | 0 | 0 |
| Actualización de b 4 | 8 | 8 | 16 | 0 | 0 | 0 |
| Eliminación 5 | 63 | 56 | 119 | 0 | 0 | 0 |
| Actualización de b 5 | 7 | 7 | 14 | 0 | 0 | 0 |
| Eliminación 6 | 48 | 42 | 90 | 0 | 0 | 0 |
| Actualización de b 6 | 6 | 6 | 12 | 0 | 0 | 0 |
| Eliminación 7 | 35 | 30 | 65 | 0 | 0 | 0 |
| Actualización de b 7 | 5 | 5 | 10 | 0 | 0 | 0 |
| Eliminación 8 | 24 | 20 | 44 | 0 | 0 | 0 |
| Actualización de b 8 | 4 | 4 | 8 | 0 | 0 | 0 |
| Eliminación 9 | 15 | 12 | 27 | 0 | 0 | 0 |
| Actualización de b 9 | 3 | 3 | 6 | 0 | 0 | 0 |
| Eliminación 10 | 8 | 6 | 14 | 0 | 0 | 0 |
| Actualización de b 10 | 2 | 2 | 4 | 0 | 0 | 0 |
| Eliminación 11 | 3 | 2 | 5 | 0 | 0 | 0 |
| Actualización de b 11 | 1 | 1 | 2 | 0 | 0 | 0 |
| Sustitución | 78 | 66 | 144 | 0 | 0 | 0 |
| **Total aritmético** | **782** | **704** | **1486** | **0** | **0** | **0** |

Total aritmético: **1486 flops**.

Comparaciones durante la búsqueda de pivote: **0**.

Divisiones para calcular razones de pivoteo: **0**.

Intercambios de filas: **0**.

## Corrida: Pivoteo escalado

| Fase | Mult./Div. | Sumas/Restas | Flops | Comparaciones | Div. pivoteo | Intercambios |
|---|---:|---:|---:|---:|---:|---:|
| Eliminación 1 | 143 | 132 | 275 | 11 | 12 | 1 |
| Eliminación 2 | 120 | 110 | 230 | 10 | 11 | 0 |
| Eliminación 3 | 99 | 90 | 189 | 9 | 10 | 1 |
| Eliminación 4 | 80 | 72 | 152 | 8 | 9 | 1 |
| Eliminación 5 | 63 | 56 | 119 | 7 | 8 | 1 |
| Eliminación 6 | 48 | 42 | 90 | 6 | 7 | 1 |
| Eliminación 7 | 35 | 30 | 65 | 5 | 6 | 1 |
| Eliminación 8 | 24 | 20 | 44 | 4 | 5 | 1 |
| Eliminación 9 | 15 | 12 | 27 | 3 | 4 | 1 |
| Eliminación 10 | 8 | 6 | 14 | 2 | 3 | 0 |
| Eliminación 11 | 3 | 2 | 5 | 1 | 2 | 0 |
| Sustitución | 144 | 132 | 276 | 0 | 0 | 0 |
| **Total aritmético** | **782** | **704** | **1486** | **66** | **77** | **8** |

Total aritmético: **1486 flops**.

Comparaciones para calcular escalas: **132**.

Comparaciones durante la búsqueda de pivote: **66**.

Divisiones para calcular razones de pivoteo: **77**.

Intercambios de filas: **8**.

