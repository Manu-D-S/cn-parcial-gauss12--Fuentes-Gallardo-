##  3.Identificación
Asignatura: Computación Numérica
Proyecto: Eliminación gaussiana con y sin pivoteo escalado
Integrantes: Manuel Fuentes y Ariel Gallardo
Enlace:https://github.com/Manu-D-S/cn-parcial-gauss12--Fuentes-Gallardo-

## 4.Planteamiento

El objetivo de este proyecto es evaluar la resolución de un sistema de ecuaciones lineales de orden \(n=12\), mediante el método de eliminación gaussiana, considerando dos enfoques: uno sin pivoteo y otro utilizando pivoteo parcial escalado.

Buscamos evaluar el funcionamiento y las diferencias entre ambos métodos, considerando sus costos operacionales, la precisión de los resultados al trabajar con números de magnitudes muy pequeñas y la estabilidad numérica durante los cálculos.

La matriz \(A\) representa los coeficientes del sistema de ecuaciones, el vector \(x\) contiene las incógnitas y el vector \(b\) corresponde a los términos independientes.

Esta evaluación es importante debido a que la matriz presenta diferencias significativas en la magnitud de sus elementos. Un ejemplo de esto es el primer elemento de la matriz, cuyo valor es aproximadamente \(1.3407\times10^{-8}\), mientras que en la misma columna existen valores considerablemente mayores.

Al realizar la eliminación sin pivoteo, utilizar un valor tan pequeño como pivote puede generar multiplicadores de gran magnitud. Esto puede amplificar los errores de redondeo y afectar los cálculos posteriores, perjudicando la precisión de la solución.

Por este motivo, se evalúan ambos enfoques para comparar sus resultados y determinar cómo influye el uso del pivoteo parcial escalado en el costo operacional y la estabilidad numérica del sistema.

##  5.Estrategia de eliminación

Para resolver el sistema de ecuaciones se utilizó el lenguaje Python para implementar los dos métodos mencionados anteriormente los cuales son : eliminación gaussiana sin pivoteo y eliminación gaussiana con pivoteo parcial escalado.

### 5.1. Eliminación gaussiana sin pivoteo

En este caso utilizamos directamente el elemento de la diagonal principal como pivote, sin realizar intercambios de filas.

El procedimiento sigue un orden de pasos. Primero se recorre la diagonal principal de la matriz, utilizando cada elemento como pivote. Luego, para cada pivote, se recorren las filas inferiores y se calcula el multiplicador necesario para eliminar los elementos que se encuentran debajo de él.

Este multiplicador se calcula una sola vez por fila y se reutiliza para actualizar los elementos correspondientes de la matriz y el vector de términos independientes. De esta manera, evitamos repetir divisiones innecesarias y tener costos operacionales mas grandes.

Una vez finalizada la eliminación y obtenida la matriz triangular superior, se aplica sustitución hacia atrás para calcular las incógnitas del sistema y tener los valores finales de nuestros xa.

### 5.2. Eliminación gaussiana con pivoteo parcial escalado

En este método se selecciona el pivote considerando la magnitud de los elementos de cada fila. Para ello, calculamos la razón entre el valor absoluto del elemento candidato a pivote y la escala de su fila.

Se selecciona la fila con la mayor razón y, si es necesario, se intercambiamos  las filas antes de continuar con la eliminación gaussiana.

Este procedimiento nos permite evitar el uso de pivotes demasiado pequeños en relación con la escala de su fila como en el caso anterior, reduciendo los multiplicadores excesivos y mejorando la estabilidad numérica.

La factorización obtenida se representa mediante las matrices \(L\) y \(U\), donde \(L\) almacena los multiplicadores utilizados durante la eliminación y \(U\) contiene la matriz triangular superior.

Los multiplicadores se guardan en \(L\), evitando tener que calcularlos nuevamente durante las sustituciones. Posteriormente, se resuelve el sistema mediante sustitución hacia adelante y hacia atrás para evalaur los valores de nuestras nuevas incognitas xa.

