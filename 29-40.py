def reservar_asiento(asientos, numero):
    if asientos[numero] == 0:
        asientos[numero] = 1
        return True
    return False

# Datos iniciales (10 asientos, todos libres)
asientos = [0] * 10

while True:
    print(f"\nAsientos: {asientos}")
    num = int(input("Número de asiento (0-9) o -1 para salir: "))
    
    if num == -1:
        break
    
    if 0 <= num < len(asientos):
        if reservar_asiento(asientos, num):
            print("✅Asiento reservado")
        else:
            print(" Asiento ocupado")
    else:
        print(" Número inválido")