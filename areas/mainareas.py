def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            print("\n--- Área del Cuadrado ---")
            try:
                lado = float(input("Ingrese la longitud del lado: "))
                if lado <= 0:
                    print("El lado debe ser un número positivo.")
                    continue
                area = area_cuadrado(lado)
                print(f" El área del cuadrado con lado {lado} es: {area:.2f}")
            except ValueError:
                print(" Entrada inválida. Por favor, ingrese un número.")

        elif opcion == '2':
            print("\n--- Área del Rectángulo ---")
            try:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                if base <= 0 or altura <= 0:
                    print("La base y la altura deben ser números positivos.")
                    continue
                area = area_rectangulo(base, altura)
                print(f" El área del rectángulo con base {base} y altura {altura} es: {area:.2f}")
            except ValueError:
                print(" Entrada inválida. Por favor, ingrese números.")

        elif opcion == '3':
            print("\n--- Área del Círculo ---")
            try:
                radio = float(input("Ingrese el radio: "))
                if radio <= 0:
                    print("El radio debe ser un número positivo.")
                    continue
                area = area_circulo(radio)
                print(f" El área del círculo con radio {radio} es: {area:.2f}")
            except ValueError:
                print(" Entrada inválida. Por favor, ingrese un número.")

        
        elif opcion == '4':
            print("\n--- Área del Triángulo ---")
            try:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                if base <= 0 or altura <= 0:
                    print("La base y la altura deben ser números positivos.")
                    continue
                area = area_triangulo(base, altura)
                print(f" El área del triángulo con base {base} y altura {altura} es: {area:.2f}")
            except ValueError:
                print(" Entrada inválida. Por favor, ingrese números.")
        

        elif opcion == '5':
            print("\n ¡Gracias por usar el Medidor de Áreas! ¡Adiós!")
            break  

        else:
            print("Opción no válida. Por favor, elija un número entre 1 y 5.")

if __name__ == "__main__":
    main()