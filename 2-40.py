def es_par_y_multiplo_de_3(numero):
    if numero % 2 == 0 and numero % 3 == 0:
        return True
    return False

# Entrada del usuario
print("Números del 1 al 100 que son pares y múltiplos de 3:")
for i in range(1, 101):
    if es_par_y_multiplo_de_3(i):
        print(f"Número {i}: Cumple ambas condiciones")