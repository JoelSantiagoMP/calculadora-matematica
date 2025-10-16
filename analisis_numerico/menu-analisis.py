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
            calcularpi()
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
    