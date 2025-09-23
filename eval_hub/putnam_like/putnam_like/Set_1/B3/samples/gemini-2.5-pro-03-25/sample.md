Let $N(s) := \int_{\mathbb{R}^n} |f(x)|^s \, dx$. The function we are interested in is $\Psi(s) = \ln(N(s))$.
The hypothesis is $f \in L^p (\mathbb{R}^n) \cap L^q (\mathbb{R}^n)$ for $0 < p < q < +\infty$. This means $N(p) = \int |f|^p < \infty$ and $N(q) = \int |f|^q < \infty$.

First, let's show that $N(s)$ is finite for all $s \in [p,q]$.
Let $s \in (p,q)$. We can write $s = \lambda p + (1-\lambda) q$ for some $\lambda \in (0,1)$.
Let $E = \{x \in \mathbb{R}^n : |f(x)| \le 1\}$ and $F = \{x \in \mathbb{R}^n : |f(x)| > 1\}$.
Then $\mathbb{R}^n = E \cup F$ (disjoint union up to a set of measure zero).
$$ N(s) = \int_{\mathbb{R}^n} |f(x)|^s \, dx = \int_E |f(x)|^s \, dx + \int_F |f(x)|^s \, dx. $$
For $x \in E$, we have $|f(x)| \le 1$. Since $p < s$, we have $|f(x)|^s \le |f(x)|^p$.
Thus, $\int_E |f(x)|^s \, dx \le \int_E |f(x)|^p \, dx \le \int_{\mathbb{R}^n} |f(x)|^p \, dx = N(p) < \infty$.
For $x \in F$, we have $|f(x)| > 1$. Since $s < q$, we have $|f(x)|^s \le |f(x)|^q$.
Thus, $\int_F |f(x)|^s \, dx \le \int_F |f(x)|^q \, dx \le \int_{\mathbb{R}^n} |f(x)|^q \, dx = N(q) < \infty$.
Therefore, $N(s) = \int_E |f(x)|^s \, dx + \int_F |f(x)|^s \, dx \le N(p) + N(q) < \infty$.
This confirms that $N(s)$ is finite for all $s \in [p,q]$.

To show that $\Psi(s)$ is convex on $[p,q]$, we need to show that for any $s_1, s_2 \in [p,q]$ and any $\lambda \in [0,1]$, the following inequality holds:
$$ \Psi(\lambda s_1 + (1-\lambda) s_2) \le \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2). $$
Let $s = \lambda s_1 + (1-\lambda) s_2$. Substituting the definition of $\Psi$, we need to show:
$$ \ln(N(s)) \le \lambda \ln(N(s_1)) + (1-\lambda) \ln(N(s_2)). $$
Since the natural logarithm function $\ln$ is strictly increasing for positive values, this inequality is equivalent to:
$$ N(s) \le N(s_1)^\lambda N(s_2)^{1-\lambda}. $$
Let's write $N(s)$ using the definition of $s$:
$$ N(s) = \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1 + (1-\lambda) s_2} \, dx = \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1} |f(x)|^{(1-\lambda) s_2} \, dx. $$
We can use Hölder's inequality. Let $\lambda \in (0,1)$. The cases $\lambda=0$ and $\lambda=1$ are trivial.
Let $r = 1/\lambda$ and $r' = 1/(1-\lambda)$. Then $r, r' > 1$ and $1/r + 1/r' = \lambda + (1-\lambda) = 1$.
Let $g(x) = |f(x)|^{\lambda s_1}$ and $h(x) = |f(x)|^{(1-\lambda) s_2}$.
Hölder's inequality states that $\int |gh| dx \le \left( \int |g|^r dx \right)^{1/r} \left( \int |h|^{r'} dx \right)^{1/r'}$.
Let's apply this to our functions $g$ and $h$:
$$ \int_{\mathbb{R}^n} |f(x)|^{\lambda s_1} |f(x)|^{(1-\lambda) s_2} \, dx = \int_{\mathbb{R}^n} g(x) h(x) \, dx. $$
The terms on the right side of Hölder's inequality are:
$$ \int |g(x)|^r \, dx = \int \left( |f(x)|^{\lambda s_1} \right)^{1/\lambda} \, dx = \int |f(x)|^{s_1} \, dx = N(s_1). $$
$$ \int |h(x)|^{r'} \, dx = \int \left( |f(x)|^{(1-\lambda) s_2} \right)^{1/(1-\lambda)} \, dx = \int |f(x)|^{s_2} \, dx = N(s_2). $$
Since $s_1, s_2 \in [p,q]$, we know $N(s_1)$ and $N(s_2)$ are finite. Thus $g \in L^r(\mathbb{R}^n)$ and $h \in L^{r'}(\mathbb{R}^n)$.
Applying Hölder's inequality:
$$ N(s) = \int g(x) h(x) \, dx \le \left( \int |g(x)|^r \, dx \right)^{1/r} \left( \int |h(x)|^{r'} \, dx \right)^{1/r'} $$
$$ N(s) \le (N(s_1))^{1/r} (N(s_2))^{1/r'} = N(s_1)^\lambda N(s_2)^{1-\lambda}. $$
This is the inequality $N(\lambda s_1 + (1-\lambda) s_2) \le N(s_1)^\lambda N(s_2)^{1-\lambda}$ we wanted to prove.

Taking the natural logarithm of both sides (assuming $N(s) > 0$. If $N(s)=0$, then $f=0$ a.e. and $\Psi(s) = -\infty$, which is convex):
$$ \ln(N(\lambda s_1 + (1-\lambda) s_2)) \le \ln(N(s_1)^\lambda N(s_2)^{1-\lambda}) $$
$$ \ln(N(s)) \le \lambda \ln(N(s_1)) + (1-\lambda) \ln(N(s_2)) $$
$$ \Psi(\lambda s_1 + (1-\lambda) s_2) \le \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2). $$
This inequality holds for all $s_1, s_2 \in [p,q]$ and $\lambda \in [0,1]$.
Therefore, the function $\Psi(s)$ is convex on the interval $[p,q]$.

Final check of edge cases:
- If $f=0$ almost everywhere, then $N(s) = 0$ for all $s \in [p, q]$. $\Psi(s) = \ln(0) = -\infty$. The constant function $-\infty$ is convex.
- If $N(s_1)=0$ or $N(s_2)=0$, then $f=0$ a.e., so $N(s)=0$ for all $s$. The result holds.
- Assume $N(s_1) > 0$ and $N(s_2) > 0$. Then $N(s) > 0$ for $s \in (s_1, s_2)$ (or $s \in (s_2, s_1)$). This is because $N(s)^{1/s} = \|f\|_s$. If $\|f\|_{s_1}>0$ and $\|f\|_{s_2}>0$, then $\|f\|_s>0$ for $s$ between $s_1$ and $s_2$. So taking logarithm is well-defined.

The argument using Hölder's inequality is robust and covers all cases.

Final Answer: The final answer is $\boxed{\Psi \text{ is convex}}$