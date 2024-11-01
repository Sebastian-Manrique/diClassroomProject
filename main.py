import functions as func


def main():
    # Bucle del menú
    while True:
        print("\nMenú de Opciones:")
        print("1. Listar todos los juegos")
        print("2. Obtener detalles de un juego")
        print("3. Agregar un nuevo juego")
        print("4. Eliminar un juego")
        print("5. Quiz")
        print("6. Salir")

        option = input("Seleccione una opción (1-6): ")

        match option:
            case '1':
                func.obtener_juegos()
            case '2':
                func.buscarJuegoPorId()
            case '3':
                func.agregar_juego()
            case '4':
                func.eliminarPorId()
            case '5':
                func.quiz()
            case '6':
                print("Saliendo del programa.")
                break
            case _:
                print("Error, introduzca un valor valido")


if __name__ == "__main__":
    main()
