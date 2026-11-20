
def resumen_conteo(stats_eliminacion, stats_sustitucion):
    md = stats_eliminacion["mult_div_A"] + stats_sustitucion["mult_div"]
    sr = stats_eliminacion["sumas_restas_A"] + stats_sustitucion["sumas_restas"]

    flops_b = stats_eliminacion.get("flops_b", 0)

    return {
        "mult_div": md,
        "sumas_restas": sr,
        "flops_b": flops_b,
        "total": md + sr + flops_b
    }


def guardar_conteo(ruta, sin_pivoteo, con_pivoteo, sustitucion_sin, sustitucion_con):
    total_sin = resumen_conteo(sin_pivoteo, sustitucion_sin)
    total_con = resumen_conteo(con_pivoteo, sustitucion_con)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("# Conteo de operaciones\n\n")
        f.write("| Operación | Sin pivoteo | Pivoteo escalado |\n")
        f.write("|---|---:|---:|\n")
        f.write(f"| Multiplicaciones/divisiones | {total_sin['mult_div']} | {total_con['mult_div']} |\n")
        f.write(f"| Sumas/restas | {total_sin['sumas_restas']} | {total_con['sumas_restas']} |\n")
        f.write(f"| Actualizaciones de b | {total_sin['flops_b']} | {total_con['flops_b']} |\n")
        f.write(f"| Total aritmético | {total_sin['total']} | {total_con['total']} |\n")
        f.write(f"| Comparaciones de pivoteo | 0 | {con_pivoteo['comparaciones']} |\n")
        f.write(f"| Intercambios de filas | 0 | {con_pivoteo['intercambios']} |\n")

    return total_sin, total_con
