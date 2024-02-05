import random
import copy
import time

def crear_matriz(m):
    return [[random.choice([0, 1]) for _ in range(m)] for _ in range(m)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))
    print()

def contar_vecinas(matriz, fila, columna):
    vecinas = 0
    filas, columnas = len(matriz), len(matriz[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            vecina_fila = (fila + i + filas) % filas
            vecina_columna = (columna + j + columnas) % columnas

            if matriz[vecina_fila][vecina_columna] == 1:
                vecinas += 1

    # Restar la celda central
    vecinas -= matriz[fila][columna]

    return vecinas

def aplicar_reglas(matriz):
    nueva_matriz = copy.deepcopy(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            vecinas = contar_vecinas(matriz, i, j)

            # Aplicar reglas
            if matriz[i][j] == 1 and (vecinas < 2 or vecinas > 3):
                nueva_matriz[i][j] = 0
            elif matriz[i][j] == 0 and vecinas == 3:
                nueva_matriz[i][j] = 1

    return nueva_matriz

# Definir el tamaño de la matriz
m = 5

# Crear matriz inicial (semilla)
semilla = crear_matriz(m)

# Imprimir semilla
print("Semilla:")
imprimir_matriz(semilla)

# Número de generaciones
num_generaciones = 5

# Simular generaciones
for generacion in range(num_generaciones):
    time.sleep(1)  # Pausa para visualizar cada generación
    semilla = aplicar_reglas(semilla)
    print(f"Generación {generacion + 1}:")
    imprimir_matriz(semilla)
