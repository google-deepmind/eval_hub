

To find the cubic polynomial with roots $\alpha^2$, $\beta^2$, and $\gamma^2$, we use Vieta's formulas on the original polynomial $x^3 + a x^2 + b x + c = 0$ and express the required coefficients in terms of $a$, $b$, and $c$.

**Given:**
- Original roots: $\alpha, \beta, \gamma$
- Vieta's formulas for the original polynomial:
  - $\alpha + \beta + \gamma = -a$
  - $\alpha\beta + \alpha\gamma + \beta\gamma = b$
  - $\alpha\beta\gamma = -c$

**New Polynomial:**
Let the new polynomial be $x^3 + p x^2 + q x + r = 0$ with roots $\alpha^2, \beta^2, \gamma^2$.

**Vieta's Formulas for the New Polynomial:**
1. **Sum of roots:**
   \[
   \alpha^2 + \beta^2 + \gamma^2 = (\alpha + \beta + \gamma)^2 - 2(\alpha\beta + \alpha\gamma + \beta\gamma) = (-a)^2 - 2b = a^2 - 2b
   \]
   Thus, $-p = a^2 - 2b \implies p = -a^2 + 2b$.

2. **Sum of products of roots two at a time:**
   \[
   \alpha^2\beta^2 + \alpha^2\gamma^2 + \beta^2\gamma^2 = (\alpha\beta + \alpha\gamma + \beta\gamma)^2 - 2\alpha\beta\gamma(\alpha + \beta + \gamma) = b^2 - 2(-c)(-a) = b^2 - 2ac
   \]
   Hence, $q = b^2 - 2ac$.

3. **Product of roots:**
   \[
   \alpha^2\beta^2\gamma^2 = (\alpha\beta\gamma)^2 = (-c)^2 = c^2
   \]
   Therefore, $-r = c^2 \implies r = -c^2$.

**Resulting Polynomial:**
\[
x^3 + (2b - a^2)x^2 + (b^2 - 2ac)x - c^2 = 0
\]

### Final Answer
The cubic polynomial is:
```markdown
\boxed{x^3 + (2b - a^2)x^2 + (b^2 - 2ac)x - c^2}
```