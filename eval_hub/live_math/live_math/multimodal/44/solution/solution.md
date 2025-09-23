Let the equilateral triangle have side length $a$. The interior angles are all $60°$.
At the $n$-th step, the circles are arranged in rows. The bottom row has $n$ circles, the row above it has $n-1$ circles, and so on, up to a single circle at the top. The total number of circles is the sum of the first $n$ integers, which is the $n$-th triangular number, $N_n = 1 + 2 + \dots + n = \frac{n(n+1)}{2}$.
All circles at the $n$-th step are congruent. Let their radius be $r_n$.

To find $r_n$, we analyze the geometry of the bottom row of $n$ circles. Let the base of the triangle lie on the x-axis. The centers of these $n$ circles are collinear and their y-coordinate is $r_n$. The horizontal distance between the centers of two adjacent tangent circles is $2r_n$.
The total horizontal distance spanned by the centers of the $n$ circles from the center of the first circle to the center of the last one is $(n-1) \times 2r_n = (2n-2)r_n$.

Now, consider the space between the leftmost circle and the left vertex of the triangle. The side of the triangle makes a $60°$ angle with the base. Let's draw a right-angled triangle formed by the center of the leftmost circle, its projection on the base, and the left vertex of the equilateral triangle. The line connecting the vertex to the circle's center bisects the $60°$ angle, so we have a $30°$ angle in our right triangle. The side opposite to this angle is the radius $r_n$. The adjacent side is the horizontal distance from the vertex to the point of tangency of the circle with the base, let's call this distance $d$.
We have $\tan(30°) = \frac{\text{opposite}}{\text{adjacent}} = \frac{r_n}{d}$.
So, $d = \frac{r_n}{\tan(30°)} = \frac{r_n}{1/\sqrt{3}} = r_n\sqrt{3}$.

The total length of the base $a$ is the sum of the horizontal distance from the left vertex to the center of the first circle, the distance between the centers of the first and last circles, and the horizontal distance from the center of the last circle to the right vertex. By symmetry, the distance at the right end is also $d$.
So, $a = d + (2n-2)r_n + d = 2d + (2n-2)r_n$.
Substituting the expression for $d$:
$$a = 2(r_n\sqrt{3}) + (2n-2)r_n = r_n(2\sqrt{3} + 2n - 2)$$
Solving for $r_n$, we get:
$$r_n = \frac{a}{2n - 2 + 2\sqrt{3}}$$

The total area of all circles at step $n$, $S_n$, is the number of circles times the area of one circle:
$$S_n = N_n \cdot \pi r_n^2 = \frac{n(n+1)}{2} \pi \left(\frac{a}{2n - 2 + 2\sqrt{3}}\right)^2$$
We need to find the limit $A = \lim_{n\to \infty} \frac{S_n}{a^2}$.
$$A = \lim_{n\to \infty} \frac{1}{a^2} \left[ \frac{n(n+1)}{2} \pi \frac{a^2}{(2n - 2 + 2\sqrt{3})^2} \right]$$
The $a^2$ terms cancel:
$$A = \lim_{n\to \infty} \frac{\pi}{2} \frac{n(n+1)}{(2n - 2 + 2\sqrt{3})^2} = \lim_{n\to \infty} \frac{\pi}{2} \frac{n^2+n}{(2n - (2-2\sqrt{3}))^2}$$
To evaluate the limit as $n \to \infty$, we consider the highest power of $n$ in the numerator and the denominator.
The numerator is a polynomial in $n$ of degree 2, with leading term $\frac{\pi}{2}n^2$.
The denominator is also a polynomial in $n$ of degree 2. The leading term is $(2n)^2 = 4n^2$.
$$A = \lim_{n\to \infty} \frac{\frac{\pi}{2}n^2 + O(n)}{4n^2 + O(n)} = \frac{\pi/2}{4} = \frac{\pi}{8}$$
The problem asks for $10000A$ rounded to the nearest integer.
$$10000A = 10000 \times \frac{\pi}{8} = 1250\pi$$
Using the value of $\pi \approx 3.14159265$:
$$1250 \times 3.14159265 \approx 3926.9908$$
Rounding to the nearest integer, we get 3927.