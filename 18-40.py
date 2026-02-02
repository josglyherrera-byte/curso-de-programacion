texto = input("Texto: ").split()
largas = [p for p in texto if len(p.strip(".,")) > 7]

print(f"Palabras >7 letras: {len(largas)}")
if largas: print(f"Lista: {', '.join(largas)}")