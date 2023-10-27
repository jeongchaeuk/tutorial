
# [pygame.mask][1]

pygame module for image masks.

Useful for fast pixel perfect collision detection.  
A mask uses **1 bit per-pixel** to store which parts collide.

Mask functions that take **positions** or **offsets** now support `pygame.math.Vector2` arguments.

### .from_surface()

    from_surface(surface) -> Mask
    from_surface(surface, threshold=127) -> Mask

Creates a Mask object from the given surface by setting all the **opaque** pixels and not setting the **transparent** pixels.

If the surface uses a **color-key**, then it is used to decide which bits in the resulting mask are set.  
All the pixels that are not equal to the color-key are set and the pixels equal to the color-key are not set.

If a color-key is not used, then the **alpha value** of each pixel is used to decide which bits in the resulting mask are set.  
All the pixels that have an (alpha value > `threshold` parameter) are **set** and the pixels with an (alpha value <= `threshold`) are **not set**.

Parameters:

    surface: Surface 
    the surface to create the mask from.

    threshold: int 
    (optional) the alpha threshold (default is 127) to compare with each surface pixel's alpha value, if the surface is color-keyed this parameter is ignored.

This function is used to create the masks for [pygame.sprite.collide_mask()][2].

### .from_threshold()

Creates a mask by thresholding Surfaces.

    from_threshold(surface, color) -> Mask
    from_threshold(surface, color, threshold=(0, 0, 0, 255), othersurface=None, palette_colors=1) -> Mask

If the optional `othersurface` is not used, all the pixels **within** the `threshold` of the `color` parameter are **set** in the resulting mask.

If the optional `othersurface` is used, every pixel in the first surface that is **within** the `threshold` of the corresponding pixel in `othersurface` is **set** in the resulting mask.

Parameters

    surface: Surface
    the surface to create the mask from.

    color: Color | int | tuple(int, int, int, [int]) | list[int, int, int, [int]]
    color used to check if the surface's pixels are within the given threshold range. 
    This parameter is ignored if the optional othersurface parameter is supplied.

    threshold: Color | int | tuple(int, int, int, [int]) | list[int, int, int, [int]]
    (optional) the threshold range used to check the difference between two colors.
    Default is (0, 0, 0, 255).

    othersurface: Surface
    (optional) used to check whether the pixels of the first surface are within the given threshold range of the pixels from this surface.

    palette_colors: int
    (optional) indicates whether to use the palette colors or not, a nonzero value causes the palette colors to be used and a 0 causes them not to be used.

# .Mask

pygame object for representing 2D bitmasks.

    Mask(size=(width, height)) -> Mask
    Mask(size=(width, height), fill=False) -> Mask

Each **bit** in the mask represents a **pixel**.  
1 is used to indicate a set bit and 0 is used to indicate an unset bit.  
Set bits in a mask can be used to detect collisions with other masks and their set bits.

A filled mask has all of its bits set to 1, conversely an unfilled/cleared/empty mask has all of its bits set to 0.  
Masks can be created **unfilled** (default) or filled by using the `fill` parameter.  
Masks can also be cleared or filled using the [pygame.mask.Mask.clear()][3] and [pygame.mask.Mask.fill()][4] methods respectively.

A mask's coordinates start in the **top left** corner at (0, 0) just like [pygame.Surface][5].  
Individual bits can be accessed using the [pygame.mask.Mask.get_at()][6] and [pygame.mask.Mask.set_at()][7] methods.

The methods `overlap(), overlap_area(), overlap_mask(), draw(), erase(), and convolve()` use an `offset` parameter to indicate the offset of another mask's top left corner from the calling mask's top left corner.  
The calling mask's top left corner is considered to be the **origin** `(0, 0)`.  
Offsets are a sequence of two values `(x_offset, y_offset)`.  
Positive and negative offset values are supported.

### offset


                0 to x (x_offset)
                :    :
        0 ..... +----:---------+
        to      |    :         |
        y .......... +-----------+
    (y_offset)  |    | othermask |
                |    +-----------+
                | calling_mask |
                +--------------+

Shallow copy supported.  
The Mask class supports the special method `__copy__()` and shallow copying via `copy.copy(mask)`.

### .copy()

    copy() -> Mask

