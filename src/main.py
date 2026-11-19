
import csv
from pathlib import Path

# Ubicacion de los archivos
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_A = BASE_DIR / "datos" / "matriz_a.csv"
RUTA_B = BASE_DIR / "datos" / "vector_b.csv"

def lecturaDatos(ruta):

    A=[]

    with open (ruta,"r",newline="",encoding="utf-8-sig") as archivo:
        lectura=csv.reader(archivo)

        for fila in lectura:
            if fila:
                A.append([float(valor)for valor in fila])
        return A

def lecturaVectores(ruta):

    B=[]
    with open (ruta,"r",newline="",encoding="utf-8-sig") as archivo:
        lectura=csv.reader(archivo)

        for fila in lectura:
            if fila:
               B.append(float(fila[0]))
        return B   

def main():
    Matriz_A = lecturaDatos(RUTA_A)
    Vectores= lecturaVectores(RUTA_B)
    print(Matriz_A)
    print(Vectores)

if __name__ == "__main__":
    main()