# Solution

I need to find all pairs $(\alpha, \beta)$ of positive real numbers such that $\lim_{n\to\infty} b_n=\beta$, where $b_n=\frac{\sum_{k=1}^n a_k}{n^{\alpha}}$.

## Understanding the sequence $(a_n)$

First, let's understand the structure of the sequence $(a_n)$:
- The first block is $(1)$ with length $1^2 = 1$
- The second block is $(1,2,3,4)$ with length $2^2 = 4$
- The third block is $(1,2,\ldots,9)$ with length $3^2 = 9$
- And so on...

In general, the $k$-th block consists of integers from 1 to $k^2$, and has length $k^2$.

## Finding the sum $S_n = \sum_{k=1}^n a_k$

Let $m_k$ be the index of the last element in the $k$-th block. We have:
$m_k = \sum_{j=1}^{k} j^2 = \frac{k(k+1)(2k+1)}{6}$

Let $S_k$ be the sum of all elements in the first $k$ blocks. The sum of the $j$-th block is $\sum_{i=1}^{j^2} i = \frac{j^2(j^2+1)}{2}$.

Therefore:
$$S_k = \sum_{j=1}^{k} \frac{j^2(j^2+1)}{2} = \frac{1}{2}\sum_{j=1}^{k} j^4 + \frac{1}{2}\sum_{j=1}^{k} j^2$$

Using standard formulas for sums of powers:
$$\sum_{j=1}^{k} j^2 = \frac{k(k+1)(2k+1)}{6}$$
$$\sum_{j=1}^{k} j^4 = \frac{k(k+1)(2k+1)(3k^2+3k-1)}{30}$$

Substituting:
$$S_k = \frac{k(k+1)(2k+1)}{60}(3k^2+3k+4)$$

For large $k$, the dominant term is $\frac{k^5}{10}$.

## Asymptotic analysis

For $n$ such that $m_k < n \leq m_{k+1}$, the sum $S_n$ consists of $S_k$ plus a partial sum from the $(k+1)$-th block:
$$S_n = S_k + \frac{(n-m_k)(n-m_k+1)}{2}$$

Since $n-m_k \leq (k+1)^2$, the second term is $O(k^4)$, which is of lower order than $S_k \sim \frac{k^5}{10}$.

We also have $m_k \sim \frac{k^3}{3}$ for large $k$, which implies $k \sim (3n)^{1/3}$ for large $n$.

Therefore:
$$S_n \sim \frac{k^5}{10} \sim \frac{(3n)^{5/3}}{10} = \frac{3^{5/3}}{10} n^{5/3}$$

## Finding the limit

Now, for $b_n = \frac{S_n}{n^{\alpha}}$, we have:
$$b_n \sim \frac{3^{5/3}}{10} \frac{n^{5/3}}{n^{\alpha}} = \frac{3^{5/3}}{10} n^{5/3-\alpha}$$

For $b_n$ to have a finite, non-zero limit, we need $5/3-\alpha = 0$, or $\alpha = 5/3$.

In that case:
$$\lim_{n\to\infty} b_n = \frac{3^{5/3}}{10}$$

If $\alpha < 5/3$, then $b_n \to \infty$ as $n \to \infty$.
If $\alpha > 5/3$, then $b_n \to 0$ as $n \to \infty$.

Since the problem requires both $\alpha$ and $\beta$ to be positive real numbers, the only valid pair is:
$$(\alpha, \beta) = \left(\frac{5}{3}, \frac{3^{5/3}}{10}\right)$$