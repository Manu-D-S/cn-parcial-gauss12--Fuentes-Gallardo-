# Codigo hecho por Ariel Gallardo y Manuel Fuentes

def eliminacion_gaussiana(A, b):
    M = [fila[:] for fila in A]
    vec_b = b[:]
    n = len(M)

    total_mult_div_A = 0
    total_sumas_restas_A = 0
    total_flops_b = 0
    desglose_pasos = []
    mult_max = 0.0

    for k in range(n - 1):
        md_paso_A = 0
        sr_paso_A = 0
        flops_paso_b = 0

        pivote = M[k][k]

        if pivote == 0:
            raise ValueError(f"Pivote cero en fila {k + 1}")

        for i in range(k + 1, n):
            multiplicador = M[i][k] / pivote
            md_paso_A += 1
            mult_max = max(mult_max, abs(multiplicador))

            for j in range(k + 1, n):
                M[i][j] -= multiplicador * M[k][j]
                md_paso_A += 1
                sr_paso_A += 1

            M[i][k] = 0.0
            vec_b[i] -= multiplicador * vec_b[k]
            flops_paso_b += 2

        total_mult_div_A += md_paso_A
        total_sumas_restas_A += sr_paso_A
        total_flops_b += flops_paso_b

        desglose_pasos.append({
            "paso": k + 1,
            "mult_div_A": md_paso_A,
            "sumas_restas_A": sr_paso_A,
            "subtotal_flops_A": md_paso_A + sr_paso_A,
            "multiplicador_maximo": mult_max,
            "flops_b": flops_paso_b
        })

    return M, vec_b, desglose_pasos, total_mult_div_A, total_sumas_restas_A, total_flops_b


def pivoteo_parcial(A, b):
    M = [fila[:] for fila in A]
    vec_b = b[:]
    n = len(M)

    escalas = [max(abs(valor) for valor in fila) for fila in M]

    total_mult_div_A = 0
    total_sumas_restas_A = 0
    total_flops_b = 0
    mult_max = 0.0

    total_comparaciones = 0
    total_intercambios_filas = 0
    total_movimientos_memoria = 0

    desglose_pasos = []

    for k in range(n - 1):
        md_paso_A = 0
        sr_paso_A = 0
        flops_paso_b = 0

        idx_max = k
        max_val = abs(M[k][k]) / escalas[k] if escalas[k] != 0 else 0
        comp_paso = 0
        intercambio_paso = 0
        movs_paso = 0

        for fila in range(k + 1, n):
            comp_paso += 1
            val_actual = abs(M[fila][k]) / escalas[fila] if escalas[fila] != 0 else 0

            if val_actual > max_val:
                max_val = val_actual
                idx_max = fila

        if idx_max != k:
            M[k], M[idx_max] = M[idx_max], M[k]
            vec_b[k], vec_b[idx_max] = vec_b[idx_max], vec_b[k]
            escalas[k], escalas[idx_max] = escalas[idx_max], escalas[k]

            intercambio_paso = 1
            movs_paso = (n - k) + 1

        pivote = M[k][k]

        if pivote == 0:
            raise ValueError(f"Pivote cero en fila {k + 1}")

        for i in range(k + 1, n):
            multiplicador = M[i][k] / pivote
            md_paso_A += 1
            mult_max = max(mult_max, abs(multiplicador))

            for j in range(k + 1, n):
                M[i][j] -= multiplicador * M[k][j]
                md_paso_A += 1
                sr_paso_A += 1

            M[i][k] = 0.0
            vec_b[i] -= multiplicador * vec_b[k]
            flops_paso_b += 2

        total_mult_div_A += md_paso_A
        total_sumas_restas_A += sr_paso_A
        total_flops_b += flops_paso_b
        total_comparaciones += comp_paso
        total_intercambios_filas += intercambio_paso
        total_movimientos_memoria += movs_paso

        desglose_pasos.append({
            "paso": k + 1,
            "mult_div_A": md_paso_A,
            "sumas_restas_A": sr_paso_A,
            "multiplicador_maximo": mult_max,
            "flops_A": md_paso_A + sr_paso_A,
            "flops_b": flops_paso_b,
            "comparaciones": comp_paso,
            "intercambio": f"F{k+1} <-> F{idx_max+1}" if intercambio_paso else "No"
        })

    return (
        M, vec_b, desglose_pasos,
        total_mult_div_A, total_sumas_restas_A, total_flops_b,
        total_comparaciones, total_intercambios_filas,
        total_movimientos_memoria
    )


def incognitas(U, b):
    n = len(U)
    x = [0.0] * n

    mult_div = 0
    sumas_restas = 0

    for i in range(n - 1, -1, -1):
        suma = 0.0

        for j in range(i + 1, n):
            suma += U[i][j] * x[j]
            mult_div += 1
            sumas_restas += 1

        if U[i][i] == 0:
            raise ValueError(f"Pivote cero en fila {i + 1}")

        x[i] = (b[i] - suma) / U[i][i]
        sumas_restas += 1
        mult_div += 1

    return x, sumas_restas, mult_div
