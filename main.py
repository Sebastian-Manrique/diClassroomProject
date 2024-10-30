import requests
import functions
import functions as func

BASE_URL = 'http://127.0.0.1:5000/games'  # Cambia esta URL si tu API está en otro lugar

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
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            func.obtener_juegos()
        elif opcion == '2':
            game_id = int(input("Ingrese el ID del juego: "))
            func.obtener_juego_por_id_local(game_id)
        elif opcion == '3':
            func.agregar_juego()
        elif opcion == '4':
            func.eliminar_juego()
        elif opcion == '5':
            func.quiz()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
