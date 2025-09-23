# Solution

I need to prove that a polynomial $P(x)=a_nx^n+\ldots+a_1x+a_0$ with integer coefficients, where $a_n$ is a power of 5, $a_0$ is a power of 3, and $P(-1)$ is odd, has no rational roots.

## Step 1: Analyze what form any rational root must take.

By the Rational Root Theorem, if $\frac{p}{q}$ is a rational root of $P(x)$ in lowest terms, then:
- $p$ divides $a_0$
- $q$ divides $a_n$

Since $a_0 = 3^m$ for some non-negative integer $m$, we have $p = 3^j$ for some $j \leq m$.
Since $a_n = 5^k$ for some non-negative integer $k$, we have $q = 5^l$ for some $l \leq k$.

Therefore, any rational root of $P(x)$ must be of the form $\frac{3^j}{5^l}$ where $j \leq m$ and $l \leq k$.

## Step 2: Derive a relation involving the coefficients of $P(x)$.

If $\frac{3^j}{5^l}$ is a root of $P(x)$, then:

$$P\left(\frac{3^j}{5^l}\right) = 0$$

This gives:

$$5^k\left(\frac{3^j}{5^l}\right)^n + a_{n-1}\left(\frac{3^j}{5^l}\right)^{n-1} + \ldots + a_1\left(\frac{3^j}{5^l}\right) + 3^m = 0$$

Multiplying both sides by $(5^l)^n$ to clear fractions:

$$5^k(3^j)^n + a_{n-1}(3^j)^{n-1}(5^l) + \ldots + a_1(3^j)(5^l)^{n-1} + 3^m(5^l)^n = 0$$

## Step 3: Analyze this relation modulo 2.

Since 3 and 5 are both odd, we have $3^j \equiv 1 \pmod{2}$ and $5^l \equiv 1 \pmod{2}$ for any $j, l \geq 0$. Thus, modulo 2:

$$1 + a_{n-1} + \ldots + a_1 + 1 \equiv 0 \pmod{2}$$

Simplifying:

$$a_{n-1} + \ldots + a_1 \equiv 0 \pmod{2}$$

This means the sum of the middle coefficients must be even.

## Step 4: Examine the constraint that $P(-1)$ is odd.

We have:

$$P(-1) = 5^k(-1)^n + a_{n-1}(-1)^{n-1} + \ldots + a_1(-1) + 3^m$$

Since $(-1)^n \equiv 1 \pmod{2}$ for any $n$ (because $(-1)^n$ is either 1 or -1, both of which are odd), and similarly $(-1)^i \equiv 1 \pmod{2}$ for any $i$, we get:

$$P(-1) \equiv 1 + a_{n-1} + \ldots + a_1 + 1 \pmod{2}$$
$$P(-1) \equiv a_{n-1} + \ldots + a_1 \pmod{2}$$

Since $P(-1)$ is odd, $P(-1) \equiv 1 \pmod{2}$, which means:

$$a_{n-1} + \ldots + a_1 \equiv 1 \pmod{2}$$

This means the sum of the middle coefficients must be odd.

## Step 5: Derive a contradiction.

From Step 3, we concluded that if $P(x)$ has a rational root, then the sum of the middle coefficients must be even.

From Step 4, we found that given $P(-1)$ is odd, the sum of the middle coefficients must be odd.

These two conditions contradict each other. Therefore, our initial assumption that $P(x)$ has a rational root must be false.

Hence, $P(x)$ has no rational roots.