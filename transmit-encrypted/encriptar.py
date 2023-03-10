from cryptography.fernet import Fernet

# Leer la clave del archivo
with open("clave.txt", "rb") as archivo_clave:
    clave = archivo_clave.read()

# Crear un objeto Fernet con la clave
fernet = Fernet(clave)

# Leer el mensaje a encriptar
with open("mensaje.txt", "rb") as archivo_mensaje:
    mensaje = archivo_mensaje.read()

# Encriptar el mensaje
mensaje_encriptado = fernet.encrypt(mensaje)

# Escribir el mensaje encriptado en un archivo
with open("mensaje_encriptado.txt", "wb") as archivo_encriptado:
    archivo_encriptado.write(mensaje_encriptado)
