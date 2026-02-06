def analizar_actividad(pasos_diarios):
    for i, pasos in enumerate(pasos_diarios):
        if pasos < 5000:
            print(f"Día {i+1}: {pasos} pasos -  Sedentario")
        else:
            print(f"Día {i+1}: {pasos} pasos -  Activo")

# Entrada
dias = int(input("¿Cuántos días? "))
pasos = [int(input(f"Pasos día {i+1}: ")) for i in range(dias)]

analizar_actividad(pasos)