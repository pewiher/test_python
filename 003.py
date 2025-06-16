# La Búsqueda del Templo Sith Perdido
# Año Galáctico 34 DBY

# La Resistencia ha interceptado un fragmento de un antiguo holocrón Sith que contiene la clave para localizar un templo Sith perdido, el cual se rumorea que guarda secretos poderosos.

# Sin embargo, el fragmento está codificado con un complejo acertijo que solo un verdadero maestro de la Fuerza y los datos puede descifrar.

# El futuro de la galaxia depende de tu habilidad para descifrar el mensaje y encontrar el templo antes que la Primera Orden.

# El Desafío
# El fragmento del holocrón, el cual se encuentra fuera de nuestra galaxia, contiene datos sobre varios lugares y personajes clave. Tu misión es analizar la forma de realizar la conexión con el holocrón y encontrar el único planeta con equilibrio en la Fuerza.

# Investigando la librería del templo Jedi en Coruscant, un antiguo pasaje menciona:

# ...el "Índice de Balance de la Fuerza" (IBF) para un planeta específico, es una medida de la
# influencia del Lado Luminoso y del Lado Oscuro de la Fuerza en ese planeta se calcula como:

# IBF = ((Número de Personajes del Lado Luminoso) - (Número de Personajes del Lado Oscuro)) /
#        (Total de Personajes en el Planeta)

# El IBF te dará un valor entre -1 y 1, donde -1 significa dominio total del Lado Oscuro, 0 significa equilibrio, y
# 1 significa dominio total del Lado Luminoso.
# Pasos
# Pistas

# Utiliza el fragmento de holocrón para recopilar datos sobre personajes y planetas de Star Wars.
# El fragmento del holocrón no contiene información sobre el lado de la fuerza al que pertenecen los personajes, por suerte podemos consultarle a un antiguo oráculo Jedi quien buscará en su rolodex, pero sus respuestas se encuentran extrañamente codificadas...
# Recursos:

# Accede a los datos de personas y planetas en SWAPI
# Accede al rolodex del oráculo aquí: [GET] /v1/s1/e3/resources/oracle-rolodex
# Envía tu respuesta aquí: [POST] /v1/s1/e3/solution
# ¡No olvides consultar la Documentación!
# ¿Estás listo para salvar la galaxia y desbloquear los secretos del templo Sith perdido? ¡Que la Fuerza te acompañe! ✨

# Back to challenges

import base64
import time
from config import APIClientConfig

api = APIClientConfig(
    base_url='https://makers-challenge.altscore.ai/v1',
    api_key='b63fd137f2ac4053b7b378c3d26d87a8'
)

import requests
import base64
import time

# Base URLs
SWAPI_PEOPLE_URL = 'https://swapi.py4e.com/api/people/'


# Cache para planetas
planet_cache = {}

def get_all_characters():
    characters = []
    url = SWAPI_PEOPLE_URL
    while url:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        characters.extend(data['results'])
        url = data['next']
    return characters

def get_planet_name(url):
    if url in planet_cache:
        return planet_cache[url]
    res = requests.get(url)
    res.raise_for_status()
    name = res.json()['name']
    planet_cache[url] = name
    return name

def query_oracle(name):
    try:
        res = api.get("s1/e3/resources/oracle-rolodex", params={'name': name})
        res.raise_for_status()
        data = res.json()
        encoded = data.get('oracle_notes', '')
        decoded = base64.b64decode(encoded).decode('utf-8').lower()
        if 'light side' in decoded:
            return 'light'
        elif 'dark side' in decoded:
            return 'dark'
        else:
            return 'unknown'
    except:
        return 'unknown'

def calculate_ibf_by_planet(mapped_characters):
    planet_data = {}
    for char in mapped_characters:
        planet = get_planet_name(char['planet_url'])
        if planet not in planet_data:
            planet_data[planet] = {'light': 0, 'dark': 0, 'total': 0}
        planet_data[planet][char['side']] += 1
        planet_data[planet]['total'] += 1
    
    ibf_results = []
    for planet, counts in planet_data.items():
        ibf = (counts['light'] - counts['dark']) / counts['total']
        ibf_results.append({'planet': planet, 'ibf': ibf})
    return ibf_results

def find_balanced_planet(ibf_results):
    ibf_results.sort(key=lambda x: abs(x['ibf']))
    return ibf_results[0] if ibf_results else None

def main():
    print("Obteniendo personajes de SWAPI...")
    characters = get_all_characters()
    
    print("Consultando oráculo para determinar lado de la Fuerza...")
    mapped = []
    for char in characters:
        side = query_oracle(char['name'])
        if side == 'unknown':
            continue
        mapped.append({'name': char['name'], 'planet_url': char['homeworld'], 'side': side})
        time.sleep(0.1)  # evita saturar API
    
    print("Calculando IBF por planeta...")
    ibf_results = calculate_ibf_by_planet(mapped)
    
    balanced = find_balanced_planet(ibf_results)
    if balanced:
        print(f"Planeta con equilibrio: {balanced['planet']}, IBF: {balanced['ibf']}")
    else:
        print("No se encontró planeta equilibrado.")
        return

    # Preparar payload para enviar solución
    payload = {'planet': balanced['planet'], 'ibf': balanced['ibf']}
    print("Enviando solución...")
    res = api.post("s1/e3/solution", data=payload)
    print(f"Respuesta del servidor: {res.status_code} - {res.text}")

if __name__ == '__main__':
    main()
