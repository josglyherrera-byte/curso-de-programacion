zona = input("Zona (A/B): ").upper()
peso = float(input("Peso (kg): "))
costo = 0

if zona == "A":
    costo = 10
    if peso > 5: costo = 15
else:
    costo = 20
    if peso > 5: costo = 25

print(f"Costo: ${costo}")