
# [pygame.time][1]

pygame module for monitoring time.

Times in pygame are represented in ***milliseconds*** (`1/1000` seconds).  
Most platforms have a limited time resolution of around 10 milliseconds.  
This resolution, in milliseconds, is given in the ***TIMER_RESOLUTION*** constant.

## .get_ticks()

Return the number of milliseconds since [pygame.init()](/doc/pygame.md/#init) was called.  
Before pygame is initialized this will always be `0`.

## .wait()

Pause the program for an amount of time.

```python
wait(milliseconds) -> time
```

This function `sleeps` the process to share the processor with other programs.  
A program that waits for even a few milliseconds will consume very little processor time.  
This returns the actual number of milliseconds used.

## .delay()

Pause the program for an amount of time.

```python
delay(milliseconds) -> time
```

This function will use the processor (rather than sleeping) in order to make the delay `more accurate` than `pygame.time.wait()`.  
This returns the actual number of milliseconds used.

## .set_timer()

```python
set_timer(event, millis) -> None
set_timer(event, millis, loops=0) -> None
```

Set an event to appear on the event queue every given number of ***milliseconds***.  
The first event will not appear until the amount of time has passed.

The `event` attribute can be a [pygame.event.Event](/doc/event.md) object or an `integer type` that denotes an event.

`loops` is an **integer** that denotes ***the number of events*** posted.  
If `0` then the events will `keep` getting posted, unless explicitly stopped.

```python
set_timer(event, millis=0)  # disable event.
```

There cannot be two timers for the same event type.  
Setting an event timer for a particular event discards the old one for that event type.

# .Clock

Creates a new Clock object that can be used to track an amount of time.  
The clock also provides several functions to help control a game's ***framerate***.

## .tick()

Update the clock.

```python
tick(framerate=0) -> milliseconds
```

This method should be called once per frame.  
It will compute how many milliseconds have passed since the previous call.

If you pass the optional framerate argument the function will delay to keep the game running slower than the given ticks per second.  
This can be used to help limit the runtime speed of a game.  
By calling Clock.tick(40) once per frame, the program will never run at more than 40 frames per second.

Note that this function uses ***SDL_Delay*** function which is not accurate on every platform, but does not use much CPU.  
Use [tick_busy_loop](#tick_busy_loop) if you want an accurate timer, and don't mind chewing CPU.

## .tick_busy_loop()

Update the clock.

```python
tick_busy_loop(framerate=0) -> milliseconds
```

This method should be called once per frame.  
It will compute how many milliseconds have passed since the previous call.

If you pass the optional framerate argument the function will delay to keep the game running slower than the given ticks per second.  
This can be used to help limit the runtime speed of a game.  
By calling Clock.tick_busy_loop(40) once per frame, the program will never run at more than 40 frames per second.

Not that this function uses [pygame.time.delay()](#delay), which uses lots of CPU in a busy loop to make sure that timing is more accurate.

## .get_time()

Time used in the previous tick.

```python
get_time() -> milliseconds
```

The number of milliseconds that passed between the previous two calls to [Clock.tick()](#tick).

## .get_rawtime()

Actual time used in the previous tick.

```python
get_rawtime() -> milliseconds
```

Similar to [Clock.get_time()](#get_time), but does not include any time used while [Clock.tick()](#tick) was delaying to limit the framerate.

## .get_fps()

```python
get_fps() -> float
```

Compute your game's framerate in frames per second.  
It is computed by averaging ***the last ten*** call to [Clock.tick()](#tick).

[1]:https://www.pygame.org/docs/ref/time.html

< End >
