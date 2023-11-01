
# [pygame.Rect][1]

pygame object for storing rectangular coordinates.

    Rect(left, top, width, height) -> Rect
    Rect((left, top), (width, height)) -> Rect
    Rect(object) -> Rect

Pygame uses `Rect` objects to store and manipulate rectangular areas.  
A Rect can be created from a combination of left, top, width, and height values.  
Rects can also be created from Python objects that are already a Rect or have an attribute named "rect".

The Rect object has several **virtual attributes** which can be used to move and align the Rect:

    x, y
    top, left, bottom, right
    topleft, bottomleft, topright, bottomright
    midtop, midleft, midbottom, midright
    center, centerx, centery
    size, width, height
    w, h

All of these attributes can be assigned to:

    rect1.right = 10
    rect2.center = (20,30)

Assigning to **size**, **width** or **height** `changes` the dimensions of the rectangle; all other assignments `move` the rectangle without resizing it.

If a Rect has a nonzero width or height, it will return `True` for a nonzero test.  
Some methods return a Rect with 0 size to represent an invalid rectangle.  
A Rect with a `0 size` will `not collide` when using collision detection methods.

The coordinates for Rect objects are all `integers`.  

The area covered by a Rect does `not` **include the right- and bottom-most edge of pixels**.  

The Rect object is also `iterable`:

    r = Rect(0, 1, 2, 3)
    x, y, w, h = r

### .copy()

Copy the rectangle

Returns a new rectangle having the same position and size as the original.

### .move()

Moves the rectangle.

    move(x, y) -> Rect

The x and y arguments can be any integer value, positive or negative.

### .move_ip()

Moves the rectangle, in place

### .inflate()

Grow or shrink the rectangle size.

    inflate(x, y) -> Rect

The rectangle remains centered around its current center.  
Negative values will shrink the rectangle. Note, uses integers, if the offset given is too small (-2 < offset < 2), center will be off.

### .inflate_ip()

Grow or shrink the rectangle size, in place.

### .scale_by()

Scale the rectangle by given a multiplier.

    scale_by(scalar) -> Rect
    scale_by(scalex, scaley) -> Rect

The rectangle remains centered around its current center.  

### .scale_by_ip()

Grow or shrink the rectangle size, in place.

### .update()

Sets the position and size of the rectangle, in place.

### .clamp()

`Moves` the rectangle inside another

    clamp(Rect) -> Rect

Returns a new rectangle that is moved to be completely inside the argument Rect.  
If the rectangle is `too large` to fit inside, it is `centered` inside the argument Rect, but its **size** is `not changed`.

### .clamp_ip()

`Moves` the rectangle inside another, in place.

### .clip()

`Crops` a rectangle inside another.

    clip(Rect) -> Rect

Returns a new rectangle that is cropped to be completely inside the argument Rect.  
If the two rectangles do `not overlap` to begin with, a Rect with `0 size` is returned.

### .clipline()

Returns the coordinates of a line that is cropped to be completely inside the rectangle.  
If the line does `not overlap` the rectangle, then an `empty tuple` is returned.

The line to crop can be any of the following formats (floats can be used in place of ints, but they will be truncated):

- four ints
- 2 lists/tuples/Vector2s of 2 ints
- a list/tuple of four ints
- a list/tuple of 2 lists/tuples/Vector2s of 2 ints

**Return type**  
tuple(tuple(int, int), tuple(int, int)) or ()

**Raises**  
`TypeError`: if the line coordinates are not given as one of the above described line formats

This method can be used for **collision detection** between a rect and a line.  
The `rect.bottom` and `rect.right` attributes of a `pygame.Rect` always lie one pixel outside of its actual border.

### .union()

Returns a new rectangle that completely covers the area of the two provided rectangles.

### .union_ip()

### .unionall()

    unionall(Rect_sequence) -> Rect

### .unionall_ip()

### .fit()

