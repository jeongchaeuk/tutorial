
# [pygame][1]

the top level pygame package.

[pygame.locals][2]

module that has most of the top-level ***variables*** in pygame.

```python
from pygame.locals import *
```

## .IS_CE

exists if current pygame is pygame-ce

```python
IS_CE = 1
```

Use `getattr(pygame, "IS_CE", False)` to check if current pygame is pygame-ce.

## .init()

Initialize all imported pygame modules.

```python
init() -> (numpass, numfail)
```

*No exceptions will be raised* if a module fails, but the total number if successful and failed inits will be returned as a tuple.  
You may want to initialize the different modules separately to speed up your program or to not use modules your game does not require.

The `init()` functions for individual modules *will raise exceptions* when they fail.

It is safe to call this `init()` more than once as repeated calls will have no effect.

## .quit()

Uninitialize all pygame modules.  
When the Python interpreter shuts down, this method is called regardless, so your program should not need it, except when it wants to terminate its pygame resources and continue.  
It is safe to call this function more than once as repeated calls have no effect.

Note: Calling `pygame.quit()` will not exit your program.  
Consider letting your program end in the same way a normal Python program will end.

## .get_init()

```python
get_init() -> bool
```

Returns `True` if pygame is currently initialized.

## *exception* .error

Standard pygame exception.

```python
raise pygame.error(message)
```

This exception is raised whenever a pygame or SDL operation fails.  
Derived from the `RuntimeError` exception, which can also be used to catch these raised errors.

## .get_error()

Get the current error message.

```python
get_error() -> errorstr
```

