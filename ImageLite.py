import struct
import StringIO

"""
    Dead simple image testing library; returns the mime type and x,y dimensions of the image in question.
    It is quite similar to:
    http://bfg-pages.googlecode.com/svn/trunk/pages/getimageinfo.py
    A coworker pointed this code out after I had already completed the GIF, BMP & PNG portions, but it proved useful
    since it was much better at finding JPEG dimensions than what I had written.

    The Bitmap header I used was from here:
        http://atlc.sourceforge.net/bmp.html
    The GIF information I used was from here:
        http://www.onicos.com/staff/iz/formats/gif.html
    and the PNG information I used was from Wikipedia 
        
"""

class ImageLite(object):
    def __init__(self,data=None):
        self._gif_header0 = 'GIF87a'
        self._gif_header1 = 'GIF89a'
        self._png_header  = '\x89PNG\r\n\x1a\n'
        self._jpeg_header = 'jfif'
        self._exif_header = 'exif'
        self.width = 0
        self.height = 0
        self.image_type = ""
        if data != None:
            self.load(data)
    def load(self,data):
        if data[:6] == self._gif_header0 or data[:6] == self._gif_header1:
            self.image_type = "image/gif"
            self.width,self.height = struct.unpack("<HH",data[6:10])
        elif data[:8] == self._png_header:
            self.image_type = "image/png"
            offset = data.find("IHDR") + 4
            self.width,self.height = struct.unpack(">LL",data[offset:offset+8])
        elif data[:2] == "BM":
            self.image_type = "image/x-ms-bitmap"
            self.width,self.height = struct.unpack("<ii",data[0x12:0x1a])
        elif data[0] == '\xFF' and (data[6:10].lower() == self._jpeg_header or data[6:10].lower() == self._exif_header):
            self.image_type = "image/jpeg"
            """ 
                The code below is from 
                http://bfg-pages.googlecode.com/svn/trunk/pages/getimageinfo.py
                Originally I had something else, but this worked *much* better, and is New BSD licensed, so I
                borrowed that. 
            """
            jpeg = StringIO.StringIO(data)
            jpeg.read(2)
            b = jpeg.read(1)
            try:
                while (b and ord(b) != 0xDA):
                    while (ord(b) != 0xFF): b = jpeg.read(1)
                    while (ord(b) == 0xFF): b = jpeg.read(1)
                    if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                        jpeg.read(3)
                        h, w = struct.unpack(">HH", jpeg.read(4))
                        break
                    else:
                        jpeg.read(int(struct.unpack(">H", jpeg.read(2))[0])-2)
                    b = jpeg.read(1)
                self.width = int(w)
                self.height = int(h)
            except struct.error:
                pass
            except ValueError:
                pass

    def __str__(self):
        if self.image_type != "":
            return "{0} width: {1}, height: {2}".format(self.image_type,self.width,self.height)
        return "ImageLite"
