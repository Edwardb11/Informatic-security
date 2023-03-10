## DOCUMENTACIÓN

### Generar Clave:

Este código genera una clave para utilizar en el proceso de encriptación y desencriptación de mensajes. La clave es una secuencia aleatoria de 32 bytes.

Para ejecutar este código, es necesario importar la biblioteca Fernet de Cryptography. Para ello, se puede utilizar el siguiente comando en la terminal:

```py
from cryptography.fernet import Fernet

```

Después, se debe ejecutar el siguiente fragmento de código para generar una clave:

```py
clave = Fernet.generate_key()

with open("clave.txt", "wb") as archivo_clave:
    archivo_clave.write(clave)

```

Este fragmento de código generará una clave y la escribirá en un archivo llamado "`clave.txt`" en el directorio actual.

### Encriptar:

Este código toma un mensaje de texto y lo encripta utilizando la clave generada previamente. El mensaje encriptado se escribe en un archivo llamado "`mensaje_encriptado.txt`".

Para ejecutar este código, es necesario importar la biblioteca Fernet de Cryptography. Para ello, se puede utilizar el siguiente comando en la terminal:

```py
from cryptography.fernet import Fernet
```

Después, se debe ejecutar el siguiente fragmento de código para leer la clave desde el archivo "`clave.txt`" y encriptar el mensaje:

```py
with open("clave.txt", "rb") as archivo_clave:
    clave = archivo_clave.read()

fernet = Fernet(clave)

with open("mensaje.txt", "rb") as archivo_mensaje:
    mensaje = archivo_mensaje.read()

mensaje_encriptado = fernet.encrypt(mensaje)

with open("mensaje_encriptado.txt", "wb") as archivo_encriptado:
    archivo_encriptado.write(mensaje_encriptado)

```

Este fragmento de código leerá la clave desde el archivo "`clave.txt`" en el directorio actual, leerá el mensaje desde el archivo "`mensaje.txt`" en el mismo directorio, encriptará el mensaje y escribirá el mensaje encriptado en un archivo llamado "`mensaje_encriptado.txt`" en el mismo directorio.

### Transmitir:

Este código muestra cómo copiar un archivo encriptado de una máquina a otra a través de la red utilizando el comando "`scp`" de Unix.

Para ejecutar este código, primero se debe copiar el archivo encriptado "`mensaje_encriptado.txt`" al directorio local de la otra máquina utilizando el siguiente comando en la terminal:

```bash

scp /ruta/de/archivo/encriptado usuario@dirección.IP.remota:/ruta/de/destino


```

Donde "`/ruta/de/archivo/encriptado`" es la ruta del archivo encriptado en la máquina local, "usuario" es el nombre de usuario en la máquina remota, "`dirección.IP.remota`" es la dirección IP de la máquina remota y "`/ruta/de/destino`" es la ruta de destino en la máquina remota.

Una vez que el archivo encriptado ha sido copiado a la otra máquina, se puede desencriptar utilizando el código proporcionado en la sección anterior.

En este caso simplemente lo copie de un desktop a documents

### Desencriptar:

Este código toma un mensaje encriptado y lo desencripta utilizando la clave generada previamente. El mensaje desencriptado se escribe en un archivo llamado "`mensaje_desencriptado.txt`".

Para ejecutar este código, es necesario importar la biblioteca Fernet de Cryptography. Para ello, se puede utilizar el siguiente comando en la terminal:

```py
from cryptography.fernet import Fernet

```

Después, se debe ejecutar el siguiente fragmento de código para leer la clave desde el archivo "`clave.txt`" y desencriptar el mensaje encriptado:

```py
with open("clave.txt", "rb") as archivo_clave:
    clave = archivo_clave.read()

fernet = Fernet(clave)

with open("mensaje_encriptado.txt", "rb") as archivo_encriptado:
    mensaje_encriptado = archivo_encriptado.read()

mensaje_desencriptado = fernet.decrypt(mensaje_encriptado)

with open("mensaje_desencriptado.txt", "wb") as archivo_desencriptado:
    archivo_desencriptado.write(mensaje_desencriptado)

```
