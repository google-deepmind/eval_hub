Solution:

Let $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ be a polynomial with integer coefficients $a_i \in \mathbb{Z}$.
We are given the following conditions:
1. The leading coefficient $a_n$ is a power of 5, so $a_n = 5^k$ for some integer $k \ge 0$.
2. The constant term $a_0$ is a power of 3, so $a_0 = 3^m$ for some integer $m \ge 0$.
3. $P(-1)$ is an odd integer.

We want to prove that $P(x)$ has no rational roots.
We will use proof by contradiction. Assume that $P(x)$ has a rational root $x_0$.
Let $x_0 = \frac{p}{q}$, where $p, q \in \mathbb{Z}$, $q \neq 0$, and $\gcd(p, q) = 1$.

According to the Rational Root Theorem, if $\frac{p}{q}$ is a rational root of the polynomial $P(x)$ with integer coefficients, then $p$ must divide the constant term $a_0$, and $q$ must divide the leading coefficient $a_n$.

From the given conditions:
1. $p$ must divide $a_0 = 3^m$. The only divisors of $3^m$ are of the form $\pm 3^j$ for $0 \le j \le m$. Thus, $p = \pm 3^j$ for some integer $j$ with $0 \le j \le m$.
2. $q$ must divide $a_n = 5^k$. The only divisors of $5^k$ are of the form $\pm 5^l$ for $0 \le l \le k$. Thus, $q = \pm 5^l$ for some integer $l$ with $0 \le l \le k$.

Since $p = \pm 3^j$, $p$ is non-zero because $3^j \ge 3^0 = 1$.
Since $q = \pm 5^l$, $q$ is non-zero because $5^l \ge 5^0 = 1$.
The condition $\gcd(p, q) = 1$ is satisfied because the only prime factor of $p$ (if $j>0$) is 3, and the only prime factor of $q$ (if $l>0$) is 5. If $j=0$, $p=\pm 1$. If $l=0$, $q=\pm 1$. In all cases, $p$ and $q$ share no common prime factors, so $\gcd(p, q) = 1$.

Now let's examine the parity of $p$ and $q$.
Since 3 is an odd number, $3^j$ is odd for all $j \ge 0$. Therefore, $p = \pm 3^j$ is an odd integer.
Since 5 is an odd number, $5^l$ is odd for all $l \ge 0$. Therefore, $q = \pm 5^l$ is an odd integer.

Since $x_0 = \frac{p}{q}$ is a root of $P(x)$, we have $P(\frac{p}{q}) = 0$.
$a_n \left(\frac{p}{q}\right)^n + a_{n-1} \left(\frac{p}{q}\right)^{n-1} + \dots + a_1 \left(\frac{p}{q}\right) + a_0 = 0$.
Multiply the entire equation by $q^n$ to clear the denominators:
$a_n p^n + a_{n-1} p^{n-1} q + \dots + a_1 p q^{n-1} + a_0 q^n = 0$.

Now, consider this equation modulo 2. Since $p$ and $q$ are odd integers, we have $p \equiv 1 \pmod 2$ and $q \equiv 1 \pmod 2$.
Consequently, $p^i \equiv 1^i \equiv 1 \pmod 2$ and $q^i \equiv 1^i \equiv 1 \pmod 2$ for any non-negative integer $i$.
Reducing the equation modulo 2, we get:
$a_n (1)^n + a_{n-1} (1)^{n-1} (1) + \dots + a_1 (1) (1)^{n-1} + a_0 (1)^n \equiv 0 \pmod 2$.
$a_n + a_{n-1} + \dots + a_1 + a_0 \equiv 0 \pmod 2$.
The sum $a_n + a_{n-1} + \dots + a_1 + a_0$ is exactly $P(1)$.
So, the existence of a rational root $\frac{p}{q}$ implies that $P(1)$ must be an even integer. $P(1) \equiv 0 \pmod 2$.

Now let's use the given condition that $P(-1)$ is odd.
$P(-1) = a_n (-1)^n + a_{n-1} (-1)^{n-1} + \dots - a_1 + a_0$.
Since $P(-1)$ is odd, we have $P(-1) \equiv 1 \pmod 2$.

Let's consider the relationship between $P(1)$ and $P(-1)$ modulo 2.
$P(1) = \sum_{i=0}^n a_i$.
$P(-1) = \sum_{i=0}^n a_i (-1)^i$.
Considering $P(-1)$ modulo 2:
$P(-1) \equiv \sum_{i=0}^n a_i (-1)^i \pmod 2$.
Since $-1 \equiv 1 \pmod 2$, we have $(-1)^i \equiv 1^i \equiv 1 \pmod 2$ for all $i \ge 0$.
Therefore, $P(-1) \equiv \sum_{i=0}^n a_i (1) \pmod 2$.
$P(-1) \equiv \sum_{i=0}^n a_i \pmod 2$.
This is the same expression as $P(1) \pmod 2$.
So, $P(1) \equiv P(-1) \pmod 2$.
This means that $P(1)$ and $P(-1)$ must have the same parity for any polynomial with integer coefficients.

We have deduced the following:
1. If $P(x)$ has a rational root, then $P(1)$ must be even. So $P(1) \equiv 0 \pmod 2$.
2. We are given that $P(-1)$ is odd. So $P(-1) \equiv 1 \pmod 2$.
3. We know that $P(1) \equiv P(-1) \pmod 2$.

Substituting the results from (1) and (2) into (3), we get:
$0 \equiv 1 \pmod 2$.
This is a contradiction.

Therefore, our initial assumption that $P(x)$ has a rational root must be false.
Conclusion: The polynomial $P(x)$ has no rational roots.

Final Answer: The final answer is $\boxed{P(x) \text{ has no rational roots}}$