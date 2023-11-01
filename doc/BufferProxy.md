
# [pygame.BufferProxy][1]

pygame object to export a surface buffer through an array protocol.

```python
BufferProxy(<parent>) -> BufferProxy
```

***BufferProxy*** is a pygame support type, designed as the return value of the [Surface.get_buffer()](/doc/Surface.md/#get_buffer) and [Surface.get_view()](/doc/Surface.md/#get_view) methods.  
For all Python versions a BufferProxy object exports a C struct and Python level array interface on behalf of its parent object's buffer.  
A new buffer interface is also exported.  
In pygame, BufferProxy is key to implementing the [pygame.surfarray](/doc/surfarray.md) module.

BufferProxy instances can be created directly from Python code, either for a `parent` that exports an interface, or from a Python `dict` describing an object's buffer layout.  
The dict entries are based on the Python level array interface mapping.  
The following ***keys*** are recognized:

|Key|Type|Description|
|-|-|-|
|"shape"|tuple|The ***length of each array dimension*** as a tuple of integers.<br>The length of the tuple is the number of dimensions in the array.|
|"typestr"|string|The array element type as a length `3` string.<br>The first character gives byteorder, '`<`' for ***little-endian***, '`>`' for ***big-endian***, and '`\|`' for ***not applicable***.<br>The second character is the element type, '`i`' for ***signed integer***, '`u`' for ***unsigned integer***, '`f`' for **floating point**, and '`V`' for an ***chunk of bytes***.<br>The third character gives the ***bytesize*** of the element, from `'1' to '9'` bytes.<br>For example, "`<u4`" is an ***unsigned 4 byte little-endian integer***, such as a ***32 bit pixel*** on a PC, while "`\|V3`" would represent a ***24 bit pixel***, which has ***no integer equivalent***.|
|"data"|tuple|The ***physical buffer start address*** and a ***read-only flag*** as a length 2 tuple.<br>The address is an `integer` value, while the read-only flag is a `bool` — `False` for ***writable***, `True` for ***read-only***.|
|"strides"|tuple(optional)|Array stride information as a tuple of integers.<br>It is required only of non C-contiguous arrays.<br>The tuple length must match that of "shape".|
|"parent"|object(optional)|The exporting object.<br>It can be used to keep the parent object alive while its buffer is visible.|
|"before"|callable(optional)|Callback invoked ***when*** the BufferProxy instance ***exports*** the buffer.<br>The callback is given one argument, the "`parent`" object if given, otherwise `None`.<br>The callback is useful for ***setting a lock*** on the parent.|
|"after"|callable(optional)|Callback invoked ***when*** an exported buffer is ***released***.<br>The callback is passed one argument, the "`parent`" object if given, otherwise `None`.<br>The callback is useful for ***releasing a lock*** on the parent.|

The BufferProxy class supports subclassing, instance variables, and weak references.

## .parent

Return wrapped exporting object.

```python
parent -> Surface
parent -> <parent>
```

The ***Surface*** which returned the BufferProxy object or the ***object*** passed to a BufferProxy call.

## .length

The size, ***in bytes***, of the exported buffer.

```python
length -> int
```

The number of valid ***bytes*** of data exported.  

For ***discontinuous data***, that is data which is ***not a single block*** of memory, the ***bytes within the gaps*** are ***excluded*** from the count.  
This property is equivalent to the Py_buffer C struct len field.

## .raw

A ***copy*** of the exported buffer as a ***single block of bytes***.

```python
raw -> bytes
```

The buffer data as a `str` or `bytes` object.  
Any ***gaps*** in the exported data are ***removed***.

## .write()

Write raw bytes to object buffer.

```python
write(buffer, offset=0)
```

Overwrite bytes in the parent object's data.  
The data must be ***C or F contiguous***, otherwise a ***ValueError*** is raised.  
Argument `buffer` is a ***'str' or 'bytes' object***.  
An optional `offset` gives a ***start position, in bytes***, within the buffer where overwriting begins.  
If the `offset` is '***< 0***' or '***>= the buffer proxy's length***' value, an ***IndexException*** is raised.  
If '***len(buffer) > proxy.length + offset***', a ***ValueError*** is raised.

[Brief recap on C, Fortran and strided memory layouts][2]

[1]:https://www.pygame.org/docs/ref/bufferproxy.html
[2]:https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html#brief-recap-on-c-fortran-and-strided-memory-layouts

< End >
