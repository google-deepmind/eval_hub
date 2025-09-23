# Solution

I'll solve this problem step by step.

## Part 1: Showing that $f\left(\frac{2}{q}\right) \in \mathbb{Q}$

We're given that $f\left(\frac{1}{2^n}\right) \in \mathbb{Q}$ for some $n \in \mathbb{N}$, where $f(x) = \sum_{i=0}^\infty a_i x^i$ with $a_i \in \{0,1\}$.

The rationality of $f\left(\frac{1}{2^n}\right)$ implies that the sequence of coefficients $\{a_i\}$ is ultimately periodic. This follows from the fact that when evaluating a power series with coefficients in $\{0,1\}$ at a rational point, the result is rational if and only if the sequence of coefficients is ultimately periodic.

Let's say the sequence $\{a_i\}$ has a period of $l$ starting from index $k$. That is, for all $i \geq k$, we have $a_i = a_{i+l}$.

Now, let's compute $f\left(\frac{2}{q}\right)$ for any odd $q \geq 3$:

$$f\left(\frac{2}{q}\right) = \sum_{i=0}^\infty a_i \left(\frac{2}{q}\right)^i$$

We can split this into two parts:

$$f\left(\frac{2}{q}\right) = \sum_{i=0}^{k-1} a_i \left(\frac{2}{q}\right)^i + \sum_{i=k}^\infty a_i \left(\frac{2}{q}\right)^i$$

For the second part, using the periodicity of $\{a_i\}$:

$$\sum_{i=k}^\infty a_i \left(\frac{2}{q}\right)^i = \sum_{j=0}^{l-1} a_{k+j} \sum_{r=0}^\infty \left(\frac{2}{q}\right)^{k+j+rl}$$

This can be rewritten as:

$$\sum_{j=0}^{l-1} a_{k+j} \left(\frac{2}{q}\right)^{k+j} \sum_{r=0}^\infty \left[\left(\frac{2^l}{q^l}\right)^r\right]$$

Since $q \geq 3$, we have $\frac{2^l}{q^l} < 1$, so the geometric series converges to:

$$\sum_{r=0}^\infty \left(\frac{2^l}{q^l}\right)^r = \frac{1}{1-\frac{2^l}{q^l}} = \frac{q^l}{q^l-2^l}$$

Therefore:

$$f\left(\frac{2}{q}\right) = \sum_{i=0}^{k-1} a_i \left(\frac{2}{q}\right)^i + \sum_{j=0}^{l-1} a_{k+j} \left(\frac{2}{q}\right)^{k+j} \frac{q^l}{q^l-2^l}$$

This is clearly a rational expression, so $f\left(\frac{2}{q}\right) \in \mathbb{Q}$.

## Part 2: Showing that $\beta$ is odd

Now, let's examine the denominator when $f\left(\frac{2}{q}\right)$ is expressed in lowest terms as $\frac{\alpha}{\beta}$ with $\gcd(\alpha, \beta) = 1$.

In the expression for $f\left(\frac{2}{q}\right)$ above:
- The first part contributes denominators that are powers of $q$: $q^i$ for $i=1,2,\ldots,k-1$
- The second part contributes denominators of the form $q^{k+j} \cdot (q^l-2^l)$ for $j=0,1,\ldots,l-1$

When we express all these terms with a common denominator, we get a denominator that is the least common multiple (LCM) of all these individual denominators. Since $q^i$ divides $q^{k+j}$ for $i \leq k+j$, the LCM will be of the form $q^{k+l-1} \cdot (q^l-2^l)$.

Since $q$ is odd, $q^{k+l-1}$ is odd. Also, $q^l$ is odd and $2^l$ is even, so $q^l-2^l$ is odd. Therefore, the LCM $q^{k+l-1} \cdot (q^l-2^l)$ is odd.

When we simplify the fraction to lowest terms, the denominator $\beta$ must be a divisor of this LCM. Since any divisor of an odd number is odd, we conclude that $\beta$ is odd.

Therefore, for every odd natural number $q \geq 3$, we have:
1. $f\left(\frac{2}{q}\right) \in \mathbb{Q}$
2. When $f\left(\frac{2}{q}\right) = \frac{\alpha}{\beta}$ with $\gcd(\alpha, \beta) = 1$, $\beta$ is odd.