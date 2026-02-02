binario = input("Binario: ")
if all(c in "01" for c in binario):
    decimal = sum(int(b) * 2**i for i, b in enumerate(binario[::-1]))
    print(f"Decimal: {decimal}")
else:
    print("Error: Solo 0 y 1")