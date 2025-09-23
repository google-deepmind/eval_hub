Here is a detailed, step-by-step solution to the problem.

### Preliminaries: Analysis of the function `f`

First, let's establish some properties of the function $f$ based on the given conditions.
We are given that $f:[0,\infty)\to\mathbb{R}$ is a strictly decreasing continuous function and $\lim_{x\to\infty}f(x)=0$.

We will prove that $f(x) > 0$ for all $x \in [0, \infty)$.
Assume, for the sake of contradiction, that there exists some $x_0 \in [0, \infty)$ such that $f(x_0) \le 0$.
Since $f$ is strictly decreasing, for any $x > x_0$, we must have $f(x) < f(x_0)$.
This implies that for all $x > x_0$, $f(x) < f(x_0) \le 0$.
The sequence of values $f(x)$ for $x > x_0$ is a set of negative numbers, bounded above by $f(x_0) \le 0$.
If $f(x_0) < 0$, then $\lim_{x\to\infty} f(x) \le f(x_0) < 0$. This contradicts the given condition that $\lim_{x\to\infty}f(x)=0$.
If $f(x_0) = 0$, then for any $x > x_0$, we have $f(x) < f(x_0) = 0$. So, for $x > x_0$, $f(x)$ is a strictly decreasing function of negative values. A strictly decreasing sequence of negative numbers cannot converge to 0; its limit must be strictly negative. For example, for any $x_1 > x_0$, all values $f(x)$ for $x > x_1$ are less than $f(x_1)$, which is a negative number. Thus, the limit cannot be 0. This again contradicts $\lim_{x\to\infty}f(x)=0$.

Therefore, our initial assumption must be false. We must have $f(x) > 0$ for all $x \in [0, \infty)$.

### Analysis of the Integrand

Let the integrand be $g(x) = \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}$. The integral is well-defined for $x \ge \alpha$.
Since $f(x) > 0$ for all $x$, the denominator is always positive.
For the numerator, we are given that $f$ is strictly decreasing and $\alpha > 0$. This means for any $x$, we have $x-\alpha < x < x+\alpha$.
Because $f$ is strictly decreasing, $f(x-\alpha) > f(x) > f(x+\alpha)$.
Thus, the numerator $f(x-\alpha) - f(x+\alpha)$ is strictly positive.
The integrand $g(x)$ is the ratio of a positive number and a positive number, so $g(x) > 0$ for all $x \ge \alpha$.

Since we are integrating a positive function, the improper integral $\int_\alpha^\infty g(x)dx$ will either converge to a positive value or diverge to $+\infty$. Our goal is to prove it diverges.

### Strategy: Decomposing the Integral

We will prove the divergence of the integral by comparing it to a divergent series. We can express the integral as a sum of integrals over adjacent intervals. A convenient choice for the length of these intervals is $2\alpha$.

$$
\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx = \sum_{n=1}^\infty \int_{(2n-1)\alpha}^{(2n+1)\alpha} \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx
$$

Let's denote the integral over the $n$-th interval as $J_n$:
$$
J_n = \int_{(2n-1)\alpha}^{(2n+1)\alpha} \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx
$$

We will find a lower bound for each $J_n$ and show that the sum of these lower bounds diverges.

### Step-by-Step Derivation

**Step 1: Find a lower bound for the integrand in the interval $[(2n-1)\alpha, (2n+1)\alpha]$.**

For $x \in [(2n-1)\alpha, (2n+1)\alpha]$, since $f$ is a decreasing function, the value of $f(x)$ is at most its value at the left endpoint of the interval.
$$
f(x) \le f((2n-1)\alpha)
$$
Since $f(x)>0$, we have:
$$
\frac{1}{f(x)} \ge \frac{1}{f((2n-1)\alpha)}
$$
Using this, we can find a lower bound for $J_n$:
$$
J_n \ge \int_{(2n-1)\alpha}^{(2n+1)\alpha} \frac{f(x-\alpha)-f(x+\alpha)}{f((2n-1)\alpha)}dx = \frac{1}{f((2n-1)\alpha)} \int_{(2n-1)\alpha}^{(2n+1)\alpha} [f(x-\alpha)-f(x+\alpha)]dx
$$

