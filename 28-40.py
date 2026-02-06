def piramide_impares(altura):
    for i in range(1, altura + 1):
        if i % 2 != 0:  # Solo filas impares
            print(" " * (altura - i) + "*" * (2*i - 1))

# Entrada
altura = int(input("Altura de la pirámide: "))
piramide_impares(altura)