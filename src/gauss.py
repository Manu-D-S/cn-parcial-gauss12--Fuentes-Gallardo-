# Código hecho por Ariel Gallardo y Manuel Fuentes

def eliminacion_gaussiana(A, b):
    M = [fila[:] for fila in A]
    vec_b = b[:]
    n = len(M)

    desglose = []
    total_md = 0
    total_sr = 0
    total_b = 0
    mult_max = 0.0

    max_inicial = max(abs(v) for fila in M for v in fila)
    max_final = max_inicial

    for k in range(n - 1):
        md = 0
        sr = 0
        flops_b = 0

        pivote = M[k][k]

        if pivote == 0:
            raise ValueError(f"Pivote cero en fila {k + 1}")

        for i in range(k + 1, n):
            m = M[i][k] / pivote
            md += 1
            mult_max = max(mult_max, abs(m))

            # Actualizar desde la columna k, como indica la guía.
            for j in range(k, n):
                M[i][j] -= m * M[k][j]
                md += 1
                sr += 1

            M[i][k] = 0.0

            # Actualización del vector b.
            vec_b[i] -= m * vec_b[k]
            flops_b += 2

        max_final = max(
            max_final,
            max(abs(v) for fila in M for v in fila)
        )

        total_md += md
        total_sr += sr
        total_b += flops_b

        desglose.append({
            "paso": k + 1,
            "mult_div_A": md,
            "sumas_restas_A": sr,
            "flops_b": flops_b,
            "multiplicador_maximo": mult_max,
            "pivote": pivote,
            "crecimiento": max_final / max_inicial
        })

    stats = {
        "desglose": desglose,
        "mult_div_A": total_md,
        "sumas_restas_A": total_sr,
        "flops_b": total_b,
        "multiplicador_maximo": mult_max,
        "factor_crecimiento": max_final / max_inicial
    }

    return M, vec_b, stats



def factorizar_pivoteo_escalado(A):
    U = [fila[:] for fila in A]
    n = len(U)

    L = [
        [1.0 if i == j else 0.0 for j in range(n)]
        for i in range(n)
    ]

    # Calcular escalas de cada fila.
    escalas = []
    comparaciones_escalas = 0

    for fila in U:
        mayor = abs(fila[0])

        for j in range(1, n):
            comparaciones_escalas += 1

            if abs(fila[j]) > mayor:
                mayor = abs(fila[j])

        escalas.append(mayor)

    perm = list(range(n))

    max_inicial = max(abs(v) for fila in U for v in fila)
    max_final = max_inicial

    total_md = 0
    total_sr = 0
    total_comp = 0
    total_div_pivoteo = 0
    total_intercambios = 0
    total_movimientos = 0
    mult_max = 0.0
    desglose = []

    for k in range(n - 1):
        md = 0
        sr = 0
        comparaciones = 0
        divisiones_pivoteo = 0
        intercambio = 0
        movimientos = 0

        idx_max = k

        if escalas[k]:
            max_val = abs(U[k][k]) / escalas[k]
            divisiones_pivoteo += 1
        else:
            max_val = 0

        # Buscar el pivote escalado.
        for i in range(k + 1, n):
            comparaciones += 1

            if escalas[i]:
                valor = abs(U[i][k]) / escalas[i]
                divisiones_pivoteo += 1
            else:
                valor = 0

            if valor > max_val:
                max_val = valor
                idx_max = i

        # Intercambiar filas si es necesario.
        if idx_max != k:
            U[k], U[idx_max] = U[idx_max], U[k]
            L[k][:k], L[idx_max][:k] = L[idx_max][:k], L[k][:k]
            escalas[k], escalas[idx_max] = escalas[idx_max], escalas[k]
            perm[k], perm[idx_max] = perm[idx_max], perm[k]

            intercambio = 1
            movimientos = 2 * n

        pivote = U[k][k]

        if pivote == 0:
            raise ValueError(f"Pivote cero en fila {k + 1}")

        # Eliminación gaussiana.
        for i in range(k + 1, n):
            m = U[i][k] / pivote
            md += 1

            mult_max = max(mult_max, abs(m))
            L[i][k] = m

            # Actualizar desde la columna k.
            for j in range(k, n):
                U[i][j] -= m * U[k][j]
                md += 1
                sr += 1

            U[i][k] = 0.0

        max_final = max(
            max_final,
            max(abs(v) for fila in U for v in fila)
        )

        total_md += md
        total_sr += sr
        total_comp += comparaciones
        total_div_pivoteo += divisiones_pivoteo
        total_intercambios += intercambio
        total_movimientos += movimientos

        desglose.append({
            "paso": k + 1,
            "pivote": pivote,
            "fila_intercambiada": (
                f"F{k + 1} <-> F{idx_max + 1}"
                if intercambio else "No"
            ),
            "mult_div_A": md,
            "sumas_restas_A": sr,
            "comparaciones": comparaciones,
            "divisiones_pivoteo": divisiones_pivoteo,
            "multiplicador_maximo": mult_max,
            "crecimiento": max_final / max_inicial
        })

    stats = {
        "desglose": desglose,
        "mult_div_A": total_md,
        "sumas_restas_A": total_sr,
        "comparaciones": total_comp,
        "comparaciones_escalas": comparaciones_escalas,
        "divisiones_pivoteo": total_div_pivoteo,
        "intercambios": total_intercambios,
        "movimientos_memoria": total_movimientos,
        "multiplicador_maximo": mult_max,
        "factor_crecimiento": max_final / max_inicial
    }

    return L, U, perm, stats



