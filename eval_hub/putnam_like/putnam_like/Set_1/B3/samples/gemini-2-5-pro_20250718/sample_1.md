Of course. Here is a detailed, step-by-step solution to the problem.

### **Problem Statement**

Let $f \in L^p (\mathbb{R}^n) \cap L^q (\mathbb{R}^n)$ for some $0 < p < q < +\infty$. Define $\Psi : [p,q] \rightarrow \mathbb{R}$ by
$$
\Psi(s) := \ln \left( \int_{\mathbb{R}^n} |f(x)|^s \, dx \right).
$$
Show that $\Psi$ is convex.

### **Solution**

#### **1. Preliminaries and Goal**

To show that $\Psi$ is a convex function on the interval $[p, q]$, we must prove that for any $s_1, s_2 \in [p, q]$ and any $\lambda \in [0, 1]$, the following inequality holds:
$$
\Psi(\lambda s_1 + (1-\lambda) s_2) \leq \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2).
$$

Let's denote the $L^s$-norm squared to the power of $s$ as $N(s)$:
$$
N(s) := \int_{\mathbb{R}^n} |f(x)|^s \, dx.
$$
With this notation, $\Psi(s) = \ln(N(s))$.

First, let's ensure that $\Psi(s)$ is well-defined for all $s \in [p, q]$. The problem states that $f \in L^p(\mathbb{R}^n) \cap L^q(\mathbb{R}^n)$, which means $N(p) = \int |f|^p dx < \infty$ and $N(q) = \int |f|^q dx < \infty$. For any $s \in (p, q)$, we can write $s$ as a convex combination of $p$ and $q$: $s = \alpha q + (1-\alpha) p$ for some $\alpha = \frac{s-p}{q-p} \in (0,1)$. We can then use Hölder's inequality to show that $N(s)$ is finite.
\begin{align*} N(s) = \int |f|^s dx &= \int |f|^{\alpha q + (1-\alpha) p} dx \\ &= \int |f|^{\alpha q} |f|^{(1-\alpha) p} dx \end{align*}
Let $g(x) = |f(x)|^{\alpha q}$ and $h(x) = |f(x)|^{(1-\alpha) p}$. Let the Hölder exponents be $r = 1/\alpha$ and $r' = 1/(1-\alpha)$. Then $\frac{1}{r} + \frac{1}{r'} = \alpha + (1-\alpha) = 1$. By Hölder's inequality:
\begin{align*} \int |g(x)h(x)| dx &\leq \left( \int |g(x)|^r dx \right)^{1/r} \left( \int |h(x)|^{r'} dx \right)^{1/r'} \\ \int |f|^s dx &\leq \left( \int (|f|^{\alpha q})^{1/\alpha} dx \right)^{\alpha} \left( \int (|f|^{(1-\alpha)p})^{1/(1-\alpha)} dx \right)^{1-\alpha} \\ &= \left( \int |f|^q dx \right)^{\alpha} \left( \int |f|^p dx \right)^{1-\alpha} \\ N(s) &\leq N(q)^\alpha N(p)^{1-\alpha} < \infty. \end{align*}
Thus, $N(s)$ is finite for all $s \in [p,q]$, and $\Psi(s)$ is well-defined (assuming $f$ is not the zero function a.e., in which case $N(s) = 0$ and $\Psi(s)=-\infty$, which is trivially convex).

#### **2. Main Proof using Hölder's Inequality**

Substituting the definition of $\Psi(s)$ into the convexity inequality, we need to show:
$$
\ln(N(\lambda s_1 + (1-\lambda) s_2)) \leq \lambda \ln(N(s_1)) + (1-\lambda) \ln(N(s_2)).
$$
Using the properties of logarithms, the right-hand side can be written as:
$$
\lambda \ln(N(s_1)) + (1-\lambda) \ln(N(s_2)) = \ln(N(s_1)^\lambda) + \ln(N(s_2)^{1-\lambda}) = \ln(N(s_1)^\lambda N(s_2)^{1-\lambda}).
$$
Since the natural logarithm function $\ln(\cdot)$ is strictly increasing, the inequality is equivalent to showing:
$$
N(\lambda s_1 + (1-\lambda) s_2) \leq N(s_1)^\lambda N(s_2)^{1-\lambda}.
$$
This property is known as log-convexity for the function $N(s)$. Let's prove this inequality.

Let $s_1, s_2 \in [p, q]$ and $\lambda \in [0,1]$.
The cases $\lambda = 0$ or $\lambda = 1$ are trivial.
- If $\lambda = 0$, the inequality becomes $\Psi(s_2) \le \Psi(s_2)$.
- If $\lambda = 1$, the inequality becomes $\Psi(s_1) \le \Psi(s_1)$.
Both are true. So, we only need to consider the case $\lambda \in (0, 1)$.

Let $s = \lambda s_1 + (1-\lambda) s_2$. The left-hand side of our target inequality is:
$$
N(s) = \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1 + (1-\lambda) s_2} dx = \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1} |f(x)|^{(1-\lambda) s_2} dx.
$$
We will use Hölder's inequality, which states that for measurable functions $g, h$ and conjugate exponents $r, r' > 1$ (i.e., $\frac{1}{r} + \frac{1}{r'} = 1$),
$$
\int_{\mathbb{R}^n} |g(x)h(x)| dx \leq \left( \int_{\mathbb{R}^n} |g(x)|^r dx \right)^{1/r} \left( \int_{\mathbb{R}^n} |h(x)|^{r'} dx \right)^{1/r'}.
$$
Let's choose our functions and exponents as follows:
- $g(x) = |f(x)|^{\lambda s_1}$
- $h(x) = |f(x)|^{(1-\lambda) s_2}$
- $r = \frac{1}{\lambda}$
- $r' = \frac{1}{1-\lambda}$

Since $\lambda \in (0, 1)$, we have $r > 1$ and $r' > 1$. Let's check if they are conjugate exponents:
$$
\frac{1}{r} + \frac{1}{r'} = \frac{1}{1/\lambda} + \frac{1}{1/(1-\lambda)} = \lambda + (1-\lambda) = 1.
$$
They are indeed conjugate exponents. Now, we apply Hölder's inequality:
$$
\int_{\mathbb{R}^n} |f(x)|^{\lambda s_1} |f(x)|^{(1-\lambda) s_2} dx \leq \left( \int_{\mathbb{R}^n} \left(|f(x)|^{\lambda s_1}\right)^r dx \right)^{1/r} \left( \int_{\mathbb{R}^n} \left(|f(x)|^{(1-\lambda) s_2}\right)^{r'} dx \right)^{1/r'}.
$$
Let's simplify the right-hand side.
The first term is:
$$
\left( \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1 r} dx \right)^{1/r} = \left( \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1 \cdot (1/\lambda)} dx \right)^{\lambda} = \left( \int_{\mathbb{R}^n} |f(x)|^{s_1} dx \right)^{\lambda} = N(s_1)^\lambda.
$$
The second term is:
$$
\left( \int_{\mathbb{R}^n} |f(x)|^{(1-\lambda) s_2 r'} dx \right)^{1/r'} = \left( \int_{\mathbb{R}^n} |f(x)|^{(1-\lambda) s_2 \cdot (1/(1-\lambda))} dx \right)^{1-\lambda} = \left( \int_{\mathbb{R}^n} |f(x)|^{s_2} dx \right)^{1-\lambda} = N(s_2)^{1-\lambda}.
$$
Combining these results, Hölder's inequality gives us:
$$
\int_{\mathbb{R}^n} |f(x)|^{\lambda s_1 + (1-\lambda) s_2} dx \leq N(s_1)^\lambda N(s_2)^{1-\lambda}.
$$
This is precisely the log-convexity inequality for $N(s)$:
$$
N(\lambda s_1 + (1-\lambda) s_2) \leq N(s_1)^\lambda N(s_2)^{1-\lambda}.
$$
Since the integrals are finite and positive (for non-trivial $f$), we can take the natural logarithm of both sides. As $\ln$ is an increasing function, it preserves the inequality:
$$
\ln(N(\lambda s_1 + (1-\lambda) s_2)) \leq \ln(N(s_1)^\lambda N(s_2)^{1-\lambda}).
$$
Using the property $\ln(ab) = \ln(a)+\ln(b)$ and $\ln(a^c) = c\ln(a)$:
$$
\ln(N(\lambda s_1 + (1-\lambda) s_2)) \leq \lambda \ln(N(s_1)) + (1-\lambda) \ln(N(s_2)).
$$
Substituting back $\Psi(s) = \ln(N(s))$, we have:
$$
\Psi(\lambda s_1 + (1-\lambda) s_2) \leq \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2).
$$
This holds for all $s_1, s_2 \in [p, q]$ and for all $\lambda \in [0, 1]$.

#### **3. Conclusion**

We have shown that for any $s_1, s_2 \in [p,q]$ and $\lambda \in [0,1]$, the defining inequality for convexity $\Psi(\lambda s_1 + (1-\lambda) s_2) \leq \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2)$ is satisfied. Therefore, the function $\Psi(s)$ is convex on the interval $[p, q]$.

---

#### **Alternative Method: Using the Second Derivative**

Another way to prove convexity for a twice-differentiable function is to show that its second derivative is non-negative, i.e., $\Psi''(s) \ge 0$.

Let $N(s) = \int_{\mathbb{R}^n} |f(x)|^s dx$. Then $\Psi(s) = \ln(N(s))$.
Let's compute the derivatives of $\Psi(s)$.
$$ \Psi'(s) = \frac{N'(s)}{N(s)} $$
$$ \Psi''(s) = \frac{N''(s)N(s) - (N'(s))^2}{(N(s))^2} $$
For $\Psi''(s) \ge 0$, we need to show $N''(s)N(s) - (N'(s))^2 \ge 0$.

Assuming we can differentiate under the integral sign (which can be justified using the Dominated Convergence Theorem for derivatives), we have:
$$ N(s) = \int |f(x)|^s dx = \int e^{s \ln|f(x)|} dx $$
$$ N'(s) = \int \frac{\partial}{\partial s} e^{s \ln|f(x)|} dx = \int |f(x)|^s \ln|f(x)| dx $$
$$ N''(s) = \int \frac{\partial^2}{\partial s^2} e^{s \ln|f(x)|} dx = \int |f(x)|^s (\ln|f(x)|)^2 dx $$
The condition $\Psi''(s) \ge 0$ is equivalent to:
$$ \left(\int |f(x)|^s (\ln|f(x)|)^2 dx\right) \left(\int |f(x)|^s dx\right) - \left(\int |f(x)|^s \ln|f(x)| dx\right)^2 \ge 0 $$
This inequality is a direct consequence of the Cauchy-Schwarz inequality for integrals.
Let's define a measure $d\mu(x) = |f(x)|^s dx$. This is a positive measure on $\mathbb{R}^n$. Let $g(x) = \ln|f(x)|$ and $h(x) = 1$. The Cauchy-Schwarz inequality states:
$$ \left( \int g(x)h(x) d\mu(x) \right)^2 \leq \left( \int g(x)^2 d\mu(x) \right) \left( \int h(x)^2 d\mu(x) \right) $$
Substituting our choices for $g, h,$ and $d\mu$:
$$ \left( \int (\ln|f(x)|) \cdot 1 \cdot |f(x)|^s dx \right)^2 \leq \left( \int (\ln|f(x)|)^2 |f(x)|^s dx \right) \left( \int 1^2 \cdot |f(x)|^s dx \right) $$
In terms of $N(s)$ and its derivatives:
$$ (N'(s))^2 \leq N''(s) N(s) $$
This confirms that $N''(s)N(s) - (N'(s))^2 \ge 0$. Since $(N(s))^2 > 0$ (for non-trivial $f$), we have $\Psi''(s) \ge 0$ for all $s \in (p, q)$. This implies that $\Psi(s)$ is convex on $[p,q]$.