### 5.3. Orden de las operaciones y reutilización

En ambos métodos se sigue un orden de eliminación por columnas. Para cada columna se identifica el pivote, se calculan los multiplicadores de las filas inferiores y se actualizan únicamente los elementos necesarios para formar la matriz triangular superior.

Se evita modificar los elementos que ya fueron eliminados, ya que estos corresponden a ceros de la matriz triangular. Además, cada multiplicador se calcula una sola vez y se reutiliza en las actualizaciones correspondientes como se nos indico para evitar el costo operacional redundante.

Esta organización permite reducir operaciones innecesarias y mantener el costo computacional cercano al mínimo teórico esperado. Según la guía que se nos proporciono, se considera como referencia un total aproximado de 1486 operaciones aritméticas, con una tolerancia del 10 %. En nuestra implementación se obtuvieron 1366 operaciones para el método sin pivoteo y 1378 para el método con pivoteo escalado, lo que representa diferencias de -8,08 % y -7,27 %, respectivamente. Por lo tanto, ambos métodos se encuentran dentro del margen permitido por lo cual cumple lo antes establecido.

### 5.4. Implementación

El programa se divide en módulos para separar las responsabilidades y tener mayos legibilidad en las operaciones:

- `gauss.py`: contiene los algoritmos de eliminación, factorización y resolución del sistema.
- `conteo.py`: registra y resume las operaciones aritméticas realizadas.
- `verificacion.py`: calcula los residuos y realiza el refinamiento iterativo.
- `main.py`: coordina la ejecución y genera los archivos de resultados.

Los datos de entrada se cargan desde archivos CSV, mientras que las soluciones, trazas y verificaciones se almacenan en la carpeta `resultados/`.

## 6.Conteo de operaciones

Para evaluar el costo computacional de ambos métodos, se registró la cantidad de operaciones realizadas durante cada etapa de eliminación gaussiana. Se contabilizaron las multiplicaciones y divisiones por separado de las sumas y restas segun lo pedido.

### 6.1. Eliminación sin pivoteo

En este método, además de actualizar los elementos de la matriz \(A\), se actualiza directamente el vector de términos independientes \(b\) durante cada paso.

| Paso | Mult./div. en A | Sumas/restas en A | Operaciones en b | Total |
|---:|---:|---:|---:|---:|
| 1 | 132 | 121 | 22 | 275 |
| 2 | 110 | 100 | 20 | 230 |
| 3 | 90 | 81 | 18 | 189 |
| 4 | 72 | 64 | 16 | 152 |
| 5 | 56 | 49 | 14 | 119 |
| 6 | 42 | 36 | 12 | 90 |
| 7 | 30 | 25 | 10 | 65 |
| 8 | 20 | 16 | 8 | 44 |
| 9 | 12 | 9 | 6 | 27 |
| 10 | 6 | 4 | 4 | 14 |
| 11 | 2 | 1 | 2 | 5 |
| **Total** | **572** | **506** | **132** | **1210** |

A las 1210 operaciones de eliminación se agregan 156 operaciones correspondientes a la sustitución hacia atrás. Por lo tanto, el total del método sin pivoteo es de **1366 operaciones aritméticas** como se meciono anteriormente.

### 6.2. Eliminación con pivoteo parcial escalado

En este otro método se realiza la factorización de la matriz mediante las matrices \(L\) y \(U\). Las operaciones de actualización del vector \(b\) se realizan posteriormente mediante sustitución hacia adelante.

| Paso | Mult./div. en A | Sumas/restas en A | Total |
|---:|---:|---:|---:|
| 1 | 132 | 121 | 253 |
| 2 | 110 | 100 | 210 |
| 3 | 90 | 81 | 171 |
| 4 | 72 | 64 | 136 |
| 5 | 56 | 49 | 105 |
| 6 | 42 | 36 | 78 |
| 7 | 30 | 25 | 55 |
| 8 | 20 | 16 | 36 |
| 9 | 12 | 9 | 21 |
| 10 | 6 | 4 | 10 |
| 11 | 2 | 1 | 3 |
| **Total** | **572** | **506** | **1078** |

