
# [SDL][1]

## Transparency

There are 3 ways to make something transparent in pygame.  

1. `Colorkey`  
all pixels with the same color as defined as colorkey will not be drawn.  
That means they are 100% transparent.  

        image.set_colorkey((255, 0, 255))

2. `Per image alpha`  
its the alpha channel for the **entire** image.  
All pixels will be drawn using the same alpha value.

        image.set_alpha(128)

3. `Per pixel alpha`  
a images that has per pixel alpha, an alpha channel for each pixel.

---

- `RGB`: surface without per pixel alpha
- `RGBA`: surface with per pixel alpha
- `SDL_SRCALPHA`: surface with per surface alpha
- `SDL_SRCCOLORKEY`: surface using a colorkey

### RGBA->RGB with SDL_SRCALPHA

The source is `alpha-blended` with the destination, using the `alpha channel`.  
`SDL_SRCCOLORKEY` and `the per-surface alpha` are **ignored**.

### RGBA->RGB without SDL_SRCALPHA

The RGB data is `copied` from the source.  
The `source alpha channel` and the `per-surface alpha` value are **ignored**.  
If `SDL_SRCCOLORKEY` is set, only the pixels not matching the colorkey value are copied.

### RGB->RGBA with SDL_SRCALPHA

The source is `alpha-blended` with the destination using the `per-surface alpha` value.  
If `SDL_SRCCOLORKEY` is set, only the pixels not matching the colorkey value are copied.  
The alpha channel of the copied pixels is set to `opaque`.

### RGB->RGBA without SDL_SRCALPHA

The RGB data is `copied` from the source and the alpha value of the copied pixels is set to `opaque`.  
If `SDL_SRCCOLORKEY` is set, only the pixels not matching the colorkey value are copied.

### RGBA->RGBA with SDL_SRCALPHA

The source is `alpha-blended` with the destination using the `source alpha channel`.  
The alpha channel in the destination surface is left `untouched`.  
`SDL_SRCCOLORKEY` is **ignored**.

### RGBA->RGBA without SDL_SRCALPHA

The RGBA data is `copied` to the destination surface.  
If `SDL_SRCCOLORKEY` is set, only the pixels not matching the colorkey value are copied.

### RGB->RGB with SDL_SRCALPHA

The source is `alpha-blended` with the destination using the `per-surface alpha` value.  
If `SDL_SRCCOLORKEY` is set, only the pixels not matching the colorkey value are copied.

### RGB->RGB without SDL_SRCALPHA

The RGB data is `copied` from the source.  
If `SDL_SRCCOLORKEY` is set, only the pixels not matching the colorkey value are copied.

[1]:https://www.libsdl.org/

< End >
