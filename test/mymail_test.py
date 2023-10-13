import unittest

import sys
sys.path.append('../')

from src.mymail import sendQuickMail
from src.mymail import sendAttachEmail

class TestMyMail(unittest.TestCase):

    def test_sendQuickMail(self):
        subject = "Prueba"
        message = "Esto es una prueba unitaria de código de envío de email."
        destination = "jc.hdez.1294@gmail.com"
        status = sendQuickMail(subject, message, destination)
        self.assertTrue(status)

    def test_sendAttachEmail(self):
        subject = "Prueba adjunto"
        message = "Esto es una prueba unitaria de código de envío de email con adjunto."
        destination = "jc.hdez.1294@gmail.com"
        attach = "resources/test_gray_scale.png"
        status = sendAttachEmail(subject, message, destination, attach)
        self.assertTrue(status)

unittest.main()