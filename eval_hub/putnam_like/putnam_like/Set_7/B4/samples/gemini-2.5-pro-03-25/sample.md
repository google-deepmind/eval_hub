Let $\mathbb{O} = \{ n_k \mid k \in \mathbb{Z}, k \geq 1 \}$, where $n_k = \sum_{i=0}^{k-1} p^i = \frac{p^k-1}{p-1}$.
We are looking for polynomials $f(x) \in \mathbb{R}[x]$ such that $f(\mathbb{O}) \subset \mathbb{O}$.
This means that for every integer $k \ge 1$, there exists an integer $m_k \ge 1$ such that $f(n_k) = n_{m_k}$.

Let $f(x) = a_d x^d + a_{d-1} x^{d-1} + \dots + a_1 x + a_0$ be such a polynomial, where $a_d, \dots, a_0 \in \mathbb{R}$.
Let $d$ be the degree of $f(x)$. $d \ge 0$.

If $d=0$, then $f(x)=c$ for some constant $c \in \mathbb{R}$. The condition $f(\mathbb{O}) \subset \mathbb{O}$ means $c \in \mathbb{O}$.
So $c$ must be of the form $n_{k_0}$ for some integer $k_0 \ge 1$.
Thus, the constant solutions are $f(x) = n_{k_0}$ for any fixed integer $k_0 \ge 1$.

Now assume $d \ge 1$.
Let $x = n_k = \frac{p^k-1}{p-1}$. Then $(p-1)x + 1 = p^k$.
We have $f(n_k) = n_{m_k} = \frac{p^{m_k}-1}{p-1}$.
This implies $(p-1)f(n_k) + 1 = p^{m_k}$.

Let $g(x) = (p-1)f(x)+1$. This is also a polynomial with real coefficients. Let $g(x) = c_d x^d + \dots + c_0$.
The condition $f(n_k) = n_{m_k}$ becomes $g(n_k) = p^{m_k}$ for all $k \ge 1$.

Let's define a new polynomial $P(y)$ related to $g(x)$.
Let $x = \frac{y-1}{p-1}$. Then $y = (p-1)x+1$.
$P(y) = g(\frac{y-1}{p-1}) = (p-1) f(\frac{y-1}{p-1}) + 1$.
Since $f$ is a polynomial of degree $d$, $P(y)$ is also a polynomial of degree $d$. Let $P(y) = b_d y^d + \dots + b_0$.
The leading coefficient $b_d$ is related to $a_d$. $f(x) = a_d x^d + \dots$.
$f(\frac{y-1}{p-1}) = a_d (\frac{y-1}{p-1})^d + \dots = a_d \frac{y^d}{(p-1)^d} + \text{lower order terms}$.
$P(y) = (p-1) f(\frac{y-1}{p-1}) + 1 = (p-1) (a_d \frac{y^d}{(p-1)^d} + \dots) + 1 = \frac{a_d}{(p-1)^{d-1}} y^d + \dots$.
So $b_d = \frac{a_d}{(p-1)^{d-1}}$.

Let $y = p^k$. Then $x = \frac{p^k-1}{p-1} = n_k$.
The condition $g(n_k) = p^{m_k}$ translates to $P(p^k) = g(n_k) = p^{m_k}$.
So we have $P(p^k) = p^{m_k}$ for all integers $k \ge 1$.
$P(y) = b_d y^d + b_{d-1} y^{d-1} + \dots + b_1 y + b_0$.
$b_d p^{kd} + b_{d-1} p^{k(d-1)} + \dots + b_1 p^k + b_0 = p^{m_k}$ for all $k \ge 1$.

Let's evaluate this equation for large $k$.
$p^{m_k} = p^k (b_d p^{k(d-1)} + \dots + b_1) + b_0$.
This implies $p^k$ must divide $b_0$ for all sufficiently large $k$. This is only possible if $b_0 = 0$.
Then $P(y) = y P_1(y)$, where $P_1(y) = b_d y^{d-1} + \dots + b_1$.
The condition becomes $p^k P_1(p^k) = p^{m_k}$, so $P_1(p^k) = p^{m_k-k}$ for all $k \ge 1$.
$P_1(p^k) = p^k (b_d p^{k(d-2)} + \dots + b_2) + b_1$.
This implies $p^k$ must divide $b_1$ for all sufficiently large $k$. This forces $b_1=0$.
Continuing this argument, we conclude that $b_0 = b_1 = \dots = b_{d-1} = 0$.
So $P(y)$ must be of the form $P(y) = b_d y^d$.

