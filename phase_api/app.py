from flask import Flask, request, jsonify

app = Flask(__name__)

# Tabla ficticia con 10 puntos
DATA = {
    10: {"specific_volume_liquid": 0.0035, "specific_volume_vapor": 0.0035},
    9: {"specific_volume_liquid": 0.0040, "specific_volume_vapor": 0.01},
    8: {"specific_volume_liquid": 0.0050, "specific_volume_vapor": 0.1},
    7: {"specific_volume_liquid": 0.0060, "specific_volume_vapor": 0.5},
    6: {"specific_volume_liquid": 0.0070, "specific_volume_vapor": 1.0},
    5: {"specific_volume_liquid": 0.0080, "specific_volume_vapor": 2.0},
    4: {"specific_volume_liquid": 0.0090, "specific_volume_vapor": 4.0},
    3: {"specific_volume_liquid": 0.0100, "specific_volume_vapor": 8.0},
    2: {"specific_volume_liquid": 0.0110, "specific_volume_vapor": 16.0},
    1: {"specific_volume_liquid": 0.0120, "specific_volume_vapor": 30.0},
}

@app.route("/phase-change-diagram")
def phase_change():
    try:
        pressure = float(request.args.get("pressure"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid pressure"}), 400

    data = DATA.get(int(pressure))
    if not data:
        return jsonify({"error": "No data for this pressure"}), 404

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20000)