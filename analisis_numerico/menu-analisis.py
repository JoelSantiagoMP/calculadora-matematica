import pi
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
            calcularfact()
        if opcion=="3":
            calcularfibo()
        if opcion=="4":
            vernumamigos()
        if opcion=="5":
            verperfectos()
        if opcion=="6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion inválida, intente de nuevo")
    