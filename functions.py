import json
import random

import pandas as pd

JSON_FILE_PATH = 'legoGames.json'


def cargar_datos_json():
    # Va hacia el json, esta función será llamado cada vez que se necesite leer este.
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def guardar_datos_json(juegos, filename=JSON_FILE_PATH):
    # Se llama hora de sobreescribir para la elimination o agregación de un juego
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(juegos, file, indent=4, ensure_ascii=False)


def obtener_juegos():
    # Se muestran todos los juegos con este bucle
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


def buscarJuegoPorId():
    # Se muestra el juego que coincide con el id escrito por el usuario
    game_id = int(input("Ingrese el ID del juego: "))
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


def agregar_juego():
    # Añade un juego a la lista, llama a comprobarID, guardar_datos_json y agregarPlataforma
    while True:  # Bucle para que se repita solo si el ID está ocupado
        game_id = comprobarInt("ID: ")
        if elIdEstaSiendoUsado(game_id):  # Si el ID está disponible, salimos del bucle
            break
        else:
            print("El ID está en uso, intenta con otro.")
    elIdEstaSiendoUsado(game_id)
    nuevo_juego = {
        'id': game_id,
        'title': input("Ingrese el nombre del juego: "),
        'release_year': comprobarInt("Ingrese el año de salida:"),
        'theme': input("Temática del juego: "),
        'director': input("Ingrese el nombre del director del juego: "),
        'production_years': comprobarInt("Años de producción del juego: "),
        'production_cost': comprobarInt("Coste de producción: "),
        'revenue': comprobarInt("Ganancias: "),
        'platforms': agregarPlataforma()
    }
    print("\n")
    df = pd.DataFrame(nuevo_juego)
    print(df)
    juegos = cargar_datos_json()
    juegos.append(nuevo_juego)
    guardar_datos_json(juegos)


def comprobarInt(texto):
    """Recibe el texto a imprimir"""
    # Se encarga de que siempre se guarden integers o floats dependiendo del caso
    '''Devuelve el int o el float creado'''
    while True:
        try:
            if "producción" in texto or "Ganancias" in texto:
                return float(input(texto))
            else:
                return int(input(texto))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero válido.")


def elIdEstaSiendoUsado(game_id):
    juegos = cargar_datos_json()
    juego = next((j for j in juegos if j['id'] == game_id), None)
    if juego:
        print(f"\nEl juego '{juego['title']}' ya tiene ese ID '{juego['id']}', inténtalo con otro ID.")
        return False
    return True


def agregarPlataforma():
    # Función llamada a la hora de agregar un juego para poner todas las plataformas para las que salió el juego
    """Devuelve la lista de las plataformas"""
    nPlataformas = int(input("¿En cuántas plataformas salió el juego? "))
    plataformas = []
    for i in range(nPlataformas):
        plataforma = input(f"Ingrese el nombre de la plataforma {i + 1}: ")
        plataformas.append(plataforma)
    print("\nPlataformas agregadas:", plataformas)
    return plataformas


def eliminarPorId():
    # Es una función muy parecida a la de buscar por id pero en vez de mostrarlo lo elimina.
    game_id = int(input("Ingrese el ID del juego: "))
    juegos = cargar_datos_json()
    index = next((i for i, j in enumerate(juegos) if j['id'] == game_id), None)
    if index is not None:
        juego = juegos[index]
        print(f"\nJuego encontrado {juego['title']}, eliminándolo . . .\n")
        del juegos[index]
        guardar_datos_json(juegos)
    else:
        print("Id no encontrado.")


def quiz():
    # Función llamada desde el menu principal que carga los intentos restantes, agarra un juego random
    # Y entra en el bucle y no sale hasta que se acierte el juego o se acaben los intentos.
    intentos = 3
    juegos = cargar_datos_json()
    if juegos:
        juego = random.choice(juegos)
        print(f"El juego empieza por: {juego['title'][5]} (dan igual las mayúsculas)")
        elJuegoSecreto = juego['title'].lower()
        while intentos > 0:
            adivinar_clean, juego_secreto_clean = quizPregunta(elJuegoSecreto)
            if adivinar_clean == juego_secreto_clean:
                print(f"¡Acertaste! El juego era: {juego_secreto_clean}")
                break
            else:
                intentos -= 1
                print(f"No acertaste, intentos restantes: {intentos}")
                if intentos == 2:
                    print(f"Pista: el juego salió en el año {juego['release_year']}")
                elif intentos == 1:
                    print(f"Pista: el juego salió en el año {juego['title'][5:7]}")
                else:
                    print(f"Se acabaron los intentos. El juego era: {juego['title']}")


def quizPregunta(elJuegoSecreto):
    """Recibe un string, que es el juego a adivinar"""
    # Función llamada desde el quiz con el unicorn objetivo de hacer la pregunta
    '''Devuelve dos strings,
    1º la respuesta del usuario sin mayúsculas y sin la palabra lego
    2º el juego a adivinar sin mayúsculas y sin la palabra lego'''

    adivinar = input("¿Qué juego crees que es? ").strip()
    adivinar_clean = adivinar.lower().replace("lego", "").strip()
    juego_secreto_clean = elJuegoSecreto.replace("lego", "").strip()
    return adivinar_clean, juego_secreto_clean
