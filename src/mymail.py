import os
import smtplib
import threading
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendQuickMail(subject:str, message:str, destination:str):
    """
    Envía un correo electrónico rápido al destino indicado.
    La función debe preguntar cual es el correo electrónico con el que se enviará.
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com

    Argumentos:
    ^^^^^^^^^^^
    :subject(str): asunto del correo.
    :message(str): cuerpo del correo.
    :destination(str): email de destinatario.

    Retorno:
    :_(boolean): resultado de la operación, True si fue satisfactorio.

    Uso:
    ^^^^

    .. code-block:: python

        sendQuickMail(subject, message, destination)
    """

    mail_message = EmailMessage()
    mail_message['Subject'] = subject
    mail_message["From"] = "pythonemail820@gmail.com"
    mail_message["To"] = destination
    mail_message.set_content(message)

    return _createMailThread(mail_message)

def sendAttachEmail(subject:str, message:str, destination:str, path:str):
    """
    Envía un correo electrónico con un archivo adjunto a la dirección indicada
    La función debe preguntar cual es el correo electrónico con el que se enviará.
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com

    Argumentos:
    ^^^^^^^^^^^
    :subject(str): asunto del correo.
    :message(str): cuerpo del correo.
    :destination(str): email de destinatario.
    :path(str): dirección del adjunto.

    Retorno:
    :_(boolean): resultado de la operación, True si fue satisfactorio.

    Uso:
    ^^^^

    .. code-block:: python

        sendAttachEmail(subject, message, destination, path)
    """

    mail_message = MIMEMultipart("alternative")
    mail_message['Subject'] = subject
    mail_message["From"] = "pythonemail820@gmail.com"
    mail_message["To"] = destination
    mail_message.attach(MIMEText(message, 'plain'))

    try:
        with open(path, 'rb') as attach:
            attach_MIME = MIMEBase('application', 'octet-stream')
            attach_MIME.set_payload((attach).read())
            encoders.encode_base64(attach_MIME)
            attach_MIME.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(path))
            mail_message.attach(attach_MIME)
        return _createMailThread(mail_message)
    except:
        return False


def _createMailThread(body):
    """
    Función que crea un hilo de ejecución para envío de correo electrónico.
    """
    try:
        thread = threading.Thread(target=_sendEmailAction, args=(body, ) )
        thread.start()
        thread.join()
        return True
    except:
        return False


def _sendEmailAction(body):
    """
    Función que de envío de correo electrónico.
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("pythonemail820@gmail.com", "olemizgkruracwel")
    server.send_message(body)
    server.quit()