If a mask subclass needs to copy any instance specific attributes then it should override the `__copy__()` method.  
The overridden `__copy__()` method needs to call `super().__copy__()` and then copy the required data as in the following example code.

    class SubMask(pygame.mask.Mask):
        def __copy__(self):
            new_mask = super().__copy__()
            # Do any SubMask attribute copying here.
            return new_mask

### .get_size()

    get_size() -> (width, height)

### .get_rect()

Returns a Rect based on the size of the mask.

    get_rect(**kwargs) -> Rect

Returns a new [pygame.Rect()][8] object based on the size of this mask.  
The rect's default position will be `(0, 0)` and its default width and height will be the same as this mask's.  
The rect's attributes can be altered via [pygame.Rect()][8] attribute keyword arguments/values passed into this method.  

### .get_at()

Gets the bit at the given position.

    get_at(pos) -> int

Raises **IndexError**, if the position is outside of the mask's bounds.

### .set_at()

Sets the bit at the given position.

    set_at(pos) -> None
    set_at(pos, value=1) -> None

Raises **IndexError**, if the position is outside of the mask's bounds.

### .overlap()

Returns the point of intersection.

    overlap(other, offset) -> (x, y)
    overlap(other, offset) -> None

Returns the first point of intersection encountered between this mask and other.  
A point of intersection is 2 overlapping set bits.

The current algorithm searches the overlapping area in `sizeof(unsigned long int) * CHAR_BIT` bit wide column blocks (this value is platform dependent, for clarity it will be referred to as **W**).  
Starting at the top left corner it checks bits 0 to W - 1 of the first row (`(0, 0) to (W - 1, 0)`) then continues to the next row (`(0, 1) to (W - 1, 1)`).  
Once this entire column block is checked, it continues to the next block (W to 2 * W - 1).  
This is repeated until it finds a point of intersection or the entire overlapping area is checked.

### .overlap_area()

Returns the number of overlapping set bits.

    overlap_area(other, offset) -> numbits


This can be useful for collision detection.  
An approximate collision normal can be found by calculating the gradient of the overlapping area through the finite difference.

    dx = mask.overlap_area(other, (x + 1, y)) - mask.overlap_area(other, (x - 1, y))
    dy = mask.overlap_area(other, (x, y + 1)) - mask.overlap_area(other, (x, y - 1))

### .overlap_mask()

    overlap_mask(other, offset) -> Mask

Returns a Mask, the same size as this mask, containing the overlapping set bits between this mask and other.

### .fill()
Sets all bits to 1.

### .clear()

Sets all bits to 0.

### .invert()

Flips all the bits.

### .scale()

    scale((width, height)) -> Mask

Creates a new Mask of the requested size with its bits scaled from this mask.

Raises **ValueError** if width < 0 or height < 0

### .draw()

    draw(other, offset) -> None

Performs a **bitwise OR**, drawing othermask onto this mask.

### .erase()

    erase(other, offset) -> None

Erases (clears) all bits set in other from this mask.

### .count()

Returns the number of set bits.
    
### .centroid()

    centroid() -> (x, y)

Finds the centroid (the center mass of the set bits) for this mask.  
It will return **(0, 0)** if the mask has **no** bits set.

### .angle()

Finds the approximate orientation (from **-90 to 90** degrees) of the set bits in the mask.  
This works best if performed on a mask with only one connected component.
The orientation of the set bits in the mask, it will return **0.0** if the mask has **no** bits set.

