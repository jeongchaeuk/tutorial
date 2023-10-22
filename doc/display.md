
# [pygame.display][1]

Module to control the display window and screen.

Pygame has a single display Surface.  
Once you create the display you treat it as a regular Surface.  
Changes are not immediately visible onscreen; you must choose one of the two **flipping** functions to update the actual display.  
The display is a basic software driven framebuffer.

Pygame can only have a single display active at any time.  
Creating a new one with `pygame.display.set_mode()` will close the previous display.  
To detect the number and size of attached screens, you can use `pygame.display.get_desktop_sizes()` and then select appropriate window size and display index to pass to `pygame.display.set_mode()`.

Use the functions to query detailed information about the display.:

    pygame.display.mode_ok()
    pygame.display.list_modes()
    pygame.display.Info()

If a new display mode is set, the existing Surface will **automatically switch** to operate on the new display.

When the display mode is set, several events are placed on the pygame event queue.  
- `pygame.QUIT` is sent when the user has requested the program to shut down.  
- The window will receive `pygame.ACTIVEEVENT` as the display gains and loses input focus.  
- If the display is set with the `pygame.RESIZABLE` flag, `pygame.VIDEORESIZE` will be sent when the user adjusts the window dimensions.  
- Hardware displays that draw direct to the screen will get `pygame.VIDEOEXPOSE` when portions of the window must be redrawn.
- [more...][2]

### .init()

Initialize the display module.  
This is usually handled for you automatically when you call the higher level `pygame.init()`.  
Before the display module is initialized the environment variable `SDL_VIDEODRIVER` can be set to control which backend is used.  
It is harmless to call this more than once.

### .quit()

Uninitialize the display module.  
This will shut down the entire display module.  
This means any active displays will be closed.  
This will also be handled automatically when the program exits.  
It is harmless to call this more than once.

### .get_init()

Returns **True** if the display module has been initialized.

### .set_mode()

Initialize a window or screen for display.

    set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface

If `no` size is passed or is set to `(0, 0)` and pygame uses SDL version `>= 1.2.10`, the created Surface will have the **same** size as the **current screen resolution**.  
If only the width or height are set to 0, the Surface will have the same width or height as the screen resolution.

It is usually best to `not pass` the depth argument.  
It will default to the best and fastest color depth for the system.

The display flags: (you can combin multiple types with '`|`')

    pygame.FULLSCREEN    create a fullscreen display
    pygame.DOUBLEBUF     only applicable with OPENGL
    pygame.OPENGL        create an OpenGL-renderable display
    pygame.RESIZABLE     display window should be sizeable
    pygame.NOFRAME       display window will have no border or controls
    pygame.SCALED        resolution depends on desktop size and scale graphics
    pygame.SHOWN         window is opened in visible mode (default)
    pygame.HIDDEN        window is opened in hidden mode

By setting the `vsync` parameter to `1`, to get a display with vertical sync, but not guaranteed.  
The request only works at all for calls to set_mode() with the `pygame.OPENGL` or `pygame.SCALED` flags set, and is still not guaranteed even with one of those set.  

    flags = pygame.OPENGL | pygame.FULLSCREEN
    size = (1920, 1080)
    screen = pygame.display.set_mode(size, flags, vsync=1)

The display index `0` means the default display is used.  
If no display index argument is provided, the default display can be overridden with an environment variable.

### .get_surface()

Get a reference to the currently set display surface.
If no display mode has been set this will return `None`.

### .flip()

Update the full display Surface to the screen.  
This will update the contents of the entire display.  
When using an `pygame.OPENGL` display mode this will perform a gl buffer swap.

### .update()

Update portions of the screen for software displays.  
It allows only a portion of the screen to be updated, instead of the entire area.  
If no argument is passed it updates the entire Surface area.

Note that calling `display.update(None)` means `no` part of the window is updated.  
Whereas `display.update()` means the `whole` window is updated.

You can pass the function a single rectangle, or a sequence of rectangles.  
It is more efficient to pass many rectangles at once than to call update multiple times with single or a partial list of rectangles.  
If passing a sequence of rectangles it is safe to include None values in the list, which will be skipped.

