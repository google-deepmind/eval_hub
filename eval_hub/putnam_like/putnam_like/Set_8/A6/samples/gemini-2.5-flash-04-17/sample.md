Let $I$ be the given integral:
\[
 I = \int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx.
\]
Since $f$ is strictly decreasing and $\lim_{x\to\infty}f(x)=0$, $f(x)>0$ for all $x\ge 0$. Indeed, if $f(x_0) \le 0$ for some $x_0$, then for any $x > x_0$, $f(x) < f(x_0) \le 0$ by strict monotonicity. This contradicts $\lim_{x\to\infty}f(x)=0$, which implies $f(x)>0$ for sufficiently large $x$.

For $x \ge \alpha$, we have $x-\alpha \ge 0$ and $x+\alpha \ge 2\alpha > 0$. Since $f$ is strictly decreasing, $f(x-\alpha) > f(x)$ and $f(x) > f(x+\alpha)$. Thus, $f(x-\alpha)-f(x+\alpha) > 0$. The integrand $\frac{f(x-\alpha)-f(x+\alpha)}{f(x)}$ is positive for $x \ge \alpha$.

Let's make the substitution $y=x-\alpha$ in the integral. Then $x=y+\alpha$ and $dx=dy$. When $x=\alpha$, $y=0$. When $x\to\infty$, $y\to\infty$.
The integral becomes:
\[
 I = \int_0^\infty \frac{f(y)-f(y+2\alpha)}{f(y+\alpha)}dy.
\]
We can split the integrand:
\[
 \frac{f(y)-f(y+2\alpha)}{f(y+\alpha)} = \frac{f(y)-f(y+\alpha) + f(y+\alpha)-f(y+2\alpha)}{f(y+\alpha)} = \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} + \frac{f(y+\alpha)-f(y+2\alpha)}{f(y+\alpha)}.
\]
So the integral is
\[
 I = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy + \int_0^\infty \frac{f(y+\alpha)-f(y+2\alpha)}{f(y+\alpha)}dy.
\]
Let's make a substitution in the second integral. Let $u=y+\alpha$. Then $y=u-\alpha$ and $dy=du$. When $y=0$, $u=\alpha$. When $y\to\infty$, $u\to\infty$.
\[
 \int_0^\infty \frac{f(y+\alpha)-f(y+2\alpha)}{f(y+\alpha)}dy = \int_\alpha^\infty \frac{f(u)-f(u+\alpha)}{f(u)}du.
\]
So,
\[
 I = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy + \int_\alpha^\infty \frac{f(y)-f(y+\alpha)}{f(y)}dy.
\]
(We replaced $u$ by $y$ in the second integral).

Since $f$ is strictly decreasing, for $y \ge 0$, $f(y) > f(y+\alpha) > f(y+2\alpha)$. Both integrands are positive.
We split the first integral $\int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy$ into intervals $[n\alpha, (n+1)\alpha)$ for $n=0, 1, 2, \dots$.
\[
 \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy = \sum_{n=0}^\infty \int_{n\alpha}^{(n+1)\alpha} \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy.
\]
For $y \in [n\alpha, (n+1)\alpha)$:
$y+\alpha \in [(n+1)\alpha, (n+2)\alpha]$. Since $f$ is strictly decreasing, $f(y+\alpha) \le f((n+1)\alpha)$.
$y \in [n\alpha, (n+1)\alpha]$. Since $f$ is strictly decreasing, $f(y) \ge f((n+1)\alpha)$.
$y+\alpha \in [(n+1)\alpha, (n+2)\alpha]$. Since $f$ is strictly decreasing, $f(y+\alpha) \ge f((n+2)\alpha)$.
So, $f(y)-f(y+\alpha) \ge f((n+1)\alpha) - f((n+2)\alpha)$.

Therefore, for $y \in [n\alpha, (n+1)\alpha)$:
\[
 \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} \ge \frac{f((n+1)\alpha)-f((n+2)\alpha)}{f((n+1)\alpha)}.
\]
This gives a lower bound for the integral over $[n\alpha, (n+1)\alpha)$:
\[
 \int_{n\alpha}^{(n+1)\alpha} \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy \ge \int_{n\alpha}^{(n+1)\alpha} \frac{f((n+1)\alpha)-f((n+2)\alpha)}{f((n+1)\alpha)}dy = \alpha \frac{f((n+1)\alpha)-f((n+2)\alpha)}{f((n+1)\alpha)}.
\]
Let $a_n = f(n\alpha)$ for $n=0, 1, 2, \dots$. The sequence $a_n$ is strictly decreasing, $a_n > 0$, and $a_n \to 0$ as $n\to\infty$.
The lower bound for the first integral is
\[
 \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy \ge \alpha \sum_{n=0}^\infty \frac{a_{n+1}-a_{n+2}}{a_{n+1}}.
\]
Let $k=n+1$. The sum is $\sum_{k=1}^\infty \frac{a_k-a_{k+1}}{a_k}$.
Since $a_k > 0$ is a strictly decreasing sequence with $a_k \to 0$, the series $\sum_{k=1}^\infty \frac{a_k-a_{k+1}}{a_k}$ diverges to $\infty$.
To show this, consider $\ln(a_{k+1}/a_k)$. Since $a_{k+1} < a_k$, $a_{k+1}/a_k < 1$, so $\ln(a_{k+1}/a_k) < 0$.
$\sum_{k=1}^N \ln(a_{k+1}/a_k) = \sum_{k=1}^N (\ln a_{k+1} - \ln a_k) = \ln a_{N+1} - \ln a_1$.
As $N\to\infty$, $a_{N+1} \to 0$, so $\ln a_{N+1} \to -\infty$. Thus, $\sum_{k=1}^\infty \ln(a_{k+1}/a_k) = -\infty$.
Using the inequality $\ln x \le x-1$ for $x>0$:
$\ln(a_{k+1}/a_k) \le a_{k+1}/a_k - 1 = -\frac{a_k-a_{k+1}}{a_k}$.
Summing over $k$: $\sum_{k=1}^\infty \ln(a_{k+1}/a_k) \le -\sum_{k=1}^\infty \frac{a_k-a_{k+1}}{a_k}$.
Since the left side is $-\infty$, the right side must be $-\infty$ or $-\infty$. But $\frac{a_k-a_{k+1}}{a_k} > 0$, so $\sum \frac{a_k-a_{k+1}}{a_k}$ is a series of positive terms.
Thus, $\sum_{k=1}^\infty \frac{a_k-a_{k+1}}{a_k}$ diverges to $\infty$.

The first integral $\int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy \ge \alpha \sum_{k=1}^\infty \frac{a_k-a_{k+1}}{a_k} = \infty$.
Since this first integral diverges to $\infty$ and the second integral $\int_\alpha^\infty \frac{f(y)-f(y+\alpha)}{f(y)}dy$ is an integral of a positive function, which is either finite or $\infty$, the sum of the two integrals must be $\infty$.

Specifically, $I = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy + \int_\alpha^\infty \frac{f(y)-f(y+\alpha)}{f(y)}dy$.
The second integral $\int_\alpha^\infty \frac{f(y)-f(y+\alpha)}{f(y)}dy$ is non-negative because $f(y) > f(y+\alpha)$ and $f(y)>0$.
Since $\int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)}dy = \infty$, we have $I = \infty + (\text{a non-negative value}) = \infty$.

The final answer is $\boxed{\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx= \infty}$.