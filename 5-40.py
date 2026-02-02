def contar_letra(texto, letra):
    contador = 0
    texto = texto.lower()
    letra = letra.lower()
    
    for caracter in texto:
        if caracter == letra:
            contador += 1
    
    if contador == 0:
        return f"Error: La letra '{letra}' no aparece en el texto"
    else:
        return f"La letra '{letra}' aparece {contador} veces"

# Entrada del usuario
frase = input("Ingrese una frase: ")
letra_buscar = input("Ingrese la letra a buscar: ")

resultado = contar_letra(frase, letra_buscar)
print(resultado)