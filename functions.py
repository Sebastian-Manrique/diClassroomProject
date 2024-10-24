from flask import Flask, jsonify
import json
import pandas as pd
import requests  # Necesario para realizar solicitudes HTTP

app = Flask(__name__)

# Define la ruta relativa para acceder a los datos

@app.route('/games', methods=['GET'])
def obtener_lista2():
    # Ruta del archivo JSON
    url = 'legoGames.json'

    # Intenta abrir y leer el archivo JSON
    try:
        with open(url) as file:
            contenido = json.load(file)
        return jsonify(contenido)  # Devuelve el contenido como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    data = pd.DataFrame(pd.read_json('legoGames.json'))
    print(data) 
    app.run(debug=True)