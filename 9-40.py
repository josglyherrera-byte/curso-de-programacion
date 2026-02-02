def calcular_precio_final(precio_base):
    if precio_base > 100:
        iva = 0.16
    else:
        iva = 0.08
    
    precio_final = precio_base * (1 + iva)
    return precio_final, iva * 100

# Entrada del usuario
precios = []
print("Ingrese los precios de los productos (escriba 'fin' para terminar):")
while True:
    precio = input("Precio: $")
    if precio.lower() == 'fin':
        break
    try:
        precios.append(float(precio))
    except ValueError:
        print("Por favor ingrese un número válido")

print("\nCálculo de precios con IVA:")
for precio in precios:
    precio_final, porcentaje_iva = calcular_precio_final(precio)
    print(f"Precio base: ${precio:.2f} | IVA: {porcentaje_iva:.0f}% | Total: ${precio_final:.2f}")