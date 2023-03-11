from cryptography.fernet import Fernet
import os


def generar_clave():
    """
    Genera una clave aleatoria y la guarda en el archivo "clave.key".
    """
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_archivo:
        clave_archivo.write(clave)


def cargar_clave():
    """
    Carga la clave guardada en el archivo "clave.key".
    """
    with open("clave.key", "rb") as clave_archivo:
        clave = clave_archivo.read()
    return clave


def cifrar_mensaje(mensaje):
    """
    Cifra el mensaje usando la clave cargada desde el archivo "clave.key" y lo guarda en el archivo "mensaje_cifrado.txt".
    """
    clave = cargar_clave()
    f = Fernet(clave)
    mensaje_cifrado = f.encrypt(mensaje.encode())
    with open("mensaje_cifrado.txt", "wb") as archivo_cifrado:
        archivo_cifrado.write(mensaje_cifrado)
    print("Mensaje cifrado guardado en archivo 'mensaje_cifrado.txt'.")
    print("Mensaje cifrado:")
    print(mensaje_cifrado)


def descifrar_mensaje():
    """
    Descifra el mensaje guardado en el archivo "mensaje_cifrado.txt" usando la clave cargada desde el archivo "clave.key".
    """
    clave = cargar_clave()
    f = Fernet(clave)
    with open("mensaje_cifrado.txt", "rb") as archivo_cifrado:
        mensaje_cifrado = archivo_cifrado.read()
    mensaje_descifrado = f.decrypt(mensaje_cifrado).decode()
    print("Mensaje descifrado:")
    print(mensaje_descifrado)


# Verificamos si existe el archivo "clave.key"
if not os.path.isfile("clave.key"):
    generar_clave()

# Pedimos al usuario que escriba el mensaje a cifrar
mensaje = input("Escriba su mensaje: ")

# Ciframos el mensaje
cifrar_mensaje(mensaje)

# Desciframos el mensaje cifrado y lo mostramos por pantalla
descifrar_mensaje()
