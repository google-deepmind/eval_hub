Of course. Here is a detailed, step-by-step solution to the problem.

### **Problem Statement**

Investigate if the integral $I = \int_0^\infty \cos(x)\cos(x^2)\,dx$ is convergent.

### **Solution**

#### **Step 1: Initial Analysis and Strategy**

The integral is an improper integral of the first kind because the upper limit of integration is infinite. The integrand, $f(x) = \cos(x)\cos(x^2)$, is a continuous function on $[0, \infty)$. To determine if the integral converges, we need to evaluate the limit:
$$ \lim_{M \to \infty} \int_0^M \cos(x)\cos(x^2)\,dx $$
The integrand oscillates, and it does not approach zero in a simple monotonic way. Direct integration is not feasible as there is no elementary antiderivative for $\cos(x)\cos(x^2)$. Also, a simple comparison test for absolute convergence is not helpful:
$$ |\cos(x)\cos(x^2)| \le 1 $$
but $\int_0^\infty 1 \, dx$ diverges. This does not rule out conditional convergence.

The oscillating nature of the integrand suggests that we should look for cancellations. A powerful technique is to use trigonometric identities to simplify the integrand. We will use the product-to-sum identity:
$$ \cos A \cos B = \frac{1}{2} \left[ \cos(A-B) + \cos(A+B) \right] $$
Applying this to our integrand with $A = x^2$ and $B = x$:
$$ \cos(x^2)\cos(x) = \frac{1}{2} \left[ \cos(x^2 - x) + \cos(x^2 + x) \right] $$
So, the original integral can be split into two separate integrals:
$$ I = \int_0^\infty \frac{1}{2} \left[ \cos(x^2 - x) + \cos(x^2 + x) \right] dx = \frac{1}{2} \int_0^\infty \cos(x^2 - x) \,dx + \frac{1}{2} \int_0^\infty \cos(x^2 + x) \,dx $$
The original integral $I$ converges if and only if both of these new integrals converge. Let's investigate them one by one.

Let $I_1 = \int_0^\infty \cos(x^2 + x) \,dx$ and $I_2 = \int_0^\infty \cos(x^2 - x) \,dx$.

---

#### **Step 2: Investigating the convergence of $I_1 = \int_0^\infty \cos(x^2 + x) \,dx$**

This is an oscillatory integral. For large $x$, the phase $\phi_1(x) = x^2 + x$ changes rapidly, suggesting the positive and negative parts of the cosine function will cancel out. We can formalize this using integration by parts.

