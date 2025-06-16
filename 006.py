import requests
from config import APIClientConfig

BASE_URL = "https://pokeapi.co/api/v2"

api = APIClientConfig(
    base_url='https://makers-challenge.altscore.ai/v1',
    api_key='b63fd137f2ac4053b7b378c3d26d87a8'
)

TIPOS_VALIDOS = [
    "bug", "dark", "dragon", "electric", "fairy", "fighting",
    "fire", "flying", "ghost", "grass", "ground", "ice",
    "normal", "poison", "psychic", "rock", "steel", "water"
]

def obtener_tipos():
    r = requests.get(f"{BASE_URL}/type")
    tipos = r.json()['results']
    return sorted(tipos, key=lambda t: t['name'])

def obtener_pokemons_por_tipo(url_tipo):
    r = requests.get(url_tipo)
    pokemons = r.json()['pokemon']
    return [p['pokemon']['name'] for p in pokemons]

def obtener_altura_pokemon(nombre):
    r = requests.get(f"{BASE_URL}/pokemon/{nombre}")
    return r.json()['height'] / 10  # decímetros a metros

def calcular_altura_promedio():
    tipos = obtener_tipos()
    resultado = {}
    for tipo in tipos:
        if tipo['name'] not in TIPOS_VALIDOS:
            continue  # Ignorar tipos no oficiales
        pokemons = obtener_pokemons_por_tipo(tipo['url'])
        alturas = [obtener_altura_pokemon(p) for p in pokemons]
        promedio = round(sum(alturas) / len(alturas), 3) if alturas else 0
        print(f"Tipo: {tipo['name']} - Promedio altura: {promedio}")
        resultado[tipo['name']] = promedio
    return resultado

def preparar_payload(alturas):
    return {tipo: round(alturas.get(tipo, 0), 3) for tipo in TIPOS_VALIDOS}

def enviar_solucion(alturas):
    payload = {"heights": preparar_payload(alturas)}
    response = api.post("/s1/e6/solution", data=payload)
    print("Status:", response.status_code)
    print("Respuesta:", response.text)

if __name__ == "__main__":
    alturas_promedio = calcular_altura_promedio()
    print("Altura promedio por tipo:", alturas_promedio)
    enviar_solucion(alturas_promedio)
