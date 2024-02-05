def movimientos_validos_caballo(fila, columna):
    movimientos = []

    # Definir todos los posibles movimientos del caballo
    posibles_movimientos = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    # Verificar cada posible movimiento y agregarlo si es válido
    for movimiento in posibles_movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        # Verificar si el nuevo movimiento está dentro del tablero (8x8)
        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos

# Ejemplo de uso
ubicacion_inicial = (2, 3)  # Coordenadas iniciales del caballo (fila, columna)

movimientos = movimientos_validos_caballo(*ubicacion_inicial)

print(f"Los movimientos válidos para el caballo en {ubicacion_inicial} son:")
for movimiento in movimientos:
    print(movimiento)
