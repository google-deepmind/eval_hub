# Problem Solution

I'll find the cubic polynomial whose roots are $\alpha^2$, $\beta^2$, and $\gamma^2$, where $\alpha$, $\beta$, and $\gamma$ are the roots of $x^3 + ax^2 + bx + c = 0$.

Let's denote the original polynomial as $P(x) = x^3 + ax^2 + bx + c$, and the cubic polynomial we seek as $Q(x)$.

## Step 1: Express $Q(x)$ in terms of its roots

Since $Q(x)$ has roots $\alpha^2$, $\beta^2$, and $\gamma^2$, we can write:
$$Q(x) = (x-\alpha^2)(x-\beta^2)(x-\gamma^2)$$

Expanding this:
$$Q(x) = x^3 - (\alpha^2+\beta^2+\gamma^2)x^2 + (\alpha^2\beta^2+\alpha^2\gamma^2+\beta^2\gamma^2)x - \alpha^2\beta^2\gamma^2$$

## Step 2: Express the coefficients in terms of $a$, $b$, and $c$

For the original polynomial $P(x) = x^3 + ax^2 + bx + c$ with roots $\alpha$, $\beta$, and $\gamma$, we have:
- $\alpha + \beta + \gamma = -a$
- $\alpha\beta + \alpha\gamma + \beta\gamma = b$
- $\alpha\beta\gamma = -c$

Now I need to express each coefficient of $Q(x)$ in terms of $a$, $b$, and $c$.

### Finding $\alpha^2 + \beta^2 + \gamma^2$:
Using the identity $(\alpha+\beta+\gamma)^2 = \alpha^2+\beta^2+\gamma^2 + 2(\alpha\beta+\alpha\gamma+\beta\gamma)$:
$$\alpha^2+\beta^2+\gamma^2 = (\alpha+\beta+\gamma)^2 - 2(\alpha\beta+\alpha\gamma+\beta\gamma) = (-a)^2 - 2b = a^2-2b$$

### Finding $\alpha^2\beta^2\gamma^2$:
$$\alpha^2\beta^2\gamma^2 = (\alpha\beta\gamma)^2 = (-c)^2 = c^2$$

### Finding $\alpha^2\beta^2+\alpha^2\gamma^2+\beta^2\gamma^2$:
Using the identity $(\alpha\beta+\alpha\gamma+\beta\gamma)^2 = \alpha^2\beta^2+\alpha^2\gamma^2+\beta^2\gamma^2 + 2\alpha\beta\gamma(\alpha+\beta+\gamma)$:
$$\alpha^2\beta^2+\alpha^2\gamma^2+\beta^2\gamma^2 = (\alpha\beta+\alpha\gamma+\beta\gamma)^2 - 2\alpha\beta\gamma(\alpha+\beta+\gamma)$$
$$= b^2 - 2(-c)(-a) = b^2-2ac$$

## Step 3: Construct the final polynomial

Substituting these values into our expression for $Q(x)$:
$$Q(x) = x^3 - (a^2-2b)x^2 + (b^2-2ac)x - c^2$$

Therefore, the cubic polynomial whose roots are $\alpha^2$, $\beta^2$, and $\gamma^2$ is:
$$x^3 - (a^2-2b)x^2 + (b^2-2ac)x - c^2$$