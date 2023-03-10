from cryptography.fernet import Fernet

# Leer la clave del archivo
with open("clave.txt", "rb") as archivo_clave:
    clave = archivo_clave.read()

# Crear un objeto Fernet con la clave
fernet = Fernet(clave)

# Leer el mensaje encriptado
with open("mensaje_encriptado.txt", "rb") as archivo_encriptado:
    mensaje_encriptado = archivo_encriptado.read()

# Desencriptar el mensaje
mensaje_desencriptado = fernet.decrypt(mensaje_encriptado)

# Escribir el mensaje desencriptado en un archivo
with open("mensaje_desencriptado.txt", "wb") as archivo_desencriptado:
    archivo_desencriptado.write(mensaje_desencriptado)
