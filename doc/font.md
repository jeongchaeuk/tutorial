
# [pygame.font][1]

pygame module for loading and rendering fonts.

The font module allows for rendering TrueType fonts into Surface objects.  
This module is built on top of the ***SDL_ttf*** library, which comes with all normal pygame installations.

Most of the work done with fonts are done by using the actual ***Font*** objects.  
The module by itself only has routines to support the creation of Font objects with [pygame.font.Font()](#font).

You can load fonts from the system by using the [pygame.font.SysFont()](#sysfont) function.

Pygame comes with a builtin default font, ***freesansbold***.  
This can always be accessed by passing `None` as the font name.

## .init()

Initialize the font module.

This method is called automatically by [pygame.init()](/doc/pygame.md/#init).  
It is safe to call this function more than once.

## .quit()

Uninitialize the font module.

Manually uninitialize SDL_ttf's font system.  
This is called automatically by [pygame.quit()](/doc/pygame.md/#quit).

It is safe to call this function even if font is currently not initialized.  
Previously created font objects will be invalid after the font module is quit.

## .get_init()

```python
get_init() -> bool
```

`True` if the font module is initialized.

## .get_default_font()

```python
get_default_font() -> string
```

Return the filename of the system font.  
This is ***not the full path*** to the file.  
This file can usually be found in the same directory as the font module, but it can also be bundled in separate archives.

## .get_sdl_ttf_version()

```python
get_sdl_ttf_version(linked=True) -> (major, minor, patch)
```

Returns a tuple of integers that identify SDL_ttf's version.  
SDL_ttf is the underlying font rendering library, written in C, on which pygame's font module depends.  
If 'linked' is `True`, the function returns the version of the linked TTF library.  
Otherwise this function returns the version of TTF pygame was compiled with.

## .get_fonts()

```python
get_fonts() -> list[strings]
```

Returns a list of all the fonts available on the system.  
The names of the fonts will be set to ***lowercase*** with all spaces and punctuation ***removed***.  
This works on most systems, but some will return an empty list if they cannot find fonts.

## .match_font()

Find a specific font on the system.

```python
match_font(name, bold=False, italic=False) -> path
```

Returns the ***full path*** to a font file on the system.  
If `bold` or `italic` are set to ***true***, this will attempt to find the correct family of font.

The font `name` can also be an iterable of font names, a string of comma-separated font names, or a bytes of comma-separated font names, in which case the set of names will be searched in order.  
If none of the given names are found, `None` is returned.

```python
>>> print(pygame.font.match_font('bitstreamverasans'))
C:\WINDOWS\Fonts\arial.ttf
```

## .SysFont()

```python
SysFont(name, size, bold=False, italic=False) -> Font
```

Return a new Font object that is loaded from the ***system*** fonts.  
The font will match the requested bold and italic flags.  
If a suitable system font is not found this will fall back on loading the ***default*** pygame font.

Accept an iterable of font names.

# .Font

Create a new Font object from a file.

```python
Font(file_path=None, size=20) -> Font
Font(file_path, size) -> Font
Font(pathlib.Path, size) -> Font
Font(object, size) -> Font
```

Load a new font from a given filename or a python file object.  
The `size` is the ***height*** of the font ***in pixels***.  
If the filename is `None` the pygame ***default*** font will be loaded.  
If a font cannot be loaded from the arguments given an ***exception*** will be raised.  
Once the font is created the size ***can NOT*** be changed.

`pygame.Font` alias.

## .bold

```python
bold -> bool
```

Gets or sets whether the font should be rendered in (`faked`) bold.  
If possible load the font from a real bold font file.

## .name

```python
name -> str
```

`Read only`.  
Returns the font's name.

## .style_name

```python
style_name -> str
```

`Read only`.  
Returns the font's style name.  
Style names are arbitrary, can be an empty string.

Here are some examples:

```python
'Black'
'Bold', 'Bold Italic', 'BoldOblique'
'Book', 'BookOblique'
'Condensed', 'Condensed Oblique'
'Italic'
'ExtraLight', 'Light', 'LightOblique'
'Medium', 'MediumOblique'
'Oblique', 'Regular'
'Semibold', 'Semilight'
'Slanted'
```

## .italic

```python
italic -> bool
```

Gets or sets whether the font should be rendered in (`faked`) italics.  
If possible load the font from a real italic font file.

## .underline

```python
underline -> bool
```

Gets or sets whether the font should be rendered with an underline.  
Always `one pixel` thick, regardless of font size.

## .strikethrough

```python
strikethrough -> bool
```

Gets or sets whether the font should be rendered with a strikethrough.  
Always `one pixel` thick, regardless of font size.

## .align

Set how rendered text is aligned when given a wrap length.

```python
align -> int
```

Can be set to `pygame.FONT_LEFT`, `pygame.FONT_RIGHT`, or `pygame.FONT_CENTER`.  
This controls the text alignment behavior for the font.

## .point_size

Gets or sets the font's point size.

```python
point_size -> int
```

Will not be accurate upon initializing the font object when the font name is initalized as `None`.

## .render()

Draw text on a new Surface.

```python
render(text, antialias: bool, color, bgcolor=None, wraplength=0) -> Surface
```

This creates a new Surface with the specified text rendered on it.  
[pygame.font](#font) provides ***NO*** way to directly draw text on an existing Surface: instead you must use [Font.render()](#render) to create an image (Surface) of the text, then ***blit*** this image onto another Surface.

`Null` characters (`'\x00'`) raise a `TypeError`.  
Both Unicode and char (byte) strings are accepted.  
For char strings a `LATIN1` encoding is assumed.  
The `antialias` is whether have smooth edges.  
The `color` is the color of the text [e.g. (0, 0, 255) for blue].

The optional `bgcolor` is a color to use for the text background.  
If `None`, the area outside the text will be ***transparent***.

The `wraplength` describes the width (***in pixels***) a line of text should be before wrapping to a new line.  
See [pygame.font.Font.align](#align) for line-alignment settings.

The Surface returned will be of the dimensions required to hold the text. (the same as those returned by [Font.size()](#size)).  
If an empty string is passed for the text, a blank surface will be returned that is zero pixel wide and the height of the font.

|Antialias|Background|Surface|
|:-:|:-:|:-:|
|No|Color|8-bit image with 2-color palette|
|No|Transparent|Set color key|
|Yes|Color|24-bit RGB image|
|Yes|Transparent|Include pixel alpha|

***Optimization:***  
If you know that the final destination for the text (on the screen) will always have a solid background, and the text is antialiased, you can improve performance by specifying the background color.  
This will cause the resulting image to maintain transparency information by colorkey rather than (much less efficient) alpha values.

Font rendering is not thread safe: only a single thread can render text at any time.

```python
>>> # To see if pygame supports rendering
>>> # UCS4 unicode include more language and emoji.
>>> hasattr(pygame.font, 'UCS4')
True
```

Newline characters ('`\n`') now will break text into multiple lines.

## .size()

```python
size(text) -> (width, height)
```

Returns the dimensions needed to render the text.  
This can be used to help determine the positioning needed for text before it is rendered.  
It can also be used for word wrapping and other layout effects.

Be aware that most fonts use ***kerning*** which adjusts the widths for specific letter pairs.  
For example, the width for "ae" will not always match the width for "a" + "e".

## .set_underline()

```python
set_underline(bool) -> None
```

When enabled, all rendered fonts will include an underline.

## .get_underline()

```python
get_underline() -> bool
```

Return ***True*** when the font underline is enabled.

## .set_strikethrough()

```python
set_strikethrough(bool) -> None
```

When enabled, all rendered fonts will include a strikethrough.

## .get_strikethrough()

```python
get_strikethrough() -> bool
```

Return ***True*** when the font strikethrough is enabled.

## .set_bold()

```python
set_bold(bool) -> None
```

Enables fake rendering of bold text.

## .get_bold()

```python
get_bold() -> bool
```

Return ***True*** when the font bold rendering mode is enabled.

## .set_italic()

```python
set_italic(bool) -> None
```

Enables fake rendering of italic text.  

## .get_italic()

```python
get_italic() -> bool
```

Check if the text will be rendered italic.

## .metrics()

```python
metrics(text) -> list
```

Gets the metrics for each character in the passed string.  
The `list` contains tuples for each character, which contain:

- the minimum X offset
- the maximum X offset
- the minimum Y offset
- the maximum Y offset
- the advance offset (bearing plus width) of the character.  

 ```python
 [(minx, maxx, miny, maxy, advance), 
  (minx, maxx, miny, maxy, advance),
  ...]
 ```

`None` is entered in the list for each ***unrecognized*** character.

## .get_linesize()

```python
get_linesize() -> int
```

Return the ***height in pixels*** for a line of text with the font.  
When rendering multiple lines of text this is the recommended amount of space between lines.

## .get_height()

Return the ***height in pixels*** of the actual rendered text.  
This is the **average** size for each glyph in the font.

## .set_point_size()

```python
set_point_size(size) -> int
```

Sets the point size of the font, which is the value that was used to initalize this font.

New in pygame-ce 2.3.1.

## .get_point_size()

```python
get_point_size() -> int
```

Returns the point size of the font.

## .get_ascent()

```python
get_ascent() -> int
```

The ascent is the number of pixels from the font baseline to the top of the font.

## .get_descent()

```python
get_descent() -> int
```

The descent is the number of pixels from the font baseline to the bottom of the font.

## .set_script()

Set the script code for text shaping.

```python
set_script(str) -> None
```

Sets the script used by harfbuzz text shaping, taking a 4 character script code as input.  
For example, Hindi is written in the Devanagari script, for which the script code is "Deva".  
See the full list of script codes in [ISO 15924](https://www.unicode.org/iso15924/iso15924-codes.html).

## .set_direction()

```python
set_direction(direction) -> None
```

Sets the font direction for harfbuzz text rendering, taking in an integer between 0 and 3 (inclusive) as input.  
There are convenient constants defined for use in this method.

- `pygame.DIRECTION_LTR` is for left-to-right text
- `pygame.DIRECTION_RTL` is for right-to-left text
- `pygame.DIRECTION_TTB` is for top-to-bottom text
- `pygame.DIRECTION_BTT` is for bottom-to-top text

[1]:https://pyga.me/docs/ref/font.html

< End >
