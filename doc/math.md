
# [pygame.math][1]

pygame module for vector classes.

The pygame math module currently provides Vector classes in two and three dimensions, Vector2 and Vector3 respectively.

They support the following numerical operations: 

    vec + vec
    vec - vec
    vec * number, number * vec
    vec / number
    vec // number
    vec += vec
    vec -= vec
    vec *= number
    vec /= number
    vec //= number
    round(vec, ndigits=0)

All these operations will be performed **elementwise**.  
In addition `vec * vec` will perform a **scalar-product** (a.k.a. **dot-product**).  
If you want to multiply every element from vector v with every element from vector w you can use the elementwise method: `v.elementwise() * w`

The coordinates of a vector can be retrieved or set using attributes or subscripts.

    v = pygame.Vector3()

    v.x = 5
    v[1] = 2 * v.x
    print(v[1]) # 10

    v.x == v[0]
    v.y == v[1]
    v.z == v[2]

Multiple coordinates can be set using slices or swizzling.

    v = pygame.Vector2()
    v.xy = 1, 2
    v[:] = 1, 2

Allow scalar construction like GLSL.

    Vector2(2) == Vector2(2.0, 2.0)

`pygame.math` import **not** required.  
More convenient `pygame.Vector2` and `pygame.Vector3`.

`round` returns a new vector with components rounded to the specified digits.

### .clamp()

    clamp(value, min, max) -> float

Clamps a numeric value so that it's no lower than min, and no higher than max.

### .lerp()

Interpolates between two values by a weight.

    lerp(a, b, weight) -> float

Linearly interpolates between a and b by weight using the formula **a + (b-a) * weight**.
Raises a **ValueError** if weight is outside the range of [0, 1].

# .Vector2

2-Dimensional Vector.

    Vector2() -> Vector2(0, 0)
    Vector2(int) -> Vector2
    Vector2(float) -> Vector2
    Vector2(Vector2) -> Vector2
    Vector2(x, y) -> Vector2
    Vector2((x, y)) -> Vector2

### .dot()

Calculates the dot- or scalar-product with the other vector.

    dot(Vector2) -> float

### .cross()

    cross(Vector2) -> float

Calculates the third component of the cross-product.

### .magnitude()

Returns the Euclidean magnitude of the vector.
Calculates the magnitude of the vector which follows from the theorem:

    vec.magnitude() == math.sqrt(vec.x**2 + vec.y**2)

### .magnitude_squared()

    vec.magnitude_squared() == vec.x**2 + vec.y**2.

This is **faster** than vec.magnitude() because it avoids the square root.

### .length()

    vec.length() == math.sqrt(vec.x**2 + vec.y**2)

### .length_squared()

    vec.length_squared() == vec.x**2 + vec.y**2.

### .normalize()

Returns a new vector that has **length** equal to **1** and the **same direction** as self.

### .normalize_ip()

Normalizes the vector **in place** so that its length is 1.

### is_normalized()

Tests if the vector is normalized i.e. has **length == 1**.

### scale_to_length()

    scale_to_length(float) -> None

Scales the vector so that it has the given length.  
The direction of the vector is not changed.  
You can also scale to length **0**.  
If the vector is the zero vector (i.e. has length 0 thus no direction) a **ValueError** is raised.

### .reflect()

Returns a vector reflected of a given **normal**.

    reflect(Vector2) -> Vector2

Returns a new vector that points in the direction as if self would bounce of a surface characterized by the given surface normal.  
The length of the new vector is the same as self's.

### reflect_ip()

Reflect the vector of a given normal **in place**.

    reflect_ip(Vector2) -> None

Changes the direction of self as if it would have been reflected of a surface with the given surface normal.

### .distance_to()

Calculates the Euclidean distance to a given vector.

    distance_to(Vector2) -> float

### .distance_squared_to()

Calculates the squared Euclidean distance to a given vector.

    distance_squared_to(Vector2) -> float

### .move_towards()

    move_towards(Vector2, float) -> Vector2

Returns a Vector which is moved towards the given Vector by a given distance and does **not overshoot past** its target Vector.  
The **first** parameter determines the **target Vector**, while the **second** parameter determines the **delta distance**.  
If the **distance** is in the **negatives**, then it will **move away** from the target Vector.

### .move_towards_ip()

    move_towards_ip(Vector2, float) -> None

### .lerp()

    lerp(Vector2, float) -> Vector2

Returns a Vector which is a linear interpolation between self and the given Vector.  
The second parameter determines how far between self and other the result is going to be.  
It must be a value between 0 and 1 where 0 means self and 1 means other will be returned.

### .slerp()

    slerp(Vector2, float) -> Vector2

Calculates the **spherical interpolation** from self to the given Vector.  
The second argument - often called **t** - must be in the range **[-1, 1]**.  
It parametrizes where - in between the two vectors - the result should be.  
If a negative value is given the interpolation will not take the complement of the shortest path.

### .elementwise()

The next operation will be performed elementwise.

    elementwise() -> VectorElementwiseProxy

Applies the following operation to each element of the vector.

### .rotate()

Rotates a vector by a given angle in **degrees**.

    rotate(angle) -> Vector2