def resolver_con_lu(L, U, perm, b):
    n = len(b)
    pb = [b[perm[i]] for i in range(n)]

    y = [0.0] * n
    md = 0
    sr = 0

    # Sustitución hacia adelante: L y = P b.
    for i in range(n):
        restante = pb[i]

        for j in range(i):
            restante -= L[i][j] * y[j]
            md += 1
            sr += 1

        y[i] = restante

    x = [0.0] * n

    # Sustitución regresiva: U x = y.
    for i in range(n - 1, -1, -1):
        restante = y[i]

        for j in range(i + 1, n):
            restante -= U[i][j] * x[j]
            md += 1
            sr += 1

        if U[i][i] == 0:
            raise ValueError(f"Pivote cero en fila {i + 1}")

        x[i] = restante / U[i][i]
        md += 1

    return x, {
        "mult_div": md,
        "sumas_restas": sr,
        "total": md + sr
    }


def resolver_con_lu_decimal(L, U, perm, b):
    from decimal import Decimal

    n = len(b)

    Ld = [
        [Decimal(str(v)) for v in fila]
        for fila in L
    ]

    Ud = [
        [Decimal(str(v)) for v in fila]
        for fila in U
    ]

    pb = [b[perm[i]] for i in range(n)]

    y = [Decimal(0)] * n

    for i in range(n):
        restante = pb[i]

        for j in range(i):
            restante -= Ld[i][j] * y[j]

        y[i] = restante

    x = [Decimal(0)] * n

    for i in range(n - 1, -1, -1):
        restante = y[i]

        for j in range(i + 1, n):
            restante -= Ud[i][j] * x[j]

        if Ud[i][i] == 0:
            raise ValueError(f"Pivote cero en fila {i + 1}")

        x[i] = restante / Ud[i][i]

    return x


def incognitas(U, b):
    n = len(U)
    x = [0.0] * n

    md = 0
    sr = 0

    for i in range(n - 1, -1, -1):
        restante = b[i]

        for j in range(i + 1, n):
            restante -= U[i][j] * x[j]
            md += 1
            sr += 1

        if U[i][i] == 0:
            raise ValueError(f"Pivote cero en fila {i + 1}")

        x[i] = restante / U[i][i]
        md += 1

    return x, {
        "mult_div": md,
        "sumas_restas": sr,
        "total": md + sr
    }
