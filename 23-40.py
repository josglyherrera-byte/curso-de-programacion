def eliminar_duplicados(lista):
    unicos = []
    
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    
    return unicos

# Entrada
nums = [int(input(f"Número {i+1}: ")) for i in range(int(input("¿Cuántos números? ")))]
print(f"Lista sin duplicados: {eliminar_duplicados(nums)}")
