def cajero_automatico():
    saldo = 1000.00
    
    while True:
        print("\n=== CAJERO AUTOMÁTICO ===")
        print(f"Saldo disponible: ${saldo:.2f}")
        print("1. Ver saldo")
        print("2. Retirar dinero")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            print(f"Su saldo actual es: ${saldo:.2f}")
        
        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a retirar: $"))
                
                if monto <= 0:
                    print("Monto no válido. Debe ser mayor a 0.")
                elif monto > saldo:
                    print("Fondos insuficientes.")
                else:
                    saldo -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            except ValueError:
                print("Por favor ingrese un monto válido")
        
        elif opcion == "3":
            print("¡Gracias por usar nuestro cajero!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

cajero_automatico()