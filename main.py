from src.images import showImageFromURL, downloadImageFromUrl, grayScaleImage

from src.mymail import sendQuickMail, sendAttachEmail

def main():
    """
    Función principal, prueba de ejecución de módulo.
    Para importar las funciones en su proyecto, quitar el src en los imports.
    Ejemplos de uso:
    """
    
    img_status = showImageFromURL("https://logowik.com/content/uploads/images/python.jpg")
    if not img_status:
        print("No se pudo descargar la imagen.")

    path = downloadImageFromUrl("https://logowik.com/content/uploads/images/python.jpg", "/Users/jeanca/Desktop/test")
    print(f"Imagen guardada en la ruta: {path}")
    
    img_gray_status = grayScaleImage("/Users/jeanca/Desktop/test/image-0bf45ca6-43cb-4e4b-8a03-523d6172d4fe.png")
    if not img_gray_status:
        print("No se pudo descargar la imagen.")

    quick_mail_status = sendQuickMail("Test1", "hola mundo", "jc.hdez.1294@gmail.com")
    if quick_mail_status:
        print("Correo enviado exitosamente.")

    attach_mail_status = sendAttachEmail("Test2", "hola mundo", "jc.hdez.1294@gmail.com", "/Users/jeanca/Desktop/test/image-0bf45ca6-43cb-4e4b-8a03-523d6172d4fe.png")
    if attach_mail_status:
        print("Correo con adjunto enviado exitosamente.")
main()