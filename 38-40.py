def calcular_total(carrito):
    total = 0
    
    for producto, categoria, precio in carrito:
        if categoria == "Alimento":
            total += precio
        elif categoria == "Lujo":
            total += precio * 1.21  # +21% IVA
        else:
            total += precio * 1.16  # +16% IVA general
    
    return total

# Entrada
carrito = []
n = int(input("¿Cuántos productos? "))

for i in range(n):
    print(f"\nProducto {i+1}:")
    nombre = input("Nombre: ")
    categoria = input("Categoría (Alimento/Lujo/Otro): ")
    precio = float(input("Precio: $"))
    carrito.append((nombre, categoria, precio))

print(f"\nTotal a pagar: ${calcular_total(carrito):.2f}")