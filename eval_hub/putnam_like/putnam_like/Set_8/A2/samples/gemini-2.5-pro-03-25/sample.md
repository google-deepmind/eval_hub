Solution:

Let the equation of the parabola be given by the general second-degree equation:
$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$
Since it is a parabola, the discriminant must be zero: $B^2 - 4AC = 0$.

We are given two tangent lines and their points of tangency:
1.  The line $y=0$ is tangent to the parabola at the point $P_1 = (\alpha, 0)$.
2.  The line $x=0$ is tangent to the parabola at the point $P_2 = (0, \beta)$.

We can use a known result for the equation of a conic tangent to two lines $u=0$ and $v=0$ at points $P_1$ and $P_2$ respectively. If $w=0$ is the line connecting $P_1$ and $P_2$, the equation of the conic can be written as $uv = k w^2$ for some constant $k$.

In our case:
-   The tangent lines are $y=0$ and $x=0$. So, $u=y$ and $v=x$.
-   The points of tangency are $P_1 = (\alpha, 0)$ and $P_2 = (0, \beta)$.
-   The line $w=0$ passes through $(\alpha, 0)$ and $(0, \beta)$. The slope is $m = \frac{\beta - 0}{0 - \alpha} = -\frac{\beta}{\alpha}$. The equation of the line is $y - 0 = -\frac{\beta}{\alpha}(x - \alpha)$, which simplifies to $\alpha y = -\beta x + \alpha \beta$, or $\beta x + \alpha y - \alpha \beta = 0$. So, $w = \beta x + \alpha y - \alpha \beta$.

The equation of the conic is therefore $xy = k (\beta x + \alpha y - \alpha \beta)^2$ for some constant $k$.
Expanding this equation:
$$xy = k (\beta^2 x^2 + \alpha^2 y^2 + (\alpha \beta)^2 + 2\alpha\beta xy - 2\alpha\beta^2 x - 2\alpha^2\beta y)$$
Rearranging into the general form $A'x^2 + B'xy + C'y^2 + D'x + E'y + F' = 0$:
$$k \beta^2 x^2 + (2k \alpha \beta - 1)xy + k \alpha^2 y^2 - 2k \alpha \beta^2 x - 2k \alpha^2 \beta y + k (\alpha \beta)^2 = 0$$
For this conic to be a parabola, the discriminant $B'^2 - 4A'C'$ must be zero.
$$A' = k \beta^2$$
$$B' = 2k \alpha \beta - 1$$
$$C' = k \alpha^2$$
The condition $B'^2 - 4A'C' = 0$ becomes:
$$(2k \alpha \beta - 1)^2 - 4 (k \beta^2) (k \alpha^2) = 0$$
$$(2k \alpha \beta - 1)^2 - 4k^2 \alpha^2 \beta^2 = 0$$
$$(2k \alpha \beta - 1)^2 - (2k \alpha \beta)^2 = 0$$
This is a difference of squares, $(a-b)(a+b)=0$:
$$[(2k \alpha \beta - 1) - (2k \alpha \beta)] [(2k \alpha \beta - 1) + (2k \alpha \beta)] = 0$$
$$(-1) (4k \alpha \beta - 1) = 0$$
Since $\alpha > 0$ and $\beta > 0$, we must have $4k \alpha \beta - 1 = 0$, which gives $k = \frac{1}{4\alpha\beta}$.

Substitute $k = \frac{1}{4\alpha\beta}$ back into the equation $xy = k (\beta x + \alpha y - \alpha \beta)^2$:
$$xy = \frac{1}{4\alpha\beta} (\beta x + \alpha y - \alpha \beta)^2$$
$$4\alpha\beta xy = (\beta x + \alpha y - \alpha \beta)^2$$
Expand the right side:
$$4\alpha\beta xy = \beta^2 x^2 + \alpha^2 y^2 + (\alpha \beta)^2 + 2\alpha\beta xy - 2\alpha\beta^2 x - 2\alpha^2\beta y$$
Move all terms to one side:
$$\beta^2 x^2 - 2\alpha\beta xy + \alpha^2 y^2 - 2\alpha\beta^2 x - 2\alpha^2\beta y + (\alpha \beta)^2 = 0$$
Notice that the first three terms form a perfect square $(\beta x - \alpha y)^2$.
$$(\beta x - \alpha y)^2 - 2\alpha\beta^2 x - 2\alpha^2\beta y + (\alpha \beta)^2 = 0$$

Alternatively, we can recognize that the parabola tangent to the $x$-axis at $(\alpha, 0)$ and the $y$-axis at $(0, \beta)$ has the equation in the form $\sqrt{\frac{x}{\alpha}} + \sqrt{\frac{y}{\beta}} = 1$, assuming $x, y \ge 0$.
To get the polynomial form, we rearrange and square:
$\sqrt{\frac{y}{\beta}} = 1 - \sqrt{\frac{x}{\alpha}}$
Squaring both sides:
$\frac{y}{\beta} = (1 - \sqrt{\frac{x}{\alpha}})^2 = 1 - 2\sqrt{\frac{x}{\alpha}} + \frac{x}{\alpha}$
Rearrange to isolate the square root term:
$2\sqrt{\frac{x}{\alpha}} = 1 + \frac{x}{\alpha} - \frac{y}{\beta}$
Square both sides again:
$4\frac{x}{\alpha} = (1 + \frac{x}{\alpha} - \frac{y}{\beta})^2$
$4\frac{x}{\alpha} = 1 + (\frac{x}{\alpha})^2 + (\frac{y}{\beta})^2 + 2\frac{x}{\alpha} - 2\frac{y}{\beta} - 2\frac{xy}{\alpha\beta}$
Rearranging gives:
$(\frac{x}{\alpha})^2 - 2\frac{xy}{\alpha\beta} + (\frac{y}{\beta})^2 - 2\frac{x}{\alpha} - 2\frac{y}{\beta} + 1 = 0$
Multiplying by $(\alpha \beta)^2$ to clear denominators:
$\beta^2 x^2 - 2\alpha\beta xy + \alpha^2 y^2 - 2\alpha\beta^2 x - 2\alpha^2\beta y + (\alpha \beta)^2 = 0$
This can be written as:
$(\frac{x}{\alpha} - \frac{y}{\beta})^2 - 2(\frac{x}{\alpha} + \frac{y}{\beta}) + 1 = 0$
Or, as derived earlier:
$(\beta x - \alpha y)^2 - 2\alpha\beta^2 x - 2\alpha^2\beta y + (\alpha \beta)^2 = 0$

Final Answer: The equation of the parabola is
$$ \boxed{(\beta x - \alpha y)^2 - 2\alpha\beta^2 x - 2\alpha^2\beta y + (\alpha \beta)^2 = 0} $$
This can also be written in the equivalent form:
$$ \left(\frac{x}{\alpha} - \frac{y}{\beta}\right)^2 - 2\left(\frac{x}{\alpha} + \frac{y}{\beta}\right) + 1 = 0 $$
Or implicitly derived from:
$$ \sqrt{\frac{x}{\alpha}} + \sqrt{\frac{y}{\beta}} = 1 $$