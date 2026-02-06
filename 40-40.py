def ordenar_burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Entrada
nums = [int(input(f"Número {i+1}: ")) for i in range(int(input("¿Cuántos números? ")))]
print(f"\nLista original: {nums}")
print(f"Lista ordenada: {ordenar_burbuja(nums.copy())}")