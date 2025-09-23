Let $f \in L^p (\mathbb{R}^n) \cap L^q (\mathbb{R}^n)$ for some $0 < p < q < +\infty$. This means $\int_{\mathbb{R}^n} |f(x)|^p \, dx < \infty$ and $\int_{\mathbb{R}^n} |f(x)|^q \, dx < \infty$.
The function $\Psi : [p,q] \rightarrow \mathbb{R}$ is defined by $\Psi(s) := \ln \left( \int_{\mathbb{R}^n} |f(x)|^s \, dx \right)$.

First, we need to ensure that the integral $\int_{\mathbb{R}^n} |f(x)|^s \, dx$ is finite for all $s \in [p,q]$.
Let $s \in [p,q]$. Then $s$ can be written as a convex combination of $p$ and $q$: $s = \alpha p + \beta q$ for some $\alpha, \beta \ge 0$ with $\alpha+\beta=1$. Specifically, $\alpha = (q-s)/(q-p)$ and $\beta = (s-p)/(q-p)$.
If $s=p$ or $s=q$, the integral is finite by assumption.
If $s \in (p,q)$, then $\alpha \in (0,1)$ and $\beta \in (0,1)$.
We can write $|f(x)|^s = |f(x)|^{\alpha p + \beta q} = |f(x)|^{\alpha p} |f(x)|^{\beta q}$.
Let $u(x) = |f(x)|^p$ and $v(x) = |f(x)|^q$. Then $|f(x)|^s = u(x)^\alpha v(x)^\beta$.
We can apply Holder's inequality to $\int u(x)^\alpha v(x)^\beta dx$ with exponents $P = 1/\alpha$ and $Q = 1/\beta$. Since $\alpha, \beta \in (0,1)$, $P>1$ and $Q>1$, and $1/P + 1/Q = \alpha + \beta = 1$.
$\int |f(x)|^s dx = \int u(x)^\alpha v(x)^\beta dx \le \left( \int (u(x)^\alpha)^{1/\alpha} dx \right)^\alpha \left( \int (v(x)^\beta)^{1/\beta} dx \right)^\beta$
$= \left( \int u(x) dx \right)^\alpha \left( \int v(x) dx \right)^\beta = \left( \int |f(x)|^p dx \right)^\alpha \left( \int |f(x)|^q dx \right)^\beta$.
Since $f \in L^p \cap L^q$, $\int |f(x)|^p dx < \infty$ and $\int |f(x)|^q dx < \infty$.
Thus, $\int |f(x)|^s dx < \infty$ for all $s \in [p,q]$.
If $\int |f(x)|^s dx = 0$ for all $s \in [p,q]$, then $f(x)=0$ a.e. and $\Psi(s) = \ln(0) = -\infty$, which is a convex function.
Assume $f$ is not identically zero, so $\int |f(x)|^s dx > 0$ for all $s \in [p,q]$. Thus $\Psi(s)$ is well-defined on $[p,q]$.

