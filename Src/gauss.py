# Codigo hecho por Ariel Gallardo y Manuel Fuentes

def eliminacion_gaussiana(A, b):
    M = [fila[:] for fila in A]
    vec_b = b[:]
    n = len(M)
    
    total_mult_div_A = 0
    total_sumas_restas_A = 0
    total_flops_b = 0
    desglose_pasos = []

    for k in range(n - 1):
        md_paso_A = 0
        sr_paso_A = 0
        flops_paso_b = 0
        
        pivote = M[k][k]
        
        for i in range(k + 1, n):
            # Se calcula el multiplicador
            multiplicador = M[i][k] / pivote
            md_paso_A += 1
            
            # Sabemos que la subdiagonal se vuelve 0, asi que se obvia y pasa a la siguiente columna y se reemplaza el 0 directamente
            for j in range(k + 1, n):
                M[i][j] = M[i][j] - multiplicador * M[k][j]
                md_paso_A += 1
                sr_paso_A += 1
            
            M[i][k] = 0.0
            
            # Se aplica al vector por separado para no juntar ambas matrices
            vec_b[i] = vec_b[i] - multiplicador * vec_b[k]
            flops_paso_b += 2
            
        total_mult_div_A += md_paso_A
        total_sumas_restas_A += sr_paso_A
        total_flops_b += flops_paso_b

        # Se crea una tupla con diccionarios donde se guarda el desglose
        desglose_pasos.append({
            "paso": k + 1,
            "mult_div_A": md_paso_A,
            "sumas_restas_A": sr_paso_A,
            "subtotal_flops_A": md_paso_A + sr_paso_A,
            "flops_b": flops_paso_b
        })

    return M, vec_b, desglose_pasos, total_mult_div_A, total_sumas_restas_A, total_flops_b

def pivoteo_parcial(A, b):
    M = [fila[:] for fila in A]
    vec_b = b[:]
    n = len(M)
    
    total_mult_div_A = 0
    total_sumas_restas_A = 0
    total_flops_b = 0
    
    total_comparaciones = 0
    total_intercambios_filas = 0
    total_movimientos_memoria = 0
    
    desglose_pasos = []

    for k in range(n - 1):
        md_paso_A = 0
        sr_paso_A = 0
        flops_paso_b = 0

        idx_max = k
        max_val = abs(M[k][k])
        comp_paso = 0
        intercambio_paso = 0
        movs_paso = 0

        # Se obtiene el valor maximo de la columna y se cambia para pivotear de ser necesario
        for fila in range(k + 1, n):
            comp_paso += 1
            val_actual = abs(M[fila][k])
            if val_actual > max_val:
                max_val = val_actual
                idx_max = fila
                
        if idx_max != k:
            M[k], M[idx_max] = M[idx_max], M[k]
            vec_b[k], vec_b[idx_max] = vec_b[idx_max], vec_b[k]
            intercambio_paso = 1
            movs_paso = (n - k) + 1 
            
        total_comparaciones += comp_paso
        total_intercambios_filas += intercambio_paso
        total_movimientos_memoria += movs_paso

        # El resto es lo mismo que la otra funcion
        pivote = M[k][k]
        
        for i in range(k + 1, n):
            multiplicador = M[i][k] / pivote
            md_paso_A += 1
            
            for j in range(k + 1, n):
                M[i][j] = M[i][j] - multiplicador * M[k][j]
                md_paso_A += 1
                sr_paso_A += 1
            
            M[i][k] = 0.0
            
            vec_b[i] = vec_b[i] - multiplicador * vec_b[k]
            flops_paso_b += 2
            
        total_mult_div_A += md_paso_A
        total_sumas_restas_A += sr_paso_A
        total_flops_b += flops_paso_b
        
        desglose_pasos.append({
            "paso": k + 1,
            "mult_div_A": md_paso_A,
            "sumas_restas_A": sr_paso_A,
            "flops_A": md_paso_A + sr_paso_A,
            "flops_b": flops_paso_b,
            "comparaciones": comp_paso,
            "intercambio": f"F{k+1} <-> F{idx_max+1}" if intercambio_paso else "No"
        })

    return (M, vec_b, desglose_pasos,
        total_mult_div_A, total_sumas_restas_A, total_flops_b,
        total_comparaciones, total_intercambios_filas, total_movimientos_memoria)
