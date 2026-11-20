# cn-parcial-gauss12--Fuentes-Gallardo-

Resolver un sistema de ecuaciones lineales de 12 incógnitas mediante eliminación gaussiana con dos metodos distintos.

## Integrantes y asignatura

- **Integrantes:** Ariel Gallardo y Manuel Fuentes.
- **Asignatura:** Computación Numérica, sección 2.
- **Universidad:** Universidad Católica del Maule.

## Requisitos
Para la correcta ejecución de este programa se necesita la libreria "numpy" con su version 2.5.4 y la librería por defecto de python "pathlib", así como el lenguaje python en su version 3.14.8, de igual forma los requerimientos de librerias estan en el archivo "requeriments.txt", usar "pip install -r requirements.txt" para instalarlos directamente con su version correspondiente.

## Ejecución
Para ejecutar el programa es necesario ejecutar el comando "python Src/main.py", junto con esto, el programa generará una carpeta llamada "resultados" la que contendrá un .txt llamado "residuo" que contiene r y su norma infinito, un .txt llamado "traza_eliminacion" que contiene 2 matrices siendo estas los resultados de aplicar eliminación gaussiana con y sin pivote parcial y un archivo .csv que contiene el vector x con sus resultados correspondientes (x1 a x12)


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

Para consultar el desarrollo completo, los procedimientos, el análisis numérico y la verificación de los resultados, revisa el [informe.md](informe.md).

## Licencia y uso

Este repositorio fue desarrollado con fines de estudio y práctica para la asignatura Computación Numérica de la Universidad Católica del Maule. Su contenido está destinado al estudio y revisión de los métodos vistos durante la asignatura.
