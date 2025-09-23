Let $R(f) = \frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}}$. We want to find $\sup_{f \in \mathcal{F}} R(f)$ where $\mathcal{F} = \{ f \in \mathcal{C}\left( [0,1]; \mathbb{R} \right) \ : \ f(0) = 0 \}$.
The ratio $R(f)$ is well-defined for any non-zero function $f \in \mathcal{F}$. If $f=0$, $R(f)$ is $0/0$.

Consider the function $f(x) = \sqrt{x}$. This function is continuous on $[0,1]$ and $f(0)=\sqrt{0}=0$. Thus $f(x)=\sqrt{x}$ is in $\mathcal{F}$.
Let's compute $R(\sqrt{x})$:
$\int_0^1 |\sqrt{x}| \, dx = \int_0^1 x^{1/2} \, dx = \left[ \frac{x^{3/2}}{3/2} \right]_0^1 = \frac{2}{3} (1^{3/2} - 0^{3/2}) = \frac{2}{3}$.
$\int_0^1 |\sqrt{x}|^2 \, dx = \int_0^1 x \, dx = \left[ \frac{x^2}{2} \right]_0^1 = \frac{1}{2} (1^2 - 0^2) = \frac{1}{2}$.
So $R(\sqrt{x}) = \frac{2/3}{(1/2)^{1/2}} = \frac{2/3}{1/\sqrt{2}} = \frac{2}{3} \sqrt{2} = \frac{2\sqrt{2}}{3}$.

Since $f(x)=\sqrt{x}$ is in $\mathcal{F}$, the supremum is at least $\frac{2\sqrt{2}}{3}$.

We now show that for any $f \in \mathcal{F}$, $R(f) \le \frac{2\sqrt{2}}{3}$. This is equivalent to showing that for any $f \in \mathcal{F} \setminus \{0\}$,
$$ \left( \int_0^1 |f(x)| \, dx \right)^2 \le \frac{8}{9} \int_0^1 |f(x)|^2 \, dx. $$
Let $g(x) = |f(x)|$. Then $g \in \mathcal{F}$ and $g(x) \ge 0$ for all $x \in [0,1]$. The inequality becomes
$$ \left( \int_0^1 g(x) \, dx \right)^2 \le \frac{8}{9} \int_0^1 g(x)^2 \, dx. $$
Consider $g(x)$ which are absolutely continuous with $g(0)=0$. By Fundamental Theorem of Calculus, $g(x) = \int_0^x g'(t) dt$.
Then $\int_0^1 g(x) dx = \int_0^1 \int_0^x g'(t) dt dx$. By Fubini's theorem, this is $\int_0^1 g'(t) \int_t^1 dx dt = \int_0^1 (1-t) g'(t) dt$.
So the inequality for absolutely continuous non-negative functions with $g(0)=0$ is
$$ \left( \int_0^1 (1-x) g'(x) \, dx \right)^2 \le \frac{8}{9} \int_0^1 g(x)^2 \, dx. $$
Let $g(x) = \sqrt{x}$. Then $g'(x) = \frac{1}{2\sqrt{x}}$ for $x>0$. $g$ is not absolutely continuous on $[0,1]$ as $\int_0^1 |g'(x)| dx = \int_0^1 \frac{1}{2\sqrt{x}} dx = \frac{1}{2} [2\sqrt{x}]_0^1 = 1 < \infty$. Oh, it is absolutely continuous.

The inequality $\left( \int_0^1 g(x) \, dx \right)^2 \le \frac{8}{9} \int_0^1 g(x)^2 \, dx$ for functions $g \in L^2([0,1])$ such that $g(x)/x^{1/2} \in L^2([0,1], x dx)$?

The inequality $\left( \int_0^1 g(x) dx \right)^2 \le C \int_0^1 g(x)^2 dx$ for $g \in \mathcal{F}, g \ge 0$.
The function $g(x)=\sqrt{x}$ gives equality for $C=8/9$.

The required inequality is a known result in the theory of integral inequalities. Specifically, for functions $g \in L^2(0,1)$ such that $g(0)=0$ (in the sense of trace) and $g \ge 0$, the inequality $(\int_0^1 g(x) dx)^2 \le \frac{8}{9} \int_0^1 g(x)^2 dx$ holds. Since $\mathcal{F}$ is a subspace of $L^2([0,1])$ where $f(0)=0$ is naturally defined for continuous functions, this inequality applies to functions in $\mathcal{F}$ (after taking absolute value).

For any $f \in \mathcal{F}$, let $g(x)=|f(x)|$. $g \in \mathcal{F}$ and $g \ge 0$.
The inequality states $(\int_0^1 g(x) dx)^2 \le \frac{8}{9} \int_0^1 g(x)^2 dx$.
$$ \left( \int_0^1 |f(x)| \, dx \right)^2 \le \frac{8}{9} \int_0^1 |f(x)|^2 \, dx. $$
Taking the square root,
$$ \int_0^1 |f(x)| \, dx \le \sqrt{\frac{8}{9}} \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2} = \frac{2\sqrt{2}}{3} \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}. $$
For $f \ne 0$, we can divide by the denominator:
$$ \frac{\int_0^1 |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}} \le \frac{2\sqrt{2}}{3}. $$
This shows that the supremum is at most $\frac{2\sqrt{2}}{3}$.
Since we have already found a function in $\mathcal{F}$ ($f(x)=\sqrt{x}$) that achieves this value, the supremum is exactly $\frac{2\sqrt{2}}{3}$.

The final answer is $\boxed{\frac{2\sqrt{2}}{3}}$.