**Step 2: Evaluate the integral term.**

Let's evaluate the integral in the expression above. We can split it into two parts:
$$
\int_{(2n-1)\alpha}^{(2n+1)\alpha} f(x-\alpha)dx - \int_{(2n-1)\alpha}^{(2n+1)\alpha} f(x+\alpha)dx
$$
For the first integral, let $u = x-\alpha$. Then $du=dx$. The limits of integration become $(2n-1)\alpha - \alpha = (2n-2)\alpha$ and $(2n+1)\alpha - \alpha = 2n\alpha$.
For the second integral, let $v = x+\alpha$. Then $dv=dx$. The limits become $(2n-1)\alpha + \alpha = 2n\alpha$ and $(2n+1)\alpha + \alpha = (2n+2)\alpha$.
So the expression becomes:
$$
\int_{(2n-2)\alpha}^{2n\alpha} f(u)du - \int_{2n\alpha}^{(2n+2)\alpha} f(v)dv
$$

**Step 3: Find a lower bound for the difference of integrals.**

Since $f$ is a continuous decreasing function, for an interval $[a,b]$, we have the bounds:
$(b-a)f(b) \le \int_a^b f(x)dx \le (b-a)f(a)$.

Let's find a lower bound for $\int_{(2n-2)\alpha}^{2n\alpha} f(u)du$ and an upper bound for $\int_{2n\alpha}^{(2n+2)\alpha} f(v)dv$.

- For the first integral, we split the interval $[(2n-2)\alpha, 2n\alpha]$ into $[(2n-2)\alpha, (2n-1)\alpha]$ and $[(2n-1)\alpha, 2n\alpha]$.
$$
\int_{(2n-2)\alpha}^{2n\alpha} f(u)du = \int_{(2n-2)\alpha}^{(2n-1)\alpha} f(u)du + \int_{(2n-1)\alpha}^{2n\alpha} f(u)du
$$
Using the property $\int_a^b f(x)dx \ge (b-a)f(b)$:
$$
\ge \alpha \cdot f((2n-1)\alpha) + \alpha \cdot f(2n\alpha)
$$

- For the second integral, we split the interval $[2n\alpha, (2n+2)\alpha]$ into $[2n\alpha, (2n+1)\alpha]$ and $[(2n+1)\alpha, (2n+2)\alpha]$.
$$
\int_{2n\alpha}^{(2n+2)\alpha} f(v)dv = \int_{2n\alpha}^{(2n+1)\alpha} f(v)dv + \int_{(2n+1)\alpha}^{(2n+2)\alpha} f(v)dv
$$
Using the property $\int_a^b f(x)dx \le (b-a)f(a)$:
$$
\le \alpha \cdot f(2n\alpha) + \alpha \cdot f((2n+1)\alpha)
$$

Now, we can find a lower bound for the difference of the integrals:
$$
\int_{(2n-2)\alpha}^{2n\alpha} f(u)du - \int_{2n\alpha}^{(2n+2)\alpha} f(v)dv \ge [\alpha f((2n-1)\alpha) + \alpha f(2n\alpha)] - [\alpha f(2n\alpha) + \alpha f((2n+1)\alpha)]
$$
$$
= \alpha [f((2n-1)\alpha) - f((2n+1)\alpha)]
$$

**Step 4: Combine the bounds to get a lower bound for $J_n$.**

Substituting this back into our inequality for $J_n$:
$$
J_n \ge \frac{1}{f((2n-1)\alpha)} \cdot \alpha [f((2n-1)\alpha) - f((2n+1)\alpha)]
$$
$$
J_n \ge \alpha \left( \frac{f((2n-1)\alpha)}{f((2n-1)\alpha)} - \frac{f((2n+1)\alpha)}{f((2n-1)\alpha)} \right) = \alpha \left(1 - \frac{f((2n+1)\alpha)}{f((2n-1)\alpha)}\right)
$$

