# Solution

I need to show that for any positive integers $a_1, \ldots, a_n$ and any permutation $\sigma \in S_n$, the following inequality holds:
$$\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}$$

Let's denote $S = \sum_{i=1}^n a_i$ for simplicity. The inequality then becomes:
$$\frac{S^S}{S!} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n (a_i!)}$$

## Step 1: Maximizing the right-hand side

I'll first show that the right-hand side is maximized when $\sigma$ is the identity permutation.

Taking the logarithm of the numerator on the right side:
$$\ln\left(\prod_{i=1}^n a_i^{a_{\sigma(i)}}\right) = \sum_{i=1}^n a_{\sigma(i)}\ln(a_i)$$

Let's reindex this sum using $j = \sigma(i)$, which gives $i = \sigma^{-1}(j)$:
$$\sum_{i=1}^n a_{\sigma(i)}\ln(a_i) = \sum_{j=1}^n a_j\ln(a_{\sigma^{-1}(j)})$$

By the rearrangement inequality, this sum is maximized when $a_j$ and $\ln(a_{\sigma^{-1}(j)})$ are ordered the same way. Since the logarithm is strictly increasing, the ordering of $\ln(a_i)$ is the same as the ordering of $a_i$. Therefore, the sum is maximized when $a_j$ and $a_{\sigma^{-1}(j)}$ have the same ordering, which occurs when $\sigma^{-1}$ (and thus $\sigma$) is the identity permutation.

Thus, it suffices to prove:
$$\frac{S^S}{S!} > \frac{\prod_{i=1}^n a_i^{a_i}}{\prod_{i=1}^n (a_i!)}$$

## Step 2: Proving the simplified inequality

I'll use the multinomial theorem. For $S = a_1 + a_2 + \ldots + a_n$, we have:
$$S^S = (a_1 + a_2 + \ldots + a_n)^S = \sum_{k_1 + k_2 + \ldots + k_n = S} \binom{S}{k_1, k_2, \ldots, k_n} a_1^{k_1} a_2^{k_2} \ldots a_n^{k_n}$$

Among the terms in this sum is the term where $k_i = a_i$ for all $i$:
$$\binom{S}{a_1, a_2, \ldots, a_n} a_1^{a_1} a_2^{a_2} \ldots a_n^{a_n}$$

Since $n \geq 2$ and all $a_i > 0$, there is at least one other term in the multinomial expansion (for example, when $k_1 = a_1+1$, $k_2 = a_2-1$, and $k_i = a_i$ for $i > 2$, assuming $a_2 > 0$). Therefore:
$$S^S > \binom{S}{a_1, a_2, \ldots, a_n} a_1^{a_1} a_2^{a_2} \ldots a_n^{a_n}$$

Recalling that $\binom{S}{a_1, a_2, \ldots, a_n} = \frac{S!}{a_1! \cdot a_2! \cdot \ldots \cdot a_n!}$, we can rearrange to get:
$$\frac{S^S}{S!} > \frac{a_1^{a_1} a_2^{a_2} \ldots a_n^{a_n}}{a_1! \cdot a_2! \cdot \ldots \cdot a_n!} = \frac{\prod_{i=1}^n a_i^{a_i}}{\prod_{i=1}^n (a_i!)}$$

This proves the inequality.