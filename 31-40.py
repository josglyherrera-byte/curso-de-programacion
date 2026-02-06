def contar_vocales(palabra):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in palabra.lower():
        if letra in vocales:
            vocales[letra] += 1
    
    # Mostrar solo vocales que aparecen
    resultado = {}
    for vocal, cantidad in vocales.items():
        if cantidad > 0:
            resultado[vocal] = cantidad
    
    return resultado

# Entrada
palabra = input("Palabra: ")
print(f"Vocales encontradas: {contar_vocales(palabra)}")