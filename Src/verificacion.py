# Codigo hecho por Ariel Gallardo y Manuel Fuentes
from gauss import incognitas
import csv
from pathlib import Path

esta_carpeta = Path(__file__).resolve().parent
resumen = esta_carpeta.parent / "resultados"
resumen.mkdir(parents=True, exist_ok=True)

from decimal import Decimal, getcontext
import numpy as np

# Se definen 50 decimales de precision
getcontext().prec = 50

def residuo(A, b, x):
    n = len(A)
    r_decimal = []
    
    for i in range(n):
        b_i = Decimal(str(b[i]))
        ax_i = sum(Decimal(str(A[i][j])) * Decimal(str(x[j])) for j in range(n))
        r_decimal.append(b_i - ax_i)
        
    norma_inf = max(abs(val) for val in r_decimal)
    r_float = [float(val) for val in r_decimal]
    
    return r_float, float(norma_inf)


def verificacion(A_orig, b_orig, x0):
    ar = open(resumen / "residuo.txt", mode="w", encoding="utf8")

    # Se calcula el residuo inicial en precision extendida
    r0, norma_r0 = residuo(A_orig, b_orig, x0)
    
    # Se aplica la refinacion
    dx = incognitas(A_orig, r0)
    x1 = [x0[i] + dx[0][i] for i in range(len(x0))]
    r1, norma_r1 = residuo(A_orig, b_orig, x1)
    
    # Se hace el contraste con numpy
    x_numpy = np.linalg.solve(np.array(A_orig, dtype=float), np.array(b_orig, dtype=float))
    error_vs_numpy_x0 = max(abs(x0[i] - x_numpy[i]) for i in range(len(x0)))
    error_vs_numpy_x1 = max(abs(x1[i] - x_numpy[i]) for i in range(len(x1)))

    # P R I N T S
    ar.write("r y su norma infinito\n")
    ar.write(f"Norma infinito residuo inicial: {norma_r0:.6e}\n")
    ar.write(f"Norma infinito residuo refinado: {norma_r1:.6e}\n")
    
    if norma_r1 < norma_r0:
        factor = norma_r0 / norma_r1
        ar.write(f"\nMejora observada: el residuo se redujo {factor:.2f} veces\n")
    else:
        ar.write("\nSin mejora adicional: la solucion inicial ya alcanzo el límite de precision float64\n")

    ar.write(f"\nDiferencia maxima: {error_vs_numpy_x0:.6e}\n")
    ar.write(f"Diferencia maxima: {error_vs_numpy_x1:.6e}\n")
    return x1, r0, r1