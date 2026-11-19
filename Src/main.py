# Codigo hecho por Ariel Gallardo y Manuel Fuentes
import csv
from pathlib import Path
from gauss import eliminacion_gaussiana, pivoteo_parcial, incognitas
from verificacion import verificacion

esta_carpeta = Path(__file__).resolve().parent
resumen = esta_carpeta.parent / "datos"
resumen.mkdir(parents=True, exist_ok=True)

# Programa principal
if __name__ == "__main__":
    matriz_lista = []
    b = []
    with open(resumen / "matriz_a.csv", mode="r", newline="", encoding="utf-8") as ar:
        lector = csv.reader(ar)
        for fila in lector:
            matriz_lista.append(list(map(float, fila)))

    with open(resumen / "vector_b.csv", mode="r", newline="", encoding="utf8") as ar:
        lector = csv.reader(ar)
        for fila in lector:
            b.append(float(fila[0]))

    # Eliminacion gaussiana sin pivoteo
    (U, b_mod, pasos, md_A, sr_A, flops_b) = eliminacion_gaussiana(matriz_lista, b)

    # con pivoteo parcial
    (M, vec_b, desglose_pasos, total_mult_div_A, total_sumas_restas_A,
     total_flops_b, total_comparaciones, total_intercambios_filas,
     total_movimientos_memoria) = pivoteo_parcial(matriz_lista, b)

    # Incognitas de x
    x, sum_res_incognitas, mult_div_incognitas = incognitas(M, vec_b)

    # La verificacion y contraste usando numpy
    verificacion(matriz_lista, b, x)

    # Resultados en terminal
    print("ELIMINACION GAUSSIANA")
    print(f"{'Paso':<6} | {'Mult/Div (A)':<14} | {'Sum/Rest (A)':<14} | {'Flops A':<10} | {'Flops b':<8}")
    print("-" * 62)
    for p in pasos:
        print(f"{p['paso']:<6} | {p['mult_div_A']:<14} | {p['sumas_restas_A']:<14} | {p['subtotal_flops_A']:<10} | {p['flops_b']:<8}")

    print("-" * 62)
    print(f"Total Mult/Div en A: {md_A}")
    print(f"Total Sumas/Restas en A: {sr_A}")
    print(f"Total Flops en A: {md_A + sr_A}")
    print(f"Total Flops en vector b: {flops_b}")
    print("-" * 100)
    print("\nPIVOTEO PARCIAL")

    print(f"{'Paso':<5} | {'M/D (A)':<8} | {'S/R (A)':<8} | {'Flops A':<8} | {'Flops b':<8} | {'Comp.':<6} | {'Intercambio'}")
    print("-" * 72)
    for p in desglose_pasos:
        print(f"{p['paso']:<5} | {p['mult_div_A']:<8} | {p['sumas_restas_A']:<8} | {p['flops_A']:<8} | {p['flops_b']:<8} | {p['comparaciones']:<6} | {p['intercambio']}")

    print("-" * 72)
    print(f"Total Mult/Div en A     : {total_mult_div_A}")
    print(f"Total Sumas/Restas en A : {total_sumas_restas_A}")
    print(f"Total Flops en A        : {total_mult_div_A + total_sumas_restas_A}")
    print(f"Total Flops en b        : {total_flops_b}")
    print("-" * 72)
    print("SOBRECOSTO DE ESTABILIDAD (PIVOTE0 PARCIAL):")
    print(f"Comparaciones de búsqueda: {total_comparaciones}")
    print(f"Intercambios de filas    : {total_intercambios_filas}")
    print(f"Elementos reubicados     : {total_movimientos_memoria}")
    