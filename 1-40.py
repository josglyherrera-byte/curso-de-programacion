def evaluar_notas():
    notas = []
    
    print("Ingresa notas (0-100). Escribe 'fin' para terminar:")
    
    while True:
        entrada = input("Nota: ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 100:
                notas.append(nota)
        except:
            print("Ingresa un número válido")
    
    if not notas:
        print("No se ingresaron notas")
        return
    
    suma = 0
    for nota in notas:
        suma += nota
    
    promedio = suma / len(notas)
    
    if promedio > 60:
        print("Aprobado")
    else:
        print("Reprobado")
    
    print(f"Promedio: {promedio:.1f}")
    
evaluar_notas()