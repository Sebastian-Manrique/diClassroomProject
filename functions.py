import json
import pandas as pd

# Define la ruta del archivo JSON
JSON_FILE_PATH = 'legoGames.json'

# Función para cargar el archivo JSON
def cargar_datos_json():
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []

# Función para obtener la lista completa de juegos
def obtener_juegos():
    juegos = cargar_datos_json()
    if juegos:
        for juego in juegos:
            print(
                f"\nID: {juego['id']}, Nombre: {juego['title']}\n"
                f"Año de salida: {juego['release_year']}\n"
                f"Plataforma: {', '.join(juego['platforms'])}\n"
                f"Ganancias: ${juego['revenue']:,}\n"
            )
    else:
        print("No se pudo cargar la lista de juegos.")

# Función para obtener un juego por ID
def obtener_juego_por_id_local(game_id):
    juegos = cargar_datos_json()
    juego = next((j for j in juegos if j['id'] == game_id), None)
    if juego:
        print(
            f"\nID: {juego['id']}, Nombre: {juego['title']}\n"
            f"Año de salida: {juego['release_year']}\n"
            f"Plataforma: {', '.join(juego['platforms'])}\n"
            f"Theme: {juego['theme']}\n"
            f"Director: {juego['director']}\n"
            f"Production Years: {juego['production_years']}\n"
            f"Production Cost: ${juego['production_cost']:,}\n"
            f"Revenue: ${juego['revenue']:,}\n"
            f"Ganancias: ${juego['revenue'] - juego['production_cost']:,}\n"
        )
    else:
        print("Juego no encontrado.")