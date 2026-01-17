precio = float(input("Precio: $"))
if precio > 100:
    final = precio * 0.85
    print(f"Precio final con 15% de descuento:, {final}")
else:
    print(f"Precio final: {precio}")    