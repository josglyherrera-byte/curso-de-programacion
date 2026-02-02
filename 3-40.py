def verificar_login():
    contraseña_correcta = "Python123"
    intentos = 3
    
    while intentos > 0:
        print(f"\nIntentos restantes: {intentos}")
        contraseña = input("Ingrese su contraseña: ")
        
        if contraseña == contraseña_correcta:
            nombre = input("¡Contraseña correcta! Ingrese su nombre: ")
            print(f"¡Bienvenido, {nombre}!")
            return True
        else:
            print("Contraseña incorrecta")
            intentos -= 1
    
    print("Cuenta bloqueada. Demasiados intentos fallidos.")
    return False

verificar_login()