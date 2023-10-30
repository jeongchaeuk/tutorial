
# [pygame.mixer.music][1]

pygame module for controlling streamed audio.

The music module is closely tied to [pygame.mixer](/doc/mixer.md).  
Use the music module to control the playback of music in the sound mixer.

The music is streamed, and `never` actually loaded `all at once`.  
The mixer system only supports a `single` music stream `at once`.

Consider using `OGG` file format for music as that can give slightly better compression than `MP3` in most cases.

### .load()

```python
load(filename) -> None
load(fileobj, namehint="") -> None
```

This will load a music filename/file object and `prepare` it for playback.  
If a music stream is already `playing` it will be `stopped`.  
This does `not` start the music `playing`.

If you are loading from a file object, the `namehint` parameter can be used to specify the `type` of music data in the object.  
For example: `load(fileobj, "ogg").`

### .unload()

This closes resources like files for any music that may be loaded.

### .play()

```python
play(loops=0, start=0.0, fade_ms=0) -> None
```

This will play the loaded music stream.  
If the music is already playing it will be `restarted`.

`loops` is an optional integer argument, which indicates how many times to `repeat` the music.  
The music repeats `indefinitely` if this argument is set to `-1`.

`start` is an optional float argument, which denotes the `position in time` from which the music starts playing.  
The starting position depends on the format of the music played.  
`MP3` and `OGG` use the position as time in `seconds`.  
For MP3 files the start time position selected may not be accurate as things like variable bit rate encoding and ID3 tags can throw off the timing calculations.  
For `MOD` music it is the `pattern order number`.

Passing a start position will raise a **NotImplementedError** if the start position cannot be set.

`fade_ms` is an optional integer argument, which denotes the period of time (in `milliseconds`) over which the music will fade up from volume level `0.0 to full volume` (or the volume level previously set by [set_volume()](#set_volume)).  
The sample may end before the fade-in is complete.  
If the music is `already` streaming fade_ms is `ignored`.

### .rewind()

Restart music.  
Resets playback of the current music to the beginning.  
If [pause()](#pause) has previously been used to pause the music, the music will `remain paused`.

Note:  
`rewind()` supports a limited number of file types and notably `WAV` files are **NOT** supported.  
For unsupported file types use [play()](#play) which will restart the music that's already playing (note that this will start the music `playing again` even if `previously paused`).

### .stop()

Stops the music playback if it is currently playing.  
`endevent` will be triggered, if set.  
It would `not unload` the music.

### .pause()

Temporarily stop playback of the music stream.  
It can be resumed with the [unpause()](#unpause) function.

### .unpause()

This will `resume` the playback of a music stream after it has been paused.

### .fadeout()

```python
fadeout(time) -> None
```

Fade out and stop the currently playing music.

The `time` argument denotes the integer `milliseconds` for which the fading effect is generated.

Note, that this function `blocks` until the music has faded out.  
Calls to [fadeout()](#fadeout) and [set_volume()](#set_volume) will have `no` effect during this time.  
If an event was set using [set_endevent()](#set_endevent) it will be called after the music has faded.

### .set_volume()

Set the music volume.

```python
set_volume(volume) -> None
```

The `volume` argument is a float between `0.0 and 1.0` that sets the volume level.  
When `new` music is loaded the volume is `reset` to full volume.  
If volume is a `negative` value it will be `ignored` and the volume will remain set at the current level.  
If the `volume` argument is `> 1.0`, the volume will be set to `1.0`.

### .get_volume()

```python
get_volume() -> value
```

Returns the current volume for the mixer.  
The value will be between `0.0 and 1.0`.

### .get_busy()

Check if the music stream is playing.

```python
get_busy() -> bool
```

Returns `True` when the music stream is `actively playing`.  
When the music is `idle` or `paused`, this returns `False`.  

### .set_pos()

Set position to play from.

```python
set_pos(pos) -> None
```

This sets the position in the music file where playback will `start`.  
The meaning of "`pos`", a `float` (or a number that can be converted to a float), depends on the music format.

For `MOD` files, pos is the `integer pattern number` in the module.  
For `OGG` it is the **absolute** position, in `seconds`, from the **beginning** of the sound.  
For `MP3` files, it is the **relative** position, in `seconds`, from the **current** position.  
For **absolute** positioning in an `MP3` file, first call [rewind()](#rewind).

Other file formats are unsupported.  
Newer versions of **SDL_mixer** have better positioning support than earlier ones.  
An **SDLError** is raised if a particular format does `not support` positioning.

Function `set_pos()` calls underlining SDL_mixer function `Mix_SetMusicPosition`.

### .get_pos()

Get the music play time.

```python
get_pos() -> time
```

This gets the number of `milliseconds` that the music has been playing for.  
The returned time only represents `how long` the music has been `playing`;  
it does `not` take into account any `starting position offsets`.

### .music.queue()

Queue a sound file to follow the current.

```python
queue(filename) -> None
queue(fileobj, namehint="", loops=0) -> None
```

This will `load` a sound file and `queue` it.  
A queued sound file will begin as soon as the current sound naturally ends.  
Only `one` sound can be queued at a time.  
Queuing a new sound while another sound is queued will result in the new sound becoming the queued sound.  
Also, if the current sound is ever `stopped` or `changed`, the queued sound will be `lost`.

If you are loading from a `file object`, the `namehint` parameter can be used to specify the type of music data in the object. For example: queue(fileobj, `"ogg"`).

The following example will play music by Bach six times, then play music by Mozart once:

```python
pygame.mixer.music.load('bach.ogg')
pygame.mixer.music.play(5)        # Plays six times, not five!
pygame.mixer.music.queue('mozart.ogg')
```

### .set_endevent()

Have the music send an event when playback `stops`.

```python
set_endevent() -> None
set_endevent(type) -> None
```

This causes pygame to signal (by means of the event queue) when the music is done playing.  
The argument determines the type of event that will be queued.

The event will be queued `every time` the music finishes, not just the first time.  
To `stop` the event from being queued, call this method with `no` argument.

### .get_endevent()

Get the event a channel sends when playback stops.

```python
get_endevent() -> type
```

Returns the event type to be sent every time the music finishes playback.  
If there is `no` endevent the function returns **pygame.NOEVENT**.

[1]:https://www.pygame.org/docs/ref/music.html

< End >
