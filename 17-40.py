def calcular_precio(cat, precio):
    descuentos = {"Electrónica": 0.3, "Ropa": 0.2, "Alimentos": 0.1}
    desc = descuentos.get(cat, 0.05)
    return precio * (1 - desc)

n = int(input("¿Cuántos productos? "))
for _ in range(n):
    nom = input("Nombre: ")
    cat = input("Categoría: ")
    pre = float(input("Precio: "))
    print(f"Precio final: ${calcular_precio(cat, pre):.2f}\n")