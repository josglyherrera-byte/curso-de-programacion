def encontrar_primos(limite):
    primos = []
    
    for numero in range(2, limite + 1):
        es_primo = True
        
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                es_primo = False
                break
        
        if es_primo:
            primos.append(numero)
    
    return primos

# Entrada del usuario
try:
    limite = int(input("Ingrese el límite para buscar números primos: "))
    if limite < 2:
        print("El límite debe ser mayor o igual a 2")
    else:
        primos = encontrar_primos(limite)
        print(f"Números primos hasta {limite}:")
        print(primos)
except ValueError:
    print("Por favor ingrese un número válido")