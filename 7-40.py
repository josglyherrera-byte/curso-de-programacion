def procesar_orden(stock, orden):
    for producto in orden:
        if producto in stock:
            if stock[producto] > 0:
                stock[producto] -= 1
                print(f"✓ {producto}: Vendido. Stock restante: {stock[producto]}")
            else:
                print(f"✗ {producto}: Sin stock disponible")
        else:
            print(f"✗ {producto}: Producto no existe")

# Datos iniciales
stock = {
    "manzanas": 10,
    "naranjas": 5,
    "plátanos": 8,
    "uvas": 0
}

# Entrada del usuario
orden_compra = []
print("Ingrese los productos a comprar (escriba 'fin' para terminar):")
while True:
    producto = input("Producto: ").lower()
    if producto == 'fin':
        break
    orden_compra.append(producto)

print("\nProcesando orden...")
procesar_orden(stock, orden_compra)
print(f"\nStock final: {stock}")