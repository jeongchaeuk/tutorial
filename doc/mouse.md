
# [pygame.mouse][1]

pygame module to work with the mouse.

The mouse functions can be used to get the current state of the mouse device.  
These functions can also alter the system cursor for the mouse.

When the display mode is set, the event queue will start receiving mouse events.  
The mouse buttons generate **pygame.MOUSEBUTTONDOWN** and **pygame.MOUSEBUTTONUP** events when they are pressed and released.  
These events contain a button attribute representing which button was pressed.  
The mouse **wheel** will generate **pygame.MOUSEBUTTONDOWN** and **pygame.MOUSEBUTTONUP** events when rolled.  
The button will be set to **4** when the wheel is **rolled up**, and to button **5** when the wheel is **rolled down**.  
Whenever the mouse is moved it generates a **pygame.MOUSEMOTION** event.  
The mouse movement is broken into small and accurate motion events.  
As the mouse is moving many motion events will be placed on the queue.  
Mouse motion events that are not properly cleaned from the event queue are the primary reason the event queue fills up.

#### virtual input mode

If the mouse cursor is **hidden**, and input is **grabbed** to the current display the mouse will enter a **virtual input mode**, where the relative movements of the mouse will never be stopped by the borders of the screen.  
See the functions [pygame.mouse.set_visible()](#set_visible) and [pygame.event.set_grab()](/doc/event.md/#set_grab) to get this configured.

### Mouse Wheel Behavior in pygame 2

There is proper functionality for mouse wheel behaviour with pygame 2 supporting **pygame.MOUSEWHEEL** events.  
The new events support horizontal and vertical scroll movements, with signed integer values representing the amount scrolled (`x` and `y`), as well as `flipped` direction (the set positive and negative values for each axis is flipped).  
Read more about SDL2 input-related changes [here](https://wiki.libsdl.org/MigrationGuide#input) (SDL Migration Guide).

In pygame 2, the mouse wheel functionality can be used by listening for the **pygame.MOUSEWHEEL** type of an event (Bear in mind they still emit **pygame.MOUSEBUTTONDOWN** events like in pygame 1.x, as well).  
When this event is triggered, a developer can access the appropriate **[Event](/doc/event.md)** object with [pygame.event.get()](/doc/event.md/#get).  
The object can be used to access data about the mouse scroll, such as `which` (it will tell you what exact mouse device trigger the event).

``` python
import pygame
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEWHEEL:
                print(event)
                print(event.x, event.y)
                print(event.flipped)
                # print(event.which)  # There is no 'which' attribute!

                # can access properties with proper notation(ex: event.y)
            elif event.type == MOUSEBUTTONDOWN:
                print(event)
    
        clock.tick(60)

# Execute game:
main()
```

### .get_pressed()

Get the state of the mouse buttons.

``` python
get_pressed(num_buttons=3) -> (button1, button2, button3)
get_pressed(num_buttons=5) -> (button1, button2, button3, button4, button5)
```

Returns a sequence of booleans representing the state of **all** the mouse buttons.  
A **True** value means the mouse is currently being **pressed** at the time of the call.

Note, to get all of the mouse events it is better to use either [pygame.event.wait()](/doc/event.md/#wait) or [pygame.event.get()](/doc/event.md/#get) and check all of those events to see if they are **MOUSEBUTTONDOWN**, **MOUSEBUTTONUP**, or **MOUSEMOTION**.

Note, remember to call [pygame.event.get()](/doc/event.md/#get) **before** this function.  
Otherwise it will not work as expected.

To support five button mice, an optional parameter `num_buttons` has been added in pygame 2.  
When this is set to 5, button4 and button5 are added to the returned tuple.  
Only `3` and `5` are **valid** values for this parameter.

### .get_pos()

Get the mouse cursor position.

``` python
get_pos() -> (x, y)
```

The position is **relative** to the **top-left** corner of the display.  
The cursor position can be located outside of the display window, but is always constrained to the screen.

### .get_rel()

Get the amount of mouse movement.

get_rel() -> (x, y)

Returns the amount of movement in `x` and `y` since the **previous call** to this function.  
The relative movement of the mouse cursor is constrained to the edges of the screen, but see the [virtual input mode](#virtual-input-mode) for a way around this.

### .set_pos()

Set the mouse cursor position.

```python
set_pos([x, y]) -> None
```

If the mouse cursor is visible it will jump to the new coordinates.  
Moving the mouse will generate a new **pygame.MOUSEMOTION** event.

### .set_visible()

Hide or show the mouse cursor.

```python
set_visible(bool) -> bool
```

This will return the **previous visible state** of the cursor.

### .get_visible()

Get the current visibility state of the mouse cursor.

### .get_focused()

Check if the display is receiving **mouse input**.  
Returns **True** when pygame is receiving mouse input events (or, in windowing terminology, is "**active**" or has the "**focus**").

This method is most useful when working in a window.  
In **full-screen mode**, this method **always** returns **True**.

Note: under MS Windows, the window that has the mouse focus also has the keyboard focus.  
But under X-Windows, one window can receive mouse events and another receive keyboard events.  
`pygame.mouse.get_focused()` indicates whether the pygame window receives mouse events.

### .set_cursor()

Set the mouse cursor to a new cursor.

```python
set_cursor(pygame.cursors.Cursor) -> None
set_cursor(size, hotspot, xormasks, andmasks) -> None
set_cursor(hotspot, surface) -> None
set_cursor(constant) -> None
```

This function accepts either an explicit **[Cursor][2]** object or arguments to create a **Cursor** object.

See [pygame.cursors.Cursor][2] for help creating cursors and for examples.

### .get_cursor()

```python
get_cursor() -> pygame.cursors.Cursor
```

Get the information about the mouse system cursor.  
The return value contains the same data as the arguments passed into [pygame.mouse.set_cursor()](#set_cursor).

Note: Code that unpacked a `get_cursor()` call into `size`, `hotspot`, `xormasks`, `andmasks` will still work, assuming the call returns an old school type cursor.

[1]:https://www.pygame.org/docs/ref/mouse.html
[2]:/doc/cursors.md/#Cusor

< End >
