import os
import unittest
import uuid

import sys
sys.path.append('../')

from src.images import showImageFromURL
from src.images import downloadImageFromUrl
from src.images import grayScaleImage

class TestImages(unittest.TestCase):

    def test_showImageFromURL(self):
        test_url = "https://logowik.com/content/uploads/images/python.jpg"
        status = showImageFromURL(test_url)
        self.assertTrue(status)

    def test_downloadImageFromUrl(self):
        test_url = "https://logowik.com/content/uploads/images/python.jpg"
        path = "resources"
        full_path = downloadImageFromUrl(test_url, path)
        self.assertTrue(os.path.exists(full_path))
        os.remove(full_path)
    
    def test_grayScaleImage(self):
        path = f"resources/test_gray_scale.png"
        status = grayScaleImage(path)
        self.assertTrue(status)

unittest.main()