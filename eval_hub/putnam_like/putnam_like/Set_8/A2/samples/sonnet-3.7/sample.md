# Solution

I need to find the equation of a parabola with specific tangent lines at given points.

First, I'll establish what we know:
- The parabola is tangent to the line $y=0$ at the point $(\alpha, 0)$
- The parabola is tangent to the line $x=0$ at the point $(0, \beta)$
- We know that $\alpha, \beta > 0$

Let me propose that the parabola has the form:

$$\sqrt{\frac{x}{\alpha}} + \sqrt{\frac{y}{\beta}} = 1$$

I'll verify that this satisfies the given conditions.

## Checking that it passes through the required points:

At $(\alpha, 0)$:
$$\sqrt{\frac{\alpha}{\alpha}} + \sqrt{\frac{0}{\beta}} = 1 + 0 = 1$$

At $(0, \beta)$:
$$\sqrt{\frac{0}{\alpha}} + \sqrt{\frac{\beta}{\beta}} = 0 + 1 = 1$$

So the curve passes through both points.

## Checking the tangent lines:

The partial derivatives of the function $f(x,y) = \sqrt{\frac{x}{\alpha}} + \sqrt{\frac{y}{\beta}} - 1$ are:

$$\frac{\partial f}{\partial x} = \frac{1}{2\alpha\sqrt{\frac{x}{\alpha}}} = \frac{1}{2\sqrt{\alpha x}}$$

$$\frac{\partial f}{\partial y} = \frac{1}{2\beta\sqrt{\frac{y}{\beta}}} = \frac{1}{2\sqrt{\beta y}}$$

At the point $(\alpha, 0)$, $\frac{\partial f}{\partial y}$ approaches infinity as $y$ approaches 0, while $\frac{\partial f}{\partial x}$ has a finite value. This means the tangent line has equation $y = 0$.

Similarly, at the point $(0, \beta)$, $\frac{\partial f}{\partial x}$ approaches infinity as $x$ approaches 0, indicating that the tangent line has equation $x = 0$.

## Verification that it's a parabola:

Let's rearrange the equation:

$$\sqrt{\frac{x}{\alpha}} = 1 - \sqrt{\frac{y}{\beta}}$$

Squaring both sides:
$$\frac{x}{\alpha} = 1 - 2\sqrt{\frac{y}{\beta}} + \frac{y}{\beta}$$

$$x = \alpha - 2\alpha\sqrt{\frac{y}{\beta}} + \frac{\alpha}{\beta}y$$

If we substitute $v = \sqrt{\frac{y}{\beta}}$ (which means $y = \beta v^2$), we get:
$$x = \alpha - 2\alpha v + \alpha v^2 = \alpha(1-v)^2$$

This parametric representation shows that our curve is indeed a parabola.

Therefore, the equation of the parabola is:

$$\boxed{\sqrt{\frac{x}{\alpha}} + \sqrt{\frac{y}{\beta}} = 1}$$