Of course. Here is a detailed, step-by-step solution to the problem.

### Problem Statement

Given an asymmetric coin with a probability of getting heads equal to $p$, which is a random variable uniformly distributed on $[0,1]$. Show that the expected number of tosses to get the first heads is infinite.

### Solution

Let's break down the problem into clear, logical steps.

1.  **Define the Random Variables:**
    *   Let $N$ be the random variable representing the number of tosses required to get the first head.
    *   Let $P$ be the random variable representing the probability of getting heads on a single toss. The problem states that $P$ is uniformly distributed on the interval $[0,1]$.

2.  **Analyze the Problem for a Fixed Probability `p`:**
    First, let's consider the simpler case where the probability of heads is a fixed, known constant, $p$.
    *   The probability of getting the first head on the $k$-th toss is the probability of getting $k-1$ tails followed by one head.
    *   The probability of tails is $(1-p)$.
    *   The probability of heads is $p$.
    *   Assuming the tosses are independent, the probability of this sequence is:
        $$ \mathbb{P}(N=k | P=p) = (1-p)^{k-1} p $$
    This is the probability mass function for a **Geometric Distribution** with success probability $p$.

    *   The expected value of a random variable following a geometric distribution is well-known. We can denote this conditional expectation as $\mathbb{E}[N | P=p]$.
        $$ \mathbb{E}[N | P=p] = \sum_{k=1}^{\infty} k \cdot \mathbb{P}(N=k | P=p) = \sum_{k=1}^{\infty} k (1-p)^{k-1} p $$
    The value of this sum is a standard result:
        $$ \mathbb{E}[N | P=p] = \frac{1}{p} $$
    So, if we *knew* the probability of heads was $p$, the expected number of tosses would be $1/p$.

3.  **Incorporate the Randomness of `p`:**
    In our problem, $p$ is not a fixed constant. It is a random variable $P$ that can take any value in $[0,1]$ with equal likelihood. We need to find the *unconditional* expectation of $N$, denoted $\mathbb{E}[N]$.

    To do this, we use the **Law of Total Expectation** (also known as the Law of Iterated Expectations). This law states that for two random variables $N$ and $P$:
    $$ \mathbb{E}[N] = \mathbb{E}[\mathbb{E}[N | P]] $$
    In words, the expected value of $N$ is the expected value of the conditional expectation of $N$ given $P$.

    *   From Step 2, we found that the inner expectation, $\mathbb{E}[N | P=p]$, is the function $1/p$.
    *   Therefore, we can write:
        $$ \mathbb{E}[N] = \mathbb{E}\left[\frac{1}{P}\right] $$

4.  **Calculate the Expectation of 1/P:**
    Now we need to calculate the expected value of the function $g(P) = 1/P$, where $P$ is a continuous random variable. The formula for the expectation of a function of a continuous random variable is:
    $$ \mathbb{E}[g(P)] = \int_{-\infty}^{\infty} g(p) f_P(p) \, dp $$
    where $f_P(p)$ is the probability density function (PDF) of $P$.

    *   The problem states that $P$ is uniformly distributed on $[0,1]$. The PDF for this distribution is:
        $$ f_P(p) = \begin{cases} 1 & \text{if } 0 \le p \le 1 \\ 0 & \text{otherwise} \end{cases} $$
    *   Substituting $g(p)=1/p$ and the PDF $f_P(p)$ into the expectation formula, we get:
        $$ \mathbb{E}[N] = \mathbb{E}\left[\frac{1}{P}\right] = \int_{0}^{1} \frac{1}{p} \cdot 1 \, dp = \int_{0}^{1} \frac{1}{p} \, dp $$

5.  **Evaluate the Integral:**
    The integral we need to solve is an improper integral because the function $1/p$ is undefined at the lower limit of integration, $p=0$. We must evaluate it using a limit:
    $$ \int_{0}^{1} \frac{1}{p} \, dp = \lim_{a \to 0^+} \int_{a}^{1} \frac{1}{p} \, dp $$
    Now, we find the antiderivative of $1/p$, which is $\ln|p|$. Since our interval $[a, 1]$ is positive, we can write it as $\ln(p)$.

    $$ \lim_{a \to 0^+} \left[ \ln(p) \right]_{a}^{1} $$
    $$ = \lim_{a \to 0^+} (\ln(1) - \ln(a)) $$
    We know that $\ln(1) = 0$. So the expression becomes:
    $$ = \lim_{a \to 0^+} (0 - \ln(a)) = - \lim_{a \to 0^+} \ln(a) $$
    As $a$ approaches $0$ from the positive side, $\ln(a)$ approaches $-\infty$.
    $$ - (-\infty) = +\infty $$

### Conclusion

The integral diverges to infinity. Therefore, the expected value of the number of tosses to get the first heads is infinite.

$$ \mathbb{E}[N] = \infty $$

**Intuitive Explanation:** The reason for this result lies in the contribution of values of $p$ that are very close to zero. The uniform distribution implies that it's just as likely for the coin's probability of heads to be in the interval $[0, 0.000001]$ as it is to be in $[0.5, 0.500001]$. If the chosen $p$ happens to be a very small number (e.g., $p=10^{-6}$), the conditional expected number of tosses, $1/p$, becomes enormous ($10^6$). The possibility of these extremely small values of $p$, and their corresponding huge expected waiting times, "pulls" the overall average up to infinity. This is mathematically analogous to the divergence of the harmonic series $\sum_{n=1}^\infty \frac{1}{n}$.