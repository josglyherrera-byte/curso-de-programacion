def encriptar(texto):
    resultado = ""
    
    for letra in texto:
        if letra.isalpha():
            if letra == 'z':
                resultado += 'a'
            elif letra == 'Z':
                resultado += 'A'
            else:
                resultado += chr(ord(letra) + 1)
        else:
            resultado += letra
    
    return resultado

# Entrada
texto = input("Texto a encriptar: ")
print(f"Texto encriptado: {encriptar(texto)}")