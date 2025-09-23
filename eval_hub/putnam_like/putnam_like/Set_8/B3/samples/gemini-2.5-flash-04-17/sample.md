Let $I_n^{(1)} = \int_{1-\frac{1}{n}}^1 f(x)dx$, $I_n^{(2)} = \int_0^1 x^{n-1}f(x)dx$, and $I_n^{(3)} = \int_0^{\frac{1}{n}}f(x)dx$.
We are given that $f: [0,1]\to \mathbb{R}$ is continuous and decreasing. We want to show $I_n^{(1)} \leq I_n^{(2)} \leq I_n^{(3)}$ for all $n\in \mathbb{N}$.

Let's rewrite the integrals using substitutions:
For $I_n^{(1)}$, let $x=1-y/n$. Then $dx = -dy/n$. When $x=1-1/n$, $y=1$. When $x=1$, $y=0$.
$I_n^{(1)} = \int_1^0 f(1-y/n)(-dy/n) = \frac{1}{n}\int_0^1 f(1-y/n)dy$.
For $I_n^{(2)}$, let $x=y^{1/n}$. Then $dx = \frac{1}{n}y^{\frac{1}{n}-1}dy$. When $x=0$, $y=0$. When $x=1$, $y=1$.
$I_n^{(2)} = \int_0^1 (y^{1/n})^{n-1} f(y^{1/n}) \frac{1}{n}y^{\frac{1}{n}-1}dy = \frac{1}{n}\int_0^1 y^{\frac{n-1}{n}} f(y^{1/n}) y^{\frac{1-n}{n}}dy = \frac{1}{n}\int_0^1 f(y^{1/n})dy$.
For $I_n^{(3)}$, let $x=y/n$. Then $dx = dy/n$. When $x=0$, $y=0$. When $x=1/n$, $y=1$.
$I_n^{(3)} = \int_0^1 f(y/n) \frac{1}{n}dy = \frac{1}{n}\int_0^1 f(y/n)dy$.

Let $g_1(y) = 1-y/n$, $g_2(y) = y^{1/n}$, and $g_3(y) = y/n$. The inequalities are equivalent to showing
$$ \frac{1}{n}\int_0^1 f(g_1(y))dy \leq \frac{1}{n}\int_0^1 f(g_2(y))dy \leq \frac{1}{n}\int_0^1 f(g_3(y))dy $$
or
$$ \int_0^1 f(g_1(y))dy \leq \int_0^1 f(g_2(y))dy \leq \int_0^1 f(g_3(y))dy. $$
Let's compare the functions $g_1(y), g_2(y), g_3(y)$ for $y \in [0,1]$.

For $n=1$, $g_1(y) = 1-y$, $g_2(y) = y$, $g_3(y) = y$. The integrals are $\int_0^1 f(1-y)dy \le \int_0^1 f(y)dy \le \int_0^1 f(y)dy$. Let $x=1-y$ in the first integral, $\int_1^0 f(x)(-dx) = \int_0^1 f(x)dx$. So the inequalities for $n=1$ are $\int_0^1 f(x)dx \le \int_0^1 f(x)dx \le \int_0^1 f(x)dx$, which are trivial.

Let's consider $n \ge 2$.
Compare $g_2(y) = y^{1/n}$ and $g_3(y) = y/n$. For $y \in (0,1]$, $y^{1/n} \ge y$ and $1/n \ge y^{1-1/n}/n \implies n \ge y^{1-1/n}$. As $y \in (0,1]$, $y^{1-1/n} \le 1$. $n \ge 1$.
Let $h(y) = y^{1/n} - y/n$. $h(0)=0$, $h(1) = 1-1/n \ge 0$. $h'(y) = \frac{1}{n}y^{\frac{1}{n}-1} - \frac{1}{n} = \frac{1}{n}(y^{\frac{1-n}{n}}-1)$. For $y \in (0,1)$, $y^{\frac{1-n}{n}} \ge 1$. So $h'(y) \ge 0$. $h(y)$ is increasing on $[0,1]$. Thus $h(y) \ge h(0)=0$ for $y \in [0,1]$.
So $y^{1/n} \ge y/n$ for all $y \in [0,1]$ and $n \ge 1$. $g_2(y) \ge g_3(y)$.

Since $f$ is a decreasing function, $a \ge b \implies f(a) \le f(b)$.
$g_2(y) \ge g_3(y) \implies f(g_2(y)) \le f(g_3(y))$.
Integrating over $[0,1]$: $\int_0^1 f(g_2(y))dy \le \int_0^1 f(g_3(y))dy$.
This shows $nI_n^{(2)} \le nI_n^{(3)}$, which is $I_n^{(2)} \le I_n^{(3)}$.

Now compare $g_1(y) = 1-y/n$ and $g_2(y) = y^{1/n}$.
Let's compare the integrals $\int_0^1 f(1-y/n)dy$ and $\int_0^1 f(y^{1/n})dy$.
This is equivalent to $I_n^{(1)} \le I_n^{(2)}$.