To show that $\Psi$ is convex on $[p,q]$, we need to show that for any $s_1, s_2 \in [p,q]$ and any $\lambda \in (0,1)$,
$$
\Psi(\lambda s_1 + (1-\lambda) s_2) \le \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2).
$$
Let $s = \lambda s_1 + (1-\lambda) s_2$. Note that since $s_1, s_2 \in [p,q]$ and $\lambda \in (0,1)$, $s \in (p,q)$.
The inequality can be written as
$$
\ln \left( \int |f(x)|^s \, dx \right) \le \lambda \ln \left( \int |f(x)|^{s_1} \, dx \right) + (1-\lambda) \ln \left( \int |f(x)|^{s_2} \, dx \right).
$$
Using the property of logarithms, $\lambda \ln A + (1-\lambda) \ln B = \ln (A^\lambda B^{1-\lambda})$, the inequality becomes
$$
\ln \left( \int |f(x)|^s \, dx \right) \le \ln \left( \left( \int |f(x)|^{s_1} \, dx \right)^\lambda \left( \int |f(x)|^{s_2} \, dx \right)^{1-\lambda} \right).
$$
Since $\ln$ is an increasing function, this is equivalent to
$$
\int |f(x)|^s \, dx \le \left( \int |f(x)|^{s_1} \, dx \right)^\lambda \left( \int |f(x)|^{s_2} \, dx \right)^{1-\lambda}.
$$
Let's write $|f(x)|^s = |f(x)|^{\lambda s_1 + (1-\lambda) s_2} = |f(x)|^{\lambda s_1} |f(x)|^{(1-\lambda) s_2}$.
Let $u(x) = |f(x)|^{s_1}$ and $v(x) = |f(x)|^{s_2}$. The inequality we need to prove is
$$
\int u(x)^\lambda v(x)^{1-\lambda} \, dx \le \left( \int u(x) \, dx \right)^\lambda \left( \int v(x) \, dx \right)^{1-\lambda}.
$$
We use Holder's inequality for this. Let $P = 1/\lambda$ and $Q = 1/(1-\lambda)$. Since $\lambda \in (0,1)$, we have $P > 1$ and $Q > 1$, and $1/P + 1/Q = \lambda + (1-\lambda) = 1$.
Apply Holder's inequality to the functions $u(x)^\lambda$ and $v(x)^{1-\lambda}$ with exponents $P$ and $Q$:
$$
\int u(x)^\lambda v(x)^{1-\lambda} \, dx \le \left( \int (u(x)^\lambda)^P \, dx \right)^{1/P} \left( \int (v(x)^{1-\lambda})^Q \, dx \right)^{1/Q}.
$$
Substitute $P=1/\lambda$ and $Q=1/(1-\lambda)$:
$$
\int u(x)^\lambda v(x)^{1-\lambda} \, dx \le \left( \int (u(x)^\lambda)^{1/\lambda} \, dx \right)^\lambda \left( \int (v(x)^{1-\lambda})^{1/(1-\lambda)} \, dx \right)^{1-\lambda}.
$$
This simplifies to
$$
\int u(x)^\lambda v(x)^{1-\lambda} \, dx \le \left( \int u(x) \, dx \right)^\lambda \left( \int v(x) \, dx \right)^{1-\lambda}.
$$
Substituting back $u(x) = |f(x)|^{s_1}$ and $v(x) = |f(x)|^{s_2}$:
$$
\int |f(x)|^{\lambda s_1} |f(x)|^{(1-\lambda) s_2} \, dx \le \left( \int |f(x)|^{s_1} \, dx \right)^\lambda \left( \int |f(x)|^{s_2} \, dx \right)^{1-\lambda}.
$$
$$
\int |f(x)|^{\lambda s_1 + (1-\lambda) s_2} \, dx \le \left( \int |f(x)|^{s_1} \, dx \right)^\lambda \left( \int |f(x)|^{s_2} \, dx \right)^{1-\lambda}.
$$
As $s = \lambda s_1 + (1-\lambda) s_2$, this is
$$
\int |f(x)|^s \, dx \le \left( \int |f(x)|^{s_1} \, dx \right)^\lambda \left( \int |f(x)|^{s_2} \, dx \right)^{1-\lambda}.
$$
Taking the natural logarithm of both sides gives
$$
\ln \left( \int |f(x)|^s \, dx \right) \le \ln \left( \left( \int |f(x)|^{s_1} \, dx \right)^\lambda \left( \int |f(x)|^{s_2} \, dx \right)^{1-\lambda} \right).
$$
$$
\Psi(s) \le \lambda \ln \left( \int |f(x)|^{s_1} \, dx \right) + (1-\lambda) \ln \left( \int |f(x)|^{s_2} \, dx \right).
$$
$$
\Psi(s) \le \lambda \Psi(s_1) + (1-\lambda) \Psi(s_2).
$$
This inequality holds for all $s_1, s_2 \in [p,q]$ and $\lambda \in (0,1)$. Thus, $\Psi$ is convex on $[p,q]$.

The final answer is $\boxed{\Psi(s) = \ln \left( \int_{\mathbb{R}^n} |f(x)|^s \, dx \right) \text{ is convex}}$.