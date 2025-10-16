def suma_divisores(n):
    divisores = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)

def es_numero_perfecto(n):
    return n == suma_divisores(n)
