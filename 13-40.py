def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Entrada del usuario
while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        
        if numero < 0:
            print("El número debe ser positivo. Intente nuevamente.")
        elif numero == 0:
            print("El factorial de 0 es 1")
            break
        else:
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
            break
    except ValueError:
        print("Por favor ingrese un número entero válido.")