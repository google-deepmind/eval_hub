

To show that $\Psi(s) := \ln \left( \int_{\mathbb{R}^n} |f(x)|^s \, dx \right)$ is convex on $[p, q]$, we demonstrate that $N(s) = \int_{\mathbb{R}^n} |f(x)|^s \, dx$ is log-convex, which implies $\Psi(s) = \ln N(s)$ is convex.

**Key Steps:**

1. **Convex Combination Representation:**  
   For any $s_1, s_2 \in [p, q]$ and $\lambda \in [0,1]$, define $s = \lambda s_1 + (1-\lambda)s_2$.

2. **Hölder's Inequality Application:**  
   Express $|f(x)|^s$ as $|f(x)|^{\lambda s_1} \cdot |f(x)|^{(1-\lambda)s_2}$. Apply Hölder's inequality with exponents $\frac{1}{\lambda}$ and $\frac{1}{1-\lambda}$ (noting $\frac{1}{\frac{1}{\lambda}} + \frac{1}{\frac{1}{1-\lambda}} = \lambda + (1-\lambda) = 1$):
   \[
   \int_{\mathbb{R}^n} |f(x)|^s \, dx \leq \left( \int_{\mathbb{R}^n} |f(x)|^{s_1} \, dx \right)^\lambda \left( \int_{\mathbb{R}^n} |f(x)|^{s_2} \, dx \right)^{1-\lambda}.
   \]

3. **Logarithmic Transformation:**  
   Taking the natural logarithm of both sides:
   \[
   \Psi(s) \leq \lambda \Psi(s_1) + (1-\lambda)\Psi(s_2).
   \]
   This inequality satisfies the definition of convexity for $\Psi$.

**Conclusion:**  
By Hölder's inequality, $\Psi(s)$ satisfies the convexity condition for all $s_1, s_2 \in [p, q]$ and $\lambda \in [0,1]$. Hence, $\Psi$ is convex on $[p, q]$.

```markdown
$\boxed{\text{By Hölder's inequality, } \Psi \text{ is convex on } [p, q].}$
```