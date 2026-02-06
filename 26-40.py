def convertir_a_letras(notas):
    letras = []
    
    for nota in notas:
        if nota >= 90:
            letras.append("A")
        elif nota >= 80:
            letras.append("B")
        elif nota >= 70:
            letras.append("C")
        elif nota >= 60:
            letras.append("D")
        else:
            letras.append("F")
    
    return letras

# Entrada
notas = [float(input(f"Nota {i+1}: ")) for i in range(int(input("¿Cuántas notas? ")))]
print(f"Calificaciones: {convertir_a_letras(notas)}")