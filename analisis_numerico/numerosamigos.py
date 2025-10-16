def suma_divisores(n):
    divisores = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)

def son_numeros_amigos(a, b):
    if a == suma_divisores(b) and b == suma_divisores(a):
        return True
    return False
