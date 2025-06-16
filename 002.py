# ¡El Enigma Cósmico de Kepler-452b! 🌌
# Año 3042: Eres un intrépido navegante a bordo del CSS Hawking, embarcado en una misión de vital importancia: contactar al legendario Oráculo de Kepler-452b. Se rumorea que este ser enigmático posee el conocimiento para guiar a la humanidad hacia una era dorada. Pero el Oráculo no se revela a cualquiera; solo aquellos que demuestren su ingenio resolviendo un acertijo cósmico serán dignos de su sabiduría.

# La Prueba: El Oráculo te presenta una interfaz holográfica que muestra una nebulosa estelar ondulante llamada " Lyra". La interfaz te permite acceder a los datos de las estrellas en la nebulosa. Para cada estrella, obtienes su " resonancia" y sus coordenadas. El Oráculo te desafía a calcular la "resonancia promedio" de las estrellas en la nebulosa.

# Pistas:

# La interfaz te permite navegar por la nebulosa en "saltos estelares", mostrando datos de 3 estrellas por salto.
# Un mensaje críptico aparece en la pantalla: "El cosmos vibra en una sinfonía matemática. La resonancia de cada estrella se construye sobre la anterior, pero el Oráculo te presenta las estrellas en un orden cósmico propio.".
# "Los secretos del cosmos no solo están en los datos visibles, sino también en los susurros ocultos en los encabezados de las respuestas."
# "La paciencia es una virtud, pero la documentación es una herramienta. ¡Úsala sabiamente y el Oráculo te recompensará!"
# Recursos:

# Puedes usar esta API para obtener los datos de las estrellas: [GET] /v1/s1/e2/resources/stars
# Envía tu respuesta aquí: [POST] /v1/s1/e2/solution
# ¡No olvides consultar la Documentación!
# ¿Estás listo para desentrañar la Armonía Oculta y obtener la sabiduría del Oráculo? ¡Que la fuerza cósmica te acompañe! 🚀

# Back to challenges

from config import APIClientConfig
import json
import math

api = APIClientConfig(
    base_url='https://makers-challenge.altscore.ai/v1',
    api_key='b63fd137f2ac4053b7b378c3d26d87a8'
)

def get_total_stars():
    response = api.get("/s1/e2/resources/stars", params={"page": 1})
    total = int(response.headers.get("x-total-count", 0))
    return total

def fetch_stars(page):
    response = api.get("/s1/e2/resources/stars", params={"page": page})
    response.raise_for_status()
    return response.json()

def main():
    print("🌌 Conectando con el Oráculo de Kepler-452b...")
    total = get_total_stars()
    print(f"🔭 Total de estrellas detectadas: {total}")

    stars = []
    pages = math.ceil(total / 3)

    for page in range(1, pages + 1):
        group = fetch_stars(page)
        stars.extend(group)
    
    stars.sort(key=lambda s: s["position"]["x"])

    total_resonance = sum(star["resonance"] for star in stars)
    average_resonance = round(total_resonance / len(stars))
    print("🎼 Resonancia promedio:", average_resonance)
    
    payload = {"average_resonance": average_resonance}
    headers = {"Content-Type": "application/json"}
    response = api.post("/s1/e2/solution", data=payload)

    try:
        print("🚀 Respuesta del Oráculo:", response.json())
    except Exception:
        print("🛑 Respuesta no válida:", response.text)

if __name__ == "__main__":
    main()
