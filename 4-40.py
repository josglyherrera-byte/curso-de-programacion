def km_a_millas(distancia_km):
    if distancia_km > 0:
        return distancia_km * 0.621371
    else:
        return None

# Entrada del usuario
distancias = []
print("Ingrese distancias en kilómetros (escriba 'fin' para terminar):")
while True:
    distancia = input("Distancia en KM: ")
    if distancia.lower() == 'fin':
        break
    try:
        distancias.append(float(distancia))
    except ValueError:
        print("Por favor ingrese un número válido")

print("\nConversión a millas:")
for km in distancias:
    millas = km_a_millas(km)
    if millas is not None:
        print(f"{km} KM = {millas:.2f} millas")
    else:
        print(f"{km} KM: Distancia no válida")