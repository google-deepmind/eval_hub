Let $\mathbb{O}$ be the set of positive integers whose digits in base $p$ are all ones. The elements of $\mathbb{O}$ are of the form $o_k = \underbrace{11\dots1}_{k \text{ digits}}$ in base $p$, for $k \geq 1$. In base 10, this is the sum of a geometric series:
$o_k = \sum_{i=0}^{k-1} p^i = \frac{p^k-1}{p-1}$ for $k \geq 1$.
So $\mathbb{O} = \left\{ \frac{p^k-1}{p-1} \mid k \in \mathbb{Z}, k \geq 1 \right\}$.

We are looking for all polynomials $f(x) \in \mathbb{R}[x]$ such that $f(\mathbb{O}) \subset \mathbb{O}$.
This means that for every $k \geq 1$, $f(o_k) \in \mathbb{O}$. So for each $k \geq 1$, there must exist an integer $m_k \geq 1$ such that $f(o_k) = o_{m_k} = \frac{p^{m_k}-1}{p-1}$.

Let $f(x) = a_d x^d + \dots + a_0$ with $a_i \in \mathbb{R}$.

If $f(x)$ is a constant polynomial, $f(x)=c$. Then $f(\mathbb{O})=\{c\}$. For $\{c\} \subset \mathbb{O}$, $c$ must be an element of $\mathbb{O}$. So $c = o_m = \frac{p^m-1}{p-1}$ for some integer $m \geq 1$.
Thus, constant polynomials $f(x) = \frac{p^m-1}{p-1}$ for $m \geq 1$ are solutions.

If $f(x)$ is not a constant polynomial, let $d = \deg(f) \geq 1$.
For $k \to \infty$, $o_k = \frac{p^k-1}{p-1} \sim \frac{p^k}{p-1} \to \infty$.
As $x \to \infty$, $f(x) \sim a_d x^d$. For $f(o_k) \in \mathbb{O}$, $f(o_k)$ must be positive for large $k$. This implies $a_d > 0$.
$f(o_k) \sim a_d \left(\frac{p^k}{p-1}\right)^d = \frac{a_d}{(p-1)^d} p^{kd}$.
Since $f(o_k) = o_{m_k} = \frac{p^{m_k}-1}{p-1} \sim \frac{p^{m_k}}{p-1}$, we have
$\frac{a_d}{(p-1)^d} p^{kd} \sim \frac{p^{m_k}}{p-1}$.
This suggests $p^{m_k} \sim \frac{a_d(p-1)}{(p-1)^d} p^{kd} = \frac{a_d}{(p-1)^{d-1}} p^{kd}$.
$m_k \approx \log_p\left(\frac{a_d}{(p-1)^{d-1}}\right) + kd$.
For large $k$, $m_k$ grows linearly with $k$, $m_k \sim kd$.

Let $y_k = p^k$. Then $o_k = \frac{y_k-1}{p-1}$. The condition $f(o_k) = o_{m_k}$ becomes $f\left(\frac{y_k-1}{p-1}\right) = \frac{p^{m_k}-1}{p-1}$.
Let $Q(y) = (p-1)f\left(\frac{y-1}{p-1}\right)+1$. $Q(y)$ is a polynomial in $y$ with real coefficients.
$Q(p^k) = (p-1)f\left(\frac{p^k-1}{p-1}\right)+1 = (p-1)o_{m_k}+1 = (p-1)\frac{p^{m_k}-1}{p-1}+1 = p^{m_k}-1+1 = p^{m_k}$.
So $Q(p^k) = p^{m_k}$ for all $k \geq 1$.
Let $Q(y) = c_d y^d + c_{d-1} y^{d-1} + \dots + c_1 y + c_0$. The degree of $Q(y)$ is $d$ if $f$ is not constant.
$c_d = \frac{a_d}{(p-1)^{d-1}}$.
For $k \geq 1$, $c_d (p^k)^d + c_{d-1} (p^k)^{d-1} + \dots + c_1 p^k + c_0 = p^{m_k}$.
$c_d p^{kd} + c_{d-1} p^{k(d-1)} + \dots + c_1 p^k + c_0 = p^{m_k}$.
Since $a_d > 0$, $c_d > 0$. For large $k$, the term $c_d p^{kd}$ dominates the LHS.
$p^{m_k} \approx c_d p^{kd}$. This implies $m_k \approx kd + \log_p(c_d)$.
Since $m_k$ and $k$ are integers, $m_k-kd$ must be an integer.
$p^{m_k-kd} = c_d + c_{d-1} p^{-k} + \dots + c_0 p^{-kd}$.
As $k \to \infty$, $p^{m_k-kd} \to c_d$. Since $m_k-kd$ is an integer for each $k$, for $p^{m_k-kd}$ to converge, $m_k-kd$ must converge to an integer, say $L$.
So $m_k - kd \to L \in \mathbb{Z}$ as $k \to \infty$.
$p^L = c_d$. Thus $c_d$ must be a power of $p$. Since $c_d \in \mathbb{R}$, $L$ can be any real number. However, $p^{m_k-kd} \to p^L$.
$p^{m_k-kd} - p^L = c_{d-1} p^{-k} + c_{d-2} p^{-2k} + \dots + c_0 p^{-kd}$.
$p^L (p^{m_k-kd-L}-1) = c_{d-1} p^{-k} + \dots + c_0 p^{-kd}$.
Let $\delta_k = m_k-kd-L$. $\delta_k \to 0$. Since $\delta_k$ is an integer, $\delta_k=0$ for $k$ large enough, say $k \geq K$.
So $m_k-kd-L = 0$, i.e., $m_k=kd+L$ for all $k \geq K$.
$Q(p^k) = p^{kd+L}$ for $k \geq K$.
The polynomial $Q(y)-p^L y^d$ has roots $p^K, p^{K+1}, \dots$. A non-zero polynomial has a finite number of roots.
So $Q(y)-p^L y^d$ must be the zero polynomial.
$Q(y) = p^L y^d$.
Comparing coefficients, $c_d=p^L$ and $c_{d-1}=\dots=c_0=0$.
$c_d = \frac{a_d}{(p-1)^{d-1}} = p^L$, which is consistent with $a_d>0$.
$c_0 = (p-1)f(0)+1 = 0$, so $f(0) = -\frac{1}{p-1}$. This contradicts $c_0=0$ unless $p^L=1$, so $L=0$.

