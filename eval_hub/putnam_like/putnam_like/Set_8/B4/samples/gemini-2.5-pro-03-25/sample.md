Let $X$ and $Y$ be independent random variables uniformly distributed in the interval $(0, 1)$. We are interested in the probability that $\left[\frac{\ln(X)}{\ln(Y)}\right]$ is an even integer. Let $Z = \frac{\ln(X)}{\ln(Y)}$.

Since $X, Y \in (0, 1)$, their logarithms $\ln(X)$ and $\ln(Y)$ are both negative. Therefore, $Z = \frac{\ln(X)}{\ln(Y)}$ is strictly positive, $Z > 0$.
Let $k = [Z]$ denote the greatest integer less than or equal to $Z$. Since $Z > 0$, $k$ can be any integer $k \ge 0$.
We want to find the probability that $k$ is even, i.e., $k \in \{0, 2, 4, \dots\}$.

The condition $[Z] = k$ is equivalent to $k \le Z < k+1$.
So we want to compute the probability $P([Z] \text{ is even}) = P(\bigcup_{j=0}^\infty \{ Z \in [2j, 2j+1) \})$.
Since these intervals are disjoint, the probability is the sum of the probabilities for each interval:
$$ P([Z] \text{ is even}) = \sum_{j=0}^\infty P(2j \le Z < 2j+1) $$

Let's compute $P(k \le Z < k+1)$ for a general integer $k \ge 0$.
The condition is $k \le \frac{\ln(X)}{\ln(Y)} < k+1$.
Since $Y \in (0, 1)$, $\ln(Y) < 0$. Multiplying the inequality by $\ln(Y)$ reverses the inequality signs:
$$ k \ln(Y) \ge \ln(X) > (k+1) \ln(Y) $$
This can be written as $(k+1) \ln(Y) < \ln(X) \le k \ln(Y)$.
Since the exponential function $t \mapsto e^t$ is strictly increasing, we can exponentiate the inequalities:
$$ e^{(k+1) \ln(Y)} < X \le e^{k \ln(Y)} $$
$$ Y^{k+1} < X \le Y^k $$
The random variables $X$ and $Y$ are independent and uniformly distributed on $(0, 1)$. Their joint probability density function is $f(x, y) = 1$ for $(x, y) \in (0, 1)^2$, and $0$ otherwise.
The probability $P(k \le Z < k+1)$ is the area of the region $R_k$ in the $xy$-plane defined by:
$$ R_k = \{(x, y) \mid 0 < x < 1, 0 < y < 1, Y^{k+1} < X \le Y^k \} $$
The area is given by the integral:
$$ P(k \le Z < k+1) = \iint_{R_k} 1 \, dx \, dy = \int_0^1 \int_{y^{k+1}}^{y^k} dx \, dy $$
For $y \in (0, 1)$ and $k \ge 0$, we have $k+1 > k$, so $y^{k+1} < y^k$. Thus, the integration interval for $x$ is valid.
The inner integral is $\int_{y^{k+1}}^{y^k} dx = [x]_{y^{k+1}}^{y^k} = y^k - y^{k+1}$.
The outer integral is:
$$ \int_0^1 (y^k - y^{k+1}) dy = \left[ \frac{y^{k+1}}{k+1} - \frac{y^{k+2}}{k+2} \right]_0^1 $$
$$ = \left(\frac{1}{k+1} - \frac{1}{k+2}\right) - (0 - 0) = \frac{1}{k+1} - \frac{1}{k+2} $$
$$ = \frac{(k+2) - (k+1)}{(k+1)(k+2)} = \frac{1}{(k+1)(k+2)} $$
So, $P(k \le Z < k+1) = \frac{1}{k+1} - \frac{1}{k+2}$.

We want to compute the sum of these probabilities for all even integers $k \ge 0$. So we sum over $k = 2j$ for $j=0, 1, 2, \dots$.
$$ P([Z] \text{ is even}) = \sum_{j=0}^\infty P(2j \le Z < 2j+1) = \sum_{j=0}^\infty \left( \frac{1}{2j+1} - \frac{1}{2j+2} \right) $$
Let's write out the first few terms of the series:
For $j=0$: $\frac{1}{1} - \frac{1}{2}$
For $j=1$: $\frac{1}{3} - \frac{1}{4}$
For $j=2$: $\frac{1}{5} - \frac{1}{6}$
...
The sum is:
$$ P([Z] \text{ is even}) = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \left(\frac{1}{5} - \frac{1}{6}\right) + \dots $$
This is the well-known alternating harmonic series. The Taylor series expansion for $\ln(1+x)$ around $x=0$ is:
$$ \ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots = \sum_{n=1}^\infty (-1)^{n-1} \frac{x^n}{n} $$
This series converges for $-1 < x \le 1$. Setting $x=1$, we get:
$$ \ln(1+1) = \ln(2) = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \dots $$
The sum we have obtained for $P([Z] \text{ is even})$ is exactly this series.
Therefore, the probability that $\left[\frac{\ln(X)}{\ln(Y)}\right]$ is even is $\ln(2)$.

Alternative method check:
Let $U = -\ln X$ and $V = -\ln Y$. Since $X, Y \sim U(0, 1)$, $U$ and $V$ are independent and follow the Exponential(1) distribution, with PDF $f(t) = e^{-t}$ for $t > 0$.
Then $Z = \frac{-U}{-V} = \frac{U}{V}$. We want $P([U/V] \text{ is even})$.
$P(k \le U/V < k+1) = P(kV \le U < (k+1)V)$.
We compute this probability by integrating the joint PDF $f(u, v) = e^{-u} e^{-v}$ over the region $R_k' = \{(u, v) \mid u > 0, v > 0, kv \le u < (k+1)v\}$.
$$ P(k \le Z < k+1) = \int_0^\infty \int_{kv}^{(k+1)v} e^{-u} e^{-v} du dv $$
$$ = \int_0^\infty e^{-v} [-e^{-u}]_{kv}^{(k+1)v} dv = \int_0^\infty e^{-v} (e^{-kv} - e^{-(k+1)v}) dv $$
$$ = \int_0^\infty (e^{-(k+1)v} - e^{-(k+2)v}) dv = \left[ -\frac{e^{-(k+1)v}}{k+1} + \frac{e^{-(k+2)v}}{k+2} \right]_0^\infty $$
$$ = (0 - 0) - \left( -\frac{1}{k+1} + \frac{1}{k+2} \right) = \frac{1}{k+1} - \frac{1}{k+2} $$
This confirms the previous calculation. The summation step remains the same.

Final result: The probability is the sum $\sum_{j=0}^\infty \left(\frac{1}{2j+1} - \frac{1}{2j+2}\right) = \ln(2)$.

Final Answer: The final answer is $\boxed{\ln(2)}$