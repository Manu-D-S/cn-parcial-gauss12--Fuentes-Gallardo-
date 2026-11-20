def resumen_conteo(stats_eliminacion, stats_sustitucion):
    # La actualización de b tiene una multiplicación
    # y una resta por cada fila actualizada.
    flops_b = stats_eliminacion.get("flops_b", 0)

    md_b = flops_b // 2
    sr_b = flops_b // 2

    md = (
        stats_eliminacion["mult_div_A"]
        + stats_sustitucion["mult_div"]
        + md_b
    )

    sr = (
        stats_eliminacion["sumas_restas_A"]
        + stats_sustitucion["sumas_restas"]
        + sr_b
    )

    return {
        "mult_div": md,
        "sumas_restas": sr,
        "total": md + sr
    }


def guardar_conteo(
    ruta,
    sin_pivoteo,
    con_pivoteo,
    sustitucion_sin,
    sustitucion_con
):
    total_sin = resumen_conteo(
        sin_pivoteo,
        sustitucion_sin
    )

    total_con = resumen_conteo(
        con_pivoteo,
        sustitucion_con
    )

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("# Conteo de operaciones por paso\n\n")

        f.write(
            "Convención: 1 flop equivale a una operación "
            "aritmética elemental (+, -, *, /). "
            "Las comparaciones, divisiones de búsqueda de pivote "
            "e intercambios se informan aparte.\n\n"
        )

        corridas = [
            (
                "Sin pivoteo",
                sin_pivoteo,
                sustitucion_sin,
                total_sin
            ),
            (
                "Pivoteo escalado",
                con_pivoteo,
                sustitucion_con,
                total_con
            )
        ]

        for nombre, stats, sustitucion, total in corridas:
            f.write(f"## Corrida: {nombre}\n\n")

            f.write(
                "| Fase | Mult./Div. | Sumas/Restas | "
                "Flops | Comparaciones | Div. pivoteo | Intercambios |\n"
            )
            f.write(
                "|---|---:|---:|---:|---:|---:|---:|\n"
            )

            for paso in stats["desglose"]:
                md = paso["mult_div_A"]
                sr = paso["sumas_restas_A"]
                flops = md + sr

                comparaciones = paso.get("comparaciones", 0)
                divisiones = paso.get("divisiones_pivoteo", 0)

                intercambio = paso.get(
                    "fila_intercambiada",
                    "No"
                )

                intercambios = int(intercambio != "No")

                f.write(
                    f"| Eliminación {paso['paso']} "
                    f"| {md} "
                    f"| {sr} "
                    f"| {flops} "
                    f"| {comparaciones} "
                    f"| {divisiones} "
                    f"| {intercambios} |\n"
                )

                flops_b = paso.get("flops_b", 0)

                if flops_b:
                    md_b = flops_b // 2
                    sr_b = flops_b // 2

                    f.write(
                        f"| Actualización de b {paso['paso']} "
                        f"| {md_b} "
                        f"| {sr_b} "
                        f"| {flops_b} "
                        f"| 0 | 0 | 0 |\n"
                    )

            md_sust = sustitucion["mult_div"]
            sr_sust = sustitucion["sumas_restas"]

            f.write(
                f"| Sustitución "
                f"| {md_sust} "
                f"| {sr_sust} "
                f"| {md_sust + sr_sust} "
                f"| 0 | 0 | 0 |\n"
            )

            comparaciones = stats.get("comparaciones", 0)
            comparaciones_escalas = stats.get(
                "comparaciones_escalas",
                0
            )

            divisiones_pivoteo = stats.get(
                "divisiones_pivoteo",
                0
            )

            intercambios = stats.get("intercambios", 0)

            f.write(
                f"| **Total aritmético** "
                f"| **{total['mult_div']}** "
                f"| **{total['sumas_restas']}** "
                f"| **{total['total']}** "
                f"| **{comparaciones}** "
                f"| **{divisiones_pivoteo}** "
                f"| **{intercambios}** |\n\n"
            )

            f.write(
                f"Total aritmético: **{total['total']} flops**.\n\n"
            )

            if comparaciones_escalas:
                f.write(
                    "Comparaciones para calcular escalas: "
                    f"**{comparaciones_escalas}**.\n\n"
                )

            f.write(
                f"Comparaciones durante la búsqueda de pivote: "
                f"**{comparaciones}**.\n\n"
            )

            f.write(
                f"Divisiones para calcular razones de pivoteo: "
                f"**{divisiones_pivoteo}**.\n\n"
            )

            f.write(
                f"Intercambios de filas: **{intercambios}**.\n\n"
            )

    return total_sin, total_con
