def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Entrada
pacientes = []
n = int(input("¿Cuántos pacientes? "))

for i in range(n):
    print(f"\nPaciente {i+1}:")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    pacientes.append((peso, altura))

print("\nResultados IMC:")
for i, (peso, altura) in enumerate(pacientes):
    clasificacion = calcular_imc(peso, altura)
    print(f"Paciente {i+1}: {clasificacion}")