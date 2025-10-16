import pi
import factorial
import fibonacci
import numerosamigos
import numerosperfectos
def obtener_precision():
    while True:
        try:
            precision = int(input("Ingresa la cantidad de dígitos decimales de precisión: "))
            if precision < 1:
                print("La precisión debe ser al menos 1.")
            else:
                return precision
        except ValueError:
            print("Por favor, ingresa un número válido.")

def menuanalisis():
    print("=== Bienvenido al menu de análisis ===")
    print("Qué desea hacer?")
    print("1. Calcular Pi")
    print("2. Calcular un factorial")
    print("3. Calcular sucesion de fibonacci")
    print("4. Ver números amigos")
    print("5. Ver números perfectos")
    print("6. Salir")
    opcion = input("Ingrese la opcion que desea:")
    while True:
        if opcion == "1":
            precision = obtener_precision
            pi_value = pi.chudnovsky_algorithm(precision)
            print(f"Valor de pi calculado con {precision} dígitos de precisión: {pi_value}")
        if opcion =="2":
            try:
                numero = int(input("Ingresa un número para calcular su factorial: "))
                if numero < 0:
                    print("El número debe ser mayor o igual a 0.")
                else:
                    resultado = factorial.factorial(numero)
                    print(f"El factorial de {numero} es {resultado}")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        if opcion=="3":
            try:
                numero = int(input("Ingresa cuántos términos de la sucesión de Fibonacci deseas calcular: "))
                if numero < 1:
                    print("Por favor, ingresa un número mayor o igual a 1.")
                else:
                    resultado = fibonacci.fibonacci(numero)
                    print(f"La sucesión de Fibonacci hasta el {numero}° término es: {resultado}")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        if opcion=="4":
            try:
                numero1 = int(input("Ingresa el primer número: "))
                numero2 = int(input("Ingresa el segundo número: "))
                if numerosamigos.son_numeros_amigos(numero1, numero2):
                    print(f"{numero1} y {numero2} son números amigos.")
                else:
                    print(f"{numero1} y {numero2} no son números amigos.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        if opcion=="5":
            try:
                numero = int(input("Ingresa un número para verificar si es perfecto: "))
                if numerosperfectos.es_numero_perfecto(numero):
                    print(f"{numero} es un número perfecto.")
                else:
                    print(f"{numero} no es un número perfecto.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        if opcion=="6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion inválida, intente de nuevo")
    