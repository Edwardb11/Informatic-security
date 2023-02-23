from cryptography.fernet import Fernet

print("------------------")

# 2DXk7sBa1dOwmQGoxo04DTBnyjSStzqxdSVijTQB2XI=

# Solicitamos al usuario que ingrese una clave
clave = input("Ingrese una clave de al menos 32 bytes: ").encode()

# CLave de ejemplo b3iMgyVE_b8ZpazXjvIoCk5qjKzJmv11yP5JvU6LYf0=

# Creamos una instancia de Fernet con la clave
fernet = Fernet(clave)

# Solicitamos al usuario que ingrese un mensaje
mensaje = input("Ingrese un mensaje para encriptar: ").encode()

# Encriptamos el mensaje
mensaje_encriptado = fernet.encrypt(mensaje)

# Mostramos el mensaje encriptado
print("Mensaje encriptado:", mensaje_encriptado)

# Desencriptamos el mensaje
mensaje_desencriptado = fernet.decrypt(mensaje_encriptado)

# Mostramos el mensaje desencriptado
print("Mensaje desencriptado:", mensaje_desencriptado.decode())


print("------------------")
