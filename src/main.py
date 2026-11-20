# Codigo hecho por Ariel Gallardo y Manuel Fuentes
import csv
from pathlib import Path
from decimal import Decimal

from gauss import (
    eliminacion_gaussiana,
    incognitas,
    factorizar_pivoteo_escalado,
    resolver_con_lu
)
from verificacion import verificacion
from conteo import guardar_conteo


CARPETA = Path(__file__).resolve().parent
RAIZ = CARPETA.parent
DATOS = RAIZ / "datos"
RESULTADOS = RAIZ / "resultados"
RESULTADOS.mkdir(parents=True, exist_ok=True)


def cargar_matriz(ruta):
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return [
            [Decimal(valor.strip()) for valor in fila]
            for fila in csv.reader(archivo)
            if fila
        ]


def cargar_vector(ruta):
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return [
            Decimal(fila[0].strip())
            for fila in csv.reader(archivo)
            if fila
        ]


def guardar_solucion(x_sin, x_con, x_refinada):
    with open(RESULTADOS / "solucion.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Incognita", "Sin_pivoteo", "Pivoteo_escalado", "Refinada"])

        for i in range(len(x_sin)):
            escritor.writerow([
                f"x{i + 1}",
                f"{x_sin[i]:.16e}",
                f"{x_con[i]:.16e}",
                f"{x_refinada[i]:.16e}"
            ])


def guardar_traza(sin_pivoteo, con_pivoteo):
    with open(RESULTADOS / "traza_eliminacion.txt", "w", encoding="utf-8") as f:
        f.write("ELIMINACIÓN SIN PIVOTEO\n\n")

        for paso in sin_pivoteo["desglose"]:
            f.write(f"{paso}\n")

        f.write("\nELIMINACIÓN CON PIVOTEO PARCIAL ESCALADO\n\n")

        for paso in con_pivoteo["desglose"]:
            f.write(f"{paso}\n")


def main():
    A_decimal = cargar_matriz(DATOS / "matriz_a.csv")
    b_decimal = cargar_vector(DATOS / "vector_b.csv")

    n = len(A_decimal)

    if n != 12 or any(len(fila) != n for fila in A_decimal):
        raise ValueError("La matriz debe ser de 12 x 12.")

    if len(b_decimal) != n:
        raise ValueError("El vector b debe tener 12 elementos.")

    A = [[float(v) for v in fila] for fila in A_decimal]
    b = [float(v) for v in b_decimal]

    U_sin, b_sin, stats_sin = eliminacion_gaussiana(A, b)
    x_sin, sustitucion_sin = incognitas(U_sin, b_sin)

    L, U, perm, stats_con = factorizar_pivoteo_escalado(A)
    x_con, sustitucion_con = resolver_con_lu(L, U, perm, b)

    x_refinada, norma_r0, norma_r1 = verificacion(
        A_decimal, b_decimal, x_con, L, U, perm
    )

    guardar_solucion(x_sin, x_con, x_refinada)
    guardar_traza(stats_sin, stats_con)

    total_sin, total_con = guardar_conteo(
        RESULTADOS / "conteo_flops.md",
        stats_sin,
        stats_con,
        sustitucion_sin,
        sustitucion_con
    )

    print("\n--- Solución sin pivoteo ---")
    for i, valor in enumerate(x_sin):
        print(f"x{i + 1} = {valor:.12e}")

    print("\n--- Solución con pivoteo escalado ---")
    for i, valor in enumerate(x_con):
        print(f"x{i + 1} = {valor:.12e}")

    print("\n--- Solución refinada ---")
    for i, valor in enumerate(x_refinada):
        print(f"x{i + 1} = {valor:.12e}")

    print("\n--- Análisis sin pivoteo ---")
    print("Multiplicador máximo:", stats_sin["multiplicador_maximo"])
    print("Factor de crecimiento:", stats_sin["factor_crecimiento"])
    print("Total de operaciones:", total_sin["total"])

    print("\n--- Análisis con pivoteo escalado ---")
    print("Multiplicador máximo:", stats_con["multiplicador_maximo"])
    print("Factor de crecimiento:", stats_con["factor_crecimiento"])
    print("Comparaciones:", stats_con["comparaciones"])
    print("Intercambios:", stats_con["intercambios"])
    print("Total de operaciones:", total_con["total"])

    print("\n--- Verificación ---")
    print("Norma del residuo inicial:", norma_r0)
    print("Norma del residuo final:", norma_r1)

    print("\nArchivos generados en:", RESULTADOS)


if __name__ == "__main__":
    main()
