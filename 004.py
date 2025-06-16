# La Búsqueda de la Forja Élfica Olvidada
# Año 3018 de la Tercera Edad

# La Tierra Media está al borde de la guerra. Las fuerzas de Sauron reúnen fuerza, y el Anillo Único ha sido encontrado. Sin embargo, en lo más profundo de las historias olvidadas de los Elfos, hay un secreto que podría inclinar la balanza del poder: una forja oculta, utilizada una vez para fabricar armas capaces de resistir el poder del Señor Oscuro.

# Los antiguos escritos hablan de un acertijo, uno que solo un verdadero maestro de las letras puede resolver, revelando la entrada a la forja. Tu misión es descifrar las pistas y descubrir las credenciales ocultas que te permitirán pasar por la puerta élfica y entrar en la forja.

# Al llegar a la entrada del templo, encuentras una puerta de piedra tallada con runas élficas. En el centro de la puerta, un poema está grabado en una lengua antigua, y debajo de él, un campo en el que puedes ingresar un usuario y una contraseña.

# El poema, escrito en un idioma perdido, reza así:

# The Keeper of Secrets, Elven Lore,
# Guards the door to ancient war.
# A name in whispers, subtly veiled,
# The key to forge the fading light.

# A password cloaked in shadows deep,
# Where truth and trust in darkness sleep.
# Reveal the word, but tread with care,
# For only those who dare to stare.

# Through webs of spells and runes that guard,
# The path to wisdom, worn and hard.
# The quest is yours, the way is paved,
# By username in light engraved.

# Password bound by hidden might,
# Shift the veil, and find the light.

# Debajo de la puerta, encuentras un campo para ingresar un usuario y una contraseña.

# Usuario: ???Not all those who wander

# Contraseña: 
# ••••••••

# Recursos:

# Envía tu respuesta aquí: [POST] /v1/s1/e4/solution
# ¡No olvides consultar la Documentación!


from config import APIClientConfig
from config import APIClientConfig

api = APIClientConfig(
    base_url='https://makers-challenge.altscore.ai/v1',
    api_key='b63fd137f2ac4053b7b378c3d26d87a8'
)
# Datos para la petición
payload = {
  "username": "Not all those who wander",
  "password": "are lost"
}




response = api.post("s1/e4/solution", data=payload)

if response.ok:
    print("Respuesta exitosa:")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