A las 1078 operaciones de factorización se agregan 300 operaciones correspondientes a las sustituciones hacia adelante y hacia atrás. De esta manera, el total del método con pivoteo escalado es de **1378 operaciones aritméticas**.

Adicionalmente, durante la selección de pivotes se realizaron 66 comparaciones y 8 intercambios de filas. Estos valores se contabilizan por separado y no forman parte del total aritmético.

### 6.3. Comparación con la cota de referencia

Según lo pedido, se considera como referencia un mínimo teórico aproximado de 1486 operaciones aritméticas, con una tolerancia del 10 %.

Por lo tanto, el intervalo permitido es:

\[
1486(0.90)\leq N\leq1486(1.10)
\]

\[
1337.4\leq N\leq1634.6
\]

| Método | Operaciones | Diferencia respecto a la referencia | Cumplimiento |
|---|---:|---:|---|
| Sin pivoteo | 1366 | -8,08 % | Dentro del margen |
| Pivoteo escalado | 1378 | -7,27 % | Dentro del margen |

Ambos métodos se encuentran dentro del margen de tolerancia establecido. Aunque el método con pivoteo escalado realiza algunas operaciones adicionales debido a las sustituciones y al manejo de la factorización, su costo aritmético total continúa dentro del límite permitido.

### 6.4. Convención de conteo

Para realizar el conteo se estableció la siguiente convención:

- Cada multiplicación cuenta como una operación.
- Cada división cuenta como una operación.
- Cada suma cuenta como una operación.
- Cada resta cuenta como una operación.
- Las comparaciones utilizadas para seleccionar pivotes se registran por separado.
- Los intercambios de filas también se registran por separado.
- Las operaciones de sustitución hacia adelante y hacia atrás se incluyen en el total aritmético.
- No se contabilizan como operaciones aritméticas las asignaciones ni los movimientos de memoria.

## 7.	Análisis de mantisa y pivoteo

Se compararon dos ejecuciones del método de eliminación gaussiana: una sin pivoteo y otra utilizando pivoteo parcial escalado.

### 7.1. Comparación de multiplicadores y crecimiento

Los resultados obtenidos fueron:

| Indicador | Sin pivoteo | Pivoteo parcial escalado |
|---|---:|---:|
| Multiplicador máximo | \(2.7526\times10^{13}\) | \(2.4656\times10^9\) |
| Factor de crecimiento | 2641.2243 | 1.7832 |
| Comparaciones | 0 | 66 |
| Intercambios de filas | 0 | 8 |

Sin pivoteo, el multiplicador máximo alcanza aproximadamente \(2.75\times10^{13}\). Esto se debe principalmente a que el algoritmo utiliza como primer pivote el elemento \(a_{11}=1.3407\times10^{-8}\), cuya magnitud es aproximadamente doce órdenes de magnitud menor que la de \(a_{21}\). Esto provoca multiplicadores extremadamente grandes y aumenta los errores de redondeo.

Por esta razón, el pivote \(a_{11}\) es inaceptable, ya que su magnitud es demasiado pequeña respecto a otros elementos de la misma columna.

Con pivoteo parcial escalado, el factor de crecimiento disminuye de 2641.22 a 1.78. Sin embargo, el multiplicador máximo continúa siendo elevado: \(2.47\times10^9\), y aparece en el tercer paso. Esto demuestra que el pivoteo escalado reduce el crecimiento de la matriz, pero no garantiza que todos los multiplicadores sean pequeños.

### 7.2. Análisis de la mantisa

Los cálculos se realizaron utilizando números de doble precisión (`float`), que disponen de 53 bits de precisión en la mantisa.