The condition $P(p^k) = p^{m_k}$ becomes $b_d p^{kd} = p^{m_k}$.
This implies $b_d$ must be a power of $p$. Let $b_d = p^j$ for some integer $j$.
Then $p^j p^{kd} = p^{kd+j} = p^{m_k}$, which implies $m_k = kd+j$.

We need $m_k \ge 1$ for all $k \ge 1$.
The condition is $kd+j \ge 1$ for all $k \ge 1$.
Since $d \ge 1$, $kd+j$ is a non-decreasing function of $k$. The minimum value is attained at $k=1$.
So we need $d+j \ge 1$.

We have found that $P(y) = p^j y^d$ for some integer $j$ such that $d+j \ge 1$.
Recalling $P(y) = g(\frac{y-1}{p-1})$, we can find $g(x)$.
Let $y=(p-1)x+1$. Then $g(x) = P((p-1)x+1) = p^j ((p-1)x+1)^d$.
Since $g(x) = (p-1)f(x)+1$, we can find $f(x)$:
$f(x) = \frac{g(x)-1}{p-1} = \frac{p^j ((p-1)x+1)^d - 1}{p-1}$.

This formula also includes the constant solutions. If we set $d=0$, $f(x) = \frac{p^j ((p-1)x+1)^0 - 1}{p-1} = \frac{p^j-1}{p-1} = n_j$.
For $f(x)=n_j$ to be a solution, we need $n_j \in \mathbb{O}$, which requires $j \ge 1$.
The condition $m_k \ge 1$ for $d=0$ becomes $j \ge 1$. So $f(x) = n_j$ for $j \ge 1$.

Let's consolidate the conditions on $d$ and $j$.
$d$ is the degree of the polynomial, so $d \in \mathbb{Z}_{\ge 0}$.
$j$ is an integer derived from $b_d=p^j$.
The requirement $f(n_k) \in \mathbb{O}$ translates to $m_k = kd+j \ge 1$ for all $k \ge 1$.
- If $d=0$, $m_k=j$. The condition is $j \ge 1$.
- If $d \ge 1$, the condition $kd+j \ge 1$ for all $k \ge 1$ is equivalent to $d+j \ge 1$ (its value at $k=1$).

So the set of solutions is the set of polynomials $f_{d,j}(x)$ defined by
$$ f_{d,j}(x) = \frac{p^j ((p-1)x+1)^d - 1}{p-1} $$
where $d, j$ are integers such that $d \ge 0$, and either ($d=0$ and $j \ge 1$) or ($d \ge 1$ and $d+j \ge 1$).

Let's check the polynomial form:
$f_{d,j}(x) = \frac{p^j \sum_{i=0}^d \binom{d}{i} ((p-1)x)^i - 1}{p-1} = \frac{p^j (1 + \sum_{i=1}^d \binom{d}{i} (p-1)^i x^i) - 1}{p-1}$
$f_{d,j}(x) = \frac{p^j-1}{p-1} + \frac{p^j}{p-1} \sum_{i=1}^d \binom{d}{i} (p-1)^i x^i = n_j + p^j \sum_{i=1}^d \binom{d}{i} (p-1)^{i-1} x^i$.
This is indeed a polynomial of degree $d$ (if $d \ge 1$). If $d=0$, the sum is empty and $f_{0,j}(x) = n_j$.
The coefficients are real (in fact, they are rational).

The solutions are:
1. Constant polynomials: $f(x) = n_j$ for $j \in \mathbb{Z}, j \ge 1$. These correspond to $(d,j)=(0,j)$ with $j \ge 1$.
2. Non-constant polynomials: $f(x) = \frac{p^j ((p-1)x+1)^d - 1}{p-1}$ for integers $d \ge 1$ and $j \ge 1-d$. These correspond to $(d,j)$ with $d \ge 1, d+j \ge 1$.

Both cases can be combined into the single formula $f_{d,j}(x) = \frac{p^j ((p-1)x+1)^d - 1}{p-1}$ for integers $d \ge 0, j \in \mathbb{Z}$ satisfying the condition $(d=0 \implies j \ge 1)$ and $(d \ge 1 \implies d+j \ge 1)$.

Final Answer: The final answer is $\boxed{f(x) = \frac{p^j ((p-1)x+1)^d - 1}{p-1} \text{ for integers } d \ge 0, j \in \mathbb{Z} \text{ s.t. } (d=0 \implies j \ge 1) \text{ and } (d \ge 1 \implies d+j \ge 1)}$