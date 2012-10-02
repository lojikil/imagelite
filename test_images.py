import unittest

from ImageLite import ImageLite


class Jpeg(unittest.TestCase):
    def setUp(self):
        with open("./image_mini.jpg", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/jpeg", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(200, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(150, img.height)


class JpegWithExif(unittest.TestCase):
    def setUp(self):
        with open("./s_exif.jpg", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/jpeg", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(500, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(278, img.height)


class Png(unittest.TestCase):
    def setUp(self):
        with open("./tux.png", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/png", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(400, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(479, img.height)


class Gif89a(unittest.TestCase):
    def setUp(self):
        with open("./bitmap-lady.gif", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/gif", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(418, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(260, img.height)


class Gif87a(unittest.TestCase):
    def setUp(self):
        with open("./tycho2.gif", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/gif", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(263, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(353, img.height)


class Bitmap(unittest.TestCase):
    def setUp(self):
        with open("./duck.bmp", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/x-ms-bitmap", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(500, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(546, img.height)


if __name__ == "__main__":
    unittest.main()