This call **cannot** be used on `pygame.OPENGL` displays and will generate an `exception`.

### .get_driver()

Get the name of the pygame display backend.  
See the `SDL_VIDEODRIVER` flags in `pygame.display.set_mode()` to see some of the common options.

### .Info()

Create a video display information object.  
If this is called **before** `pygame.display.set_mode()` some platforms can provide information about the **default** display mode.  
This can also be called after setting the display mode to verify specific display options were satisfied.  
The `VideoInfo` object has several attributes:

    hw:         1 if the display is hardware accelerated
    wm:         1 if windowed display modes can be used
    video_mem:  The megabytes of video memory on the display. This is 0 if
                unknown
    bitsize:    Number of bits used to store each pixel
    bytesize:   Number of bytes used to store each pixel
    masks:      Four values used to pack RGBA values into pixels
    shifts:     Four values used to pack RGBA values into pixels
    losses:     Four values used to pack RGBA values into pixels
    blit_hw:    1 if hardware Surface blitting is accelerated
    blit_hw_CC: 1 if hardware Surface colorkey blitting is accelerated
    blit_hw_A:  1 if hardware Surface pixel alpha blitting is accelerated
    blit_sw:    1 if software Surface blitting is accelerated
    blit_sw_CC: 1 if software Surface colorkey blitting is accelerated
    blit_sw_A:  1 if software Surface pixel alpha blitting is accelerated
    current_h, current_w:  Height and width of the current video mode, or
                of the desktop mode if called before the display.set_mode
                is called. (current_h, current_w are available since
                SDL 1.2.10, and pygame 1.8.0). They are -1 on error, or if
                an old SDL is being used.

### .get_wm_info()

Get information about the current windowing system.  
Most platforms will return a `"window"` key with the value set to the `system id` for the current display.

### .get_desktop_sizes()

Get sizes of active desktops.

### .list_modes()

Get list of available **fullscreen** modes.

    list_modes(depth=0, flags=pygame.FULLSCREEN, display=0) -> list

If depth is `0`, the current/best color depth for the display is used.  
The flags defaults to `pygame.FULLSCREEN`, but you may need to add additional flags for specific fullscreen modes.

The display index `0` means the default display is used.

To find a suitable size for non-fullscreen windows, it is preferable to use `pygame.display.get_desktop_sizes()` to get the size of the current desktop, and to then choose a smaller window size.  
This way, the window is guaranteed to fit, even when the monitor is configured to a lower resolution than the maximum supported by the hardware.

To avoid changing the physical monitor resolution, it is also preferable to use `pygame.display.get_desktop_sizes()` to determine the fullscreen resolution.  
Developers are strongly advised to default to the current physical monitor resolution unless the user explicitly requests a different one (e.g. in an options menu or configuration file).

### .mode_ok()

Pick the best color depth for a display mode.

    mode_ok(size, flags=0, depth=0, display=0) -> depth

It will return `0` if the display mode cannot be set.  
Otherwise it will return a pixel depth that best matches the display asked for.

### .gl_get_attribute()

Get the value for an OpenGL flag for the current display.

After calling `pygame.display.set_mode()` with the `pygame.OPENGL` flag, it is a good idea to check the value of any requested OpenGL attributes.

### .gl_set_attribute()

Request an OpenGL display attribute for the display mode.

When calling `pygame.display.set_mode()` with the `pygame.OPENGL` flag, Pygame automatically handles setting the OpenGL attributes like color and double-buffering.  
This must be called **before** `pygame.display.set_mode()`.

The `OPENGL` flags are:

    GL_ALPHA_SIZE,
    GL_ACCUM_RED_SIZE,
    GL_ACCUM_GREEN_SIZE,
    GL_ACCUM_BLUE_SIZE,
    GL_ACCUM_ALPHA_SIZE,
    GL_MULTISAMPLESAMPLES

**GL_MULTISAMPLEBUFFERS**  
Whether to enable multisampling anti-aliasing.  
Defaults to `0` (disabled).  
Set to a value above 0 to control the amount of anti-aliasing.  
A typical value is 2 or 3.

**GL_STENCIL_SIZE**  
Minimum bit size of the stencil buffer.  
Defaults to `0`.

