def imprimir_saltando_multiplos(limite):
    for numero in range(1, limite + 1):
        if numero % 4 == 0:
            continue
        print(f"Número: {numero}")

# Entrada del usuario
try:
    limite = int(input("Ingrese el límite máximo: "))
    imprimir_saltando_multiplos(limite)
except ValueError:
    print("Por favor ingrese un número válido")