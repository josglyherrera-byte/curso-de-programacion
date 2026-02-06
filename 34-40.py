def simular_elevador():
    piso_actual = 0
    
    while True:
        destino = int(input(f"\nPiso actual: {piso_actual}. Piso destino (-1 para salir): "))
        
        if destino == -1:
            print("¡Viaje finalizado!")
            break
        
        if destino < -2 or destino > 10:
            print(" Piso inválido (solo -2 a 10)")
            continue
        
        # Mostrar trayecto
        if destino > piso_actual:
            for p in range(piso_actual + 1, destino + 1):
                print(f"Subiendo... Piso {p}")
        else:
            for p in range(piso_actual - 1, destino - 1, -1):
                print(f"Bajando... Piso {p}")
        
        piso_actual = destino

simular_elevador()