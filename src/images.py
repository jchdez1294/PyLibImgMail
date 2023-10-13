import os
import uuid
import requests
from PIL import Image, ImageOps

def showImageFromURL(url:str):
    """
    Descarga una imagen desde una URL y la muestra.

    Argumentos:
    ^^^^^^^^^^^
    :url(str): dirección de descarga de imagen.

    Retorno: 
    :_(boolean): resultado de la operación, True si fue satisfactorio.

    Uso:
    ^^^^

    .. code-block:: python

        showImageFromURL(url)
    """

    try:
        with Image.open(requests.get(url, stream = True).raw) as image:
            image.show()
        return True
    except:
        return False

def downloadImageFromUrl(url:str, path:str):
    """
    Descarga una imagen y la guarda en la ruta indicada.

    Argumentos:
    ^^^^^^^^^^^
    :url(str): dirección de descarga de imagen.
    :path(str): ruta local en la que se va a guardar la imagen.

    Retorno:
    :full_path(str): ruta de guardado, en caso de error retorna un mensaje.

    Uso:
    ^^^^

    .. code-block:: python

        downloadImageFromUrl(url, path)
    """

    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except:
       return "No se pudo crear la carpeta."

    try:
        full_path = f"{path}/image-{str(uuid.uuid4())}.png" 
        with Image.open(requests.get(url, stream = True).raw) as image:
            image.save(full_path)
        return full_path
    except:
        return "No se pudo guardar la imagen."

def grayScaleImage(path:str):
    """
    Convierte una imagen a blanco y negro.

    Argumentos:
    ^^^^^^^^^^^   
    :path(str): ruta local donde está la imagen que se va a transformar a escala de grises.

    Retorno:
    :_(boolean): resultado de la operación, True si fue satisfactorio.

    Uso:
    ^^^^

    .. code-block:: python

        grayScaleImage(path)
    """

    try:
        with Image.open(path) as image:
            gray_image = ImageOps.grayscale(image) 
            gray_image.show()
        return True
    except:
        return False