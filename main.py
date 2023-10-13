from src.images import showImageFromURL
from src.images import downloadImageFromUrl
from src.images import grayScaleImage

from src.mymail import sendQuickMail
from src.mymail import sendAttachEmail

def main():
    """
    Función principal, prueba de ejecución de módulo.
    """

    showImageFromURL("https://logowik.com/content/uploads/images/python.jpg")
    downloadImageFromUrl("https://logowik.com/content/uploads/images/python.jpg", "/Users/jeanca/Desktop/test")
    grayScaleImage("/Users/jeanca/Desktop/test/image-0bf45ca6-43cb-4e4b-8a03-523d6172d4fe.png")

    sendQuickMail("Test1", "hola mundo", "jc.hdez.1294@gmail.com")
    sendAttachEmail("Test2", "hola mundo", "jc.hdez.1294@gmail.com", "/Users/jeanca/Desktop/test/image-0bf45ca6-43cb-4e4b-8a03-523d6172d4fe.png")

main()