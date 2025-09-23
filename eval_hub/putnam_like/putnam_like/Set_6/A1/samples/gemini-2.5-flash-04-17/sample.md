Let the given cubic polynomial be $P(x) = x^3 + a x^2 + b x + c$. The roots of this polynomial are $\alpha,$ $\beta,$ and $\gamma$.
According to Vieta's formulas, the following relationships hold between the roots and the coefficients:
$\alpha + \beta + \gamma = -a$
$\alpha \beta + \beta \gamma + \gamma \alpha = b$
$\alpha \beta \gamma = -c$

We are looking for a new cubic polynomial, let's call it $Q(y)$, whose roots are $\alpha^2,$ $\beta^2,$ and $\gamma^2$. Let this polynomial be $Q(y) = y^3 + Ay^2 + By + C = 0$.
Using Vieta's formulas for the polynomial $Q(y)$, the coefficients $A, B, C$ are related to the roots $\alpha^2, \beta^2, \gamma^2$ as follows:
$A = -(\alpha^2 + \beta^2 + \gamma^2)$
$B = \alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2$
$C = -(\alpha^2 \beta^2 \gamma^2)$

We need to express $A, B, C$ in terms of $a, b, c$.

First, let's find the sum of the squares of the roots:
$\alpha^2 + \beta^2 + \gamma^2 = (\alpha + \beta + \gamma)^2 - 2(\alpha \beta + \beta \gamma + \gamma \alpha)$
Substituting the expressions from the original Vieta's formulas:
$\alpha^2 + \beta^2 + \gamma^2 = (-a)^2 - 2(b) = a^2 - 2b$
So, the coefficient $A$ is:
$A = -(\alpha^2 + \beta^2 + \gamma^2) = -(a^2 - 2b) = 2b - a^2$

Next, let's find the sum of the pairwise products of the squares of the roots:
$\alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2 = (\alpha \beta)^2 + (\beta \gamma)^2 + (\gamma \alpha)^2$
We can express this using the identity $u^2 + v^2 + w^2 = (u+v+w)^2 - 2(uv+vw+wu)$. Let $u = \alpha \beta$, $v = \beta \gamma$, $w = \gamma \alpha$.
The sum is $u+v+w = \alpha \beta + \beta \gamma + \gamma \alpha$, which is equal to $b$.
The sum of the products of pairs is $uv + vw + wu$:
$uv + vw + wu = (\alpha \beta)(\beta \gamma) + (\beta \gamma)(\gamma \alpha) + (\gamma \alpha)(\alpha \beta)$
$= \alpha \beta^2 \gamma + \beta \gamma^2 \alpha + \gamma \alpha^2 \beta$
$= \alpha \beta \gamma (\beta + \gamma + \alpha)$
Substituting the expressions from the original Vieta's formulas:
$uv + vw + wu = (-c)(-a) = ac$
Now substitute these into the expression for the sum of squares of $u, v, w$:
$\alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2 = (u+v+w)^2 - 2(uv+vw+wu) = (b)^2 - 2(ac) = b^2 - 2ac$
So, the coefficient $B$ is:
$B = \alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2 = b^2 - 2ac$

Finally, let's find the product of the squares of the roots:
$\alpha^2 \beta^2 \gamma^2 = (\alpha \beta \gamma)^2$
Substituting the expression from the original Vieta's formulas:
$\alpha^2 \beta^2 \gamma^2 = (-c)^2 = c^2$
So, the coefficient $C$ is:
$C = -(\alpha^2 \beta^2 \gamma^2) = -c^2$

The cubic polynomial whose roots are $\alpha^2$, $\beta^2$, $\gamma^2$ is $y^3 + Ay^2 + By + C = 0$.
Substituting the expressions for $A, B, C$ in terms of $a, b, c$:
$y^3 + (2b - a^2) y^2 + (b^2 - 2ac) y - c^2 = 0$

Alternatively, we can use a transformation method. Let the original equation be $x^3 + a x^2 + b x + c = 0$. We want a polynomial in $y$ such that $y = x^2$. This means $x = \pm \sqrt{y}$. Substitute $x = \sqrt{y}$ into the original equation:
$(\sqrt{y})^3 + a (\sqrt{y})^2 + b (\sqrt{y}) + c = 0$
$y\sqrt{y} + ay + b\sqrt{y} + c = 0$
Group the terms with $\sqrt{y}$ and the terms without $\sqrt{y}$:
$(y+b)\sqrt{y} + (ay+c) = 0$
Isolate the term with $\sqrt{y}$:
$(y+b)\sqrt{y} = -(ay+c)$
Square both sides to eliminate the square root:
$((y+b)\sqrt{y})^2 = (-(ay+c))^2$
$(y+b)^2 y = (ay+c)^2$
$(y^2 + 2by + b^2) y = a^2 y^2 + 2acy + c^2$
$y^3 + 2by^2 + b^2 y = a^2 y^2 + 2acy + c^2$
Move all terms to the left side to form a standard polynomial equation:
$y^3 + (2b - a^2) y^2 + (b^2 - 2ac) y - c^2 = 0$
This is a cubic polynomial in $y$ whose roots are the squares of the roots of the original equation.
Replacing the variable $y$ with $x$ to present the polynomial in the standard variable:

The cubic polynomial whose roots are $\alpha^2$, $\beta^2$, $\gamma^2$ is $x^3 + (2b - a^2) x^2 + (b^2 - 2ac) x - c^2$.

The final answer is $\boxed{x^3 + (2b - a^2) x^2 + (b^2 - 2ac) x - c^2}$.