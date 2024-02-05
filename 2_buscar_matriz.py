def buscar_elemento(matriz, elemento):
    # Obtener las dimensiones de la matriz
    n = len(matriz)
    
    # Bucle para recorrer la matriz
    for i in range(n):
        for j in range(n):
            # Verificar si el elemento actual es igual al elemento buscado
            if matriz[i][j] == elemento:
                # Devolver las coordenadas si se encuentra el elemento
                return i, j
    
    # Devolver None si el elemento no se encuentra en la matriz
    return None

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento_buscado = 9

coordenadas = buscar_elemento(matriz, elemento_buscado)

if coordenadas:
    print(f"El elemento {elemento_buscado} se encuentra en las coordenadas {coordenadas}")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la matriz")
