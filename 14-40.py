def calcular_salario(horas, tarifa):
    if horas <= 40: 
        return horas * tarifa, 0
    else:
        extra = horas - 40
        return (40 * tarifa) + (extra * tarifa * 2), extra

tarifa = float(input("Tarifa por hora: $"))
n = int(input("¿Cuántos empleados? "))

for _ in range(n):
    nombre = input("Nombre: ")
    horas = float(input("Horas trabajadas: "))
    salario, extra = calcular_salario(horas, tarifa)
    print(f"{nombre}: ${salario:.2f} (Extra: {extra} hrs)\n")