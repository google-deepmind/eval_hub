Okay, here is the solution.

Let $N$ be the random variable representing the number of tosses required to get the first heads.
Let $p$ be the probability of getting heads on a single toss.
We are given that $p$ is a random variable uniformly distributed on the interval $[0, 1]$. The probability density function (PDF) of $p$ is given by:
$f(p) = 1$ for $p \in [0, 1]$
$f(p) = 0$ otherwise.

We want to find the expected value of $N$, denoted by $E[N]$.

We can use the Law of Total Expectation (also known as the Tower Property):
$E[N] = E[E[N|p]]$

First, let's find the conditional expectation $E[N|p]$. Given a fixed value of $p$, the number of tosses $N$ required to get the first success (heads) follows a Geometric distribution with parameter $p$. The probability mass function is $P(N=k|p) = (1-p)^{k-1}p$ for $k = 1, 2, 3, \dots$.
The expected value of a Geometric distribution with parameter $p$ is well-known:
$E[N|p] = \frac{1}{p}$

Now, we need to find the expectation of this conditional expectation with respect to the distribution of $p$. The conditional expectation $E[N|p] = \frac{1}{p}$ is a function of the random variable $p$.
Using the definition of expected value for a continuous random variable:
$E[N] = E[E[N|p]] = E\left[\frac{1}{p}\right] = \int_{-\infty}^{\infty} \frac{1}{p} f(p) \, dp$

Substituting the PDF $f(p)$ for the uniform distribution on $[0, 1]$:
$E[N] = \int_{0}^{1} \frac{1}{p} \cdot 1 \, dp = \int_{0}^{1} \frac{1}{p} \, dp$

This is an improper integral because the integrand $\frac{1}{p}$ approaches infinity as $p$ approaches $0$. We evaluate it using a limit:
$E[N] = \lim_{a \to 0^+} \int_{a}^{1} \frac{1}{p} \, dp$

The antiderivative of $\frac{1}{p}$ is $\ln|p|$. Since $p \in (0, 1]$, $|p| = p$.
$E[N] = \lim_{a \to 0^+} [\ln p]_{a}^{1}$
$E[N] = \lim_{a \to 0^+} (\ln(1) - \ln(a))$
$E[N] = \lim_{a \to 0^+} (0 - \ln(a))$
$E[N] = \lim_{a \to 0^+} (-\ln(a))$

As $a$ approaches $0$ from the positive side ($a \to 0^+$), $\ln(a)$ approaches $-\infty$. Therefore, $-\ln(a)$ approaches $+\infty$.
$E[N] = +\infty$

Thus, the expected number of tosses to get the first heads is infinite.

```markdown
Let $N$ be the random variable representing the number of tosses required to get the first heads.
Let $p$ be the probability of getting heads on a single toss.
We are given that $p$ is a random variable uniformly distributed on the interval $[0, 1]$. The probability density function (PDF) of $p$ is given by:
$$ f(p) = \begin{cases} 1 & \text{if } 0 \le p \le 1 \\ 0 & \text{otherwise} \end{cases} $$
We want to find the expected value of $N$, denoted by $E[N]$.

We can use the Law of Total Expectation (also known as the Tower Property):
$$ E[N] = E[E[N|p]] $$
First, we find the conditional expectation $E[N|p]$. Given a fixed value of $p$, the number of tosses $N$ required to get the first heads follows a Geometric distribution with parameter $p$. The probability mass function is $P(N=k|p) = (1-p)^{k-1}p$ for $k = 1, 2, 3, \dots$.
The expected value of a Geometric distribution with success probability $p$ is given by:
$$ E[N|p] = \frac{1}{p} $$
Now, we need to compute the expectation of this conditional expectation over the distribution of $p$. $E[N|p] = \frac{1}{p}$ is a function of the random variable $p$. Using the definition of the expected value for a function of a continuous random variable:
$$ E[N] = E[E[N|p]] = E\left[\frac{1}{p}\right] = \int_{-\infty}^{\infty} \frac{1}{p} f(p) \, dp $$
Substituting the PDF $f(p)$ for the uniform distribution on $[0, 1]$:
$$ E[N] = \int_{0}^{1} \frac{1}{p} \cdot 1 \, dp = \int_{0}^{1} \frac{1}{p} \, dp $$
This integral is an improper integral because the integrand $\frac{1}{p}$ is unbounded as $p \to 0^+$. We evaluate it using a limit:
$$ E[N] = \lim_{a \to 0^+} \int_{a}^{1} \frac{1}{p} \, dp $$
The antiderivative of $\frac{1}{p}$ is $\ln|p|$. For $p \in (0, 1]$, we have $\ln|p| = \ln p$.
$$ E[N] = \lim_{a \to 0^+} [\ln p]_{a}^{1} $$
$$ E[N] = \lim_{a \to 0^+} (\ln(1) - \ln(a)) $$
Since $\ln(1) = 0$:
$$ E[N] = \lim_{a \to 0^+} (-\ln(a)) $$
As $a$ approaches $0$ from the positive side ($a \to 0^+$), $\ln(a)$ approaches $-\infty$. Therefore, $-\ln(a)$ approaches $+\infty$.
$$ E[N] = +\infty $$
Thus, the expected number of tosses to get the first heads is infinite.
```