**GL_DEPTH_SIZE**  
Minimum bit size of the depth buffer.  
Defaults to `16`.

**GL_STEREO**  
1 enables stereo 3D.  
Defaults to `0`.

**GL_BUFFER_SIZE**  
Minimum bit size of the frame buffer.  
Defaults to `0`.

Additional attributes:

    GL_CONTEXT_MAJOR_VERSION, GL_CONTEXT_MINOR_VERSION,
    GL_CONTEXT_FLAGS,
    GL_CONTEXT_PROFILE_MASK,
    GL_SHARE_WITH_CURRENT_CONTEXT,
    GL_CONTEXT_RELEASE_BEHAVIOR,
    GL_FRAMEBUFFER_SRGB_CAPABLE

**GL_CONTEXT_PROFILE_MASK**  
Sets the OpenGL profile to one of these values:

    GL_CONTEXT_PROFILE_CORE
        disable deprecated features
    GL_CONTEXT_PROFILE_COMPATIBILITY
        allow deprecated features
    GL_CONTEXT_PROFILE_ES
        allow only the ES feature
        subset of OpenGL

**GL_ACCELERATED_VISUAL**  
Set to `1` to require hardware acceleration, or `0` to force software render.  
By default, both are allowed.

### .get_active()

Returns `True` when the display Surface is considered actively renderable on the screen and may be visible to the user.  
This is the default state immediately after `pygame.display.set_mode()`.  
This method may return `True` even if the application is fully hidden behind another application window.

This will return `False` if the display Surface has been `iconified` or `minimized` (either via `pygame.display.iconify()` or via an OS specific method such as the minimize-icon available on most desktops).  
Or if the user has multiple virtual desktops and the display Surface is not on the active virtual desktop.

This function returning True is `unrelated` to whether the application has `input focus`. Please see [pygame.key.get_focused()][3] and [pygame.mouse.get_focused()][4] for APIs related to input focus.

### .iconify()

Request the window for the display surface be iconified or hidden.  

The event queue should receive an `ACTIVEEVENT` when the window has been iconified.  
Additionally, the event queue also receives a `WINDOWEVENT_MINIMIZED` when the window has been iconified.

### .toggle_fullscreen()

Switch between fullscreen and windowed displays.

Supported display drivers:

- windows (Windows)
- x11 (Linux/Unix)
- wayland (Linux/Unix)
- cocoa (OSX/Mac)

This doesn't work on Windows unless the window size is in `pygame.display.list_modes()`.  
Or the window is created with the flag `pygame.SCALED`.

### .set_icon()

Change the system image for the display window.

Most systems want a smaller image around `32x32`.  
The image can have `colorkey` transparency which will be passed to the system.

This function can be called **before** `pygame.display.set_mode()` to create the icon before the display mode is set.

### .set_caption()

Set the current window caption.

### .get_caption()

Get the current window caption.

### .set_palette()

Set the display color palette for indexed displays.

This will change the video display color palette for `8-bit` displays.  
This does not change the palette for the actual display Surface, only the palette that is used to display the Surface.  
If no palette argument is passed, the system default palette will be restored.  
The palette is a sequence of `RGB` triplets.

Changed in pygame 2.5.0: Added support for keyword arguments.

### .get_num_displays()

Returns the number of available displays.

### .get_window_size()

Returns the size of the window initialized with `pygame.display.set_mode()`.  
This may differ from the size of the display surface if `SCALED` is used.

### .get_allow_screensaver()

Return whether the screensaver is allowed to run.

Default is `False`.

### .set_allow_screensaver()

Set whether the screensaver may run.

The default value of the argument to the function is `True`.

If the screensaver has been disallowed due to this function,  
it will automatically be allowed to run when `pygame.quit()` is called.

It is possible to influence the default value via the environment variable `SDL_HINT_VIDEO_ALLOW_SCREENSAVER`,  
which can be set to either `0` (disable) or `1` (enable).

[1]:https://www.pygame.org/docs/ref/display.html
[2]:https://www.pygame.org/docs/ref/event.html
[3]:https://www.pygame.org/docs/ref/key.html#pygame.key.get_focused
[4]:https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_focused

< End >
