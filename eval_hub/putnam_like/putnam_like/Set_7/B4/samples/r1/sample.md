

To solve the problem, we analyze the structure of the set $\mathbb{O}$ and the behavior of polynomials evaluated at its elements.

**Step 1: Characterize $\mathbb{O}$**
The set $\mathbb{O}$ consists of numbers representable in base $p$ with all digits equal to 1. These numbers are given by:
\[
S_n = \frac{p^n - 1}{p - 1} \quad \text{for } n \geq 1.
\]

**Step 2: Constant Polynomials**
A constant polynomial $f(x) = c$ must satisfy $c \in \mathbb{O}$. Thus, $c = S_m$ for some $m \geq 1$.

**Step 3: Linear Polynomials**
Consider linear polynomials $f(x) = ax + b$. For $f(S_n) \in \mathbb{O}$, we require:
\[
a S_n + b = S_{m(n)} \quad \text{for some } m(n) \geq 1.
\]
Substituting $S_n = \frac{p^n - 1}{p - 1}$, we get:
\[
a \frac{p^n - 1}{p - 1} + b = \frac{p^{m(n)} - 1}{p - 1}.
\]
Multiplying through by $p - 1$:
\[
a(p^n - 1) + b(p - 1) = p^{m(n)} - 1.
\]
Matching coefficients for $p^n$ and constants, we find $a = p^k$ for some $k \geq 0$ and $b = \frac{p^k - 1}{p - 1} = S_k$. Thus, the linear polynomials are:
\[
f(x) = p^k x + S_k \quad \text{for } k \geq 0.
\]

**Step 4: Higher-Degree Polynomials**
For a polynomial $f$ of degree $d \geq 2$, asymptotic analysis shows that $f(S_n)$ grows faster than any $S_m$, making it impossible for $f(S_n) \in \mathbb{O}$ for all $n$. Hence, no such polynomials exist.

**Conclusion**
The solutions are:
1. **Constant polynomials**: $f(x) = S_m$ for some $m \geq 1$.
2. **Linear polynomials**: $f(x) = p^k x + S_k$ for some $k \geq 0$.

$\boxed{f(x) = S_m \text{ for some } m \geq 1 \text{ or } f(x) = p^k x + S_k \text{ for some } k \geq 0}$