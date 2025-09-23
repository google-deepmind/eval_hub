```markdown
We start with the cubic equation
\[
x^3 + a x^2 + b x + c = 0,
\]
whose roots are \(\alpha\), \(\beta\), and \(\gamma\). By Vieta's formulas, we know that
\[
\alpha + \beta + \gamma = -a, \quad \alpha\beta + \alpha\gamma + \beta\gamma = b, \quad \alpha\beta\gamma = -c.
\]

We wish to find the cubic polynomial whose roots are \(\alpha^2\), \(\beta^2\), and \(\gamma^2\). Such a polynomial can be written as
\[
(x - \alpha^2)(x - \beta^2)(x - \gamma^2) = 0.
\]
Expanding this product gives
\[
x^3 - (\alpha^2+\beta^2+\gamma^2)x^2 + (\alpha^2\beta^2+\alpha^2\gamma^2+\beta^2\gamma^2)x - \alpha^2\beta^2\gamma^2 = 0.
\]

Our task is now to find the expressions for the new symmetric sums in terms of \(a\), \(b\), and \(c\).

1. **Sum of the squares:**
   \[
   \alpha^2 + \beta^2 + \gamma^2 = (\alpha+\beta+\gamma)^2 - 2(\alpha\beta+\alpha\gamma+\beta\gamma) = (-a)^2 - 2b = a^2 - 2b.
   \]

2. **Sum of the products of the squares taken two at a time:**
   \[
   \alpha^2\beta^2 + \alpha^2\gamma^2 + \beta^2\gamma^2 = (\alpha\beta)^2 + (\alpha\gamma)^2 + (\beta\gamma)^2.
   \]
   Notice that
   \[
   (\alpha\beta + \alpha\gamma + \beta\gamma)^2 = (\alpha\beta)^2 + (\alpha\gamma)^2 + (\beta\gamma)^2 + 2\alpha\beta\alpha\gamma + 2\alpha\beta\beta\gamma + 2\alpha\gamma\beta\gamma.
   \]
   The cross terms can be factored as
   \[
   2\alpha\beta\alpha\gamma + 2\alpha\beta\beta\gamma + 2\alpha\gamma\beta\gamma = 2\alpha\beta\gamma(\alpha+\beta+\gamma).
   \]
   Therefore, we have
   \[
   (\alpha\beta)^2+(\alpha\gamma)^2+(\beta\gamma)^2 = (\alpha\beta+\alpha\gamma+\beta\gamma)^2 - 2\alpha\beta\gamma(\alpha+\beta+\gamma).
   \]
   Substituting the known values:
   \[
   (\alpha\beta)^2+(\alpha\gamma)^2+(\beta\gamma)^2 = b^2 - 2(-c)(-a) = b^2 - 2ac.
   \]

3. **Product of the squares:**
   \[
   \alpha^2\beta^2\gamma^2 = (\alpha\beta\gamma)^2 = (-c)^2 = c^2.
   \]

Thus, the polynomial with roots \(\alpha^2\), \(\beta^2\), and \(\gamma^2\) is
\[
x^3 - (a^2-2b)x^2 + (b^2-2ac)x - c^2 = 0.
\]

This is the desired cubic polynomial.
```