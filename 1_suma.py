def suma_maxima_subarreglo(arr):
    if not arr:
        return 0

    suma_maxima = suma_actual = arr[0]

    for num in arr[1:]:
        suma_actual = max(num, suma_actual + num)
        suma_maxima = max(suma_maxima, suma_actual)

    return suma_maxima

# Ejemplo de uso:
arr = [1,2,-1,-2,3,4,-5,4]
resultado = suma_maxima_subarreglo(arr)
print(f"La suma máxima de subarreglo es: {resultado}")