**Step 5: Show that the sum of the lower bounds diverges.**

The total integral is bounded below by the sum of these $J_n$:
$$
\int_\alpha^\infty g(x)dx = \sum_{n=1}^\infty J_n \ge \sum_{n=1}^\infty \alpha \left(1 - \frac{f((2n+1)\alpha)}{f((2n-1)\alpha)}\right)
$$
Let's define a sequence $a_n = f((2n-1)\alpha)$ for $n=1, 2, 3, \ldots$.
Since $f$ is strictly decreasing and positive, $\{a_n\}$ is a strictly decreasing sequence of positive numbers.
Also, as $n\to\infty$, $(2n-1)\alpha \to \infty$, so $\lim_{n\to\infty} a_n = \lim_{n\to\infty} f((2n-1)\alpha) = 0$.
The term in the sum can be written as $1 - a_{n+1}/a_n$, since $(2(n+1)-1)\alpha = (2n+1)\alpha$.
So we need to prove that the series $\sum_{n=1}^\infty \left(1 - \frac{a_{n+1}}{a_n}\right)$ diverges.

We use the fundamental inequality $\ln(x) \le x-1$ for $x>0$, which implies $1-x \ge -\ln(x)$.
Let $x = a_{n+1}/a_n$. Since $\{a_n\}$ is a strictly decreasing sequence of positive numbers, $0 < a_{n+1} < a_n$, so $0 < x < 1$.
Thus, $1 - \frac{a_{n+1}}{a_n} \ge -\ln\left(\frac{a_{n+1}}{a_n}\right) = \ln(a_n) - \ln(a_{n+1})$.

Let $S_N$ be the $N$-th partial sum of the series of lower bounds:
$$
S_N = \sum_{n=1}^N \alpha \left(1 - \frac{a_{n+1}}{a_n}\right) \ge \alpha \sum_{n=1}^N (\ln(a_n) - \ln(a_{n+1}))
$$
The sum on the right is a telescoping series:
$$
\sum_{n=1}^N (\ln(a_n) - \ln(a_{n+1})) = (\ln(a_1) - \ln(a_2)) + (\ln(a_2) - \ln(a_3)) + \dots + (\ln(a_N) - \ln(a_{N+1}))
$$
$$
= \ln(a_1) - \ln(a_{N+1})
$$
So, $S_N \ge \alpha(\ln(a_1) - \ln(a_{N+1}))$.

Now we take the limit as $N\to\infty$:
$$
\lim_{N\to\infty} S_N \ge \lim_{N\to\infty} \alpha(\ln(a_1) - \ln(a_{N+1}))
$$
We know that $\lim_{N\to\infty} a_{N+1} = 0$, and since $a_{N+1} > 0$, we have $\lim_{N\to\infty} \ln(a_{N+1}) = -\infty$.
Therefore,
$$
\lim_{N\to\infty} \alpha(\ln(a_1) - \ln(a_{N+1})) = \alpha(\ln(a_1) - (-\infty)) = +\infty
$$
By the comparison test for series, since the partial sums $S_N$ are bounded below by a sequence that diverges to $+\infty$, the series $\sum_{n=1}^\infty \alpha \left(1 - \frac{a_{n+1}}{a_n}\right)$ must also diverge to $+\infty$.

Since $\int_\alpha^\infty g(x)dx \ge \sum_{n=1}^\infty J_n$, and the sum of the lower bounds for $J_n$ diverges to $+\infty$, the integral itself must diverge to $+\infty$.

### Conclusion

We have shown that:
1. The integrand is strictly positive.
2. The integral can be written as an infinite sum of integrals over intervals of length $2\alpha$.
3. We found a lower bound for each term in this sum, of the form $\alpha(1 - a_{n+1}/a_n)$.
4. We proved that the series of these lower bounds diverges to $+\infty$ by comparing it to a telescoping sum of logarithms.

Therefore, we conclude that
$$
\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx = \infty.
$$