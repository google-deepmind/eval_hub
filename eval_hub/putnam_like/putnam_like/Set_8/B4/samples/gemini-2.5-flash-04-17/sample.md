Let $X$ and $Y$ be independent random variables chosen uniformly from the interval $(0, 1)$. Their joint probability density function is $f_{X,Y}(x, y) = 1$ for $0 < x < 1$ and $0 < y < 1$, and 0 otherwise.

We are interested in the probability that $[\frac{\ln(X)}{\ln(Y)}]$ is even.
Since $0 < X < 1$ and $0 < Y < 1$, we have $\ln(X) < 0$ and $\ln(Y) < 0$.
Let $U = -\ln(X)$ and $V = -\ln(Y)$. Then $U > 0$ and $V > 0$.
The ratio $\frac{\ln(X)}{\ln(Y)}$ becomes $\frac{-U}{-V} = \frac{U}{V}$.
We want to find the probability that $[\frac{U}{V}]$ is an even integer.

Let's find the probability distribution of $U$ and $V$.
For $u > 0$, $P(U \le u) = P(-\ln(X) \le u) = P(\ln(X) \ge -u) = P(X \ge e^{-u})$.
Since $X$ is uniform on $(0, 1)$, $P(X \ge x_0) = 1 - x_0$ for $0 < x_0 < 1$.
For $u > 0$, $e^{-u} \in (0, 1)$, so $P(X \ge e^{-u}) = 1 - e^{-u}$.
The cumulative distribution function of $U$ is $F_U(u) = 1 - e^{-u}$ for $u > 0$. For $u \le 0$, $F_U(u) = 0$.
The probability density function of $U$ is $f_U(u) = F_U'(u) = \frac{d}{du}(1 - e^{-u}) = e^{-u}$ for $u > 0$, and 0 otherwise.
$U$ is an exponential random variable with parameter $\lambda=1$. Similarly, $V$ is an independent exponential random variable with parameter $\lambda=1$.
The joint density of $U$ and $V$ is $f_{U,V}(u, v) = f_U(u)f_V(v) = e^{-u}e^{-v} = e^{-(u+v)}$ for $u > 0, v > 0$.

Let $Z = U/V$. We want to find $P([Z] \text{ is even})$.
$[Z]$ is even means $[Z] \in \{0, 2, 4, \dots\}$. Since $U, V > 0$, $Z = U/V > 0$. So $[Z]$ is a non-negative integer.
$P([Z] \text{ is even}) = \sum_{k=0}^{\infty} P([Z] = 2k)$.
$P([Z] = m)$ means $m \le Z < m+1$, which is $m \le U/V < m+1$.
Since $V > 0$, this is equivalent to $mV \le U < (m+1)V$.

Let's calculate $P(m \le U/V < m+1)$ for an integer $m \ge 0$.
$P(m \le U/V < m+1) = P(mV \le U < (m+1)V)$.
This probability is the integral of the joint density $e^{-(u+v)}$ over the region $R_m = \{(u,v) : v > 0, mV \le u < (m+1)V\}$.
$P(m \le U/V < m+1) = \int_0^{\infty} \left( \int_{mv}^{(m+1)v} e^{-(u+v)} du \right) dv$.

The inner integral is $\int_{mv}^{(m+1)v} e^{-u}e^{-v} du = e^{-v} \int_{mv}^{(m+1)v} e^{-u} du = e^{-v} [-e^{-u}]_{mv}^{(m+1)v} = e^{-v}(-e^{-(m+1)v} - (-e^{-mv})) = e^{-v}(e^{-mv} - e^{-(m+1)v}) = e^{-(m+1)v} - e^{-(m+2)v}$.

The outer integral is $\int_0^{\infty} (e^{-(m+1)v} - e^{-(m+2)v}) dv$.
For any $a > 0$, $\int_0^{\infty} e^{-av} dv = [-\frac{1}{a}e^{-av}]_0^{\infty} = 0 - (-\frac{1}{a}) = \frac{1}{a}$.
So, $\int_0^{\infty} (e^{-(m+1)v} - e^{-(m+2)v}) dv = \frac{1}{m+1} - \frac{1}{m+2}$.
This formula is valid for $m+1 > 0$ and $m+2 > 0$. Since $m \ge 0$, this is true.

So, $P([Z] = m) = \frac{1}{m+1} - \frac{1}{m+2}$ for $m \ge 0$.
This can be rewritten as $P([Z] = m) = \frac{(m+2) - (m+1)}{(m+1)(m+2)} = \frac{1}{(m+1)(m+2)}$.

We want to find the probability that $[Z]$ is even, which is the sum of $P([Z]=m)$ for $m \in \{0, 2, 4, \dots\}$.
$P([Z] \text{ is even}) = \sum_{k=0}^{\infty} P([Z] = 2k)$.
$P([Z] = 2k) = \frac{1}{(2k+1)(2k+2)}$.

The required probability is $\sum_{k=0}^{\infty} \frac{1}{(2k+1)(2k+2)}$.
Using partial fraction decomposition, $\frac{1}{(2k+1)(2k+2)} = \frac{1}{2k+1} - \frac{1}{2k+2}$.
So the sum is $\sum_{k=0}^{\infty} (\frac{1}{2k+1} - \frac{1}{2k+2})$.

Let's write out the first few terms of the sum:
For $k=0$: $\frac{1}{1} - \frac{1}{2}$
For $k=1$: $\frac{1}{3} - \frac{1}{4}$
For $k=2$: $\frac{1}{5} - \frac{1}{6}$
...
The sum is $(1 - \frac{1}{2}) + (\frac{1}{3} - \frac{1}{4}) + (\frac{1}{5} - \frac{1}{6}) + \dots = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \dots$.
This is the alternating harmonic series, which is the Taylor series expansion of $\ln(1+x)$ evaluated at $x=1$.
$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} = \ln(1+1) = \ln(2)$.

The sum $\sum_{k=0}^{\infty} (\frac{1}{2k+1} - \frac{1}{2k+2})$ can be written as $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$ by letting $n=2k+1$ and $n=2k+2$.
The terms are $\frac{1}{1}, -\frac{1}{2}, \frac{1}{3}, -\frac{1}{4}, \frac{1}{5}, -\frac{1}{6}, \dots$
This corresponds to the series $\frac{1}{1} - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots = \ln(2)$.

The probability that $[\frac{\ln(X)}{\ln(Y)}]$ is even is $\ln(2)$.

The final answer is $\boxed{\ln(2)}$.