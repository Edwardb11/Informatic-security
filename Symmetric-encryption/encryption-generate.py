

#GENERAR LA CLAVE
from cryptography.fernet import Fernet
print("------------------")

# Generar una clave aleatoria de 32 bytes
clave = Fernet.generate_key()

# Crear un objeto Fernet con la clave generada
fernet = Fernet(clave)

# Ejemplo de cifrado y descifrado
mensaje = b"Hola mundo"
mensaje_cifrado = fernet.encrypt(mensaje)
mensaje_descifrado = fernet.decrypt(mensaje_cifrado)

print("Clave:", clave)
print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
print("------------------")
