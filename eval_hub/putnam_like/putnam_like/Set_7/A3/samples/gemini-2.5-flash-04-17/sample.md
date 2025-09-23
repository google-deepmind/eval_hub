Let $S = \sum_{i=1}^n a_i$. The inequality to be shown is
$$
\frac{S^S}{S!} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}
$$
Since $a_i$ are positive integers, $a_i!$ are positive, and $S!$ is positive. We can multiply both sides by $S! \prod_{i=1}^n (a_i!)$ without changing the direction of the inequality:
$$
S^S \prod_{i=1}^n (a_i!) > S! \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Divide both sides by $\prod_{i=1}^n (a_i!)$:
$$
S^S > \frac{S!}{\prod_{i=1}^n (a_i!)} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
The term $\frac{S!}{\prod_{i=1}^n (a_i!)}$ is the multinomial coefficient $\binom{S}{a_1, \ldots, a_n}$.
So the inequality is equivalent to:
$$
S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
By the multinomial theorem, for positive integers $a_1, \ldots, a_n$, we have:
$$
\left( \sum_{i=1}^n a_i \right)^S = \left( a_1 + \ldots + a_n \right)^S = \sum_{k_1 + \ldots + k_n = S, k_i \geq 0} \binom{S}{k_1, \ldots, k_n} a_1^{k_1} a_2^{k_2} \ldots a_n^{k_n}
$$
So $S^S = \sum_{K} \binom{S}{K} \prod_{i=1}^n a_i^{k_i}$, where the sum is over all $n$-tuples $K=(k_1, \ldots, k_n)$ of non-negative integers such that $\sum_{i=1}^n k_i = S$.

Let's examine the term on the right side of the inequality: $\binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}$.
Consider the tuple of exponents $K_0 = (a_{\sigma(1)}, a_{\sigma(2)}, \ldots, a_{\sigma(n)})$.
Since $\sigma$ is a permutation of $\{1, \ldots, n\}$, the set $\{a_{\sigma(1)}, \ldots, a_{\sigma(n)}\}$ is a permutation of the set $\{a_1, \ldots, a_n\}$ as a multiset.
The sum of the elements in $K_0$ is $\sum_{i=1}^n a_{\sigma(i)} = \sum_{j=1}^n a_j = S$.
Since $a_i$ are positive integers, $a_i \geq 1$ for all $i$. Thus $a_{\sigma(i)} \geq 1$ for all $i$.
So $K_0 = (a_{\sigma(1)}, \ldots, a_{\sigma(n)})$ is a valid tuple of non-negative integers that sum to $S$.

The term in the multinomial expansion corresponding to the tuple $K_0=(a_{\sigma(1)}, \ldots, a_{\sigma(n)})$ is:
$$
\binom{S}{a_{\sigma(1)}, \ldots, a_{\sigma(n)}} a_1^{a_{\sigma(1)}} a_2^{a_{\sigma(2)}} \ldots a_n^{a_{\sigma(n)}} = \binom{S}{a_{\sigma(1)}, \ldots, a_{\sigma(n)}} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Since $\{a_{\sigma(1)}, \ldots, a_{\sigma(n)}\}$ is a permutation of $\{a_1, \ldots, a_n\}$ as a multiset, the multinomial coefficient is equal:
$$
\binom{S}{a_{\sigma(1)}, \ldots, a_{\sigma(n)}} = \binom{S}{a_1, \ldots, a_n}
$$
Thus, the term in the multinomial expansion corresponding to the tuple of exponents $(a_{\sigma(1)}, \ldots, a_{\sigma(n)})$ is exactly the right side of the inequality:
$$
\binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
So $S^S$ is the sum of all terms $\binom{S}{K} \prod_{i=1}^n a_i^{k_i}$ where $\sum k_i = S, k_i \ge 0$. The right side of the inequality is one of these terms.

For the inequality $S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}$ to be strict, we need to show that there is at least one other term in the sum which is positive.
All $a_i$ are positive integers ($a_i \geq 1$). For any valid tuple $K=(k_1, \ldots, k_n)$ with $k_i \geq 0$ and $\sum k_i = S$, the term $\binom{S}{K} \prod_{i=1}^n a_i^{k_i}$ is positive because $\binom{S}{K} = \frac{S!}{k_1!\ldots k_n!}$ is positive for $k_i \geq 0, \sum k_i = S$, and $\prod a_i^{k_i} > 0$ since $a_i > 0$.

Thus, $S^S$ is the sum of positive terms. The inequality $S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}$ holds if there is more than one term in the sum.
The number of terms in the sum is the number of distinct tuples $K=(k_1, \ldots, k_n)$ of non-negative integers such that $k_1 + \ldots + k_n = S$. This number is given by $\binom{S+n-1}{n-1}$.

Since $a_i \geq 1$ for all $i$, $S = \sum_{i=1}^n a_i \geq n$.
The problem states $n \geq 2$.
So $S \geq 2$.
The number of terms is $\binom{S+n-1}{n-1}$. Since $S \geq 2$ and $n \geq 2$, we have $S+n-1 \geq 2+2-1 = 3$ and $n-1 \geq 1$.
$\binom{m}{k} > 1$ for $m > k > 0$. Here $m=S+n-1$ and $k=n-1$.
$S+n-1 > n-1$ because $S \ge 2$.
$n-1 > 0$ because $n \ge 2$.
So $\binom{S+n-1}{n-1} > 1$.
This shows that there is always more than one tuple $K$ of non-negative integers summing to $S$.

Let $T_{K_0} = \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}$ be the term corresponding to $K_0=(a_{\sigma(1)}, \ldots, a_{\sigma(n)})$.
$S^S = \sum_{K} T_K = T_{K_0} + \sum_{K \neq K_0} T_K$.
Since there is more than one tuple $K$, the sum $\sum_{K \neq K_0} T_K$ is not empty.
As shown earlier, all terms $T_K$ are positive for valid $K$.
Therefore, $\sum_{K \neq K_0} T_K > 0$.
This implies $S^S > T_{K_0}$.
Substituting $T_{K_0}$ back, we get $S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}$, which is equivalent to the original inequality.

This holds for any permutation $\sigma \in S_n$.

The final answer is $\boxed{\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )} }$.