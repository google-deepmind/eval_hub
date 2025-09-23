# Solution

## Understanding the Problem

We're given a sequence $(X_n=(R_n,S_n,T_n))$ of independent random variables, where each $X_n$ has a uniform distribution on the set of permutations of $(1,2,3)$. We define the sums $\hat{X}_n = (\hat{R}_n,\hat{S}_n,\hat{T}_n)=(\sum_{i=1}^{n}R_i,\sum_{i=1}^{n}S_i,\sum_{i=1}^{n}T_i)$.

We need to compare:
- $p_n = P(\hat{R}_n=\hat{S}_n=\hat{T}_n)$: the probability that all three sums are equal
- $q_n = P(\hat{R}_n,\hat{S}_n,\hat{T}_n \in \{2n-1,2n,2n+1\}, \hat{R}_n\neq\hat{S}_n)$: the probability that all sums are in $\{2n-1,2n,2n+1\}$ and the first two sums are not equal

Our goal is to show that $4p_n < q_n$ for infinitely many $n$.

## Approach

I'll use the central limit theorem to analyze the asymptotic behavior of $p_n$ and $q_n$.

### Step 1: Transforming the problem

Let's define:
- $Y_i = R_i - 2$
- $Z_i = S_i - 2$
- $W_i = T_i - 2$

Then $(Y_i,Z_i,W_i)$ is a permutation of $(-1,0,1)$, and $Y_i + Z_i + W_i = 0$ for each $i$.

We also have:
- $\hat{Y}_n = \hat{R}_n - 2n$
- $\hat{Z}_n = \hat{S}_n - 2n$
- $\hat{W}_n = \hat{T}_n - 2n$

So our probabilities become:
- $p_n = P(\hat{Y}_n = \hat{Z}_n = \hat{W}_n = 0)$
- $q_n = P(\hat{Y}_n, \hat{Z}_n, \hat{W}_n \in \{-1,0,1\}, \hat{Y}_n \neq \hat{Z}_n)$

Note that $\hat{Y}_n + \hat{Z}_n + \hat{W}_n = 0$ for all $n$.

### Step 2: Analyzing the distribution

To better understand the joint distribution, let's define:
- $U_n = \hat{Y}_n - \hat{Z}_n$
- $V_n = \hat{Y}_n - \hat{W}_n$

Then we have:
- $p_n = P(U_n = 0, V_n = 0)$
- $(U_n, V_n)$ is the sum of $n$ independent and identically distributed random vectors $(U_i, V_i)$

The covariance matrix of $(U_i, V_i)$ can be calculated as:
$$\Sigma = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

And $|\Sigma| = 3$.

### Step 3: Applying the local central limit theorem

By the local central limit theorem, for large $n$:

$$p_n = P(U_n = 0, V_n = 0) \approx \frac{1}{2\pi\sqrt{|n\Sigma|}} = \frac{1}{2\pi n\sqrt{3}}$$

For $q_n$, we need to find the probability that $(\hat{Y}_n, \hat{Z}_n, \hat{W}_n)$ is one of the following:
- $(1,0,-1)$
- $(1,-1,0)$
- $(0,1,-1)$
- $(0,-1,1)$
- $(-1,1,0)$
- $(-1,0,1)$

Converting to $(U_n, V_n)$ coordinates, these correspond to the points:
- $(1,2)$
- $(2,1)$
- $(-1,1)$
- $(1,-1)$
- $(-2,-1)$
- $(-1,-2)$

By the local central limit theorem and due to symmetry, each of these points has probability approximately $\frac{1}{2\pi n\sqrt{3}}$ for large $n$.

Therefore:
$$q_n \approx 6 \cdot \frac{1}{2\pi n\sqrt{3}} = \frac{3}{\pi n\sqrt{3}}$$

### Step 4: Comparing $p_n$ and $q_n$

We have:
$$4p_n \approx 4 \cdot \frac{1}{2\pi n\sqrt{3}} = \frac{2}{\pi n\sqrt{3}}$$

And:
$$q_n \approx \frac{3}{\pi n\sqrt{3}}$$

Since $\frac{2}{\pi n\sqrt{3}} < \frac{3}{\pi n\sqrt{3}}$ for all $n > 0$, we have $4p_n < q_n$ for all sufficiently large $n$.

## Conclusion

By the local central limit theorem, we have shown that for sufficiently large $n$:
$$4p_n \approx \frac{2}{\pi n\sqrt{3}} < \frac{3}{\pi n\sqrt{3}} \approx q_n$$

Therefore, $4p_n < q_n$ for infinitely many values of $n$, which proves the desired result.