Se utiliza el logaritmo en base 2 del multiplicador máximo como estimación de su capacidad de amplificación:

| Método | Multiplicador máximo | \(\log_2(|m_{\max}|)\) |
|---|---:|---:|
| Sin pivoteo | \(2.75\times10^{13}\) | 44.65 bits |
| Pivoteo escalado | \(2.47\times10^9\) | 31.20 bits |

Estos valores no representan una medición exacta de los bits perdidos, sino una estimación de la amplificación. La pérdida real también depende de las operaciones posteriores, la cancelación numérica y el condicionamiento del sistema.

La eliminación sin pivoteo presenta una amplificación potencial mayor, mientras que el pivoteo escalado reduce considerablemente este riesgo.

### 7.3. Comparación y conclusión

La comparación demuestra que la elección del pivote influye en la estabilidad numérica del método. Sin pivoteo, el primer pivote demasiado pequeño genera multiplicadores enormes y un crecimiento considerable de la matriz.

Por otra parte, el pivoteo parcial escalado reduce el factor de crecimiento a 1.78 y evita utilizar directamente el pivote inicial inadecuado.

En conclusión, el pivoteo parcial escalado ofrece un comportamiento más favorable, aunque sus resultados deben analizarse junto con el condicionamiento del sistema y la verificación del residuo para determinar la precisión de la solución final.

## 8.	Condicionamiento 

Según la guía, el número de condición de la matriz es aproximadamente:

\[
\kappa(A)\approx 3.1\times10^{13}
\]

Este valor indica que el sistema está mal condicionado, por lo que pequeñas variaciones en los datos de entrada pueden producir cambios importantes en la solución.

Considerando la precisión doble (`float`), cuya precisión de máquina es:

\[
\varepsilon \approx 2.22\times10^{-16}
\]

Se obtiene la siguiente cota:

\[
\kappa(A)\cdot\varepsilon
\approx 6.88\times10^{-3}
\]

Esta cota representa un error relativo potencial cercano al 0.688 %, equivalente aproximadamente a dos dígitos significativos confiables en el peor caso.

Sin embargo, esta estimación es pesimista, ya que representa un escenario desfavorable y no necesariamente el error que se obtiene en la ejecución. En nuestros resultados, la solución con pivoteo escalado presentó entre 10 y 13 dígitos significativos correctos respecto a la referencia de mayor precisión. Después del refinamiento iterativo, se alcanzaron entre 22 y 25 dígitos.

Por lo tanto, aunque el sistema presenta un condicionamiento elevado, los resultados obtenidos fueron mejores que la cota teórica debido al comportamiento concreto de los datos y del algoritmo utilizado.


## 9.	Resultados 

Se presentan las soluciones obtenidas mediante eliminación gaussiana sin pivoteo, con pivoteo parcial escalado y después del refinamiento iterativo. La precisión se evaluó comparando las soluciones con una referencia calculada utilizando `Decimal` con 50 dígitos.

