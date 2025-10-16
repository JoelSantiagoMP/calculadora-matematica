def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor o igual a 1."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2]) 
        return fib