Resize and move a rectangle with `aspect ratio`.

    fit(Rect) -> Rect

The `aspect ratio of the original` Rect is **preserved**, so the new rectangle may be smaller than the target in either width or height.

### .normalize()

Correct negative sizes, in place.

The rectangle will remain in the same place, with only the sides swapped.

### .contains()

Test if one rectangle is completely inside another.

### .collidepoint()

Test if a point is inside a rectangle.

```python
collidepoint(x, y) -> bool
collidepoint((x,y)) -> bool
```

A point along the ***right or bottom edge*** is `not` ***considered*** to be inside the rectangle.

### .colliderect()

Test if two rectangles `overlap`.

### .collidelist()

    collidelist(list) -> index

Test whether the rectangle collides with any in a sequence of rectangles.  
The index of the `first` collision found is returned.  
If `no` collisions are found an index of `-1` is returned.

### .collidelistall()

    collidelistall(list) -> indices

Returns a list of all the indices that contain rectangles that collide with the Rect.  
If `no` intersecting rectangles are found, an `empty` list is returned.

Not only Rects are valid arguments, but these are all valid calls:

    Rect = pygame.Rect
    r = Rect(0, 0, 10, 10)

    list_of_rects = [Rect(1, 1, 1, 1), Rect(2, 2, 2, 2)]
    indices0 = r.collidelistall(list_of_rects)

    list_of_lists = [[1, 1, 1, 1], [2, 2, 2, 2]]
    indices1 = r.collidelistall(list_of_lists)

    list_of_tuples = [(1, 1, 1, 1), (2, 2, 2, 2)]
    indices2 = r.collidelistall(list_of_tuples)

    list_of_double_tuples = [((1, 1), (1, 1)), ((2, 2), (2, 2))]
    indices3 = r.collidelistall(list_of_double_tuples)

    class ObjectWithRectAttribute(object):
        def __init__(self, r):
            self.rect = r

    list_of_object_with_rect_attribute = [
        ObjectWithRectAttribute(Rect(1, 1, 1, 1)),
        ObjectWithRectAttribute(Rect(2, 2, 2, 2)),
    ]
    indices4 = r.collidelistall(list_of_object_with_rect_attribute)

    class ObjectWithCallableRectAttribute(object):
        def __init__(self, r):
            self._rect = r

        def rect(self):
            return self._rect

    list_of_object_with_callable_rect = [
        ObjectWithCallableRectAttribute(Rect(1, 1, 1, 1)),
        ObjectWithCallableRectAttribute(Rect(2, 2, 2, 2)),
    ]
    indices5 = r.collidelistall(list_of_object_with_callable_rect)

### .collideobjects()

Test if any object in a list intersects.

    collideobjects(rect_list) -> object
    collideobjects(obj_list, key=func) -> object

Test whether the rectangle collides with any object in the sequence.  
The object of the `first` collision found is returned.  
If `no` collisions are found then `None` is returned.

If `key` is given, then it should be a method taking an object from the list as input and returning a `rect like object`.  

    key=lambda obj: obj.rectangle

If an object has multiple attributes of type Rect then key could return one of them.

    r = Rect(1, 1, 10, 10)

    rects = [
        Rect(1, 1, 10, 10),
        Rect(5, 5, 10, 10),
        Rect(15, 15, 1, 1),
        Rect(2, 2, 1, 1),
    ]

    result = r.collideobjects(rects)  # -> <rect(1, 1, 10, 10)>
    print(result)

    class ObjectWithSomRectAttribute:
        def __init__(self, name, collision_box, draw_rect):
            self.name = name
            self.draw_rect = draw_rect
            self.collision_box = collision_box

        def __repr__(self):
            return f'<{self.__class__.__name__}("{self.name}", {list(self.collision_box)}, {list(self.draw_rect)})>'

    objects = [
        ObjectWithSomRectAttribute("A", Rect(15, 15, 1, 1), Rect(150, 150, 50, 50)),
        ObjectWithSomRectAttribute("B", Rect(1, 1, 10, 10), Rect(300, 300, 50, 50)),
        ObjectWithSomRectAttribute("C", Rect(5, 5, 10, 10), Rect(200, 500, 50, 50)),
    ]

    # this does not work because the items in the list are no Rect like object
    # collision = r.collideobjects(objects)

    collision = r.collideobjects(
        objects, key=lambda o: o.collision_box
    )  # -> <ObjectWithSomRectAttribute("B", [1, 1, 10, 10], [300, 300, 50, 50])>
    print(collision)

    screen_rect = r.collideobjects(objects, key=lambda o: o.draw_rect)  # -> None
    print(screen_rect)

