a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print(f"Dos soluciones: {x1:.2f}, {x2:.2f}")
elif d == 0:
    x = -b/(2*a)
    print(f"Una solución: {x:.2f}")
else:
    print("Sin soluciones reales")