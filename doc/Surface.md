
# [pygame.Surface][1]

pygame object for representing images.

    Surface((width, height), flags=0, depth=0, masks=None) -> Surface
    Surface((width, height), flags=0, Surface) -> Surface

The Surface has a fixed resolution and pixel format.  
Surfaces with `8-bit` pixels use a `color palette` to map to 24-bit color.

Call `pygame.Surface()` to create a new image object.  
The Surface will be `cleared` to all black.  
The only required arguments are the `sizes`.  
With no additional arguments, the Surface will be created in a format that best matches the display Surface.

The pixel format can be controlled by passing the bit depth or an existing Surface.  
The flags argument is a bitmask of additional features for the surface.  
Flags are only a request, and may not be possible for all displays and formats.

Advance users can combine a set of bitmasks with a depth value.  
The masks are a set of 4 integers representing which bits in a pixel will represent each color.  
Normal Surfaces should not require the masks argument.

Surfaces can have many extra attributes like alpha planes, colorkeys, source rectangle clipping.  
These functions mainly effect how the Surface is blitted to other Surfaces.  

There are three types of transparency supported in pygame: `colorkeys`, `surface alphas`, and `pixel alphas`.  

Surface alphas can be mixed with colorkeys, but an image with per pixel alphas cannot use the other modes.  

Colorkey transparency makes a single color value transparent.  
Any pixels matching the colorkey will not be drawn.  

The surface alpha value is a single value that changes the transparency for the entire image.  
A surface alpha of `255` is `opaque`, and a value of `0` is completely `transparent`.

Per pixel alphas are different because they store a transparency value for every pixel.  
This allows for the most precise transparency effects, but it also the slowest.  
Per pixel alphas cannot be mixed with surface alpha and colorkeys.

