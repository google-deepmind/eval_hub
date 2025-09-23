# Solution: Expected Number of Tosses to Get First Heads

We want to find the expected number of tosses until the first heads occurs when using an asymmetric coin with probability of heads $p$, where $p$ is uniformly distributed on $[0,1]$.

Let's denote:
- $T$ = the random variable representing the number of tosses to get the first heads
- $P$ = the random variable representing the probability of heads

## Step 1: Find the conditional expectation
Given that $P = p$, the number of tosses $T$ follows a geometric distribution with parameter $p$. The probability mass function is:

$$P(T = k | P = p) = (1-p)^{k-1} \cdot p \quad \text{for } k = 1, 2, 3, \ldots$$

The expected value of this geometric distribution is:

$$E[T | P = p] = \sum_{k=1}^{\infty} k \cdot (1-p)^{k-1} \cdot p$$

We can factor out $p$:

$$E[T | P = p] = p \cdot \sum_{k=1}^{\infty} k \cdot (1-p)^{k-1}$$

Using the formula $\sum_{k=1}^{\infty} k \cdot q^{k-1} = \frac{1}{(1-q)^2}$ for $|q| < 1$, with $q = 1-p$:

$$E[T | P = p] = p \cdot \frac{1}{(1-(1-p))^2} = p \cdot \frac{1}{p^2} = \frac{1}{p}$$

## Step 2: Find the unconditional expectation
Using the law of iterated expectations:

$$E[T] = E[E[T | P]] = E\left[\frac{1}{P}\right]$$

Since $P$ is uniformly distributed on $[0, 1]$, the PDF of $P$ is $f(p) = 1$ for $0 \leq p \leq 1$. Therefore:

$$E\left[\frac{1}{P}\right] = \int_{0}^{1} \frac{1}{p} \cdot 1 \, dp = \int_{0}^{1} \frac{1}{p} \, dp$$

This integral equals $[\ln(p)]_{0}^{1} = \ln(1) - \ln(0) = 0 - (-\infty) = \infty$

## Conclusion
Therefore, the expected number of tosses to get the first heads is infinite.