See [connected_component()](#connected_component) for details on how a connected component is calculated.

### .outline()

    outline() -> [(x, y), ...]
    outline(every=1) -> [(x, y), ...]

Returns a list of points of the outline of the first connected component encountered in the mask.  
To find a connected component, the mask is searched per **row (left to right)** starting in the **top left** corner.

The `every` optional parameter skips set bits in the outline.  
For example, setting it to 10 would return a list of every 10th set bit in the outline.

An **empty** list is returned if the mask has **no** bits set.

### .convolve()

Returns the convolution of this mask with another mask

    convolve(other) -> Mask
    convolve(other, output=None, offset=(0, 0)) -> Mask

Convolve this mask with the given other Mask.

Parameters

    other: Mask
    mask to convolve this mask with.

    output: Mask | NoneType
    (optional) mask for output.

    offset
    the offset of other from this mask.

Returns a Mask with the (i - offset[0], j - offset[1]) bit set, if shifting other (such that its bottom right corner is at (i, j)) causes it to overlap with this mask.

If an `output` Mask is specified, the output is drawn onto it and it is returned.  
Otherwise a mask of size **(MAX(0, width + other mask's width - 1), MAX(0, height + other mask's height - 1))** is created and returned.

### .connected_component()

Returns a mask containing a connected component.

    connected_component() -> Mask
    connected_component(pos) -> Mask

A connected component is a group (1 or more) of connected set bits (orthogonally and diagonally).  
The **SAUF** algorithm, which checks 8 point connectivity, is used to find a connected component in the mask.

By default this method will return a Mask (same size as this mask) containing **the largest** connected component in the mask.  
Optionally, a bit coordinate can be specified and the connected component containing it will be returned.  
If the bit at the given location is **not set**, the returned Mask will be **empty** (no bits set).

Parameters

    pos
    (optional) selects the connected component that contains the bit at this position

if this mask has **no** bits set then an **empty** mask will be returned.  
Raises **IndexError** if the optional pos parameter is outside of the mask's bounds.

### .connected_components()

Returns a list of masks of connected components.

    connected_components() -> [Mask, ...]
    connected_components(minimum=0) -> [Mask, ...]

Parameters

    minimum: int
    (optional) indicates the minimum number of bits (to filter out noise) per connected component (default is 0, which equates to no minimum and is equivalent to setting it to 1, as a connected component must have at least 1 bit set)

An **empty** list is returned if the mask has **no** bits set.

### .get_bounding_rects()

Returns a list of bounding rects of connected components.

    get_bounding_rects() -> [Rect, ...]

An **empty** list is returned if the mask has **no** bits set.

### .to_surface()

    to_surface() -> Surface
    to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 255), dest=(0, 0)) -> Surface

Draws this mask on the given surface.  
Set bits and unset bits can be drawn onto a surface.

|Parameters|type|
|-|-|
|surface|Surface \| None|
||(optional) Surface to draw mask onto, if **no** surface is provided one will be created (which will cause a surface with the parameters `Surface(size=mask.get_size(), flags=SRCALPHA, depth=32)` to be created, drawn on, and returned).|
|setsurface|Surface \| None|
||(optional) use this surface's color values to draw **set bits**, if this surface is smaller than the mask any bits outside its bounds will use the setcolor value.|
|unsetsurface|Surface \| None|
||(optional) use this surface's color values to draw **unset bits**, if this surface is smaller than the mask any bits outside its bounds will use the unsetcolor value.|
|setcolor|Color \| str \| int \| tuple(int, int, int, [int]) \| list(int, int, int, [int]) \| None|
||(optional) color to draw set bits (default is opaque white), use **None** to skip drawing the set bits, the `setsurface` parameter (if set) will takes precedence over this parameter.|
|unsetcolor|Color \| str \| int \| tuple(int, int, int, [int]) \| list(int, int, int, [int]) \| None|
||(optional) color to draw unset bits (default is opaque black), use **None** to skip drawing the unset bits, the unsetsurface parameter (if set) will takes precedence over this parameter.|
|dest|Rect \| tuple(int, int) \| list(int, int) \| Vector2(int, int)|
||(optional) surface destination of where to position the topleft corner of the mask being drawn, if a `Rect` is used as the dest parameter, its `x` and `y` attributes will be used as the destination,<br>**NOTE1**: rects with a **negative** width or height value will **not** be normalized before using their x and y values,<br>**NOTE2**: this destination value is only used to position the mask on the surface, it does not offset the setsurface and unsetsurface from the mask, they are always aligned with the mask (i.e. position (0, 0) on the mask always corresponds to position (0, 0) on the setsurface and unsetsurface).|

Raises **ValueError** if the setsurface parameter or unsetsurface parameter does **not** have the same format **(bytesize, bitsize, alpha)** as the surface parameter.

To **skip** drawing the **set** bits both `setsurface` and `setcolor` must be **None**.  
The setsurface parameter defaults to None, but setcolor defaults to a color value and therefore must be set to None.

To **skip** drawing the **unset** bits, both `unsetsurface` and `unsetcolor` must be **None**.  
The unsetsurface parameter defaults to None, but unsetcolor defaults to a color value and therefore must be set to None.

[1]:https://www.pygame.org/docs/ref/mask.html
[2]:/doc/sprite.md/#collide_mask
[3]:#clear
[4]:#fill
[5]:/doc/Surface.md
[6]:#get_at
[7]:#set_at
[8]:/doc/Rect.md

< End >
