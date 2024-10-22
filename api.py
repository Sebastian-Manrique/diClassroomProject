from flask import Flask, jsonify
# %% Lista 1.


app = Flask(__name__)


@app.route('/api/lista1', methods=['GET'])
def obtener_lista1():
    datos = {
        "nombre": "Sebastian",
        "Edad": 19,
        "Residencia": "Seseña"
    }
    return jsonify(datos)

# %% Lista 2.


@app.route('/api/lista2', methods=['GET'])
def obtener_lista2():
    lista_datos = [
        {"nombre": "Sebastian", "Edad": 19, "Residencia": "Seseña"},
        {"nombre": "Javi", "Edad": 19, "Residencia": "Seseña"},
        {"nombre": "Manu", "Edad": 26, "Residencia": "Ciudad Real"},
        {"nombre": "Tymur", "Edad": 20, "Residencia": "Seseña Nuevo"}]
    return jsonify(lista_datos)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
