def años_para_duplicar(inversion, interes):
    años = 0
    monto = inversion
    
    while monto < inversion * 2:
        monto *= (1 + interes/100)
        años += 1
    
    return años

# Entrada
inversion = float(input("Inversión inicial: $"))
interes = float(input("Interés anual (%): "))
print(f"Años para duplicar: {años_para_duplicar(inversion, interes)}")