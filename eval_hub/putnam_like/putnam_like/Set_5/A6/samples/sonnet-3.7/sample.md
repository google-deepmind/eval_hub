# Solution

I'll tackle this step-by-step by finding the circumradius $r(P,Q)$ and then determining its infimum.

## Finding the tangent lines

Let $P = (a, 1/a)$ and $Q = (b, 1/b)$ be two distinct points on the positive branch of the hyperbola $\mathcal{H}$.

The tangent line at a point $(x_0, y_0)$ on the hyperbola $xy = 1$ has the equation:
$$x_0y + xy_0 = 2$$

Therefore:
- The tangent line $k$ at $P = (a, 1/a)$ has equation: $\frac{x}{a} + ay = 2$
- The tangent line $l$ at $Q = (b, 1/b)$ has equation: $\frac{x}{b} + by = 2$

## Finding the intersection point R

To find $R$, I solve the system of equations for the two tangent lines:
$$\frac{x}{a} + ay = 2$$
$$\frac{x}{b} + by = 2$$

Solving this system:
$$y = \frac{2}{b+a}$$
$$x = 2a - \frac{2a^2}{b+a}$$

So $R = (2a - \frac{2a^2}{b+a}, \frac{2}{b+a})$.

## Computing the sides of triangle PQR

For the sides of triangle $PQR$, I compute:

$$|PQ|^2 = (b-a)^2 + (\frac{1}{b}-\frac{1}{a})^2 = (b-a)^2(1 + \frac{1}{a^2b^2})$$

Therefore:
$$|PQ| = |b-a|\sqrt{\frac{a^2b^2+1}{a^2b^2}}$$

Similarly:
$$|PR| = |b-a|\sqrt{\frac{a^4+1}{a^2(b+a)^2}}$$
$$|QR| = |b-a|\sqrt{\frac{b^4+1}{b^2(b+a)^2}}$$

## Finding the area of triangle PQR

Using the shoelace formula:
$$\text{Area}(PQR) = \frac{|b-a|^3}{2ab(b+a)}$$

## Computing the circumradius

The circumradius of a triangle can be calculated using:
$$r = \frac{abc}{4A}$$

where $a$, $b$, $c$ are the side lengths and $A$ is the area.

Substituting our values:
$$r(a,b) = \frac{1}{2ab(b+a)}\sqrt{(a^2b^2+1)(a^4+1)(b^4+1)}$$

## Finding the infimum

Since the points $P$ and $Q$ must be distinct, I'll examine what happens when they get arbitrarily close.

Let $b = a+h$ where $h$ is small. As $h \to 0$:
$$\lim_{h \to 0} r(a,a+h) = \frac{(a^4+1)^{3/2}}{4a^3}$$

To find the minimum value of this expression, I differentiate with respect to $a$ and set it equal to zero:
$$\frac{d}{da}\left[\frac{(a^4+1)^{3/2}}{4a^3}\right] = 0$$

This leads to the equation:
$$3a^{12} + a^8 - 3a^4 - 1 = 0$$

This can be factored as:
$$(a^4-1)(3a^8+1) = 0$$

Since $a > 0$, the only valid solution is $a = 1$.

Evaluating the circumradius at $a = 1$:
$$\inf_{P,Q} r(P,Q) = \frac{(1^4+1)^{3/2}}{4 \cdot 1^3} = \frac{2^{3/2}}{4} = \frac{\sqrt{2}}{2}$$

Therefore, $\inf_{P,Q} r(P,Q) = \frac{\sqrt{2}}{2}$.