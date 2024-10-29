import requests
import functions
import threading
import functions as func

BASE_URL = 'http://127.0.0.1:5000/games'  # Cambia esta URL si tu API está en otro lugar

def listar_juegos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        juegos = response.json()
        print("\n")
        for juego in juegos:
         print(
                f"\nID: {juego['id']}, Nombre: {juego['title']}\n"
                f"Año de salida: {juego['release_year']}\n"
                f"Plataforma: {', '.join(juego['platforms'])}\n"
                f"Ganancias: ${juego['revenue']:,}\n"
            )

    else:
        print("Error al obtener la lista de juegos.")

def agregar_juego():
    nuevo_juego = {}
    nuevo_juego['name'] = input("Ingrese el nombre del juego: ")
    nuevo_juego['platform'] = input("Ingrese la plataforma del juego: ")
    
    response = requests.post(BASE_URL, json=nuevo_juego)
    if response.status_code == 201:
        print("Juego agregado exitosamente.")
    else:
        print("Error al agregar el juego.")

def eliminar_juego():
    game_id = int(input("Ingrese el ID del juego a eliminar: "))
    response = requests.delete(f"{BASE_URL}/{game_id}")
    if response.status_code == 200:
        print("Juego eliminado exitosamente.")
    else:
        print("Error al eliminar el juego o juego no encontrado.")


def run_server():
    functions.app.run(debug=True)

def main():
    # Bucle del menú
    while True:
        print("\nMenú de Opciones:")
        print("1. Listar todos los juegos")
        print("2. Obtener detalles de un juego")
        print("3. Agregar un nuevo juego")
        print("4. Eliminar un juego")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            func.obtener_juegos()
        elif opcion == '2':
            game_id = int(input("Ingrese el ID del juego: "))
            func.obtener_juego_por_id_local(game_id)
        elif opcion == '3':
            agregar_juego()
        elif opcion == '4':
            eliminar_juego()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
