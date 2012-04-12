### ImageLite ###

 A dead simple library for detecting mime type & dimensions of an image, with 0 dependencies outside of
 Python, struct and StringIO. 

### Example Usage ###

ImageLite was written because I had a web application that needed to detect type & dimension of 
user-supplied images. To this end, it is meant to be a a drop-in replacement for using a more 
full-featured library such as PIL (which is where the name comes from; originally we were using
PIL's `Image` class to do much the same thing, but PIL is quite heavy-weight for something so simple).

    from ImageLite import ImageLite
    f = open('some_image','rb')
    data = f.read()
    img = ImageLite(data)
    print img.width, img.height, img.image_type

### To Do ###

- More image types would be nice
- Support for raw file handles, ala the JPEG work
- &c.