Returns a vector which has the same length as self but is rotated **counterclockwise** by the given angle in degrees.  
(Note that due to pygame's **inverted y coordinate system**, the rotation will look clockwise if displayed).

### .rotate_ip()

Rotates the vector by a given angle in degrees **in place**.

### .rotate_rad()

Rotates a vector by a given angle in **radians**.

    rotate_rad(angle) -> Vector2

### .rotate_rad_ip()

Rotates the vector by a given angle in radians **in place**.

### .angle_to()

Calculates the angle to a given vector in **degrees**.

    angle_to(Vector2) -> float

Returns the angle from self to the passed Vector2 that would rotate self to be aligned with the passed Vector2 **without crossing over the negative x-axis**.

![/doc/vector2_angle_to.png](/doc/vector2_angle_to.png)

### .as_polar()

    as_polar() -> (r, phi)

Where `r` is the **radial distance**, and `phi` is the **azimuthal angle**.

### .from_polar()

Creates a Vector2(x, y) or sets x and y from a polar coordinates tuple.

    Vector2.from_polar((r, phi)) -> Vector2
    Vector2().from_polar((r, phi)) -> None

If used from the class creates a Vector2(x,y), else sets x and y.  
The values of x and y are defined from a tuple (r, phi) where `r` is the **radial distance**, and `phi` is the **azimuthal angle**.

### .project()

Projects a vector onto another.

    project(Vector2) -> Vector2

This is useful for **collision detection** in finding the components in a certain direction (e.g. in direction of the wall). [Wikipedia][2].

### .copy()

Returns a new Vector2 having the same dimensions.

### .clamp_magnitude()

Returns a copy of a vector with the magnitude clamped between max_length and min_length.

    clamp_magnitude(max_length) -> Vector2
    clamp_magnitude(min_length, max_length) -> Vector2

This function raises **ValueError** if min_length is greater than max_length, or if either of these values are negative.

### .clamp_magnitude_ip()

    clamp_magnitude_ip(max_length) -> None
    clamp_magnitude_ip(min_length, max_length) -> None

### .update()

Sets the coordinates of the vector.

    update() -> None
    update(int) -> None
    update(float) -> None
    update(Vector2) -> None
    update(x, y) -> None
    update((x, y)) -> None

### .epsilon
Determines the **tolerance** of vector calculations.
Both Vector classes have a value named epsilon that defaults to **1e-6**.  
This value acts as a numerical margin in various methods to account for floating point arithmetic errors.  
Specifically, epsilon is used in the following places:

- comparing Vectors (`==` and `!=`)
- the `is_normalized` method (if the square of the length is within epsilon of 1, it's normalized)
- slerping (a Vector with a length of **< epsilon** is considered a **zero vector**, and can't slerp with that)
- reflection (can't reflect over the zero vector)
- projection (can't project onto the zero vector)
- rotation (only used when rotating by a multiple of 90 degrees)

While it's possible to change epsilon for a specific instance of a Vector, all the other Vectors will retain the default value.  
Changing epsilon on a specific instance however could lead to some asymmetric behavior where symmetry would be expected, such as

    u = pygame.Vector2(0, 1)
    v = pygame.Vector2(0, 1.2)
    u.epsilon = 0.5  # don't set it nearly this large.

    print(u == v)  # True
    print(v == u)  # False

You'll probably never have to change epsilon from the default value, but in rare situations you might find that either the margin is too large or too small, in which case changing epsilon slightly might help you out.

# .Vector3

3-Dimensional Vector.

    Vector3() -> Vector3(0, 0, 0)
    Vector3(int) -> Vector3
    Vector3(float) -> Vector3
    Vector3(Vector3) -> Vector3
    Vector3(x, y, z) -> Vector3
    Vector3((x, y, z)) -> Vector3

### .dot()

Calculates the dot- or scalar-product with the other vector.

    dot(Vector3) -> float

### .cross()

calculates the cross- or vector-product.
    
    cross(Vector3) -> Vector3

### .magnitude()

Returns the Euclidean magnitude of the vector.

    vec.magnitude() == math.sqrt(vec.x**2 + vec.y**2 + vec.z**2)

### .magnitude_squared()

Returns the squared Euclidean magnitude of the vector.

    vec.magnitude_squared() == vec.x**2 + vec.y**2 + vec.z**2.

This is **faster** than vec.magnitude() because it avoids the square root.

### .length()

Returns the Euclidean length of the vector.

    vec.length() == math.sqrt(vec.x**2 + vec.y**2 + vec.z**2)

### .length_squared()

Returns the squared Euclidean length of the vector.

    vec.length_squared() == vec.x**2 + vec.y**2 + vec.z**2.

This is **faster** than vec.length() because it avoids the square root.

### .normalize()

Returns a new vector that has length equal to 1 and the same direction as self.

### .normalize_ip()

Normalizes the vector so that it has length equal to 1.  
The direction of the vector is not changed.

### .is_normalized()

Tests if the vector is normalized i.e. has length == 1.

### .scale_to_length()

    scale_to_length(float) -> None

Scales the vector so that it has the given length.  
The **direction** of the vector is **not** changed.  
You can also scale to length 0.  
If the vector is the zero vector (i.e. has length 0 thus no direction) a **ValueError** is raised.

### .reflect()

    reflect(Vector3) -> Vector3

Returns a new vector that points in the direction as if self would bounce of a surface characterized by the given surface normal.  
The length of the new vector is the same as self's.

### .reflect_ip()

    reflect_ip(Vector3) -> None

### .distance_to()

Calculates the Euclidean distance to a given vector.

    distance_to(Vector3) -> float
 
### .distance_squared_to()

Calculates the squared Euclidean distance to a given vector.

    distance_squared_to(Vector3) -> float

### .move_towards()

    move_towards(Vector3, float) -> Vector3

Returns a Vector which is moved towards the given Vector by a given distance and does not overshoot past its target Vector.  
The `first` parameter determines the **target Vector**, while the `second` parameter determines the **delta distance**.  
If the distance is in the **negatives**, then it will **move away** from the target Vector.

### .move_towards_ip()

    move_towards_ip(Vector3, float) -> None

### .lerp()

    lerp(Vector3, float) -> Vector3

Returns a Vector which is a **linear interpolation** between self and the given Vector.  
The `second` parameter determines **how far** between self an other the result is going to be.  
It must be a value between `0` and `1`, where **0** means **self** and **1** means **other** will be returned.

### .slerp()

    slerp(Vector3, float) -> Vector3

Calculates the spherical interpolation from self to the given Vector.  
The `second` argument - often called **t** - must be in the range **[-1, 1]**.  
It parametrizes where - in between the two vectors - the result should be.  
If a **negative** value is given the interpolation will not take the complement of the shortest path.

### .elementwise()

The next operation will be performed elementwise.

    elementwise() -> VectorElementwiseProxy

### .rotate()

    rotate(degrees, Vector3) -> Vector3

Returns a vector which has the **same length** as self but is rotated **counterclockwise** by the given angle around the given axis.  
(Note that due to **pygame's inverted y coordinate system**, the rotation will look clockwise if displayed).

### .rotate_ip()

    rotate_ip(degrees, Vector3) -> None

### .rotate_rad()

    rotate_rad(radians, Vector3) -> Vector3

### .rotate_rad_ip()

    rotate_rad_ip(radians, Vector3) -> None

### .rotate_x()

Rotates a vector around the **x-axis** by the degrees.

    rotate_x(degrees) -> Vector3

### .rotate_x_ip()

    rotate_x_ip(degrees) -> None

### .rotate_x_rad()

    rotate_x_rad(radians) -> Vector3

### .rotate_x_rad_ip()

    rotate_x_rad_ip(radians) -> None

### .rotate_y()

Rotates a vector around the **y-axis** by the degrees.

    rotate_y(degrees) -> Vector3

### .rotate_y_ip()

    rotate_y_ip(degrees) -> None

### .rotate_y_rad()

    rotate_y_rad(radians) -> Vector3

### .rotate_y_rad_ip()

    rotate_y_rad_ip(radians) -> None

### .rotate_z()

Rotates a vector around the **z-axis** by the degrees.

    rotate_z(degrees) -> Vector3

### .rotate_z_ip()

    rotate_z_ip(degrees) -> None

### .rotate_z_rad()

    rotate_z_rad(radians) -> Vector3

### .rotate_z_rad_ip()

    rotate_z_rad_ip(radians) -> None

### .angle_to()

    angle_to(Vector3) -> float

Returns the angle in **degrees** between self and the given vector.

### .as_spherical()

    as_spherical() -> (r, theta, phi)

Returns a tuple (r, theta, phi) where `r` is the **radial distance**, `theta` is the **inclination angle** and `phi` is the **azimuthal angle**.

### .from_spherical()

Creates a Vector3(x, y, z) or sets x, y and z from a spherical coordinates 3-tuple.

    Vector3.from_spherical((r, theta, phi)) -> Vector3
    Vector3().from_spherical((r, theta, phi)) -> None

### .project()

Projects a vector onto another.

    project(Vector3) -> Vector3

This is useful for **collision detection** in finding the components in a certain direction (e.g. in direction of the wall).

### .copy()

copy() -> Vector3

### .clamp_magnitude()

Returns a copy of a vector with the magnitude clamped between max_length and min_length.

    clamp_magnitude(max_length) -> Vector3
    clamp_magnitude(min_length, max_length) -> Vector3

This function raises **ValueError** if min_length is greater than max_length, or if either of these values are negative.

### .clamp_magnitude_ip()

    clamp_magnitude_ip(max_length) -> None
    clamp_magnitude_ip(min_length, max_length) -> None

### .update()

Sets the coordinates of the vector.

    update() -> None
    update(int) -> None
    update(float) -> None
    update(Vector3) -> None
    update(x, y, z) -> None
    update((x, y, z)) -> None

### .epsilon

Determines the tolerance of vector calculations.
With lengths within this number, vectors are considered equal.

[1]:https://www.pygame.org/docs/ref/math.html
[2]:https://en.wikipedia.org/wiki/Vector_projection

< End >
