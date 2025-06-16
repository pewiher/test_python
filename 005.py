import time
from config import APIClientConfig

api = APIClientConfig(
    base_url='https://makers-challenge.altscore.ai/v1',
    api_key='b63fd137f2ac4053b7b378c3d26d87a8'
)

# Inicia la batalla
def start_battle():
    response = api.post("/s1/e5/actions/start")
    print("Inicio:", response.json())
    return response

# Leer radar con acción correcta
def read_radar():
    data = {
        "action": "radar",
        "attack_position": {
            "x": "a",
            "y": 1
        }
    }
    response = api.post("/s1/e5/actions/perform-turn", data=data)
    return response.json()


# Atacar en coordenadas x,y
def attack(x, y):
    data = {
        "action": "attack",
        "attack_position": {
            "x": x,
            "y": y
        }
    }
    response = api.post("/s1/e5/actions/perform-turn", data=data)
    return response.json()

# Parsear radar recibido en formato de texto plano con '|'
def parse_radar(raw_text):
    lines = raw_text.split('|')[:-1]  # Eliminar último vacío
    grid = []
    for row in lines:
        grid_row = []
        for i in range(0, len(row), 3):
            cell = row[i:i+3]
            grid_row.append(cell)
        grid.append(grid_row)
    return grid

# Buscar coordenadas del objetivo en la grilla (retorna (x,y))
def find_coordinates(grid, target='^'):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if target in val:
                return (x, y)
    return None

# Convertir coordenadas numéricas (0-7) a estilo ajedrez 'a1'..'h8'
def to_chess_coords(x, y):
    col = chr(ord('a') + x)
    row = str(y + 1)
    return col + row

if __name__ == "__main__":
    start_battle()

    positions = []
    for turn in range(3):
        radar_data = read_radar()
        print("radar_data", radar_data)
        grid = parse_radar(radar_data['action_result'])
        pos = find_coordinates(grid, '^')
        if pos:
            positions.append(pos)
            print(f"Turno {turn+1}: Nave enemiga en {to_chess_coords(*pos)}")
        else:
            print("Nave enemiga no detectada en radar.")
        time.sleep(1)

    # Predicción simple de movimiento lineal para el siguiente turno
    if len(positions) >= 2:
        dx = positions[-1][0] - positions[-2][0]
        dy = positions[-1][1] - positions[-2][1]
        pred_x = positions[-1][0] + dx
        pred_y = positions[-1][1] + dy

        # Limitar dentro de la cuadrícula 0-7
        pred_x = max(0, min(7, pred_x))
        pred_y = max(0, min(7, pred_y))

        pred_coord = to_chess_coords(pred_x, pred_y)
        print(f"Predicción: ({pred_x},{pred_y}) => {pred_coord}")

        # Atacar en la posición predicha
        result = attack(pred_coord[0], int(pred_coord[1]))
        print("Resultado del ataque:", result)
    else:
        print("No hay suficientes datos para predecir movimiento.")
