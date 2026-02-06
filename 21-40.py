def fibonacci_pares(n):
    a, b = 0, 1
    pares = []
    
    while a <= n:
        if a % 2 == 0:
            pares.append(a)
        a, b = b, a + b
    
    return pares

# Entrada
n = int(input("Límite para Fibonacci: "))
print(f"Fibonacci pares hasta {n}: {fibonacci_pares(n)}")