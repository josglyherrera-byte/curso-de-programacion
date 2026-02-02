import random
num = random.randint(1, 100)

for i in range(10):
    intento = int(input(f"Intento {i+1}/10: "))
    
    if intento == num:
        print(f"¡Ganaste! Número: {num}")
        break
    elif intento < num:
        print("Muy BAJO")
    else:
        print("Muy ALTO")