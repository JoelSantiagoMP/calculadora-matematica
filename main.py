def mostrar_menu_principal():
    """Muestra el menú principal de la calculadora."""
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Cálculo de áreas")
    print("2. Cálculo de superficies")
    print("3. Análisis numérico")
    print("4. [Pendiente de implementar]")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")
def main():
    """Función principal del programa."""
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            print("Módulo de áreas aún no implementado")
        elif opcion == "2":
            print("Módulo de superficies aún no implementado")
        elif opcion == "3":
            print("Módulo de análisis numérico aún no implementado")
        elif opcion == "4":
            print("Esta funcionalidad está pendiente de implementar")
        elif opcion == "5":
            print("¡Gracias por usar la calculadora matemática!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
main()