| Incógnita | Sin pivoteo | Con pivoteo | Refinada | Dígitos iniciales correctos | Dígitos refinados correctos |
|---|---:|---:|---:|---:|---:|
| \(x_1\) | 7.384915716927e-01 | 7.384915717404e-01 | 7.384915717405e-01 | 13 | 25 |
| \(x_2\) | -1.205937385991e+00 | -1.205937386583e+00 | -1.205937386583e+00 | 12 | 25 |
| \(x_3\) | 4.387196576063e-03 | 4.387196254167e-03 | 4.387196253927e-03 | 10 | 22 |
| \(x_4\) | -9.172647502986e-02 | -9.172647482482e-02 | -9.172647482467e-02 | 11 | 24 |
| \(x_5\) | 2.846109322130e+00 | 2.846109322433e+00 | 2.846109322433e+00 | 13 | 25 |
| \(x_6\) | -6.281531466726e-03 | -6.281531937646e-03 | -6.281531937997e-03 | 10 | 22 |
| \(x_7\) | 1.473820715848e+00 | 1.473820715447e+00 | 1.473820715446e+00 | 12 | 25 |
| \(x_8\) | -3.849284141692e-02 | -3.849284147699e-02 | -3.849284147703e-02 | 11 | 24 |
| \(x_9\) | 9.152647323449e-01 | 9.152647324915e-01 | 9.152647324916e-01 | 12 | 25 |
| \(x_{10}\) | -2.607139458280e+00 | -2.607139457958e+00 | -2.607139457958e+00 | 13 | 25 |
| \(x_{11}\) | 5.187367027263e-02 | 5.187367033093e-02 | 5.187367033097e-02 | 12 | 24 |
| \(x_{12}\) | -1.084937205143e+00 | -1.084937204847e+00 | -1.084937204846e+00 | 12 | 25 |

La solución con pivoteo escalado presenta entre 10 y 13 dígitos significativos correctos. Después del refinamiento iterativo, se alcanzan entre 22 y 25 dígitos correctos.

Estos resultados muestran que el refinamiento mejora considerablemente la precisión de las incógnitas respecto a la solución de referencia.

## 10.	Verificación 

Para comprobar la precisión de la solución obtenida, se calculó el residuo del sistema mediante aritmética de precisión extendida, utilizando `Decimal` con 50 dígitos de precisión.

### 10.1. Cálculo del residuo

El residuo se define como:

\[
r=b-Ax
\]

Para evaluar el error global se utilizó la norma infinito:

\[
\|r\|_{\infty}=\max_i |r_i|
\]

En la solución inicial con pivoteo parcial escalado se obtuvo:

\[
\|r_{\text{inicial}}\|_{\infty}
=2.09695651654\times10^{-10}
\]

Este valor representa la diferencia entre el vector de términos independientes y el resultado de multiplicar la matriz por la solución calculada.

### 10.2. Refinamiento iterativo

Se aplicó un paso de refinamiento iterativo para mejorar la solución. Este procedimiento utiliza el residuo calculado con mayor precisión y resuelve un sistema de corrección utilizando los factores LU obtenidos previamente.

La norma del residuo después del refinamiento fue:

\[
\|r_{\text{final}}\|_{\infty}
=2.8221763338\times10^{-24}
\]

La comparación de ambos resultados muestra que el residuo disminuyó aproximadamente \(7.43\times10^{13}\) veces. Por lo tanto, el refinamiento iterativo logró mejorar considerablemente la precisión de la solución.

### 10.3. Comparación con una biblioteca numérica

Como control adicional, se comparó la solución obtenida con pivoteo escalado y refinamiento con una solución calculada mediante NumPy.

Las diferencias máximas observadas fueron:

| Comparación | Diferencia máxima |
|---|---:|
| Solución inicial frente a NumPy | \(8.3267\times10^{-14}\) |
| Solución refinada frente a NumPy | \(3.5727\times10^{-13}\) |

NumPy se utilizó únicamente como referencia de control y no como solución exacta, ya que también trabaja con precisión de punto flotante.

### 10.4. Conclusión de la verificación

Los resultados muestran que el refinamiento iterativo redujo significativamente el residuo del sistema, pasando de aproximadamente \(2.10\times10^{-10}\) a \(2.82\times10^{-24}\).

Esto confirma que el procedimiento permitió obtener una solución que satisface el sistema con mayor precisión. La comparación con NumPy aporta un control adicional, mientras que la verificación principal se basa en el residuo calculado con aritmética de precisión extendida.

## 11.	Conclusiones

Durante el proyecto se utilizaron dos estrategias para afrontar la problematica y comparar sus resultados y costes.

