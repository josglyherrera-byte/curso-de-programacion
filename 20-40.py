def permisos(rango):
    return {"Admin": "Ver/Editar/Borrar", 
            "Editor": "Ver/Editar", 
            "Lector": "Solo ver"}.get(rango, "Sin permisos")

n = int(input("¿Cuántos usuarios? "))
for _ in range(n):
    nombre = input("Nombre: ")
    rango = input("Rango: ")
    print(f"{nombre}: {permisos(rango)}")