`SDL` maintains an internal error message.  
This message will usually be given to you when [pygame.error()](#exception-error) is raised, so this function will rarely be needed.

## .set_error()

Set the current error message.

```python
set_error(error_msg) -> None
```

`SDL` maintains an internal error message.  
This message will usually be given to you when [pygame.error()](#exception-error) is raised, so this function will rarely be needed.

## .get_sdl_version()

Get the version number of SDL.

```python
get_sdl_version(linked=True) -> major, minor, patch
```

`linked=True` will cause the function to return the version of the library that pygame is *linked* against.  
While `linked=False` will cause the function to return the version of the library that pygame is *compiled* against.  
It can be used to detect which features may or may not be available through pygame.

## .get_sdl_byteorder()

Get the byte order of SDL.

```python
get_sdl_byteorder() -> int
```

It returns `1234` for ***little endian*** byte order and `4321` for ***big endian*** byte order.

## .register_quit()

Register a function to be called when pygame quits.

```python
register_quit(callable) -> None
```

When [pygame.quit()](#quit) is called, all registered quit functions are called.  
Pygame modules do this automatically when they are initializing, so this function will rarely be needed.

## .encode_string()

Encode a Unicode or bytes object.

```python
encode_string([obj [, encoding [, errors [, etype]]]]) -> bytes or None
```

`obj`  
If *Unicode*, `encode`;  
if *bytes*, return `unaltered`;  
if anything else, return `None`;  
if not given, raise `SyntaxError`.

`encoding: string`  
If present, encoding to use.  
The default is '`unicode_escape`'.

`errors: string`  
If given, how to handle unencodable characters.  
The default is '`backslashreplace`'.

`etype: exception type`  
If given, the exception type to raise for an encoding error.  
The default is `UnicodeEncodeError`, as returned by `PyUnicode_AsEncodedString()`.  
For the default encoding and errors values there should be no encoding errors.

This function is used in encoding file paths. Keyword arguments are supported.  
This function is not needed for normal pygame-ce usage. (primarily for use in unit tests)

## .encode_file_path()

Encode a Unicode or bytes object as a file system path.

```python
encode_file_path([obj [, etype]]) -> bytes or None
```

`obj`  
If *Unicode*, `encode`;  
if *bytes*, return `unaltered`;  
if anything else, return `None`;  
if not given, raise `SyntaxError`.

`etype: exception type`  
If given, the exception type to raise for an encoding error.  
The default is `UnicodeEncodeError`, as returned by `PyUnicode_AsEncodedString()`.

This function is used to encode file paths in pygame.  
Encoding is to the codec as returned by `sys.getfilesystemencoding()`.  
Keyword arguments are supported.

This function is not needed for normal pygame-ce usage. (primarily for use in unit tests)

## .print_debug_info()

Retrieves useful information for debugging and issue-reporting purposes.

```python
print_debug_info(filename=None) -> None
```

Constructs a string containing details on the system, the python interpreter, the pygame version, and the linked and compiled versions of the libraries that pygame wraps.  
If filename is `None`, then the string is printed into the *console*.  
Otherwise, the debug string is written to the specified file.

Note: If `pygame.freetype` has not been initialized with [pygame.init()](#init) or [pygame.freetype.init()](/doc/freetype.md/#init), then the linked and compiled versions of FreeType will be `"Unk"` since this information is not available before initialization.

## .version

```python
>>> pygame.version.ver
'2.3.2'

>>> pygame.version.vernum
PygameVersion(major=2, minor=3, patch=2)

>>> # All True
>>> pygame.version.vernum.major == pygame.version.vernum[0]
>>> pygame.version.vernum.minor == pygame.version.vernum[1]
>>> pygame.version.vernum.patch == pygame.version.vernum[2]

>>> pygame.version.SDL  
SDLVersion(major=2, minor=26, patch=5)
```

```python
if pygame.version.vernum < (1, 5):
    print(f'Warning, older version of pygame {pygame.version.ver}')
    disable_advanced_features = True
```

# Setting Environment Variables

In python, environment variables are usually set in code like this:  

```python
import os
os.environ['NAME_OF_ENVIRONMENT_VARIABLE'] = 'value_to_set'

import os
os.environ['ENV_VAR'] = os.environ.get('ENV_VAR', 'value')
```

## Windows

```python
> set NAME_OF_ENVIRONMENT_VARIABLE=value_to_set
> python my_application.py
```

## Linux/Mac

```python
> ENV_VAR=value python my_application.py
```

# Pygame Environment Variables

Defined by pygame itself.

> ***PYGAME_DISPLAY*** (Experimental)  
Set index of the display to use, `"0"` is the default.

This sets the display where pygame will open its window or screen.  
The value set here will be used if set before calling `pygame.display.set_mode()`.  
And as long as no 'display' parameter is passed into `pygame.display.set_mode()`.

> ***PYGAME_FORCE_SCALE***  
Set to `"photo"` or `"default"`.

This forces `set_mode()` to use the **SCALED** display mode.  
If `"photo"` is set, makes the scaling use the slowest, but highest quality anisotropic scaling algorithm.  
If it is available, must be set ***before*** calling [pygame.display.set_mode()][4].

> ***PYGAME_BLEND_ALPHA_SDL2***  
Set to `"1"` to enable the SDL2 blitter.

This makes pygame use the SDL2 blitter for all alpha blending.  
It is sometimes faster than the default blitter but uses a different formula so the final colours may differ.  
Must be set ***before*** [pygame.init()](#init).

> ***PYGAME_HIDE_SUPPORT_PROMPT***  
Set to "`1`" to hide the prompt.

This *stops the welcome message* popping up in the console that tells you which version of python, pygame & SDL you are using.  
Must be set *before* importing pygame.

> ***PYGAME_FREETYPE***  
Set to `"1"` to enable.

This switches the `pygame.font` module to a pure freetype implementation that bypasses SDL_ttf.  
Must be set ***before*** importing pygame.

> ***PYGAME_CAMERA***  
Set to "opencv".

Forces the library backend used in the camera module, overriding the platform defaults.  
Must be set *before* calling `pygame.camera.init()`.

# SDL Environment Variables

Defined by SDL.

> ***SDL_VIDEO_CENTERED***  
Set to `"1"` to enable centering the window.

Must be set ***before*** calling [pygame.display.set_mode()][4].

> ***SDL_VIDEO_WINDOW_POS***  
Set to `"x,y"` to position the top left corner of the window.

Must be set ***before*** calling [pygame.display.set_mode()][4].

> ***SDL_VIDEODRIVER***  
Set to `"drivername"` to change the video driver used.

[More info][3]  
Must be set **before** calling [pygame.init()](#init) or [pygame.display.init()](/doc/display.md/#init).

> ***SDL_AUDIODRIVER***  
Set to `"drivername"` to change the audio driver used.

[More info][3]  
Must be set **before** calling [pygame.init()](#init) or [pygame.mixer.init()](/doc/mixer.md/#init).

> ***SDL_VIDEO_ALLOW_SCREENSAVER***  
Set to `"1"` to allow screensavers while pygame apps are running.

By *default* pygame apps ***disable*** screensavers.

> ***SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS***  
Set to `"1"` to allow joysticks to be updated even when the window is out of focus.

By *default*, when the window is not in focus, input devices do not get updated.  
Must be set **before** calling [pygame.init()](#init) or [pygame.joystick.init()](/doc/joystick.md/#init).

> ***SDL_MOUSE_TOUCH_EVENTS***  
Set to `"1"` to make mouse events also generate touch events.

Useful for testing touch events on desktop platforms (e.g. with a trackpad) where this is set to `0` by *default*.

> ***SDL_WINDOWS_DPI_AWARENESS***  
Set to `"permonitorv2"` on ***windows 10 (and later)*** to declare the pygame
window DPI aware and ignore the desktop scaling,  
`"permonitor"` for ***windows 8.1 and later*** DPI awareness and  
`"system"` for ***windows Vista and later*** DPI awareness (not per monitor).  
Finally set it to `"unaware"`, to have the pygame window scale with the desktop scaling.  

This hint only affects the windows platform, other platforms can control DPI awareness via a Window creation keyword parameter called "allow_high_dpi".

[1]:https://pyga.me/docs/ref/pygame.html
[2]:https://pyga.me/docs/ref/locals.html
[3]:https://wiki.libsdl.org/FAQUsingSDL "FAQ: Using SDL"
[4]:/doc/display.md/#set_mode

< End >
