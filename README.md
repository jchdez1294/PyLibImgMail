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

<img width="609" alt="Screenshot 2023-10-12 at 21 05 22" src="https://github.com/jchdez1294/PyLibImgMail/assets/55639913/198f6ee3-3a36-4dfb-9114-f73ff51fe6bd">

#### 2- Descarga una imagen y la guarda en la ruta indicada.

Lo que hace éste método es que descarga una imagen en la ruta especificada por el usuario.

Uso:

```
downloadImageFromUrl("https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png", "/Users/{user}/Desktop/test")
```

Resultado:

<img width="609" alt="Screenshot 2023-10-12 at 21 08 08" src="https://github.com/jchdez1294/PyLibImgMail/assets/55639913/79fa72e8-4c74-477d-af7a-f48c4daa327c">

#### 3- Convierte una imagen a blanco y negro.

Este método tranforma una imagen a escala de grises, se necesita la ruta de la imagen.

Uso:

```
grayScaleImage("/Users/{username}/Desktop/test/image-a13faa52-bae6-419c-92b6-9a59c20d9138.png")
```
 
Resultado:

<img width="609" alt="Screenshot 2023-10-12 at 21 11 33" src="https://github.com/jchdez1294/PyLibImgMail/assets/55639913/075d3746-1612-4a4a-9581-b69416655a35">

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

Nota: las rutas de archivos en documentación son tomadas de sistemas Mac, solamente reemplazar o usar las del sistema deseado en las funciones.