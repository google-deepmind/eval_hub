Let the equation of the parabola be $f(x,y)=0$.
The parabola is tangent to the line $y=0$ (the $x$-axis) at the point $A(\alpha, 0)$. This means $A(\alpha, 0)$ is on the parabola and the tangent line at $A$ is $y=0$.
The parabola is tangent to the line $x=0$ (the $y$-axis) at the point $B(0, \beta)$. This means $B(0, \beta)$ is on the parabola and the tangent line at $B$ is $x=0$.

Let the tangent lines be $L_1: y=0$ and $L_2: x=0$. The points of tangency are $P_1(\alpha,0)$ and $P_2(0,\beta)$.
The line passing through $P_1$ and $P_2$ is the line segment AB. Its equation is $\frac{x}{\alpha} + \frac{y}{\beta} = 1$, which can be written as $M: \frac{x}{\alpha} + \frac{y}{\beta} - 1 = 0$.

A general theorem states that a conic tangent to two lines $L_1=0$ and $L_2=0$ at points $P_1$ and $P_2$, respectively, has an equation of the form $\lambda L_1 L_2 = (kM)^2$, where $M=0$ is the line passing through $P_1$ and $P_2$, and $\lambda, k$ are constants.

In our case, $L_1 = y$, $L_2 = x$, and $M = \frac{x}{\alpha} + \frac{y}{\beta} - 1$.
The equation of the conic is $\lambda (y)(x) = k^2 \left(\frac{x}{\alpha} + \frac{y}{\beta} - 1\right)^2$.
$\lambda xy = k^2 \left(\frac{x^2}{\alpha^2} + \frac{y^2}{\beta^2} + 1 + \frac{2xy}{\alpha\beta} - \frac{2x}{\alpha} - \frac{2y}{\beta}\right)$.
Rearranging into the general form $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$:
$\frac{k^2}{\alpha^2}x^2 + \left(\frac{2k^2}{\alpha\beta} - \lambda\right)xy + \frac{k^2}{\beta^2}y^2 - \frac{2k^2}{\alpha}x - \frac{2k^2}{\beta}y + k^2 = 0$.

For this conic section to be a parabola, the discriminant $B^2 - 4AC$ must be zero.
$A = \frac{k^2}{\alpha^2}$, $B = \frac{2k^2}{\alpha\beta} - \lambda$, $C = \frac{k^2}{\beta^2}$.
$B^2 - 4AC = \left(\frac{2k^2}{\alpha\beta} - \lambda\right)^2 - 4\left(\frac{k^2}{\alpha^2}\right)\left(\frac{k^2}{\beta^2}\right) = 0$.
$\left(\frac{2k^2}{\alpha\beta} - \lambda\right)^2 - \frac{4k^4}{\alpha^2\beta^2} = 0$.
$\left(\frac{2k^2}{\alpha\beta} - \lambda\right)^2 = \left(\frac{2k^2}{\alpha\beta}\right)^2$.
This implies $\frac{2k^2}{\alpha\beta} - \lambda = \pm \frac{2k^2}{\alpha\beta}$.

