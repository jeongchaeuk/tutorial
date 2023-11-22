
# [pygame.display][1]

*Module to control the display window and screen.*

Pygame has a single display Surface that is either contained in a ***window*** or runs ***full screen***.  
Once you create the display you treat it as a regular Surface.  
Changes are not immediately visible onscreen.  
You must choose one of the two ***flipping*** functions to update the actual display.  

The origin(0, 0) of the display is the ***top left*** of the screen.  
Both axes increase positively towards the ***bottom right*** of the screen.

By default, the display is a basic software driven framebuffer.  
You can request special modules like automatic scaling or ***OpenGL*** support.  
These are controlled by ***flags*** passed to [pygame.display.set_mode()](#set_mode).

To detect the number and size of attached screens, you can use pygame.display.get_desktop_sizes and then select appropriate window size and display index to pass to [pygame.display.set_mode()](#set_mode).

Pygame can only have a ***single*** display active at any time.  
Creating a new one with [pygame.display.set_mode()](#set_mode) will close the previous display.  
To detect the number and size of attached screens, you can use [pygame.display.get_desktop_sizes()](#get_desktop_sizes) and then select appropriate window size and display index to pass to [pygame.display.set_mode()](#set_mode).

Use the functions to query detailed information about the display.:

```python
pygame.display.mode_ok()
pygame.display.list_modes()
pygame.display.Info()
```

Once the display Surface is created, the functions from this module affect the single existing display.  
The Surface becomes invalid if the module is uninitialized.  
If a new display mode is set, the existing Surface will ***automatically switch*** to operate on the new display.

When the display mode is set, several events are placed on the pygame event queue. pygame.QUIT is sent when the user has requested the program to shut down. The window will receive pygame.ACTIVEEVENT events as the display gains and loses input focus. If the display is set with the pygame.RESIZABLE flag, pygame.VIDEORESIZE events will be sent when the user adjusts the window dimensions. Hardware displays that draw direct to the screen will get pygame.VIDEOEXPOSE events when portions of the window must be redrawn.

When the display mode is set, several events are placed on the pygame event queue.

|Event|Description|
|-|-|
|pygame.QUIT|is sent when the user has requested the program to ***shut down***.|
|pygame.ACTIVEEVENT|The window will receive this events as the display gains and loses ***input focus***.|
|pygame.VIDEORESIZE|If the display is set with the `pygame.RESIZABLE` flag, this will be sent when the user adjusts the window dimensions.|
|pygame.VIDEOEXPOSE|Hardware displays that draw direct to the screen will get `pygame.VIDEOEXPOSE` when portions of the window must be redrawn.|

[more...][2]

Some display environments have an option for automatically stretching all windows.  
When this option is enabled, this automatic stretching distorts the appearance of the pygame window.  
Example code: [prevent_display_stretching.py](https://github.com/pygame-community/pygame-ce/blob/main/examples/prevent_display_stretching.py).  
Only Microsoft Windows (Vista or newer required).

```python
import ctypes

# Prevent stretching.
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
```

## .init()

Initialize the display module.  
This is usually handled for you automatically when you call the higher level [pygame.init()](/doc/pygame.md/#init).  
Before the display module is initialized the environment variable [SDL_VIDEODRIVER](/doc/pygame.md/#sdl-environment-variables) can be set to control which backend is used.

The systems with multiple choices are listed here.

|Platform|Drivers|
|-|-|
|Windows|windib, directx|
|Unix|x11, dga, fbcon, directfb, ggi, vgl, svgalib, aalib|

On some platforms it is possible to embed the pygame display into an already existing window.  
To do this, the environment variable `SDL_WINDOWID` must be set to a string containing the window id or handle.  
The environment variable is checked when the pygame display is initialized.  
Be aware that there can be many strange side effects when running in an embedded display.

It is harmless to call this more than once, repeated calls have no effect.

## .quit()

Uninitialize the display module.  
This will shut down the entire display module.  
This means any active displays will be closed.  
This will also be handled automatically when the program exits.  
It is harmless to call this more than once, repeated calls have no effect.

## .get_init()

```python
get_init() -> bool
```

Returns `True` if the display module has been initialized.

## .set_mode()

Initialize a window or screen for display.

```python
set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
```

The actual created display will be the ***best possible match*** supported by the system.

Note that calling this function implicitly initializes `pygame.display`, if it was not initialized before.

The `size` is a pair of numbers representing the *width* and *height*.  
The `flags` is a collection of additional options.  
The `depth` represents the number of *bits* to use for color.

The returned `Surface` can be drawn to like a regular Surface but changes will eventually be *seen on the monitor*.

If no size is passed or is set to `(0, 0)`, the created Surface will have the same size as the ***current screen resolution***.  
If only the width or height are set to `0`, the Surface will have the same width or height as the screen resolution.

Since pygame 2, the `depth` is ignored, in favour of the best and fastest one. It also raises a *deprecation warning* since pygame-ce 2.4.0 if the passed in depth is not 0 or the one pygame selects.

When requesting fullscreen display modes, sometimes an exact match for the requested size *cannot* be made. In these situations pygame will select *the closest* compatible match.  
The returned surface will still always match the requested size.

On high resolution displays(4k, 1080p) and tiny graphics games (640x480) show up very small so that they are unplayable.  
`pygame.SCALED`(*experimental*) scales up the window for you.  
The game thinks it's a 640x480 window, but really it can be bigger.  
Mouse events are scaled for you, so your game doesn't need to do it.

The `flags` controls which type of display you want. There are several to choose from, and you can even combine multiple types using the *bitwise `or` operator*, (the pipe "`|`" character).  

|Flags|Description|
|-|-|
|pygame.FULLSCREEN|    create a fullscreen display|
|pygame.DOUBLEBUF|     only applicable with `OPENGL`|
|pygame.OPENGL|        create an OpenGL-renderable display|
|pygame.RESIZABLE|     display window should be sizeable|
|pygame.NOFRAME|       display window will have no border or controls|
|pygame.SCALED|        resolution depends on desktop size and scale graphics (*experimental*)|
|pygame.SHOWN|         window is opened in visible mode (*default*)|
|pygame.HIDDEN|        window is opened in hidden mode|

By setting the `vsync` to `1`, it is possible to get a display with vertical sync at a constant frame rate determined by the monitor and graphics drivers.  
Subsequent calls to [pygame.display.flip()](#flip) or [pygame.display.update()](#update) will block (i.e. wait) until the screen has refreshed, in order to prevent "[screen tearing](https://en.wikipedia.org/wiki/Screen_tearing)".

Be careful when using this feature together with [pygame.time.Clock](/doc/time.md/#clock) or [pygame.time.delay()](/doc/time.md/#delay), as multiple forms of waiting and frame rate limiting may interact to cause skipped frames.

The request only works when *graphics acceleration* is available on the system.  
The exact behaviour depends on the hardware and driver configuration.  
When `vsync` is requested, but unavailable, `set_mode()` may raise an ***exception***.

Setting the `vsync` to `-1` in conjunction with `OPENGL` will request the OpenGL-specific feature "[adaptive vsync](https://www.khronos.org/opengl/wiki/Swap_Interval#Adaptive_Vsync)".

```python
flags = pygame.OPENGL | pygame.FULLSCREEN
try:
   window_surface = pygame.display.set_mode((1920, 1080), flags, vsync=1)
   vsync_success=True
except pygame.error:
   window_surface = pygame.display.set_mode((1920, 1080), flags)
   vsync_success=False
```

The `display` index `0` means the ***default*** display is used.  
If `no` display index argument is provided, the default display can be overridden with an *environment* variable.

pygame now ensures that subsequent calls to this function ***clears*** the window to `black`.  

## .get_surface()

Get a reference to the currently set display surface.

```python
get_surface() -> Surface
```

If `no` display mode has been set this will return `None`.

## .flip()

Update the ***entire*** display Surface to the screen.  
When using an `pygame.OPENGL` display mode this will perform a *gl buffer swap*.

## .update()

```python
update(rectangle=None) -> None
update(rectangle_list) -> None
```

Update all, or a portion, of the display. For non-OpenGL displays.

|Parameter|Means|
|-|-|
|display.update(`None`)|***no*** part of the window is updated.|
|display.update()|the ***whole*** window is updated.|

In most applications it is simply more efficient to update the entire display surface at once, it also means you do not need to keep track of a list of rectangles for each call to update.

If passing a sequence of rectangles it is safe to include `None` values in the list, which will be *skipped*.

This call cannot be used on `pygame.OPENGL` displays and will generate an *exception*.

## .get_driver()

```python
get_driver() -> name
```

Get the name of the pygame display backend.  
See the `SDL_VIDEODRIVER` flags in [pygame.display.init()](#init) to see some of the common options.

## .Info()

```python
Info() -> VidInfo
```

Create a video display information object.  

If this is called *before* [pygame.display.set_mode()](#set_mode) some platforms can provide information about the *default* display mode.  
This can also be called after setting the display mode to verify specific display options were satisfied.

The `VidInfo` object has several attributes:

|Attributes|Description|
|-|-|
|hw|1 if the display is hardware accelerated|
|wm|1 if windowed display modes can be used|
|video_mem|The megabytes of video memory on the display. This is `0` if unknown|
|bitsize|Number of bits used to store each pixel|
|bytesize|Number of bytes used to store each pixel|
|masks|Four values used to pack RGBA values into pixels|
|shifts|Four values used to pack RGBA values into pixels|
|losses|Four values used to pack RGBA values into pixels|
|blit_hw|1 if hardware Surface blitting is accelerated|
|blit_hw_CC|1 if hardware Surface colorkey blitting is accelerated|
|blit_hw_A|1 if hardware Surface pixel alpha blitting is accelerated|
|blit_sw|1 if software Surface blitting is accelerated|
|blit_sw_CC|1 if software Surface colorkey blitting is accelerated|
|blit_sw_A|1 if software Surface pixel alpha blitting is accelerated|
|current_h, current_w|Height and width of the current video mode, or of the *desktop* mode if called *before* the `display.set_mode` is called. They are `-1` on *error*.|
|pixel_format|The pixel format of the display Surface as a string. e.g `PIXELFORMAT_RGB888`.|

## .get_wm_info()

```python
get_wm_info() -> dict
```

Get information about the current windowing system.  
Some systems may have no information and an empty dictionary will be returned.  
Most platforms will return a `"window"` key with the value set to the `system id` for the current display.

## .get_desktop_sizes()

Get sizes of active desktops.

```python
get_desktop_sizes() -> list[(int, int)]
```

## .list_modes()

Get list of available ***fullscreen*** modes.

```python
list_modes(depth=0, flags=pygame.FULLSCREEN, display=0) -> list
```

This function returns a list of possible sizes for a specified color depth.  
The return value will be an `empty` list if no display modes are available with the given arguments.  
A return value of `-1` means that any requested size should work (this is likely the case for ***windowed modes***).  
Mode sizes are sorted from biggest to smallest.

If `depth` is `0`, the current/best color depth for the display is used.  
The flags defaults to `pygame.FULLSCREEN`, but you may need to add additional flags for specific fullscreen modes.

The `display` index `0` means the ***default*** display is used.

To find a suitable size for non-fullscreen windows, it is preferable to use [pygame.display.get_desktop_sizes()](#get_desktop_sizes) to get the size of the current desktop, and to then choose a smaller window size.  
This way, the window is guaranteed to fit, even when the monitor is configured to a lower resolution than the maximum supported by the hardware.

To avoid changing the physical monitor resolution, it is also preferable to use [pygame.display.get_desktop_sizes()](#get_desktop_sizes) to determine the fullscreen resolution.

## .mode_ok()

Pick the best color depth for a display mode.

```python
mode_ok(size, flags=0, depth=0, display=0) -> depth
```

It will return `0` if the display mode cannot be set. Otherwise it will return a pixel depth that best matches the display asked for.

## .gl_get_attribute()

Get the value for an OpenGL flag for the current display.

```python
gl_get_attribute(flag) -> value
```

After calling [pygame.display.set_mode()](#set_mode) with the `pygame.OPENGL` flag, it is a good idea to check the value of any requested OpenGL attributes.

## .gl_set_attribute()

Request an OpenGL display attribute for the display mode.

```python
gl_set_attribute(flag, value) -> None
```

When calling [pygame.display.set_mode()](#set_mode) with the `pygame.OPENGL` flag, Pygame automatically handles setting the OpenGL attributes like *color* and *double-buffering*.  
This must be called ***before*** [pygame.display.set_mode()](#set_mode).

The `OPENGL` flags are:

```python
GL_ALPHA_SIZE
GL_DEPTH_SIZE
GL_STENCIL_SIZE
GL_ACCUM_RED_SIZE
GL_ACCUM_GREEN_SIZE
GL_ACCUM_BLUE_SIZE
GL_ACCUM_ALPHA_SIZE
GL_MULTISAMPLEBUFFERS
GL_MULTISAMPLESAMPLES
GL_STEREO
```

**GL_MULTISAMPLEBUFFERS**  
Whether to enable multisampling anti-aliasing. Defaults to `0` (disabled).  
Set `GL_MULTISAMPLESAMPLES` to a value above 0 to control the amount of anti-aliasing. A typical value is 2 or 3.

**GL_STENCIL_SIZE**  
Minimum bit size of the stencil buffer. Defaults to `0`.

**GL_DEPTH_SIZE**  
Minimum bit size of the depth buffer. Defaults to `16`.

**GL_STEREO**  
`1` enables stereo 3D. Defaults to `0`.

**GL_BUFFER_SIZE**  
Minimum bit size of the frame buffer. Defaults to `0`.

Additional attributes:

```python
GL_ACCELERATED_VISUAL
GL_CONTEXT_MAJOR_VERSION, GL_CONTEXT_MINOR_VERSION
GL_CONTEXT_FLAGS, GL_CONTEXT_PROFILE_MASK
GL_SHARE_WITH_CURRENT_CONTEXT
GL_CONTEXT_RELEASE_BEHAVIOR
GL_FRAMEBUFFER_SRGB_CAPABLE
```

**GL_CONTEXT_PROFILE_MASK**  
Sets the OpenGL profile to one of these values:

|||
|-|-|
|GL_CONTEXT_PROFILE_CORE|disable deprecated features|
|GL_CONTEXT_PROFILE_COMPATIBILITY|allow deprecated features|
|GL_CONTEXT_PROFILE_ES|allow only the ES feature subset of OpenGL|

**GL_ACCELERATED_VISUAL**  
Set to `1` to require hardware acceleration, or `0` to force software render. By default, both are allowed.

## .get_active()

```python
get_active() -> bool
```

Returns `True` when the display Surface is considered actively renderable on the screen and may be visible to the user.  
This is the default state immediately after [pygame.display.set_mode()](#set_mode).  
This method may return `True` even if the application is fully hidden behind another application window.

This will return `False` if the display Surface has been `iconified` or `minimized` (either via [pygame.display.iconify()](#iconify) or via an OS specific method such as the minimize-icon available on most desktops).  
Or if the user has multiple virtual desktops and the display Surface is not on the active virtual desktop.

This function returning True is ***unrelated*** to whether the application has ***input focus***.  
Please see [pygame.key.get_focused()][3] and [pygame.mouse.get_focused()][4] for APIs related to input focus.

## .iconify()

```python
iconify() -> bool
```

Request the window for the display surface be iconified or hidden. Not all systems and displays support an iconified display. The function will return *True* if successful.

The event queue should receive an `ACTIVEEVENT` when the window has been iconified. Additionally, the event queue also receives a `WINDOWEVENT_MINIMIZED` when the window has been iconified.

## .toggle_fullscreen()

```python
toggle_fullscreen() -> int
```

Switch between fullscreen and windowed displays.

Supported display drivers:

- windows (Windows)
- x11 (Linux/Unix)
- wayland (Linux/Unix)
- cocoa (OSX/Mac)

This doesn't work on Windows unless the window size is in [pygame.display.list_modes()](#list_modes).  
Or the window is created with the flag `pygame.SCALED`.

## .set_icon()

```python
set_icon(Surface) -> None
```

Sets the runtime icon the system will use to represent the display window.

Most systems want a smaller image around `32x32`.  
The image can have ***colorkey*** transparency which will be passed to the system.

This function can be called ***before*** [pygame.display.set_mode()](#set_mode) to create the icon before the display mode is set.

## .set_caption()

```python
set_caption(title, icontitle=None) -> None
```

Set the current window caption. `icontitle` does nothing.

## .get_caption()

```python
get_caption() -> (title, icontitle)
```

Get the current window caption. These will always be the same value.

## .set_palette()

Set the display color palette for indexed displays.

```python
set_palette(palette=None) -> None
```

This will change the video display color palette for `8-bit` displays.  
This does not change the palette for the actual display Surface, only the palette that is used to display the Surface.  
If *no* palette argument is passed, the system *default* palette will be restored.  
The palette is a sequence of `RGB` triplets.

## .get_num_displays()

```python
get_num_displays() -> int
```

Returns the number of available displays.

## .get_window_size()

```python
get_window_size() -> tuple
```

Returns the size of the window initialized with [pygame.display.set_mode()](#set_mode). This may differ from the size of the display surface if `SCALED` is used.

## .get_allow_screensaver()

Return whether the screensaver is allowed to run.
Default is `False`.

## .set_allow_screensaver()

```python
set_allow_screensaver(bool=True) -> None
```

Change whether screensavers should be allowed whilst the app is running.

If the screensaver has been disallowed due to this function, it will automatically be allowed to run when [pygame.quit()](#quit) is called.

It is possible to influence the default value via the environment variable `SDL_HINT_VIDEO_ALLOW_SCREENSAVER`,  
which can be set to either `0` (disable) or `1` (enable).

## .is_fullscreen()

Returns True if the pygame window created by [pygame.display.set_mode()](#set_mode) is in *full-screen* mode.

```python
is_fullscreen() -> bool
```

Edge cases:  
If the window is in ***windowed mode***, but ***maximized***, this will return ***False***.  
If the window is in ***"borderless fullscreen"*** mode, this will return ***True***.

## .is_vsync()

```python
is_vsync() -> bool
```

Returns True if vertical synchronisation for [pygame.display.flip()](#flip) and [pygame.display.update()](#update) is enabled.

## .get_current_refresh_rate()

Returns the screen refresh rate or `0` if unknown.

```python
get_current_refresh_rate() -> int
```

The screen refresh rate for the current window.  
In windowed mode, this should be equal to the refresh rate of the desktop the window is on.  
If no window is open, an exception is raised.  
When a constant refresh rate cannot be determined, `0` is returned.

## .get_desktop_refresh_rates()

Returns the screen refresh rates for all displays (in windowed mode).

```python
get_desktop_refresh_rates() -> list
```

If the current window is in full-screen mode, the actual refresh rate for that window can differ.  
This is safe to call when no window is open (i.e. before any calls to [pygame.display.set_mode()](#set_mode)).  
When a constant refresh rate cannot be determined, `0` is returned for that desktop.

[1]:https://pyga.me/docs/ref/display.html
[2]:https://pyga.me/docs/ref/event.html
[3]:https://pyga.me/docs/ref/key.html#pygame.key.get_focused
[4]:https://pyga.me/docs/ref/mouse.html#pygame.mouse.get_focused

< End >
