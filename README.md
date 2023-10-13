# PyLibImgMail

Librería que permite hacer operaciones sencillas sobre imágenes así como envío de correos.

### Funciones:

#### 1- Descargar y mostrar una imagen dada una dirección URL.

Lo que hace este método es descargar una imagen y mostrarla (no la guarda en la computadora).

Uso:

```
showImageFromURL("https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png")
```

Resultado:

<img width="858" alt="Screenshot 2023-10-13 at 08 47 04" src="https://github.com/jchdez1294/PyLibImgMail/assets/55639913/d56d0f13-40fa-45e5-8ae9-6c2a4d6e3c22">

#### 2- Descarga una imagen y la guarda en la ruta indicada.

Lo que hace éste método es que descarga una imagen en la ruta especificada por el usuario.

Uso:

```
downloadImageFromUrl("https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png", "/Users/{user}/Desktop/test")
```

Resultado:

<img width="717" alt="Screenshot 2023-10-13 at 08 48 04" src="https://github.com/jchdez1294/PyLibImgMail/assets/55639913/9de1657c-6cf7-4e42-b94e-6ca510d4c5e1">

#### 3- Convierte una imagen a blanco y negro.

Este método tranforma una imagen a escala de grises, se necesita la ruta de la imagen.

Uso:

```
grayScaleImage("/Users/{username}/Desktop/test/image-a13faa52-bae6-419c-92b6-9a59c20d9138.png")
```
 
Resultado:

<img width="858" alt="Screenshot 2023-10-13 at 08 47 22" src="https://github.com/jchdez1294/PyLibImgMail/assets/55639913/ee8a65c0-ce6d-40c8-81dd-6986c1b8a918">

#### 4- Envía un correo electrónico rápido al destino indicado.

Este método envía un correo electrónico, se requiere el asunto, mensaje y destinatario.

Uso:

```
sendQuickMail("Asunto", "Mensaje de prueba, cuerpo del correo", "destino@gmail.com")
```
#### 4- Envía un correo electrónico con adjunto al destino indicado.

Este método envía un correo electrónico, se requiere el asunto, mensaje, destinatario y ruta de adjunto.

Uso:

```
sendQuickMail("Asunto", "Mensaje de prueba, cuerpo del correo", "destino@gmail.com", "/Users/{username}/Desktop/test/image-a13faa52-bae6-419c-92b6-9a59c20d9138.png")
```

#### Como se importa?
```
from images import showImageFromURL, downloadImageFromUrl, grayScaleImage
from mymail import sendQuickMail, sendAttachEmail

```

Nota: las rutas de archivos en documentación son tomadas de sistemas Mac, solamente reemplazar o usar las del sistema deseado en las funciones.
