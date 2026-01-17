p1 = input("Jugador 1 (piedra/papel/tijera): ").lower()
p2 = input("Jugador 2 (piedra/papel/tijera): ").lower()

if p1 == p2:
    print("Empate")
elif (p1 == "piedra" and p2 == "tijera") or \
     (p1 == "papel" and p2 == "piedra") or \
     (p1 == "tijera" and p2 == "papel"):
    print("Gana Jugador 1")
else:
    print("Gana Jugador 2")