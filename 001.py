# ¡La Sonda Silenciosa! 🛰️
# Misión: Eres un intrépido explorador estelar en una misión crucial para mapear un sistema solar recién descubierto. Tu objetivo es determinar la velocidad orbital instantánea de un planeta potencialmente habitable para evaluar su idoneidad para la vida.

# Desafío: La extraña interferencia cósmica en esta región del espacio dificulta la obtención de lecturas exitosas de tu escáner de largo alcance.

# Datos Clave: Cuando el escáner funciona, te proporciona:

# distance: La distancia recorrida por el planeta en su órbita durante el período de observación (en unidades astronómicas).
# time: El tiempo transcurrido durante la observación (en horas).
# Objetivo: Calcular la velocidad orbital instantánea del planeta hasta el número entero más cercano.

# Recursos:

# API para obtener una lectura del escáner: [GET] /v1/s1/e1/resources/measurement (Siempre recibirás un código de estado HTTP 200, incluso si el escaneo no es exitoso).
# Envía tu respuesta aquí: [POST] /v1/s1/e1/solution
# Consulta la Documentación para más detalles https://makers-challenge.altscore.ai/docs.
# ¡Prepárate para desafiar la interferencia cósmica y desentrañar los secretos de este nuevo mundo! 🚀

# Back to challenges

import requests
import math
from config import APIClientConfig

def parse_number(value, default=1):
    print(value)
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

api = APIClientConfig(
    base_url='https://makers-challenge.altscore.ai/v1',
    api_key='b63fd137f2ac4053b7b378c3d26d87a8'
)


res = api.get("/s1/e1/resources/measurement")
data = res.json()

distance = parse_number(data.get("distance"))
time = parse_number(data.get("time"))

if not distance or not time or time == 0:
    raise Exception("Lectura inválida. Reintenta.")

speed = round(distance / time)

post_data = {"speed": speed}
r = api.post("/s1/e1/solution", data=post_data)
print(r.json())
