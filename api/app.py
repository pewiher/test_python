from flask import Flask, jsonify, request, make_response
import random

app = Flask(__name__)

# Tabla de códigos de sistema
SYSTEM_CODES = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Variable para almacenar el último sistema dañado
damaged_system = None

@app.route('/status', methods=['GET'])
def status():
    global damaged_system
    damaged_system = random.choice(list(SYSTEM_CODES.keys()))
    return jsonify({"damaged_system": damaged_system})

@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    if damaged_system is None:
        return "No damaged system reported yet.", 400

    system_code = SYSTEM_CODES.get(damaged_system, "UNKNOWN")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{system_code}</div>
    </body>
    </html>
    """
    return html

@app.route('/teapot', methods=['POST'])
def teapot():
    return make_response("I'm a teapot", 418)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
