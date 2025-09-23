Let the given cubic polynomial be $P(x) = x^3 + a x^2 + b x + c$.
The roots of $P(x)=0$ are $\alpha$, $\beta$, and $\gamma$.
By Vieta's formulas, we have:
$\sigma_1 = \alpha + \beta + \gamma = -a$
$\sigma_2 = \alpha \beta + \beta \gamma + \gamma \alpha = b$
$\sigma_3 = \alpha \beta \gamma = -c$

We want to find a new cubic polynomial, let's call it $Q(y)$, whose roots are $\alpha^2$, $\beta^2$, $\gamma^2$.
Let the roots of $Q(y)$ be $y_1 = \alpha^2$, $y_2 = \beta^2$, $y_3 = \gamma^2$.
A monic cubic polynomial $Q(y)$ can be written as $Q(y) = y^3 + A y^2 + B y + C$, where $A, B, C$ are coefficients determined by the roots.
Using Vieta's formulas for $Q(y)$:
$A = -(y_1 + y_2 + y_3) = -(\alpha^2 + \beta^2 + \gamma^2)$
$B = y_1 y_2 + y_2 y_3 + y_3 y_1 = \alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2$
$C = -(y_1 y_2 y_3) = -(\alpha^2 \beta^2 \gamma^2)$

We need to express $A, B, C$ in terms of $a, b, c$.
For $A$:
$\alpha^2 + \beta^2 + \gamma^2 = (\alpha + \beta + \gamma)^2 - 2(\alpha \beta + \beta \gamma + \gamma \alpha) = \sigma_1^2 - 2\sigma_2$
$A = -(\sigma_1^2 - 2\sigma_2) = -((-a)^2 - 2b) = -(a^2 - 2b) = 2b - a^2$.

For $B$:
$\alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2 = (\alpha \beta + \beta \gamma + \gamma \alpha)^2 - 2(\alpha \beta \cdot \beta \gamma + \beta \gamma \cdot \gamma \alpha + \gamma \alpha \cdot \alpha \beta)$
$= \sigma_2^2 - 2(\alpha \beta^2 \gamma + \beta \gamma^2 \alpha + \gamma \alpha^2 \beta)$
$= \sigma_2^2 - 2 \alpha \beta \gamma (\beta + \gamma + \alpha)$
$= \sigma_2^2 - 2 \sigma_3 \sigma_1$
$B = b^2 - 2(-c)(-a) = b^2 - 2ac$.

For $C$:
$\alpha^2 \beta^2 \gamma^2 = (\alpha \beta \gamma)^2 = \sigma_3^2$
$C = - \sigma_3^2 = -(-c)^2 = -c^2$.

Substituting the computed coefficients $A, B, C$ into the polynomial $Q(y)$:
$Q(y) = y^3 + (2b - a^2) y^2 + (b^2 - 2ac) y - c^2$.

Alternatively, we can use a substitution method.
Let $x$ be a root of $x^3 + a x^2 + b x + c = 0$. We want to find a polynomial whose roots are $y = x^2$.
From the given equation:
$x^3 + b x = - (a x^2 + c)$
$x(x^2 + b) = - (a x^2 + c)$
Substitute $y = x^2$:
$x(y + b) = - (ay + c)$
Square both sides to eliminate $x$:
$x^2 (y+b)^2 = (-(ay+c))^2$
$y (y+b)^2 = (ay+c)^2$
Expand the equation:
$y (y^2 + 2by + b^2) = a^2 y^2 + 2acy + c^2$
$y^3 + 2by^2 + b^2 y = a^2 y^2 + 2acy + c^2$
Rearrange the terms to form a polynomial equation in $y$:
$y^3 + (2b - a^2) y^2 + (b^2 - 2ac) y - c^2 = 0$.
The polynomial $Q(y) = y^3 + (2b - a^2) y^2 + (b^2 - 2ac) y - c^2$ is the required polynomial whose roots are $\alpha^2, \beta^2, \gamma^2$.

Let's express the final polynomial using the variable $x$ as is conventional, though using a different variable like $y$ is clearer in derivation. The problem asks for "the cubic polynomial", which usually means the expression itself.

The cubic polynomial whose roots are $\alpha^2$, $\beta^2$, $\gamma^2$ is:
$P_{new}(x) = x^3 + (2b - a^2) x^2 + (b^2 - 2ac) x - c^2$.

Final Answer: The final answer is $\boxed{x^3 + (2b - a^2) x^2 + (b^2 - 2ac) x - c^2}$