# cn-parcial-gauss12--Fuentes-Gallardo-

Resolver un sistema de ecuaciones lineales de 12 incógnitas mediante eliminación gaussiana con dos metodos distintos.

## Integrantes y asignatura

- **Integrantes:** Ariel Gallardo y Manuel Fuentes.
- **Asignatura:** Computación Numérica, sección 2.

## Requisitos


## Ejecución


## Estructura del proyecto

## Estructura del proyecto

```text
.
├── datos/
│   ├── matriz_a.csv
│   └── vector_b.csv
├── resultados/
│   ├── conteo_flops.md
│   ├── residuo.txt
│   ├── solucion.csv
│   └── traza_eliminacion.txt
├── src/
│   ├── conteo.py
│   ├── gauss.py
│   ├── main.py
│   └── verificacion.py
├── .gitignore
├── informe.md
├── README.md
└── requirements.txt
```

## Resultados resumidos

Solución obtenida después del refinamiento iterativo, expresada con 10 cifras significativas:

| Incógnita | Valor |
|---|---:|
| \(x_1\) | 7.384915717E-1 |
| \(x_2\) | -1.205937387E+0 |
| \(x_3\) | 4.387196254E-3 |
| \(x_4\) | -9.172647482E-2 |
| \(x_5\) | 2.846109322E+0 |
| \(x_6\) | -6.281531938E-3 |
| \(x_7\) | 1.473820715E+0 |
| \(x_8\) | -3.849284148E-2 |
| \(x_9\) | 9.152647325E-1 |
| \(x_{10}\) | -2.607139458E+0 |
| \(x_{11}\) | 5.187367033E-2 |
| \(x_{12}\) | -1.084937205E+0 |

| Indicador | Resultado |
|---|---:|
| Operaciones sin pivoteo | 1366 |
| Operaciones con pivoteo escalado | 1378 |
| Norma infinito del residuo refinado | \(2.8222\times10^{-24}\) |

## Informe

Para consultar el desarrollo, [informe.md](informe.md).

## Licencia y uso

Este repositorio fue desarrollado con fines de studio y practicas para la asignatura Computación Numérica de la Universidad Católica del Maule. Su contenido está destinado al estudio y revision de metodos vistos durante la asignatura.
