
# [pygame][1]

the top level pygame package.

[pygame.locals][2]  
module that has most of the top-level ***variables*** in pygame.
 
    from pygame.locals import *

### .init()

Initialize all imported pygame modules.  
You may want to initialize the different modules separately to speed up your program or to not use modules your game does not require.  
It is safe to call this init() more than once as repeated calls will have no effect.

### .quit()

Uninitialize all pygame modules.  
When the Python interpreter shuts down, this method is called regardless, so your program should not need it,  
except when it wants to terminate its pygame resources and continue.  
It is safe to call this function more than once as repeated calls have no effect.

### .get_init()

Returns **True** if pygame is currently initialized.

### *exception* .error

This exception is raised whenever a pygame or SDL operation fails.

    raise pygame.error(message)

### .register_quit()

Register a function to be called when pygame quits.

### pygame.version

    >>> pygame.version.ver
    '2.5.2'

    >>> pygame.version.vernum
    PygameVersion(major=2, minor=5, patch=2)

    >>> pygame.version.SDL  
    SDLVersion(major=2, minor=28, patch=3)

# Setting Environment Variables

In python, environment variables are usually set in code like this:  

    import os
    os.environ['NAME_OF_ENVIRONMENT_VARIABLE'] = 'value_to_set'

    import os
    os.environ['ENV_VAR'] = os.environ.get('ENV_VAR', 'value')

### Windows:

    > set NAME_OF_ENVIRONMENT_VARIABLE=value_to_set
    > python my_application.py

### Linux/Mac:

    > ENV_VAR=value python my_application.py

# Pygame Environment Variables

Defined by pygame itself.

> *PYGAME_DISPLAY*  
Set index of the display to use, `"0"` is the default.

This sets the display where pygame will open its window or screen.  
The value set here will be used if set before calling `pygame.display.set_mode()`.  
And as long as no 'display' parameter is passed into `pygame.display.set_mode()`.

> *PYGAME_FORCE_SCALE*  
Set to `"photo"` or `"default"`.

This forces `set_mode()` to use the **SCALED** display mode.  
If `"photo"` is set, makes the scaling use the slowest, but highest quality anisotropic scaling algorithm.  
If it is available, must be set **before** calling `pygame.display.set_mode()`.

> *PYGAME_BLEND_ALPHA_SDL2*  
Set to `"1"` to enable the SDL2 blitter.

This makes pygame use the SDL2 blitter for all alpha blending.  
It is sometimes faster than the default blitter but uses a different formula so the final colours may differ.  
Must be set **before** `pygame.init()`.

> *PYGAME_FREETYPE*  
Set to `"1"` to enable.

This switches the `pygame.font` module to a pure freetype implementation that bypasses SDL_ttf.  
Must be set **before** importing pygame.

# SDL Environment Variables

Defined by SDL.
> *SDL_VIDEO_CENTERED*  
Set to `"1"` to enable centering the window.

Must be set **before** calling `pygame.display.set_mode()`.

> *SDL_VIDEO_WINDOW_POS*  
Set to `"x,y"` to position the top left corner of the window.

Must be set **before** calling `pygame.display.set_mode()`.

> *SDL_VIDEODRIVER*  
Set to `"drivername"` to change the video driver used.

[More info][3]  
Must be set **before** calling `pygame.init()` or `pygame.display.init()`.

> *SDL_AUDIODRIVER*  
Set to `"drivername"` to change the audio driver used.

[More info][3]  
Must be set **before** calling `pygame.init()` or `pygame.mixer.init()`.

> *SDL_VIDEO_ALLOW_SCREENSAVER*  
Set to `"1"` to allow screensavers while pygame apps are running.

By default pygame apps disable screensavers.

> *SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS*  
Set to `"1"` to allow joysticks to be updated even when the window is out of focus.

By default, when the window is not in focus, input devices do not get updated.  
Must be set **before** calling `pygame.init()` or `pygame.joystick.init()`.

[1]:https://www.pygame.org/docs/ref/pygame.html
[2]:https://www.pygame.org/docs/ref/locals.html#module-pygame.locals
[3]:https://wiki.libsdl.org/FAQUsingSDL "FAQ: Using SDL"

< End >
