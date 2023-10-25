
# [pygame.image][1]

pygame module for image transfer.

The image module contains functions for loading and saving pictures, as well as transferring Surfaces to formats usable by other packages.

An image is loaded as a [Surface][2] object.

pygame is built to support extended formats, using the `SDL_Image` library.  

`pygame.image.load()` function can **load** the following formats.

- BMP
- GIF (non-animated)
- JPEG (the same as JPG)
- LBM (and PBM, PGM, PPM)
- PCX
- PNG
- PNM
- SVG (limited support, using Nano SVG)
- TGA (uncompressed)
- TIFF (the same as TIF)
- WEBP
- XPM

You can **save** to the following formats.

- BMP
- JPEG
- PNG
- TGA

### .load()

Load new image from a file (or file-like object).

    load(filename) -> Surface
    load(fileobj, namehint="") -> Surface

You can pass either a `filename`, a `Python file-like object`, or a `pathlib.Path`.

Pygame will automatically determine the image type (e.g., GIF or bitmap) and create a new Surface object from the data.  
In some cases it will need to know the file extension (e.g., GIF images should end in ".gif").  
If you pass a raw file-like object, you may also want to pass the original filename as the `namehint` argument.

The returned Surface will contain the same color format, colorkey and alpha transparency as the file it came from.  
You will often want to call `pygame.Surface.convert()` with no arguments, to create a copy that will draw more quickly on the screen.

For alpha transparency, like in .png images, use the `pygame.Surface.convert_alpha()` method after loading so that the image has per pixel transparency.

Pygame may not always be built to support all image formats. At minimum it will support uncompressed BMP.  
If `pygame.image.get_extended()` returns **True**, you should be able to load most images (including PNG, JPG and GIF).

You should use os.path.join() for compatibility.

    eg. asurf = pygame.image.load(os.path.join('data', 'bla.png'))  # 'data\\bla.png'

### .save()

Save an image to file (or file-like object).

    save(Surface, filename) -> None
    save(Surface, fileobj, namehint="") -> None

This will save your Surface as either a `BMP`, `TGA`, `PNG`, or `JPEG` image.  
If the filename extension is unrecognized it will `default to TGA`.  
Both `TGA`, and `BMP` file formats create **uncompressed** files.  
You can pass a `filename`, a `pathlib.Path` or a `Python file-like object`.  
For file-like object, the image is saved to `TGA` format unless a namehint with a recognizable extension is passed in.

When saving to a file-like object, it seems that for most formats, the object needs to be `flushed` after saving to it to make loading from it possible.

### .get_sdl_image_version()

Get version number of the `SDL_Image` library being used.

If pygame is built with `extended image formats`, then this function will return the SDL_Image library's version number as a tuple of 3 integers `(major, minor, patch)`.  
If `not`, then it will return **None**.

### .get_extended()

Test if extended image formats can be loaded.

### .tobytes()

Transfer image to byte buffer.

    tobytes(Surface, format, flipped=False) -> bytes

Creates a string of bytes that can be transferred with the `fromstring` or `frombytes` methods in other Python imaging packages.  
Some Python image packages prefer their images in bottom-to-top format (PyOpenGL for example).  
If you pass **True** for the `flipped` argument, the byte buffer will be `vertically flipped`.

The `format` argument is a string of one of the following values.  
Note that only 8-bit Surfaces can use the "P" format.  
The other formats will work for any Surface.  
Also note that other Python image packages support more formats than pygame.

- `P`, 8-bit palettized Surfaces
- `RGB`, 24-bit image
- `RGBX`, 32-bit image with unused space
- `RGBA`, 32-bit image with an alpha channel
- `ARGB`, 32-bit image with alpha channel first
- `BGRA`, 32-bit image with alpha channel, red and blue channels swapped
- `RGBA_PREMULT`, 32-bit image with colors scaled by alpha channel
- `ARGB_PREMULT`, 32-bit image with colors scaled by alpha channel, alpha channel first

### .frombytes()

Create new Surface from a byte buffer.

    frombytes(bytes, size, format, flipped=False) -> Surface

This function takes arguments similar to `pygame.image.tobytes()`.  
The `size` argument is a pair of numbers representing the **width** and **height**.  
Once the new Surface is created it is **independent** from the memory of the bytes passed in.

The bytes and format passed must compute to the exact size of image specified. Otherwise a `ValueError` will be raised.

See the `pygame.image.frombuffer()` method for a potentially faster way to transfer images into pygame.

### .frombuffer()

Create a new Surface that shares data inside a bytes buffer.

    frombuffer(buffer, size, format) -> Surface

This buffer can be `bytes`, a `bytearray`, a `memoryview`, a `pygame.BufferProxy` or any object that supports the buffer protocol.  

This will run much faster since no pixel data must be allocated and copied.

It accepts the following `'format'` arguments:

- P, 8-bit palettized Surfaces
- RGB, 24-bit image
- BGR, 24-bit image, red and blue channels swapped.
- RGBX, 32-bit image with unused space
- RGBA, 32-bit image with an alpha channel
- ARGB, 32-bit image with alpha channel first
- BGRA, 32-bit image with alpha channel, red and blue channels swapped

### .load_basic()

Load only `BMP` image from a file (or file-like object).

    load_basic(file) -> Surface

You can pass either a `filename` or a `Python file-like object`, or a `pathlib.Path`.

### .load_extended()

Load an image from a file (or file-like object).

    load_extended(filename) -> Surface
    load_extended(fileobj, namehint="") -> Surface

This function is always available, but raises an `NotImplementedError` if extended image formats are not supported.  

### .save_extended()

Save a PNG or JPEG image to file (or file-like object).

    save_extended(Surface, filename) -> None
    save_extended(Surface, fileobj, namehint="") -> None

In case the image is being saved to a file-like object, this function uses the `namehint` argument to determine the format of the file being saved.  
Saves to **JPEG** in case the `namehint` was `not` specified while saving to a file-like object.

This function is always available, but raises an `NotImplementedError` if extended image formats are not supported.   

[1]:https://www.pygame.org/docs/ref/image.html
[2]:https://www.pygame.org/docs/ref/surface.html

< End >
