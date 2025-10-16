import math

def chudnovsky_algorithm(precision):
    C = 640320
    M = 1
    L = 13591409
    K = 6
    X = 1
    K_plus_3 = 3
    S = L
    threshold = 10 ** (-precision)
    pi_prev = 0
    n = 1
    while True:
        M = (K**3 - 16*K) * M // (n**3)
        L += 545140134
        X *= -262537412640768000
        K += 12
        K_plus_3 += 6
        term = M * L / (X * K_plus_3)
        S += term
        pi = (12 * S) ** -1
        if abs(pi - pi_prev) < threshold:
            break
        pi_prev = pi
        n += 1
    return pi



 