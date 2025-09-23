```markdown
We begin with the given equation
\[
\left(\int_{a}^b g(x)f(x)^2\,dx\right)^2 = \left(\int_{a}^b f(x)^2\,dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\,dx\right).
\]

A natural way to approach this problem is to recognize that the equation is the equality case in the Cauchy–Schwarz inequality. To see this, define the functions
\[
u(x) = f(x) \quad \text{and} \quad v(x) = g(x)f(x).
\]
Then the equation can be rewritten as
\[
\left(\int_{a}^b u(x)v(x)\,dx\right)^2 = \left(\int_{a}^b u(x)^2\,dx\right) \left(\int_{a}^b v(x)^2\,dx\right).
\]

Since the Cauchy–Schwarz inequality tells us that
\[
\left(\int_{a}^b u(x)v(x)\,dx\right)^2 \leq \left(\int_{a}^b u(x)^2\,dx\right) \left(\int_{a}^b v(x)^2\,dx\right),
\]
with equality if and only if there is a constant \(\lambda\) such that
\[
v(x) = \lambda u(x)
\]
almost everywhere on \([a,b]\), we deduce that
\[
g(x)f(x) = \lambda f(x)
\]
almost everywhere on \([a,b]\).

There are two cases to consider:

1. **If \(f\not\equiv 0\):**  
   There is a set of positive measure where \(f(x) \neq 0\). For every \(x\) where \(f(x) \neq 0\),
   \[
   g(x) = \lambda.
   \]
   Because \(g\) is continuous on \([a,b]\), the value of \(g(x)\) must equal the same constant \(\lambda\) on the entire interval. Hence, 
   \[
   g(x) = c \quad \text{for some constant } c \in \mathbb{R} \text{ and for all } x \in [a,b].
   \]

2. **If \(f \equiv 0\) on \([a,b]\):**  
   In this case, we have
   \[
   \int_a^b f(x)^2\,dx = 0,
   \]
   and consequently each of the integrals in the equation is zero. Therefore, the equation holds trivially regardless of the choice of \(g\). That is, every continuous function \(g: [a,b] \to \mathbb{R}\) satisfies the equation.

**Conclusion:**

- If \(f \equiv 0\), then any continuous function \(g\) on \([a,b]\) is a solution.
- If \(f\not\equiv 0\), then the only continuous functions \(g\) that satisfy the equation are the constant functions:
  \[
  g(x) = c \quad \text{for some } c \in \mathbb{R} \text{ and for all } x \in [a,b].
  \]
```