def gestionar_agenda():
    agenda = {}
    
    while True:
        print("\n1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            if nombre in agenda:
                print("Contacto ya existe")
            else:
                telefono = input("Teléfono: ")
                agenda[nombre] = telefono
                print(" Contacto agregado")
        
        elif opcion == "2":
            print("\nContactos:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        
        elif opcion == "3":
            break

gestionar_agenda()