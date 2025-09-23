1.  **Determine the equation of the parabola.**
    From the provided image, the parabola has x-intercepts at $x=0$ and $x=-4$. Thus, its equation is of the form $y = kx(x+4)$ for some constant $k$. The vertex of the parabola is labeled as point $C$. The x-coordinate of the vertex is the midpoint of the intercepts, $x_C = \frac{0 + (-4)}{2} = -2$. The image shows the y-coordinate of the vertex is $y_C = 4$. We can use the vertex coordinates to find $k$:
    $4 = k(-2)(-2+4) = k(-2)(2) = -4k$
    This gives $k=-1$. So, the equation of the parabola is $y = -x(x+4) = -x^2 - 4x$. The coordinates of vertex $C$ are $(-2, 4)$.

2.  **Set up the coordinates of the triangle's vertices.**
    The triangle $ABC$ is equilateral, and its side $AB$ is parallel to the x-axis. This means that the altitude from $C$ to $AB$ is a vertical line segment along the axis of symmetry of the parabola, $x=-2$. Let the side length of the triangle be $s$.
    The coordinates of the vertices can be expressed in terms of $s$. Let $M$ be the midpoint of $AB$. Its coordinates are $(-2, y_A)$. The coordinates of $A$ and $B$ are:
    $A = (-2 - s/2, y_A)$
    $B = (-2 + s/2, y_A)$
    The height of the equilateral triangle is $h = \frac{s\sqrt{3}}{2}$. Since $C$ is above $AB$, its y-coordinate is $y_C = y_A + h$. We know $y_C = 4$, so we can express $y_A$ in terms of $s$:
    $y_A = y_C - h = 4 - \frac{s\sqrt{3}}{2}$.

3.  **Solve for the side length $s$.**
    Point $A$ lies on the parabola, so its coordinates must satisfy the parabola's equation $y = -x^2 - 4x$.
    Substitute the coordinates of $A$ into the equation:
    $y_A = -x_A^2 - 4x_A$
    $$4 - \frac{s\sqrt{3}}{2} = -(-2 - s/2)^2 - 4(-2 - s/2)$$
    $$4 - \frac{s\sqrt{3}}{2} = -(4 + 2s + s^2/4) + 8 + 2s$$
    $$4 - \frac{s\sqrt{3}}{2} = -4 - 2s - s^2/4 + 8 + 2s$$
    $$4 - \frac{s\sqrt{3}}{2} = 4 - s^2/4$$
    Subtracting 4 from both sides gives:
    $$-\frac{s\sqrt{3}}{2} = -\frac{s^2}{4}$$
    Since $s \neq 0$ (the triangle has a positive area), we can divide both sides by $-s$:
    $$\frac{\sqrt{3}}{2} = \frac{s}{4}$$
    Solving for $s$, we get:
    $$s = 4 \cdot \frac{\sqrt{3}}{2} = 2\sqrt{3}$$

4.  **Calculate the area of the triangle.**
    The area of an equilateral triangle with side length $s$ is given by the formula $Area = \frac{s^2\sqrt{3}}{4}$.
    $$Area = \frac{(2\sqrt{3})^2\sqrt{3}}{4} = \frac{(4 \cdot 3)\sqrt{3}}{4} = \frac{12\sqrt{3}}{4} = 3\sqrt{3}$$

5.  **Represent the area in the required format and find $a+b$.**
    The problem states that the area can be represented as $\frac{a}{\sqrt{b}}$ for integers $a$ and $b$. We have $Area = 3\sqrt{3}$.
    To match the format, we can multiply the numerator and denominator by $\sqrt{3}$:
    $$3\sqrt{3} = \frac{3\sqrt{3} \cdot \sqrt{3}}{\sqrt{3}} = \frac{3 \cdot 3}{\sqrt{3}} = \frac{9}{\sqrt{3}}$$
    Comparing this with $\frac{a}{\sqrt{b}}$, we find $a=9$ and $b=3$. These are integers as required.

6.  **Calculate the final answer.**
    The problem asks for the value of $a+b$.
    $$a+b = 9 + 3 = 12$$