Case 1: $\frac{2k^2}{\alpha\beta} - \lambda = \frac{2k^2}{\alpha\beta}$. This gives $\lambda = 0$.
The equation becomes $k^2 \left(\frac{x}{\alpha} + \frac{y}{\beta} - 1\right)^2 = 0$. Assuming $k \neq 0$ (otherwise it's $0=0$), this simplifies to $\frac{x}{\alpha} + \frac{y}{\beta} - 1 = 0$. This is the equation of the line passing through $(\alpha,0)$ and $(0,\beta)$, which is a degenerate parabola. We are looking for a non-degenerate parabola.

Case 2: $\frac{2k^2}{\alpha\beta} - \lambda = -\frac{2k^2}{\alpha\beta}$. This gives $\lambda = \frac{4k^2}{\alpha\beta}$.
Substitute this value of $\lambda$ back into the conic equation $\lambda xy = k^2 \left(\frac{x}{\alpha} + \frac{y}{\beta} - 1\right)^2$.
$\frac{4k^2}{\alpha\beta} xy = k^2 \left(\frac{x}{\alpha} + \frac{y}{\beta} - 1\right)^2$.
Since $k \neq 0$, we can divide by $k^2$:
$\frac{4}{\alpha\beta} xy = \left(\frac{x}{\alpha} + \frac{y}{\beta} - 1\right)^2$.
Expanding the right side:
$\frac{4xy}{\alpha\beta} = \frac{x^2}{\alpha^2} + \frac{y^2}{\beta^2} + 1 + \frac{2xy}{\alpha\beta} - \frac{2x}{\alpha} - \frac{2y}{\beta}$.
Rearranging the terms to put them all on one side:
$\frac{x^2}{\alpha^2} - \frac{2xy}{\alpha\beta} + \frac{y^2}{\beta^2} - \frac{2x}{\alpha} - \frac{2y}{\beta} + 1 = 0$.

This equation can also be written by grouping the quadratic terms:
$\left(\frac{x}{\alpha} - \frac{y}{\beta}\right)^2 - \frac{2x}{\alpha} - \frac{2y}{\beta} + 1 = 0$.

Let's verify this equation represents a parabola tangent to $y=0$ at $(\alpha,0)$ and $x=0$ at $(0,\beta)$.
Let $f(x,y) = \frac{x^2}{\alpha^2} - \frac{2xy}{\alpha\beta} + \frac{y^2}{\beta^2} - \frac{2x}{\alpha} - \frac{2y}{\beta} + 1$.
Point $(\alpha,0)$: $f(\alpha,0) = \frac{\alpha^2}{\alpha^2} - 0 + 0 - \frac{2\alpha}{\alpha} - 0 + 1 = 1 - 2 + 1 = 0$. Point is on the curve.
Point $(0,\beta)$: $f(0,\beta) = 0 - 0 + \frac{\beta^2}{\beta^2} - 0 - \frac{2\beta}{\beta} + 1 = 1 - 2 + 1 = 0$. Point is on the curve.

The gradient vector $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$ is normal to the tangent line.
$\frac{\partial f}{\partial x} = \frac{2x}{\alpha^2} - \frac{2y}{\alpha\beta} - \frac{2}{\alpha}$.
$\frac{\partial f}{\partial y} = -\frac{2x}{\alpha\beta} + \frac{2y}{\beta^2} - \frac{2}{\beta}$.
At $(\alpha,0)$: $\nabla f(\alpha,0) = \left(\frac{2\alpha}{\alpha^2} - 0 - \frac{2}{\alpha}, -\frac{2\alpha}{\alpha\beta} + 0 - \frac{2}{\beta}\right) = \left(\frac{2}{\alpha} - \frac{2}{\alpha}, -\frac{2}{\beta} - \frac{2}{\beta}\right) = \left(0, -\frac{4}{\beta}\right)$.
The normal vector $(0, -4/\beta)$ is parallel to the $y$-axis. The tangent line is perpendicular to this vector, so it's a horizontal line, $y=c$. Since $(\alpha,0)$ is on the tangent, $0=c$. The tangent line is $y=0$.

At $(0,\beta)$: $\nabla f(0,\beta) = \left(0 - \frac{2\beta}{\alpha\beta} - \frac{2}{\alpha}, 0 + \frac{2\beta}{\beta^2} - \frac{2}{\beta}\right) = \left(-\frac{2}{\alpha} - \frac{2}{\alpha}, \frac{2}{\beta} - \frac{2}{\beta}\right) = \left(-\frac{4}{\alpha}, 0\right)$.
The normal vector $(-4/\alpha, 0)$ is parallel to the $x$-axis. The tangent line is perpendicular to this vector, so it's a vertical line, $x=c'$. Since $(0,\beta)$ is on the tangent, $0=c'$. The tangent line is $x=0$.

Both tangency conditions are satisfied. The equation is a parabola (since $B^2-4AC=0$ and it's not degenerate).

Another common form for a parabola tangent to the coordinate axes is $\sqrt{\frac{x}{a}} + \sqrt{\frac{y}{b}} = 1$ for $x,y \ge 0$. Squaring this gives $\frac{x}{a} + \frac{y}{b} + 2\sqrt{\frac{xy}{ab}} = 1$, and squaring again gives $(\frac{x}{a} + \frac{y}{b} - 1)^2 = 4\frac{xy}{ab}$, which expands to $\frac{x^2}{a^2} + \frac{y^2}{b^2} + 1 + \frac{2xy}{ab} - \frac{2x}{a} - \frac{2y}{b} = \frac{4xy}{ab}$. Rearranging gives $\frac{x^2}{a^2} - \frac{2xy}{ab} + \frac{y^2}{b^2} - \frac{2x}{a} - \frac{2y}{b} + 1 = 0$. Comparing this to our derived equation, we see that $a=\alpha$ and $b=\beta$. The equation $\sqrt{x/\alpha} + \sqrt{y/\beta} = 1$ (for $x,y \ge 0$) represents the part of the parabola in the first quadrant. The question asks for "the equation", which usually implies the full algebraic equation of the curve.

The equation is $\frac{x^2}{\alpha^2} - \frac{2xy}{\alpha\beta} + \frac{y^2}{\beta^2} - \frac{2x}{\alpha} - \frac{2y}{\beta} + 1 = 0$.

The final answer is $\boxed{\frac{x^2}{\alpha^2} - \frac{2xy}{\alpha\beta} + \frac{y^2}{\beta^2} - \frac{2x}{\alpha} - \frac{2y}{\beta} + 1 = 0}$.