La eliminación sin pivoteo tuvo un costo de 1366 operaciones aritméticas, mientras que el pivoteo parcial escalado requirió 1378 operaciones, además de 66 comparaciones y 8 intercambios de filas. Aunque el segundo método presenta un costo ligeramente mayor, se eligió porque ofrece un comportamiento numérico más favorable. Esto se observa en la reducción del factor de crecimiento de 2641.22 a 1.78 y en la disminución de los multiplicadores máximos.

También se aplicó refinamiento iterativo, que permitió reducir la norma infinito del residuo desde \(2.10\times10^{-10}\) hasta \(2.82\times10^{-24}\). Por lo tanto, el costo adicional de esta se puede justificar debido a la mejora que este presenta.

Si el tamaño del sistema aumentara a \(n=1000\), utilizaría pivoteo parcial escalado y consideraría una implementación optimizada con otras herramientas para evitar perdida de infromacion con numeros tan bajos. Para una matriz densa, la eliminación gaussiana tiene un costo computacional de orden \(O(n^3)\), por lo que el tiempo de cálculo y la memoria necesaria aumentarían considerablemente con un aumento tan grande en nxn con n=1000. Además, se deberia evaluar si la matriz presenta estructura dispersa para utilizar métodos especializados que eviten almacenar y operar sobre tantos elementos nulos.

En conclusión,debido a la complejidad presentada para el sistema estudiado con un sistema de N*N con N=12  se priorizó la confiabilidad numérica por sobre una pequeña reducción del costo computacional. El pivoteo parcial escalado, junto con la verificación en precisión extendida y el refinamiento iterativo, permitió obtener una solución más confiable y comprobar su precisión.
## 12.	Reproducibilidad

## 13. Uso de inteligencia artificial

Durante el desarrollo del proyecto no fue necesario utilizar inteligencia artificial para diseñar la estructura inicial del repositorio. Sin embargo, se utilizó como herramienta de apoyo durante la implementación, revisión y verificación del código.

En el archivo `gauss.py`, se recurrió a la inteligencia artificial para identificar y corregir errores en el cálculo de algunas variables que se habían producido durante la implementación. Asimismo, a medida que se desarrollaban y modificaban las funciones, se utilizó para revisar si los procedimientos implementados cumplían con los requisitos establecidos en la pauta.

También fue de utilidad durante las modificaciones realizadas en distintos archivos, ya que algunos cambios podían afectar otras partes del proyecto y, debido a la cantidad de líneas de código implementadas, no siempre identificábamos estos efectos. En estos casos, la IA nos ayudó a localizar posibles inconsistencias y determinar qué archivos o funciones necesitaban ajustes.

Otro aporte importante fue la detección de un uso incorrecto del pivoteo. Inicialmente, se había implementado un tipo de pivoteo que no correspondía al solicitado en la guía, por lo que se utilizó la IA para identificar esta diferencia y orientar la corrección hacia el pivoteo parcial escalado requerido.

Por otra parte, en `main.py` se utilizó como apoyo para organizar las llamadas a las funciones y las instrucciones `print()` encargadas de mostrar los resultados en pantalla. Estas tareas eran principalmente sencillas y repetitivas, pero facilitaron la visualización de los resultados y la revisión de las distintas ejecuciones. También se utilizó para comprobar valores intermedios y comprender mejor el comportamiento de los métodos implementados.

El uso de esta herramienta no presentó mayores inconvenientes, debido a que conocíamos la lógica de los métodos y teníamos presentes los posibles errores que debíamos revisar. Por esta razón, las sugerencias proporcionadas fueron evaluadas antes de incorporarlas al proyecto.

En conclusión, la inteligencia artificial se utilizó como una herramienta de asistencia para la revisión, depuración y comprensión del código. No reemplazó el desarrollo ni la ejecución de los procedimientos que habiamos decidido, sino que facilitó la detección de errores que se tenia , nos permitió verificar que la implementación se ajustara a los requisitos de la actividad lo cual fue crucial en los datos y tambien los errores ortografia que teniamos.