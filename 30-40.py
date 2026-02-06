def promedio_ventas(ventas):
    total = 0
    dias_con_ventas = 0
    
    for venta in ventas:
        if venta > 0:
            total += venta
            dias_con_ventas += 1
    
    return total / dias_con_ventas if dias_con_ventas > 0 else 0

# Entrada
ventas = [float(input(f"Ventas día {i+1}: $")) for i in range(int(input("¿Cuántos días? ")))]
print(f"Promedio (sin días en 0): ${promedio_ventas(ventas):.2f}")