def calcular_multas(velocidades):
    multas = 0
    
    for v in velocidades:
        if v > 120:
            multas += 500
            print(f"Velocidad {v}km/h: Multa $500")
        elif 100 <= v <= 120:
            multas += 200
            print(f"Velocidad {v}km/h: Multa $200")
    
    return multas

# Entrada
velocidades = [float(input(f"Velocidad auto {i+1}: ")) for i in range(int(input("¿Cuántos autos? ")))]
print(f"\nTotal multas: ${calcular_multas(velocidades)}")