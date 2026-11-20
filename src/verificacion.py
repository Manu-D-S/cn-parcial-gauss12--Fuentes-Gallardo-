# Codigo hecho por Ariel Gallardo y Manuel Fuentes

from decimal import Decimal, getcontext
from pathlib import Path
import numpy as np

from gauss import resolver_con_lu_decimal

getcontext().prec = 50

CARPETA = Path(__file__).resolve().parent
RESULTADOS = CARPETA.parent / "resultados"
RESULTADOS.mkdir(parents=True, exist_ok=True)


def residuo(A, b, x):
    n = len(A)
    r = []

    for i in range(n):
        ax = sum(
            A[i][j] * x[j]
            for j in range(n)
        )
        r.append(b[i] - ax)

    return r, max(abs(v) for v in r)


def resolver_referencia_decimal(A, b):
    """
    Resuelve el sistema usando eliminacion gaussiana
    con pivoteo parcial y aritmetica Decimal.
    """
    n = len(A)
    M = [fila[:] for fila in A]
    vec_b = b[:]

    # Eliminacion gaussiana
    for k in range(n - 1):

        # Buscar el pivote de mayor valor absoluto
        fila_pivote = max(
            range(k, n),
            key=lambda i: abs(M[i][k])
        )

        if M[fila_pivote][k] == 0:
            raise ValueError("La matriz es singular.")

        # Intercambiar filas
        if fila_pivote != k:
            M[k], M[fila_pivote] = M[fila_pivote], M[k]
            vec_b[k], vec_b[fila_pivote] = (
                vec_b[fila_pivote],
                vec_b[k]
            )

        # Eliminar elementos bajo el pivote
        for i in range(k + 1, n):
            m = M[i][k] / M[k][k]

            for j in range(k + 1, n):
                M[i][j] -= m * M[k][j]

            vec_b[i] -= m * vec_b[k]
            M[i][k] = Decimal(0)

    # Sustitucion regresiva
    x = [Decimal(0)] * n

    for i in range(n - 1, -1, -1):
        suma = sum(
            M[i][j] * x[j]
            for j in range(i + 1, n)
        )

        if M[i][i] == 0:
            raise ValueError("La matriz es singular.")

        x[i] = (vec_b[i] - suma) / M[i][i]

    return x


def comparar_soluciones(x, referencia):
    errores = []

    for i in range(len(x)):
        error_absoluto = abs(x[i] - referencia[i])

        if referencia[i] != 0:
            error_relativo = error_absoluto / abs(referencia[i])
        else:
            error_relativo = error_absoluto

        if error_relativo == 0:
            digitos = "Exacto"
        else:
            digitos = str(
                max(0, int(-error_relativo.log10()))
            )

        errores.append(
            (error_absoluto, error_relativo, digitos)
        )

    return errores


def verificacion(A, b, x0, L, U, perm):

    # Solucion de referencia con 50 digitos
    referencia = resolver_referencia_decimal(A, b)

    # Convertir solucion inicial a Decimal
    x0_decimal = [Decimal(str(v)) for v in x0]

    # Residuo inicial
    r0, norma_r0 = residuo(A, b, x0_decimal)

    # Refinamiento iterativo
    dx = resolver_con_lu_decimal(L, U, perm, r0)

    candidato = [
        x0_decimal[i] + dx[i]
        for i in range(len(x0_decimal))
    ]

    r_candidato, norma_candidato = residuo(A, b, candidato)

    if norma_candidato < norma_r0:
        x1 = candidato
        r1 = r_candidato
        norma_r1 = norma_candidato
        mejora = True
    else:
        x1 = x0_decimal
        r1 = r0
        norma_r1 = norma_r0
        mejora = False

    # Comparacion contra la referencia Decimal
    errores_iniciales = comparar_soluciones(
        x0_decimal, referencia
    )

    errores_finales = comparar_soluciones(
        x1, referencia
    )

    error_relativo_inicial = max(
        e[1] for e in errores_iniciales
    )

    error_relativo_final = max(
        e[1] for e in errores_finales
    )

    # NumPy como control, no como referencia exacta
    A_float = np.array([[float(v) for v in fila] for fila in A])
    b_float = np.array([float(v) for v in b])
    x_numpy = np.linalg.solve(A_float, b_float)

    error_numpy = max(
        abs(float(x1[i]) - x_numpy[i])
        for i in range(len(x1))
    )

    # Guardar resultados
    with open(RESULTADOS / "residuo.txt", "w", encoding="utf-8") as f:

        f.write("SOLUCION DE REFERENCIA (DECIMAL, 50 DIGITOS)\n")
        for i, valor in enumerate(referencia):
            f.write(f"x{i + 1} = {valor}\n")

        f.write("\nRESIDUO INICIAL\n")
        for valor in r0:
            f.write(f"{valor}\n")

        f.write(f"\nNorma infinito inicial: {norma_r0}\n")

        f.write("\nRESIDUO DESPUES DEL REFINAMIENTO\n")
        for valor in r1:
            f.write(f"{valor}\n")

        f.write(f"\nNorma infinito final: {norma_r1}\n")
        f.write(f"Refinamiento mejoro: {'Si' if mejora else 'No'}\n")

        f.write("\nCOMPARACION CON LA REFERENCIA\n")
        f.write(
            "Variable | Error relativo inicial | "
            "Digitos iniciales | Error relativo final | Digitos finales\n"
        )

        for i in range(len(referencia)):
            ei = errores_iniciales[i]
            ef = errores_finales[i]

            f.write(
                f"x{i + 1} | {ei[1]} | {ei[2]} | "
                f"{ef[1]} | {ef[2]}\n"
            )

        f.write(
            f"\nMaximo error relativo inicial: "
            f"{error_relativo_inicial}\n"
        )

        f.write(
            f"Maximo error relativo final: "
            f"{error_relativo_final}\n"
        )

        f.write(
            f"\nDiferencia final respecto a NumPy: "
            f"{error_numpy}\n"
        )

    return [float(v) for v in x1], norma_r0, norma_r1
