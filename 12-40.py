def es_palindromo(palabra):
    return palabra.lower() == palabra[::-1].lower()

# Entrada del usuario
palabras = [input(f"Palabra {i+1}: ") for i in range(int(input("¿Cuántas palabras? ")))]

print("\nPalíndromos (+5 letras):")
for p in palabras:
    if len(p) > 5 and es_palindromo(p):
        print(f"- {p}")