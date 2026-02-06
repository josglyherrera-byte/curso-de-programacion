def censurar_texto(texto, prohibidas):
    palabras = texto.split()
    
    for i in range(len(palabras)):
        if palabras[i] in prohibidas:
            palabras[i] = "****"
    
    return " ".join(palabras)

# Entrada
texto = input("Texto: ")
prohibidas = input("Palabras prohibidas (separadas por espacio): ").split()
print(f"Texto censurado:\n{censurar_texto(texto, prohibidas)}")