Consider the densities $p_1(x)=n\mathbf{1}_{[1-1/n,1]}(x)$, $p_2(x)=nx^{n-1}$, $p_3(x)=n\mathbf{1}_{[0,1/n]}(x)$ on $[0,1]$. These integrate to 1.
$I_n^{(1)} = \int_{1-1/n}^1 f(x)dx = \frac{1}{n}\int_{1-1/n}^1 f(x) n dx = \frac{1}{n}\int_0^1 f(x) p_1(x)dx = \frac{1}{n}\mathbb{E}_{P_1}[f(X)]$.
$I_n^{(2)} = \int_0^1 f(x) x^{n-1}dx = \frac{1}{n}\int_0^1 f(x) nx^{n-1}dx = \frac{1}{n}\int_0^1 f(x) p_2(x)dx = \frac{1}{n}\mathbb{E}_{P_2}[f(X)]$.
$I_n^{(3)} = \int_0^{1/n} f(x)dx = \frac{1}{n}\int_0^{1/n} f(x) n dx = \frac{1}{n}\int_0^1 f(x) p_3(x)dx = \frac{1}{n}\mathbb{E}_{P_3}[f(X)]$.
Let $P_i$ be probability measures with densities $p_i(x)$. We want to show $\mathbb{E}_{P_1}[f(X)] \le \mathbb{E}_{P_2}[f(X)] \le \mathbb{E}_{P_3}[f(X)]$.
For a decreasing function $f$, $\mathbb{E}[f(X)] \le \mathbb{E}[f(Y)]$ if and only if $X$ is stochastically greater than $Y$, which means $P(X>t) \ge P(Y>t)$ for all $t$. Let $F_i$ be the CDFs of $P_i$. This condition is $1-F_1(t) \ge 1-F_2(t) \ge 1-F_3(t)$, which is $F_1(t) \le F_2(t) \le F_3(t)$ for all $t \in [0,1]$.

Let's compute the CDFs:
$F_1(t) = \int_0^t p_1(x)dx = \int_0^t n\mathbf{1}_{[1-1/n,1]}(x)dx$.
For $t < 1-1/n$, $F_1(t)=0$. For $t \in [1-1/n, 1]$, $F_1(t) = \int_{1-1/n}^t n dx = n(t-(1-1/n))$.
$F_2(t) = \int_0^t p_2(x)dx = \int_0^t nx^{n-1}dx = [x^n]_0^t = t^n$ for $t \in [0,1]$.
$F_3(t) = \int_0^t p_3(x)dx = \int_0^t n\mathbf{1}_{[0,1/n]}(x)dx$.
For $t \in [0, 1/n]$, $F_3(t) = \int_0^t n dx = nt$. For $t \in (1/n, 1]$, $F_3(t) = \int_0^{1/n} n dx = 1$.

We need to show $F_1(t) \le F_2(t) \le F_3(t)$ for all $t \in [0,1]$.

Inequality $F_2(t) \le F_3(t)$:
For $t \in [0, 1/n]$, we need $t^n \le nt$. For $t>0$, this is $t^{n-1} \le n$. For $t \in (0, 1/n]$, $t^{n-1} \le (1/n)^{n-1}$. We need $(1/n)^{n-1} \le n$, which is $1 \le n^n$, true for $n \ge 1$. For $t=0$, $0^n \le n \cdot 0$ is $0 \le 0$, true.
For $t \in (1/n, 1]$, we need $t^n \le 1$. This is true for $t \in (1/n, 1]$.
So $F_2(t) \le F_3(t)$ for all $t \in [0,1]$.

Inequality $F_1(t) \le F_2(t)$:
For $t < 1-1/n$, $F_1(t)=0$. We need $0 \le t^n$, which is true.
For $t \in [1-1/n, 1]$, we need $n(t-(1-1/n)) \le t^n$. Let $h(t) = t^n - n(t-1+1/n) = t^n - nt + n-1$. We need to show $h(t) \ge 0$ for $t \in [1-1/n, 1]$.
$h(1-1/n) = (1-1/n)^n - n(1-1/n - 1 + 1/n) = (1-1/n)^n \ge 0$ (for $n \ge 1$).
$h(1) = 1^n - n(1-1+1/n) = 1 - n(1/n) = 1-1 = 0$.
$h'(t) = nt^{n-1} - n = n(t^{n-1}-1)$. For $t \in [1-1/n, 1)$, $t < 1$, so $t^{n-1} < 1$ (for $n \ge 2$). $h'(t) < 0$.
For $n=1$, $h(t)=t-t+1-1=0$. $F_1(t)=1(t-0)=t$. $F_2(t)=t^1=t$. $F_1(t) \le F_2(t)$ is $t \le t$, true.
For $n \ge 2$, $h(t)$ is decreasing on $[1-1/n, 1]$. Since $h(1)=0$, $h(t) \ge h(1)=0$ for $t \in [1-1/n, 1]$.
So $F_1(t) \le F_2(t)$ for all $t \in [0,1]$.

We have shown $F_1(t) \le F_2(t) \le F_3(t)$ for all $t \in [0,1]$.
This means that the random variable $X_1 \sim P_1$ is stochastically greater than or equal to $X_2 \sim P_2$, which is stochastically greater than or equal to $X_3 \sim P_3$. $X_1 \ge_{st} X_2 \ge_{st} X_3$.
For a decreasing function $f$, if $X \ge_{st} Y$, then $\mathbb{E}[f(X)] \le \mathbb{E}[f(Y)]$.
Thus, $\mathbb{E}_{P_1}[f(X)] \le \mathbb{E}_{P_2}[f(X)] \le \mathbb{E}_{P_3}[f(X)]$.
Multiplying by $1/n$, we get $I_n^{(1)} \le I_n^{(2)} \le I_n^{(3)}$.

The final answer is $\boxed{\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx \text{ for all }n\in \mathbb{N}}$.