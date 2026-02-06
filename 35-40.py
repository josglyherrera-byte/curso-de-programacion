def validar_isbn(isbn):
    if len(isbn) != 10 or not isbn[:-1].isdigit():
        return False
    
    suma = 0
    for i in range(9):
        suma += int(isbn[i]) * (i + 1)
    
    digito_control = isbn[9]
    digito_calculado = suma % 11
    
    if digito_control == 'X':
        return digito_calculado == 10
    else:
        return int(digito_control) == digito_calculado

# Entrada
isbn = input("ISBN (10 dígitos): ")
print(f"ISBN válido: {' Sí' if validar_isbn(isbn) else ' No'}")