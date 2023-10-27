
# [pygame.Color][1]

pygame object for color representations

    Color(r, g, b) -> Color
    Color(r, g, b, a=255) -> Color
    Color(color_value) -> Color

The Color class represents **RGBA** color values using a value range of **0 to 255** inclusive.  
It allows basic arithmetic operations — binary operations `` `+, -, *, //, %` ``, and unary operation `` `~` `` — to create new colors, supports conversions to other color spaces such as **HSV** or **HSL** and lets you adjust single color channels.  
**Alpha** defaults to **255** (fully **opaque**) when not given.  
The arithmetic operations and `correct_gamma()` method preserve subclasses.  
For the binary operators, the class of the returned color is that of the left hand color object of the operator.

Color objects support equality comparison with other color objects and 3 or 4 element tuples of integers.  

Color objects export the C level array interface.  
The interface exports a read-only one dimensional unsigned byte array of the same assigned length as the color.  
The new buffer interface is also exported, with the same characteristics as the array interface.

The floor division ( // ), and modulus ( % ), operators do **not raise** an exception for **division by zero**.  
Instead, if a color, or alpha, channel in the right hand color is 0, then the result is 0.

    # These expressions are True
    Color(255, 255, 255, 255) // Color(0, 64, 64, 64) == Color(0, 3, 3, 3)
    Color(255, 255, 255, 255) % Color(64, 64, 64, 0) == Color(63, 63, 63, 0)

Use `int(color)` to return the immutable integer value of the color, usable as a **dict key**.  
This integer value **differs** from the mapped pixel values of [pygame.Surface.get_at_mapped()][2], [pygame.Surface.map_rgb()][3] and [pygame.Surface.unmap_rgb()][4].  
It can be passed as a `color_value` argument to `Color` (useful with sets).

See [Named Colors][5] for samples of the available named colors.

|Parameters|Type|
|-|-|
|r|int|
||**red** value in the range of 0 to 255 inclusive.|
|g|int|
||**green** value in the range of 0 to 255 inclusive.|
|b|int|
||**blue** value in the range of 0 to 255 inclusive.|
|a|int|
||(optional) **alpha** value in the range of 0 to 255 inclusive, default is **255**.|
|color_value|Color \| str \| int \| tuple(int, int, int, [int]) \| list(int, int, int, [int])|
||color value (see note below for the supported formats).|

Note: Supported `color_value` formats:

- **Color object**: clones the given Color object.
- **Color name: str**: name of the color to use, e.g. 'red' (all the supported name strings can be found in the [Named Colors][5], with sample swatches).
- **HTML color format str**: `'#rrggbbaa'` or `'#rrggbb'`, where rr, gg, bb, and aa are 2-digit hex numbers in the range of `0 to 0xFF` inclusive, the aa (alpha) value defaults to `0xFF` if not provided.
- **hex number str**: `'0xrrggbbaa'` or `'0xrrggbb'`, where rr, gg, bb, and aa are 2-digit hex numbers in the range of `0x00 to 0xFF` inclusive, the aa (alpha) value defaults to `0xFF` if not provided.
- **int**: int value of the color to use, using hex numbers can make this parameter more readable, e.g. `0xrrggbbaa`, where rr, gg, bb, and aa are 2-digit hex numbers in the range of `0x00 to 0xFF` inclusive.  
Note that the aa (alpha) value is **not optional** for the int format and must be provided.
- **tuple/list of int color values**: `(R, G, B, A)` or `(R, G, B)`, where R, G, B, and A are int values in the range of `0 to 255` inclusive, the A (alpha) value defaults to `255` if not provided.

### .r

Gets or sets the **red** value of the Color.

### .g

Gets or sets the **green** value of the Color.

### .b

Gets or sets the **blue** value of the Color.

### .a

Gets or sets the **alpha** value of the Color.

### .cmy

Gets or sets the **CMY** (Cyan, Magenta, Yellow) representation of the Color.

    cmy -> tuple

The **CMY** components are in the ranges `C = [0, 1], M = [0, 1], Y = [0, 1]`.  
Note that this will **not** return the absolutely **exact** CMY values for the set RGB values in all cases.  
Due to the RGB mapping from 0-255 and the CMY mapping from 0-1 rounding errors may cause the CMY values to differ slightly from what you might expect.

### .hsva

Gets or sets the **HSVA** (Hue, Saturation, Value, Alpha) representation of the Color.

    hsva -> tuple

The **HSVA** components are in the ranges `H = [0, 360], S = [0, 100], V = [0, 100], A = [0, 100]`.  
Note that this will **not** return the absolutely **exact** HSV values for the set RGB values in all cases.  
Due to the RGB mapping from 0-255 and the HSV mapping from 0-100 and 0-360 rounding errors may cause the HSV values to differ slightly from what you might expect.

### .hsla

Gets or sets the **HSLA** (Hue, Saturation, Lightness, Alpha) representation of the Color.
    
    hsla -> tuple

The **HSLA** components are in the ranges `H = [0, 360], S = [0, 100], L = [0, 100], A = [0, 100]`.  
Note that this will **not** return the absolutely **exact** HSL values for the set RGB values in all cases.  
Due to the RGB mapping from 0-255 and the HSL mapping from 0-100 and 0-360 rounding errors may cause the HSL values to differ slightly from what you might expect.

### .i1i2i3

Gets or sets the **I1I2I3** representation of the Color.

    i1i2i3 -> tuple

The **I1I2I3** components are in the ranges `I1 = [0, 1], I2 = [-0.5, 0.5], I3 = [-0.5, 0.5]`.  
Note that this will **not** return the absolutely **exact** I1I2I3 values for the set RGB values in all cases.  
Due to the RGB mapping from 0-255 and the I1I2I3 mapping from 0-1 rounding errors may cause the I1I2I3 values to differ slightly from what you might expect.

### .normalize()

    normalize() -> tuple

Returns the normalized RGBA values of the Color as **floating point** values.  
e.g. (255, 255, 255, 255) -> (1.0, 1.0, 1.0, 1.0)

### .correct_gamma()

Applies a certain gamma value to the Color.

    correct_gamma(gamma) -> Color

### .grayscale()

Returns the grayscale of a Color.

    grayscale() -> Color

### .lerp()

    lerp(Color, float) -> Color

Returns a Color which is a linear interpolation between self and the given Color in RGBA space.  
The **second parameter** determines how far between self and other the result is going to be.  
It must be a value between **0(self) and 1(other)**.

### .premul_alpha()

Returns a new Color where each of the red, green and blue colour channels have been multiplied by the alpha channel of the original color.  
The **alpha** channel remains **unchanged**.

This is useful when working with the **BLEND_PREMULTIPLIED** blending mode flag for [pygame.Surface.blit()][6], which assumes that all surfaces using it are using pre-multiplied alpha colors.

### .update()

Sets the elements of the color.

    update(r, g, b) -> None
    update(r, g, b, a=255) -> None
    update(color_value) -> None

If the alpha value was not set it will not change.

[1]:https://www.pygame.org/docs/ref/color.html
[2]:/doc/Surface.md/#get_at_mapped
[3]:/doc/Surface.md/#map_rgb
[4]:/doc/Surface.md/#unmap_rgb
[5]:https://www.pygame.org/docs/ref/color_list.html
[6]:/doc/Surface.md/#blit

< End >
