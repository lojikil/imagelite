import unittest

from ImageLite import ImageLite


class Jpeg(unittest.TestCase):
    def setUp(self):
        # http://upload.wikimedia.org/wikipedia/commons/9/99/Jak052004.jpg
        with open("fixtures/Jak052004.jpg", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/jpeg", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(563, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(539, img.height)


class JpegWithExif(unittest.TestCase):
    # http://commons.wikimedia.org/wiki/File:Hietaniemen_hautausmaa_ilmasta.jpg
    def setUp(self):
        with open("fixtures/Hietaniemen_hautausmaa_ilmasta.jpg", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/jpeg", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(800, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(329, img.height)


class Png(unittest.TestCase):
    # http://commons.wikimedia.org/wiki/File:8x8-Y-Board.png
    def setUp(self):
        with open("fixtures/8x8-Y-Board.png", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/png", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(300, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(270, img.height)


class Gif89a(unittest.TestCase):
    # http://commons.wikimedia.org/wiki/File:Check64x48bwrg16pal_25fps_noaudio.avi.026v10_ogv.gif
    def setUp(self):
        with open("fixtures/Check64x48bwrg16pal_25fps_noaudio.avi.026v10_ogv.gif", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/gif", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(64, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(48, img.height)


class Gif87a(unittest.TestCase):
    # http://commons.wikimedia.org/wiki/File:Earth.gif
    def setUp(self):
        with open("fixtures/Earth.gif", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/gif", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(192, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(190, img.height)


class Bitmap(unittest.TestCase):
    # I made this bitmap with GNU Paint.
    def setUp(self):
        with open("fixtures/jerry.bmp", "rb") as f:
            self.d = f.read()

    def test_can_identify(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual("image/x-ms-bitmap", img.image_type)

    def test_finds_width(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(640, img.width)

    def test_finds_height(self):
        img = ImageLite()
        img.load(self.d)
        self.assertEqual(480, img.height)


if __name__ == "__main__":
    unittest.main()
