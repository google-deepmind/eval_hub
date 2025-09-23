Let the equation of the curve be given by $F(x, y) = 7y^2 - 13x^3 - ax^2 = 0$.
The point A shown in the figure is a self-intersection point, also known as a node. A node is a type of singular point on a curve. To find the coordinates of the singular points, we need to find where the partial derivatives of $F(x,y)$ with respect to $x$ and $y$ are both zero.

The partial derivatives are:
$$ \frac{\partial F}{\partial x} = -39x^2 - 2ax = -x(39x + 2a) $$
$$ \frac{\partial F}{\partial y} = 14y $$

Setting the partial derivatives to zero to find the singular points:
1. From $\frac{\partial F}{\partial y} = 14y = 0$, we get $y = 0$.
2. From $\frac{\partial F}{\partial x} = -x(39x + 2a) = 0$, we get $x = 0$ or $x = -\frac{2a}{39}$.

A singular point must also lie on the curve itself. We substitute $y=0$ into the curve's equation:
$7(0)^2 = 13x^3 + ax^2$
$0 = x^2(13x + a)$
This gives solutions $x=0$ or $x = -\frac{a}{13}$.

The coordinates of a singular point must satisfy all these conditions. The point $(0,0)$ satisfies $y=0$ and both conditions for $x$, so it is a singular point. For another singular point to exist, we would need $x = -\frac{2a}{39} = -\frac{a}{13}$, which implies $-2a = -3a$, so $a=0$. If $a=0$, the equation becomes $7y^2 = 13x^3$, which has a cusp at the origin, not a node as shown in the figure. Thus, the only singular point is the origin $(0,0)$, which must be the point A.

To find the slopes of the tangents at the origin, we examine the lowest-degree terms in the equation $7y^2 - ax^2 - 13x^3 = 0$. The lowest-degree terms are $7y^2 - ax^2$. Setting the sum of these terms to zero gives the equation of the tangent lines at the origin:
$$ 7y^2 - ax^2 = 0 $$
$$ 7y^2 = ax^2 $$
This equation can be rewritten as $y^2 = \frac{a}{7}x^2$. This represents two distinct lines passing through the origin, provided $a/7 > 0$:
$$ y = \sqrt{\frac{a}{7}} x \quad \text{and} \quad y = -\sqrt{\frac{a}{7}} x $$
The slopes of these two tangent lines are $m_1 = \sqrt{\frac{a}{7}}$ and $m_2 = -\sqrt{\frac{a}{7}}$.

The problem states that the two tangents are perpendicular. For two lines to be perpendicular, the product of their slopes must be -1.
$$ m_1 \cdot m_2 = -1 $$
$$ \left(\sqrt{\frac{a}{7}}\right) \left(-\sqrt{\frac{a}{7}}\right) = -1 $$
$$ -\frac{a}{7} = -1 $$
Solving for $a$, we find:
$$ a = 7 $$
With $a=7$, the slopes are $m_1=1$ and $m_2=-1$, which correspond to the perpendicular lines $y=x$ and $y=-x$.