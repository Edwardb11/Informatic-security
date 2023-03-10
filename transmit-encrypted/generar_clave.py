from cryptography.fernet import Fernet

# Generar una clave de 32 bytes
clave = Fernet.generate_key()

# Escribir la clave en un archivo
with open("clave.txt", "wb") as archivo_clave:
    archivo_clave.write(clave)
