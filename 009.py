from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos simulados basados en el diagrama
phase_data = {
    0.1:  {"specific_volume_liquid": 0.001043, "specific_volume_vapor": 1.694},
    0.5:  {"specific_volume_liquid": 0.001093, "specific_volume_vapor": 0.3749},
    1.0:  {"specific_volume_liquid": 0.001127, "specific_volume_vapor": 0.1944},
    2.0:  {"specific_volume_liquid": 0.001170, "specific_volume_vapor": 0.09863},
    5.0:  {"specific_volume_liquid": 0.001237, "specific_volume_vapor": 0.03939},
    7.5:  {"specific_volume_liquid": 0.001280, "specific_volume_vapor": 0.0263},
    9.0:  {"specific_volume_liquid": 0.001295, "specific_volume_vapor": 0.0218},
    9.5:  {"specific_volume_liquid": 0.001300, "specific_volume_vapor": 0.0200},
    9.9:  {"specific_volume_liquid": 0.001304, "specific_volume_vapor": 0.0185},
    10.0: {"specific_volume_liquid": 0.0035,   "specific_volume_vapor": 0.0035}  # Punto crítico
}

@app.route('/phase-change-diagram', methods=['GET'])
def phase_change_diagram():
    try:
        pressure = float(request.args.get('pressure', ''))
    except ValueError:
        return jsonify({"error": "Invalid pressure value"}), 400

    if pressure not in phase_data:
        return jsonify({"error": "Pressure not found in dataset"}), 404

    return jsonify(phase_data[pressure])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