### .collideobjectsall()

Test if all objects in a list intersect.

    collideobjectsall(rect_list) -> objects
    collideobjectsall(obj_list, key=func) -> objects

Returns a list of all the objects that contain rectangles that collide with the Rect.  
If `no` intersecting objects are found, an `empty` list is returned.

If key is given, then it should be a method taking an object from the list as input and returning a rect like object e.g. lambda obj: obj.rectangle. If an object has multiple attributes of type Rect then key could return one of them.

    r = Rect(1, 1, 10, 10)

    rects = [
        Rect(1, 1, 10, 10),
        Rect(5, 5, 10, 10),
        Rect(15, 15, 1, 1),
        Rect(2, 2, 1, 1),
    ]

    result = r.collideobjectsall(
        rects
    )  # -> [<rect(1, 1, 10, 10)>, <rect(5, 5, 10, 10)>, <rect(2, 2, 1, 1)>]
    print(result)

    class ObjectWithSomRectAttribute:
        def __init__(self, name, collision_box, draw_rect):
            self.name = name
            self.draw_rect = draw_rect
            self.collision_box = collision_box

        def __repr__(self):
            return f'<{self.__class__.__name__}("{self.name}", {list(self.collision_box)}, {list(self.draw_rect)})>'

    objects = [
        ObjectWithSomRectAttribute("A", Rect(1, 1, 10, 10), Rect(300, 300, 50, 50)),
        ObjectWithSomRectAttribute("B", Rect(5, 5, 10, 10), Rect(200, 500, 50, 50)),
        ObjectWithSomRectAttribute("C", Rect(15, 15, 1, 1), Rect(150, 150, 50, 50)),
    ]

    # this does not work because ObjectWithSomRectAttribute is not a Rect like object
    # collisions = r.collideobjectsall(objects)

    collisions = r.collideobjectsall(
        objects, key=lambda o: o.collision_box
    )  # -> [<ObjectWithSomRectAttribute("A", [1, 1, 10, 10], [300, 300, 50, 50])>, <ObjectWithSomRectAttribute("B", [5, 5, 10, 10], [200, 500, 50, 50])>]
    print(collisions)

    screen_rects = r.collideobjectsall(objects, key=lambda o: o.draw_rect)  # -> []
    print(screen_rects)

### .collidedict()

Test if one rectangle in a dictionary intersects.

    collidedict(dict) -> (key, value)
    collidedict(dict) -> None
    collidedict(dict, use_values=0) -> (key, value)
    collidedict(dict, use_values=0) -> None

Returns the `first` key and value pair that intersects with the calling Rect object.  
If `no` collisions are found, `None` is returned.  
If `use_values` is `0` then the dict's `keys` will be used in the collision detection, otherwise the dict's `values` will be used.

Rect objects cannot be used as keys in a dictionary, so they must be `converted to a tuple`.

    rect.collidedict({tuple(key_rect) : value})

### .collidedictall()

    collidedictall(dict) -> [(key, value), ...]
    collidedictall(dict, use_values=0) -> [(key, value), ...]

[1]:https://www.pygame.org/docs/ref/rect.html

< End >