The trick is to write the integrand as $\frac{1}{\phi_1'(x)} \cdot \phi_1'(x) \cos(\phi_1(x))$.
Here, $\phi_1(x) = x^2+x$, so $\phi_1'(x) = 2x+1$. This derivative is non-zero for $x \in [0, \infty)$.

$$ I_1 = \int_0^\infty \cos(x^2 + x) \,dx = \int_0^\infty \frac{1}{2x+1} \cdot (2x+1)\cos(x^2 + x) \,dx $$
We use integration by parts, $\int u \,dv = uv - \int v \,du$, with:
*   $u = \frac{1}{2x+1} \quad \implies \quad du = \frac{-2}{(2x+1)^2} \,dx$
*   $dv = (2x+1)\cos(x^2 + x) \,dx \quad \implies \quad v = \sin(x^2 + x)$

$$
\begin{aligned}
\int_0^M \cos(x^2 + x) \,dx &= \left[ \frac{\sin(x^2 + x)}{2x+1} \right]_0^M - \int_0^M \sin(x^2+x) \left( \frac{-2}{(2x+1)^2} \right) \,dx \\
&= \left( \frac{\sin(M^2 + M)}{2M+1} - \frac{\sin(0)}{1} \right) + 2 \int_0^M \frac{\sin(x^2+x)}{(2x+1)^2} \,dx
\end{aligned}
$$
Now, we take the limit as $M \to \infty$:
1.  **The boundary term:**
    $$ \lim_{M\to\infty} \frac{\sin(M^2 + M)}{2M+1} $$
    Since $-1 \le \sin(M^2+M) \le 1$, we have $\frac{-1}{2M+1} \le \frac{\sin(M^2+M)}{2M+1} \le \frac{1}{2M+1}$. By the Squeeze Theorem, this limit is 0. The other boundary term is $\frac{\sin(0)}{1}=0$. So, the boundary part evaluates to $0$.

2.  **The remaining integral:**
    $$ 2 \int_0^\infty \frac{\sin(x^2+x)}{(2x+1)^2} \,dx $$
    We check if this integral converges absolutely using the Comparison Test.
    $$ \left| \frac{\sin(x^2+x)}{(2x+1)^2} \right| \le \frac{1}{(2x+1)^2} $$
    We know that the integral $\int_1^\infty \frac{1}{x^p} \,dx$ converges for $p > 1$. Our integral $\int_0^\infty \frac{1}{(2x+1)^2} \,dx$ behaves like $\int \frac{1}{4x^2} \,dx$ for large $x$.
    Let's evaluate it directly:
    $$ \int_0^\infty \frac{1}{(2x+1)^2} \,dx = \lim_{M\to\infty} \left[ -\frac{1}{2(2x+1)} \right]_0^M = \lim_{M\to\infty} \left( -\frac{1}{2(2M+1)} - \left(-\frac{1}{2(1)}\right) \right) = 0 + \frac{1}{2} = \frac{1}{2} $$
    Since $\int_0^\infty \frac{1}{(2x+1)^2} \,dx$ converges, by the Comparison Test, the integral $\int_0^\infty \left| \frac{\sin(x^2+x)}{(2x+1)^2} \right| \,dx$ also converges. This means that $2 \int_0^\infty \frac{\sin(x^2+x)}{(2x+1)^2} \,dx$ converges absolutely, and therefore it converges.

Since both the boundary term and the remaining integral have finite limits, the integral $I_1$ converges.

---

#### **Step 3: Investigating the convergence of $I_2 = \int_0^\infty \cos(x^2 - x) \,dx$**

We use the same strategy. Let $\phi_2(x) = x^2 - x$. Then $\phi_2'(x) = 2x-1$.
Here, the derivative $\phi_2'(x)$ is zero at $x=1/2$. The term $\frac{1}{2x-1}$ is undefined at this point. To handle this, we must split the integral at a point away from the singularity, for example at $x=1$.

$$ I_2 = \int_0^1 \cos(x^2 - x) \,dx + \int_1^\infty \cos(x^2 - x) \,dx $$
The first integral, $\int_0^1 \cos(x^2 - x) \,dx$, is a proper integral of a continuous function over a finite interval. Therefore, it has a finite value and is convergent.

We now only need to investigate the convergence of the second part, $I_{2, \text{improper}} = \int_1^\infty \cos(x^2 - x) \,dx$.
For $x \in [1, \infty)$, the derivative $\phi_2'(x) = 2x-1$ is non-zero and positive. We can apply the same integration by parts technique.

$$ I_{2, \text{improper}} = \int_1^\infty \frac{1}{2x-1} \cdot (2x-1)\cos(x^2-x) \,dx $$
We use integration by parts with:
*   $u = \frac{1}{2x-1} \quad \implies \quad du = \frac{-2}{(2x-1)^2} \,dx$
*   $dv = (2x-1)\cos(x^2 - x) \,dx \quad \implies \quad v = \sin(x^2 - x)$

$$
\begin{aligned}
\int_1^M \cos(x^2 - x) \,dx &= \left[ \frac{\sin(x^2 - x)}{2x-1} \right]_1^M - \int_1^M \sin(x^2-x) \left( \frac{-2}{(2x-1)^2} \right) \,dx \\
&= \left( \frac{\sin(M^2 - M)}{2M-1} - \frac{\sin(1^2-1)}{2(1)-1} \right) + 2 \int_1^M \frac{\sin(x^2-x)}{(2x-1)^2} \,dx
\end{aligned}
$$
Now, we take the limit as $M \to \infty$:
1.  **The boundary term:**
    $$ \lim_{M\to\infty} \frac{\sin(M^2 - M)}{2M-1} $$
    By the Squeeze Theorem, this limit is 0. The other boundary term is $\frac{\sin(0)}{1}=0$. So, the boundary part evaluates to $0$.

2.  **The remaining integral:**
    $$ 2 \int_1^\infty \frac{\sin(x^2-x)}{(2x-1)^2} \,dx $$
    We check for absolute convergence.
    $$ \left| \frac{\sin(x^2-x)}{(2x-1)^2} \right| \le \frac{1}{(2x-1)^2} $$
    The integral $\int_1^\infty \frac{1}{(2x-1)^2} \,dx$ converges (by comparison with the p-integral $\int_1^\infty \frac{1}{x^2}dx$). We can also compute it directly:
    $$ \int_1^\infty \frac{1}{(2x-1)^2} \,dx = \lim_{M\to\infty} \left[ -\frac{1}{2(2x-1)} \right]_1^M = 0 - \left(-\frac{1}{2(1)}\right) = \frac{1}{2} $$
    Since $\int_1^\infty \frac{1}{(2x-1)^2} \,dx$ converges, the integral $\int_1^\infty \left| \frac{\sin(x^2-x)}{(2x-1)^2} \right| \,dx$ converges by the Comparison Test. Therefore, $2 \int_1^\infty \frac{\sin(x^2-x)}{(2x-1)^2} \,dx$ converges.

Since the boundary term and the remaining integral both have finite limits, the integral $\int_1^\infty \cos(x^2 - x) \,dx$ converges.
Since both $\int_0^1 \cos(x^2-x) \,dx$ and $\int_1^\infty \cos(x^2 - x) \,dx$ converge, their sum $I_2 = \int_0^\infty \cos(x^2 - x) \,dx$ also converges.

---

#### **Step 4: Final Conclusion**

We have successfully shown that both integrals $I_1 = \int_0^\infty \cos(x^2 + x) \,dx$ and $I_2 = \int_0^\infty \cos(x^2 - x) \,dx$ are convergent.

The original integral $I$ is a linear combination of these two convergent integrals:
$$ I = \frac{1}{2} I_2 + \frac{1}{2} I_1 $$
The sum of two convergent integrals is convergent. Therefore, the integral $\int_0^\infty \cos (x)\cos (x^2)\,dx$ is **convergent**.