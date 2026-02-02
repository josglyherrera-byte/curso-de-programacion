def limpiar_nombre(nombre):
    nombre = nombre.strip("!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~` ")
    return nombre

def validar_nombre(nombre):
    return len(nombre) >= 2 and not nombre.isdigit()

# Entrada del usuario
usuarios = [input(f"Usuario {i+1}: ") for i in range(int(input("¿Cuántos usuarios? ")))]

print("\nUsuarios validados:")
for u in usuarios:
    u_limpio = limpiar_nombre(u)
    if validar_nombre(u_limpio):
        print(f"✓ '{u_limpio}'")