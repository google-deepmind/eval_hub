```markdown
# Solution

Let $X$ be the number of tosses required to obtain the first head. The probability of getting a head on any given toss is $p$.
Given that the probability of heads is $p$, $X$ follows a geometric distribution with parameter $p$. The probability mass function, conditional on $p$, is $P(X=k | p) = (1-p)^{k-1}p$ for $k=1, 2, 3, \ldots$. This distribution is valid for $p > 0$.
The expected value of a geometric distribution with parameter $p$ is $E[X | p] = \frac{1}{p}$ for $p > 0$. If $p=0$, the first head is never observed, so the number of tosses is infinite, $E[X | p=0] = \infty$.

The problem states that $p$ is a random variable, let's denote it by $P$, which is uniformly distributed on the interval $[0,1]$. The probability density function (PDF) of $P$ is $f(p) = 1$ for $p \in [0,1]$ and $f(p) = 0$ otherwise.

We want to find the expected number of tosses, $E[X]$. We can compute this using the law of total expectation, which states $E[X] = E[E[X|P]]$.
The inner expectation is $E[X|P=p] = \frac{1}{p}$ for $p>0$.
The outer expectation is taken with respect to the distribution of $P$. The expectation of a function $g(P)$ of a continuous random variable $P$ with PDF $f(p)$ is $E[g(P)] = \int_{-\infty}^{\infty} g(p)f(p)dp$. Here, $g(p) = \frac{1}{p}$ and $f(p)=1$ for $p \in [0,1]$ (and 0 otherwise).
$$E[X] = E\left[\frac{1}{P}\right] = \int_{0}^{1} \frac{1}{p} \cdot 1 dp$$
This is an improper integral because the integrand $\frac{1}{p}$ is unbounded as $p$ approaches the lower limit of integration, 0. We evaluate this integral using a limit:
$$ \int_{0}^{1} \frac{1}{p} dp = \lim_{\epsilon \to 0^+} \int_{\epsilon}^{1} \frac{1}{p} dp $$
Now, we evaluate the definite integral $\int_{\epsilon}^{1} \frac{1}{p} dp$:
$$ \int_{\epsilon}^{1} \frac{1}{p} dp = [\ln|p|]_{\epsilon}^{1} $$
Since $\epsilon > 0$, we have $\ln|p| = \ln p$ for $p \in [\epsilon, 1]$.
$$ [\ln p]_{\epsilon}^{1} = \ln(1) - \ln(\epsilon) = 0 - \ln(\epsilon) = -\ln(\epsilon) $$
Now, we take the limit as $\epsilon \to 0^+$:
$$ \lim_{\epsilon \to 0^+} (-\ln(\epsilon)) $$
As $\epsilon$ approaches 0 from the positive side, $\ln(\epsilon)$ approaches $-\infty$. Therefore, $-\ln(\epsilon)$ approaches $-(-\infty) = +\infty$.
$$ \lim_{\epsilon \to 0^+} (-\ln(\epsilon)) = +\infty $$
Thus, the expected number of tosses is infinite:
$$ E[X] = \int_{0}^{1} \frac{1}{p} dp = \infty $$

Alternatively, we can first find the unconditional probability mass function of $X$.
$$ P(X=k) = E[P(X=k|P)] = \int_{0}^{1} P(X=k|P=p) f(p) dp = \int_{0}^{1} (1-p)^{k-1}p \cdot 1 dp $$
This integral is related to the Beta function $B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1} dt$. Specifically, $\int_{0}^{1} p^{1}(1-p)^{k-1} dp = B(2,k)$. Using the property $B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$, we get:
$$ P(X=k) = B(2,k) = \frac{\Gamma(2)\Gamma(k)}{\Gamma(2+k)} = \frac{1! (k-1)!}{(k+1)!} = \frac{(k-1)!}{(k+1)k(k-1)!} = \frac{1}{k(k+1)} $$
for $k=1, 2, 3, \ldots$.
The expected value $E[X]$ is the sum $\sum_{k=1}^{\infty} k P(X=k)$:
$$ E[X] = \sum_{k=1}^{\infty} k \frac{1}{k(k+1)} = \sum_{k=1}^{\infty} \frac{1}{k+1} $$
Let $j = k+1$. As $k$ goes from 1 to $\infty$, $j$ goes from 2 to $\infty$.
$$ E[X] = \sum_{j=2}^{\infty} \frac{1}{j} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \ldots $$
This is the harmonic series starting from the second term. The harmonic series $\sum_{n=1}^{\infty} \frac{1}{n}$ is known to diverge to infinity.
$$ \sum_{j=2}^{\infty} \frac{1}{j} = \left(\sum_{j=1}^{\infty} \frac{1}{j}\right) - 1 = \infty - 1 = \infty $$
Both methods confirm that the expected number of tosses to get the first head is infinite. This is because the uniform distribution of $p$ on $[0,1]$ assigns non-zero probability density to values of $p$ arbitrarily close to zero, and for such small values of $p$, the expected number of tosses $1/p$ becomes arbitrarily large, leading to an infinite overall expectation.

The final answer is $\boxed{The\ expected\ number\ of\ tosses\ to\ get\ the\ first\ heads\ is\ infinite}$.
```