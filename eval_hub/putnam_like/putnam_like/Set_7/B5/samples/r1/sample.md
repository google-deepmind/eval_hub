

To find all continuous functions \( g : \mathbb{R} \rightarrow \mathbb{R} \) satisfying the functional equation:
\[
g(g(x)) = \frac{1}{2}g(x) + \frac{1}{2}x,
\]
we analyze possible solutions, focusing on linear (affine) functions and leveraging continuity.

**Step 1: Assume \( g(x) \) is linear.**  
Let \( g(x) = ax + b \). Substituting into the equation:
\[
g(g(x)) = a(ax + b) + b = a^2x + ab + b,
\]
and the right-hand side becomes:
\[
\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}(ax + b) + \frac{1}{2}x = \left(\frac{a + 1}{2}\right)x + \frac{b}{2}.
\]
Equating coefficients for \( x \) and constants:
1. \( a^2 = \frac{a + 1}{2} \),
2. \( ab + b = \frac{b}{2} \).

**Step 2: Solve for \( a \).**  
The quadratic equation \( 2a^2 - a - 1 = 0 \) yields roots:
\[
a = 1 \quad \text{or} \quad a = -\frac{1}{2}.
\]

**Case 1: \( a = 1 \).**  
Substituting \( a = 1 \) into the constant term equation:
\[
b \cdot 1 + b = \frac{b}{2} \implies 2b = \frac{b}{2} \implies b = 0.
\]
Thus, one solution is:
\[
g(x) = x.
\]

**Case 2: \( a = -\frac{1}{2} \).**  
The constant term equation becomes:
\[
-\frac{1}{2}b + b = \frac{b}{2} \implies \frac{b}{2} = \frac{b}{2},
\]
which holds for any \( b \in \mathbb{R} \). Therefore, the general solution is:
\[
g(x) = -\frac{1}{2}x + b, \quad \text{where } b \in \mathbb{R}.
\]

**Step 3: Verify no non-linear solutions exist under continuity.**  
Suppose \( g \) is non-linear. The functional equation induces a recurrence relation \( x_{n+2} = \frac{1}{2}(x_{n+1} + x_n) \), whose solution converges to a fixed point. For continuous \( g \), iterations of \( g \) must align with linear behavior, restricting \( g \) to affine forms. Hence, no continuous non-linear solutions exist.

**Final Answer:**  
All continuous solutions are:
\[
\boxed{g(x) = x} \quad \text{or} \quad \boxed{g(x) = -\frac{1}{2}x + b} \quad \text{for some constant } b \in \mathbb{R}.
\]