Let's recheck $Q(y)=p^L y^d$.
$Q(y)=(p-1)f(\frac{y-1}{p-1})+1 = p^L y^d$.
Let $y=(p-1)x+1$. Then $x=\frac{y-1}{p-1}$.
$(p-1)f(x)+1 = p^L ((p-1)x+1)^d$.
$f(x) = \frac{p^L ((p-1)x+1)^d - 1}{p-1}$.
This is a polynomial in $x$ with real coefficients for any integers $d \geq 0$ and $L$.

We have $f(o_k) = o_{m_k}$ for all $k \geq 1$.
Substitute $x=o_k=\frac{p^k-1}{p-1}$ into the expression for $f(x)$:
$f(o_k) = \frac{p^L ((p-1)\frac{p^k-1}{p-1}+1)^d - 1}{p-1} = \frac{p^L (p^k-1+1)^d - 1}{p-1} = \frac{p^L (p^k)^d - 1}{p-1} = \frac{p^{kd+L}-1}{p-1} = o_{kd+L}$.
For $f(o_k)$ to be in $\mathbb{O}$ for all $k \geq 1$, the index $kd+L$ must be an integer $\geq 1$ for all $k \geq 1$.
Since $k \geq 1$ is an integer, $d$ and $L$ must be such that $kd+L$ is a positive integer for all $k \geq 1$.
If $d<0$, $kd \to -\infty$ as $k \to \infty$. $kd+L$ would be negative for large $k$. So $d \geq 0$.
$d$ must be an integer because it's the degree of the polynomial $f$. $d \geq 0$.
If $d \geq 1$, $kd+L \geq d+L$ for $k \geq 1$. So we need $d+L \geq 1$. Since $d \geq 1$, this means $1+L \geq 1$, so $L \geq 0$.
If $d=0$, $f(x) = \frac{p^L - 1}{p-1}$. This is a constant polynomial. It must be in $\mathbb{O}$.
$\frac{p^L-1}{p-1} = \frac{p^m-1}{p-1}$ for some $m \geq 1$. This implies $p^L=p^m$, so $L=m$. Thus $L \geq 1$.
For $d=0$, $kd+L = L$. $L \geq 1$ ensures $o_L \in \mathbb{O}$.
The condition $d+L \geq 1$ for $d \geq 0, L \in \mathbb{Z}$ covers both cases:
If $d=0$, $L \geq 1$.
If $d \geq 1$, $L \geq 0$.

$L$ must be an integer. $c_d=p^L$, $c_d = \frac{a_d}{(p-1)^{d-1}}$. $a_d = p^L(p-1)^{d-1}$. The coefficients of $f(x)$ are real if $L$ is real. However, $L$ arose as the limit of integers $m_k-kd$, so $L$ must be an integer.

So the polynomials are of the form $f(x) = \frac{p^L ((p-1)x+1)^d - 1}{p-1}$ where $d, L$ are integers satisfying $d \geq 0$, $L \geq 0$, and $d+L \geq 1$.

Final list of polynomials:
$f(x) = \frac{p^L ((p-1)x+1)^d - 1}{p-1}$ for integers $d \geq 0$, $L \geq 0$ such that $d+L \geq 1$.

Let's check $d=1, L=0$: $f(x) = \frac{p^0 ((p-1)x+1)^1 - 1}{p-1} = \frac{(p-1)x+1-1}{p-1} = x$. $d+L=1 \geq 1$. $f(x)=x$ is a solution.
Let's check $d=0, L=1$: $f(x) = \frac{p^1 ((p-1)x+1)^0 - 1}{p-1} = \frac{p-1}{p-1} = 1$. $d+L=1 \geq 1$. $f(x)=1$ is a solution. $1 = o_1 \in \mathbb{O}$.

The final answer is $\boxed{f(x) = \frac{p^L ((p-1)x+1)^d - 1}{p-1} \text{ for integers } d \geq 0, L \geq 0 \text{ with } d+L \geq 1}$.