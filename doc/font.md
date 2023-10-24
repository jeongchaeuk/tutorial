
# [pygame.font][1]

pygame module for loading and rendering fonts

The font module allows for rendering TrueType fonts into Surface objects.  
This module is built on top of the **SDL_ttf** library, which comes with all normal pygame installations.

Pygame comes with a builtin default font, `freesansbold`. This can always be accessed by passing `None` as the font name.

### .init()

Initialize the font module.

This method is called automatically by `pygame.init()`.  
It is safe to call this function more than once.

### .quit()

Uninitialize the font module.

Manually uninitialize SDL_ttf's font system.  
This is called automatically by `pygame.quit()`.

It is safe to call this function even if font is currently not initialized.

### .get_init()

`True` if the font module is initialized.

### .get_default_font()

Get the filename of the default font.

### .get_sdl_ttf_version()

gets SDL_ttf version.

### .get_fonts()

Get all available fonts.

The names of the fonts will be set to `lowercase` with all spaces and punctuation `removed`.

### .match_font()

Find a specific font on the system.

Returns the `full path` to a font file on the system.  
If bold or italic are set to true, this will attempt to find the correct family of font.

### .SysFont()

Create a Font object from the system fonts.

# .Font

Create a new Font object from a file.

    Font(file_path=None, size=12) -> Font
    Font(file_path, size) -> Font
    Font(pathlib.Path, size) -> Font
    Font(object, size) -> Font

Load a new font from a given filename or a python file object.  
The **size** is the `height` of the font in `pixels.`  
If the filename is `None` the pygame `default font` will be loaded.  
If a font cannot be loaded from the arguments given an `exception` will be raised.  
Once the font is created the size `cannot` be changed.

### .bold

Gets or sets whether the font should be rendered in (faked) bold.

### .italic

Gets or sets whether the font should be rendered in (faked) italics.

### .underline

Gets or sets whether the font should be rendered with an underline.  
Always `one pixel` thick, regardless of font size.

### .strikethrough

Gets or sets whether the font should be rendered with a strikethrough.

Always `one pixel` thick, regardless of font size.

### .render()

Draw text on a new Surface.

    render(text, antialias, color, background=None) -> Surface

This creates a new Surface with the specified text rendered on it.  
`pygame.font` provides no way to directly draw text on an existing Surface: instead you must use `Font.render()` to create an image (Surface) of the text, then blit this image onto another Surface.

The **text** can only be a `single line`.  
`newline` characters are **not** rendered.  
`Null` characters ('x00') raise a `TypeError`.  
Both Unicode and char (byte) strings are accepted.  
For Unicode strings only `UCS-2` characters (`'\u0001'` to `'\uFFFF'`) were previously supported and any greater unicode codepoint would raise a `UnicodeError`.  
Now, characters in the `UCS-4` range are supported.  
For char strings a `LATIN1` encoding is assumed.  
The **antialias** argument is a boolean.  
The **color** argument is the color of the text.  
The optional **background** argument is a color to use for the text background.  
If `no` background is passed the area outside the text will be `transparent`.

The Surface returned will be of the dimensions required to hold the text. (the same as those returned by `Font.size()`).  
If an empty string is passed for the text, a blank surface will be returned that is zero pixel wide and the height of the font.

If antialiasing is `not` used, the return image will always be an `8-bit` image with a two-color palette.  
If the background is transparent a `colorkey` will be set.  

Antialiased images are rendered to `24-bit` RGB images.  
If the background is transparent a pixel alpha will be included.

**Optimization**: if you know that the final destination for the text (on the screen) will always have a solid background, and the text is antialiased, you can improve performance by specifying the background color. This will cause the resulting image to maintain transparency information by colorkey rather than (much less efficient) alpha values.

Font rendering is not thread safe: only a single thread can render text at any time.

Changed in pygame 2.0.3: Rendering UCS4 unicode works and does not raise an exception.  
Use if `hasattr(pygame.font, "UCS4")`: to see if pygame supports rendering UCS4 unicode including more languages and emoji.

### .size()

Determine the amount of space needed to render text.

### .metrics()

Gets the metrics for each character in the passed string.

The list contains tuples for each character, which contain:

- the minimum X offset
- the maximum X offset
- the minimum Y offset
- the maximum Y offset
- the advance offset (bearing plus width) of the character.  

`None` is entered in the list for each unrecognized character.

### .get_linesize()

Return the height in pixels for a line of text with the font.  

When rendering multiple lines of text this is the recommended amount of space between lines.

### .get_height()

Return the height in pixels of the actual rendered text.  

This is the **average** size for each glyph in the font.

### .get_ascent()

The ascent is the number of pixels from the font baseline to the top of the font.

### .get_descent()

The descent is the number of pixels from the font baseline to the bottom of the font.

[1]:https://www.pygame.org/docs/ref/font.html

< End >
