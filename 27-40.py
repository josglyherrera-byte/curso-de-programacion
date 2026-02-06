def palabras_con_mayuscula(texto):
    palabras = texto.split()
    con_mayuscula = []
    
    for palabra in palabras:
        if palabra[0].isupper():
            con_mayuscula.append(palabra)
    
    return con_mayuscula

# Entrada
texto = input("Ingrese un párrafo: ")
resultado = palabras_con_mayuscula(texto)
print(f"Palabras con mayúscula ({len(resultado)}): {resultado}")