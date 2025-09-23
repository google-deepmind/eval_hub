Let $P(x) = a_nx^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0$ be a polynomial with integer coefficients $a_0, \dots, a_n$.
We are given that $a_n = 5^k$ for some non-negative integer $k$, and $a_0 = 3^m$ for some non-negative integer $m$. Since $a_n$ is the leading coefficient of a polynomial of degree $n$, $a_n \ne 0$, which is true for $a_n=5^k$ for $k \ge 0$. The constant term $a_0=3^m$ is also non-zero for $m \ge 0$.

We are also given that $P(-1)$ is odd.
$P(-1) = a_n(-1)^n + a_{n-1}(-1)^{n-1} + \dots + a_1(-1) + a_0$.
Let $S = a_0 + a_1 + \dots + a_n$ be the sum of coefficients.
Let $A = P(-1) = a_0 - a_1 + a_2 - \dots + (-1)^n a_n$.
We are given $A \equiv 1 \pmod 2$.

Consider the sum $S+A$:
$S+A = (a_0 + a_1 + a_2 + \dots) + (a_0 - a_1 + a_2 - \dots) = 2a_0 + 2a_2 + 2a_4 + \dots = 2(a_0 + a_2 + a_4 + \dots)$.
Thus, $S+A$ is even, so $S+A \equiv 0 \pmod 2$.
Since $A \equiv 1 \pmod 2$, we have $S+1 \equiv 0 \pmod 2$, which implies $S \equiv 1 \pmod 2$.
The sum of the coefficients $S = a_0 + a_1 + \dots + a_n$ must be odd.

Now, suppose $P(x)$ has a rational root $r$. By the Rational Root Theorem, if $r = p/q$ is a rational root in lowest terms (where $p, q$ are integers, $q \ne 0$, and $\gcd(p, q) = 1$), then $p$ must divide $a_0$ and $q$ must divide $a_n$.

In this problem, $a_0 = 3^m$ and $a_n = 5^k$.
The divisors of $a_0 = 3^m$ are $\pm 3^j$ for $0 \le j \le m$. So $p$ must be of the form $\pm 3^j$.
The divisors of $a_n = 5^k$ are $\pm 5^l$ for $0 \le l \le k$. So $q$ must be of the form $\pm 5^l$.
We can write the rational root as $r = p/q = \frac{\pm 3^j}{\pm 5^l}$. We can absorb the signs into $p$. So $r = \pm \frac{3^j}{5^l}$ for $0 \le j \le m$ and $0 \le l \le k$.
Since $p/q$ is in lowest terms, $\gcd(p,q)=1$. For $p = \pm 3^j$ and $q = 5^l$, this condition is always satisfied because $p$ is only divisible by primes dividing 3 (i.e., 3) and $q$ is only divisible by primes dividing 5 (i.e., 5).

So any rational root $r=p/q$ must have $p = \pm 3^j$ and $q=5^l$ for some $0 \le j \le m, 0 \le l \le k$.
Note that $p = \pm 3^j$ is always an odd integer for $j \ge 0$.
Note that $q = 5^l$ is always an odd integer for $l \ge 0$.
So any rational root $p/q$ must be a ratio of two odd integers.

If $p/q$ is a root, then $P(p/q) = 0$. Multiplying by $q^n$, we get:
$a_n p^n + a_{n-1} p^{n-1} q + \dots + a_1 p q^{n-1} + a_0 q^n = 0$.

Let's consider this equation modulo 2.
Since $p$ and $q$ are odd, $p \equiv 1 \pmod 2$ and $q \equiv 1 \pmod 2$.
For any term $a_i p^i q^{n-i}$ with $0 \le i \le n$, we have:
$p^i q^{n-i} \equiv (1)^i (1)^{n-i} \equiv 1 \pmod 2$.
So, $a_i p^i q^{n-i} \equiv a_i \cdot 1 \equiv a_i \pmod 2$.

The equation $a_n p^n + a_{n-1} p^{n-1} q + \dots + a_1 p q^{n-1} + a_0 q^n = 0$ becomes modulo 2:
$a_n + a_{n-1} + \dots + a_1 + a_0 \equiv 0 \pmod 2$.
This means the sum of coefficients $S = a_0 + a_1 + \dots + a_n$ must be even.

However, from the condition that $P(-1)$ is odd, we deduced that $S = a_0 + a_1 + \dots + a_n$ must be odd.
This is a contradiction: $S \equiv 0 \pmod 2$ and $S \equiv 1 \pmod 2$.
This contradiction shows that the assumption that $P(x)$ has a rational root must be false.

Therefore, $P(x)$ has no rational roots.

The final answer is $\boxed{P(x) \text{ has no rational roots}}$.