There is support for pixel access for the Surfaces.  
Pixel access on hardware surfaces is slow and not recommended.  
Pixels can be accessed using the `get_at()` and `set_at()` functions.  
These methods are fine for simple access, but will be considerably `slow` when doing of pixel work with them.  
If you plan on doing a lot of pixel level work, it is **recommended** to use a [pygame.PixelArray][2], which gives an array like view of the surface.  
For involved mathematical manipulations try the [pygame.surfarray][3] module. (It's quite `quick`, but requires `NumPy`.)

Any functions that directly access a surface's pixel data will need that surface to be locked.  
These functions can `lock()` and `unlock()` the surfaces themselves without assistance.  
But, if a function will be called many times, there will be a lot of overhead for multiple locking and unlocking of the surface.  
It is best to lock the surface manually before making the function call many times, and then unlocking when you are finished.  
All functions that need a locked surface will say so in their docs.  
Remember to leave the Surface locked only while necessary.

Surface pixels are stored internally as a single number that has all the colors encoded into it.  
Use the `map_rgb()` and `unmap_rgb()` to convert between individual red, green, and blue values into a packed integer for that Surface.

Surfaces can also reference sections of other Surfaces. These are created with the `subsurface()` method.  
Any change to either Surface will effect the other.

Each Surface contains a clipping area.  
By default the clip area covers the entire Surface.  
If it is changed, all drawing operations will only effect the smaller area.

### .blit()

Draw one image onto another.

    blit(source, dest, area=None, special_flags=0) -> Rect

Draws a source Surface onto this Surface.  
The draw can be **positioned** with the `dest` argument.  
The `dest` argument can either be a pair of coordinates representing the position of the `upper left corner` of the blit or a Rect, where the upper left corner of the rectangle will be used as the position for the blit.  
The `size` of the destination rectangle does `not` effect the blit.

An optional `area` rectangle can be passed as well.  
This represents a smaller `portion of the source Surface` to draw.

Optional `special_flags`:

    BLEND_ADD
    BLEND_SUB
    BLEND_MULT
    BLEND_MIN
    BLEND_MAX

    BLEND_RGBA_ADD
    BLEND_RGBA_SUB
    BLEND_RGBA_MULT
    BLEND_RGBA_MIN
    BLEND_RGBA_MAX

    BLEND_RGB_ADD
    BLEND_RGB_SUB
    BLEND_RGB_MULT
    BLEND_RGB_MIN
    BLEND_RGB_MAX

    BLEND_PREMULTIPLIED

    BLEND_ALPHA_SDL2
    Uses the SDL2 blitter for alpha blending, this gives different results than the default blitter, which is modelled after SDL1, due to different approximations used for the alpha blending formula.
    The SDL2 blitter also supports RLE on alpha blended surfaces which the pygame one does not.

The return rectangle is the area of the affected pixels, excluding any pixels outside the destination Surface, or outside the clipping area.

Pixel alphas will be **ignored** when blitting to an `8 bit` Surface.

For a surface with colorkey or blanket alpha, a blit to self may give slightly different colors than a non self-blit.

### .blits()

Draw many images onto another.

    blits(blit_sequence=((source, dest), ...), doreturn=1) -> [Rect, ...] or None
    blits(((source, dest, area), ...)) -> [Rect, ...]
    blits(((source, dest, area, special_flags), ...)) -> [Rect, ...]

Draws many surfaces onto this Surface.  
It takes a sequence as input, with each of the elements corresponding to the ones of blit().  
It needs at minimum a sequence of (source, dest).

Parameters:
- **blit_sequence**: a sequence of surfaces and arguments to blit them, they correspond to the blit() arguments.
- **doreturn**: if `True`, return a list of rects of the areas changed, otherwise return `None`

### .convert()

Change the pixel format of an image.

    convert(Surface=None) -> Surface
    convert(depth, flags=0) -> Surface
    convert(masks, flags=0) -> Surface

Creates a new copy of the Surface with the pixel format changed.  
The new pixel format can be determined from another existing Surface.  
Otherwise depth, flags, and masks arguments can be used, similar to the `pygame.Surface()` call.

If `no` arguments are passed the new Surface will have the same pixel format as the `display Surface`.  
This is always the fastest format for blitting.  
It is a good idea to convert all Surfaces before they are blitted many times.

The converted Surface will have `no` pixel alphas.  
They will be stripped if the original had them.  

The new copy will have the same class as the copied surface.  
This lets as Surface subclass inherit this method without the need to override, unless subclass specific instance attributes also need copying.

### .convert_alpha()

Change the pixel format of an image including per pixel alphas.

    convert_alpha(Surface) -> Surface
    convert_alpha() -> Surface

Creates a new copy of the surface with the desired pixel format.  
The new surface will be in a format suited for **quick** blitting to the given format with per pixel alpha.  
If `no` surface is given, the new surface will be optimized for blitting to the `current display`.

Unlike the `convert()` method, the pixel format for the new image will `not be exactly the same` as the requested source, but it will be optimized for `fast alpha blitting` to the destination.

As with `convert()` the returned surface has the same class as the converted surface.

### .copy()

Create a new copy of a Surface.

If a Surface subclass also needs to copy any instance specific attributes then it should override `copy()`.

### .fill()

Fill Surface with a solid color.

    fill(color, rect=None, special_flags=0) -> Rect

If `no` rect argument is given the `entire` Surface will be filled.  
The `rect` argument will **limit** the fill to a specific area.  
The fill will also be contained by the Surface clip area.

The `color` argument can be either a **RGB** sequence, a **RGBA** sequence or a mapped color **index**.  
If using RGBA, the Alpha (A part of RGBA) is ignored unless the surface uses per pixel alpha (Surface has the `SRCALPHA` flag).

Optional `special_flags`:

    BLEND_ADD
    BLEND_SUB
    BLEND_MULT
    BLEND_MIN
    BLEND_MAX

    BLEND_RGBA_ADD
    BLEND_RGBA_SUB
    BLEND_RGBA_MULT
    BLEND_RGBA_MIN
    BLEND_RGBA_MAX
    
    BLEND_RGB_ADD
    BLEND_RGB_SUB
    BLEND_RGB_MULT
    BLEND_RGB_MIN
    BLEND_RGB_MAX

This will return the affected Surface area.

### .scroll()

Shift the surface image in place.

    scroll(dx=0, dy=0) -> None

Move the image by `dx` pixels `right` and `dy` pixels `down`.  
dx and dy may be `negative` for `left` and `up` scrolls respectively.  
Areas of the surface that are not overwritten retain their original pixel values.  
Scrolling is contained by the Surface clip area.  
It is safe to have dx and dy values that exceed the surface size.

### .set_colorkey()

Set the transparent colorkey.

    set_colorkey(Color, flags=0) -> None
    set_colorkey(None) -> None

The same color as the colorkey will be `transparent`.  
The color can be an `RGB` color or a `mapped color integer`.  
If `None` is passed, the colorkey will be `unset`.

The colorkey will be ignored if the Surface is formatted to use per pixel alpha values.  
The colorkey can be mixed with the full `Surface alpha` value.

The optional `flags` argument can be set to `pygame.RLEACCEL` to provide better performance on non accelerated displays.  
An `RLEACCEL` Surface will be slower to modify, but quicker to blit as a source.

### .get_colorkey()

Get the current transparent colorkey.

    get_colorkey() -> RGB or None

### .set_alpha()

Set the alpha value for the full Surface image.

    set_alpha(value, flags=0) -> None
    set_alpha(None) -> None

The alpha value is an **integer** from `0 to 255`, `0` is fully `transparent` and `255` is fully `opaque`.  
If `None` is passed for the alpha value, then **alpha blending** will be `disabled`, including per-pixel alpha.

For a surface with per pixel alpha, ***blanket alpha is ignored*** and `None` is returned.

per-surface alpha can be combined with per-pixel alpha.

The optional `flags` argument can be set to `pygame.RLEACCEL` to provide better performance on non accelerated displays.  
An RLEACCEL Surface will be slower to modify, but quicker to blit as a source.

### .get_alpha()

Get the current Surface transparency value.

### .lock()

Lock the Surface memory for pixel access.

On accelerated Surfaces, the pixel data may be stored in volatile video memory or nonlinear compressed forms.  
When a Surface is locked the pixel memory becomes available to access by regular software.  
Code that reads or writes pixel values will need the Surface to be locked.

Surfaces should not remain locked for more than necessary.  
A locked Surface can often not be displayed or managed by pygame.

Not all Surfaces require locking.  
The `mustlock()` method can determine if it is actually required.  
There is `no` performance penalty for locking and unlocking a Surface that does not need it.

All pygame functions will automatically lock and unlock the Surface data as needed.  
If a section of code is going to make calls that will repeatedly lock and unlock the Surface many times, it can be helpful to wrap the block inside a lock and unlock pair.

It is safe to nest locking and unlocking calls.  
The surface will only be unlocked after the final lock is released.

### .unlock()

Unlock the Surface memory from pixel access.

The unlocked Surface can once again be drawn and managed by pygame.

### .mustlock()

Test if the Surface requires locking.

Returns `True` if the Surface is required to be locked to access pixel data.  
Usually pure software Surfaces do not require locking.  
This method is rarely needed, since it is safe and quickest to just lock all Surfaces as needed.

### .get_locked()

Test if the Surface is current locked.

### .get_locks()

Gets the locks for the Surface.

### .get_at()

Get the `RGBA` color value at a single pixel.
  
If the Surface has `no` per pixel alpha, then the alpha value will always be `255 (opaque)`.  
If the pixel position is outside the area of the Surface an `IndexError` exception will be raised.

Getting and setting pixels one at a time is generally `too slow` to be used in a game or realtime situation.  
It is better to use methods which operate on many pixels at a time like with the `blit`, `fill` and `draw` methods - or by using `pygame.surfarray`, `pygame.PixelArray`.

This function will temporarily lock and unlock the Surface as needed.

### .set_at()

Set the `RGBA` or `mapped integer color` value for a single pixel.  

If the Surface does not have per pixel alphas, the alpha value is ignored.  
Setting pixels outside the Surface area or outside the Surface clipping will have `no` effect.

This function will temporarily lock and unlock the Surface as needed.

If the surface is palettized, the pixel color will be set to the most similar color in the palette.

### .get_at_mapped()

Get the `mapped integer color` value at a single pixel.

If the pixel position is outside the area of the Surface an `IndexError` exception will be raised.

This method is intended for pygame `unit testing`.

This function will temporarily lock and unlock the Surface as needed.

### .get_palette()

Get the color index palette for an 8-bit Surface.

    get_palette() -> [RGB, RGB, RGB, ...]

Return a list of up to `256 color elements` that represent the indexed colors used in an 8-bit Surface.  
The returned list is a `copy` of the palette, and changes will have no effect on the Surface.

### .get_palette_at()

Get the color for a single entry in a palette.

    get_palette_at(index) -> RGB

The index should be a value from `0 to 255`.

### .set_palette()

Set the color palette for an 8-bit Surface.

    set_palette([RGB, RGB, RGB, ...]) -> None

A partial palette can be passed and only the first colors in the original palette will be changed.

This function has `no` effect on a Surface with more than 8-bits per pixel.

### .set_palette_at()

Set the color for a single index in an 8-bit Surface palette.

    set_palette_at(index, RGB) -> None

The index should be a value from `0 to 255`.

This function has `no` effect on a Surface with more than 8-bits per pixel.

### .map_rgb()

Convert a color into a mapped color value.

    map_rgb(Color) -> mapped_int

Convert an RGBA color into the mapped integer value for this Surface.  
The returned integer will contain no more bits than the bit depth of the Surface.  
Mapped color values are not often used inside pygame, but can be passed to most functions that require a Surface and a color.

### .unmap_rgb()

Convert a mapped integer color value into a Color.

    unmap_rgb(mapped_int) -> Color

### .set_clip()

Set the current clipping area of the Surface.

    set_clip(rect) -> None
    set_clip(None) -> None

Each Surface has an active clipping area.  
This is a rectangle that represents the only pixels on the Surface that can be modified.  
If `None` is passed for the rectangle the `full Surface` will be available for changes.

The clipping area is always `restricted` to the area of the Surface itself.  
If the clip rectangle is too large it will be shrunk to fit inside the Surface.

### .get_clip()

Get the current clipping area of the Surface.

    get_clip() -> Rect

### .subsurface()

Create a new surface that references its parent.

    subsurface(Rect) -> Surface

Returns a new Surface that shares its pixels with its new parent.  
The new Surface is considered a child of the original.  
Modifications to either Surface pixels will effect each other.  
Surface information like **clipping area** and **color keys** are `unique` to each Surface.

The new Surface will inherit the `palette`, `color key`, and `alpha settings` from its parent.

It is possible to have any number of subsurfaces and subsubsurfaces on the parent.  
It is also possible to subsurface the display Surface if the display mode is not hardware accelerated.

A subsurface will have the same class as the parent surface.

### .get_parent()

Find the parent of a subsurface.

    get_parent() -> Surface | None

### .get_abs_parent()

Find the top level parent of a subsurface.

    get_abs_parent() -> Surface

If this is `not` a subsurface then `this surface` will be returned.

### .get_offset()

Get the offset position of a child subsurface inside of a parent.  
If the Surface is `not` a subsurface this will return `(0, 0)`.

### .get_abs_offset()

Find the absolute position of a child subsurface inside its top level parent.

If the Surface is `not` a subsurface this will return `(0, 0)`.

### .get_size()

Get the dimensions of the Surface.

### .get_width()

Get the width of the Surface.

### .get_height()

Get the height of the Surface.

### .get_rect()

Get the rectangular area of the Surface.

    get_rect(**kwargs) -> Rect

This rectangle will always start at `(0, 0)` with a width and height the same size as the image.

These named values will be applied to the attributes of the Rect before it is returned.  
An example would be `mysurf.get_rect(center=(100, 100))` to create a rectangle for the Surface centered at a given position.

### .get_bitsize()

Get the bit depth of the Surface pixel format.

This value may not exactly fill the number of bytes used per pixel.  
For example a `15 bit` Surface still requires a full `2 bytes`.

### .get_bytesize()

Get the bytes used per Surface pixel.

### .get_flags()

Get the additional flags used for the Surface.

Typical flags are `RLEACCEL`, `SRCALPHA`, and `SRCCOLORKEY`.

    SWSURFACE      0x00000000    # Surface is in system memory

See [pygame.display.set_mode()][4] for flags exclusive to the display surface.

Used internally (read-only)

    HWACCEL        0x00000100    # Blit uses hardware acceleration
    SRCCOLORKEY    0x00001000    # Blit uses a source color key
    RLEACCELOK     0x00002000    # Private flag
    RLEACCEL       0x00004000    # Surface is RLE encoded
    SRCALPHA       0x00010000    # Blit uses source alpha blending
    PREALLOC       0x01000000    # Surface uses preallocated memory

### .get_pitch()

Return the number of bytes `separating each row` in the Surface.  
Surfaces in video memory are not always linearly packed.  
Subsurfaces will also have a larger pitch than their real width.

This value is `not` needed for normal pygame usage.

### .get_masks()

The bitmasks needed to convert between a color and a mapped integer.

    get_masks() -> (R, G, B, A)

Returns the bitmasks used to isolate each color in a mapped integer.

This value is `not` needed for normal pygame usage.

### .get_shifts()

The bit shifts needed to convert between a color and a mapped integer.

    get_shifts() -> (R, G, B, A)

This value is `not` needed for normal pygame usage.

### .get_losses()

    get_losses() -> (R, G, B, A)

Return the least significant number of bits stripped from each color in a mapped integer.

This value is `not` needed for normal pygame usage.

### .get_bounding_rect()

Find the smallest rect containing data.

    get_bounding_rect(min_alpha=1) -> Rect

Returns the smallest rectangular region that contains all the pixels in the surface that have an `alpha value >= minimum alpha value`.

This function will temporarily lock and unlock the Surface as needed.

### .get_view()

Return a buffer view of the Surface's pixels.

    get_view(<kind> = '2') -> BufferProxy

Return an object which exports a surface's internal pixel buffer as a C level array struct, Python level array interface or a C level buffer interface.  
The new buffer protocol is supported.

The `kind` argument is the length 1 string `'0', '1', '2', '3', 'r', 'g', 'b', or 'a'`.  
The letters are case insensitive.  
The argument can be either a Unicode or byte (char) string.  

`'0'` returns a **contiguous unstructured bytes** view.  
No surface shape information is given.  
A `ValueError` is raised if the surface's pixels are **discontinuous**.

`'1'` returns a **(surface-width * surface-height) array** of `continuous` pixels.  
A `ValueError` is raised if the surface pixels are **discontinuous**.

`'2'` returns a **(surface-width, surface-height) array** of `raw` pixels.  
The pixels are surface-bytesize-d unsigned integers.  
The pixel format is surface specific.  
The 3 byte unsigned integers of 24 bit surfaces are unlikely accepted by anything other than other pygame functions.

`'3'` returns a **(surface-width, surface-height, 3) array** of RGB color components.  
Each of the red, green, and blue components are unsigned bytes.  
Only `24`-bit and `32`-bit surfaces are supported.  
The color components must be in either `RGB` or `BGR` order within the pixel.

`'r'` for red, `'g'` for green, `'b'` for blue, and `'a'` for alpha return a **(surface-width, surface-height)** view of a single color component within a surface: a `color plane`.  
Color components are unsigned bytes.  
Both `24`-bit and `32`-bit surfaces support **'r', 'g', and 'b'**.  
Only `32`-bit surfaces with `SRCALPHA` support **'a'**.

The surface is locked only when an exposed interface is accessed.  
For new buffer interface accesses, the surface is unlocked once the last buffer view is released. For array interface and old buffer interface accesses, the surface remains locked until the BufferProxy object is released.

### .get_buffer()

Acquires a buffer object for the pixels of the Surface.

    get_buffer() -> BufferProxy

The buffer can be used for direct pixel access and manipulation.  
Surface pixel data is represented as an unstructured block of memory, with a start address and length in bytes.  
The data need not be contiguous.  
Any gaps are included in the length, but otherwise ignored.

This method implicitly locks the Surface.  
The lock will be released when the returned [pygame.BufferProxy][5] object is garbage collected.

### ._pixels_address

The starting address of the surface's raw pixel bytes.

### .premul_alpha()

Returns a copy of the surface with the RGB channels pre-multiplied by the alpha channel.

This is intended to make it easier to work with the `BLEND_PREMULTIPLED` blend mode flag of the `blit()` method.  
Surfaces which have called this method will only look correct after blitting if the `BLEND_PREMULTIPLED` special flag is used.

It is worth noting that after calling this method, methods that return the colour of a pixel such as get_at() will return the alpha multiplied colour values.  
It is not possible to fully reverse an alpha multiplication of the colours in a surface as integer colour channel data is generally reduced by the operation  (e.g. 255 x 0 = 0, from there it is not possible to reconstruct the original 255 from just the two remaining zeros in the colour and alpha channels).

If you call this method, and then call it again, it will multiply the colour channels by the alpha channel twice.  
There are many possible ways to obtain a surface with the colour channels pre-multiplied by the alpha channel in pygame, and it is not possible to tell the difference just from the information in the pixels.  
It is completely possible to have two identical surfaces - one intended for pre-multiplied alpha blending and one intended for normal blending.  
For this reason we do not store state on surfaces intended for pre-multiplied alpha blending.

Surfaces `without an alpha channel` cannot use this method and will return an `error` if you use it on them.  
It is best used on 32 bit surfaces (the default on most platforms) as the blitting on these surfaces can be accelerated by SIMD versions of the pre-multiplied blitter.

In general pre-multiplied alpha blitting is faster then 'straight alpha' blitting and produces superior results when blitting an alpha surface onto another surface with alpha - assuming both surfaces contain pre-multiplied alpha colours.

[1]:https://www.pygame.org/docs/ref/surface.html
[2]:https://www.pygame.org/docs/ref/pixelarray.html
[3]:https://www.pygame.org/docs/ref/surfarray.html
[4]:https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
[5]:https://www.pygame.org/docs/ref/bufferproxy.html#pygame.BufferProxy

< End >
