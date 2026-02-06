def suma_digitos(numero):
    suma = 0
    
    for digito in str(numero):
        if digito.isdigit():
            suma += int(digito)
    
    return suma

# Entrada
numero = input("Ingrese un número: ")
print(f"Suma de dígitos: {suma_digitos(numero)}")