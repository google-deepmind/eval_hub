Let $(a_n)_{n=1}^{\infty}$ be the sequence. The sequence is formed by concatenating groups of integers.
The first group is $G_1 = (1)$, which has $1^2=1$ element. The sum of elements in $G_1$ is $1$.
The second group is $G_2 = (1, 2, 3, 4)$, which has $2^2=4$ elements. The sum of elements in $G_2$ is $\sum_{j=1}^4 j = \frac{4(5)}{2} = 10$.
The $k$-th group is $G_k = (1, 2, \ldots, k^2)$, which has $k^2$ elements. The sum of elements in $G_k$ is $\sum_{j=1}^{k^2} j = \frac{k^2(k^2+1)}{2}$.

Let $N_k$ be the total number of elements up to the end of the $k$-th group.
$N_k = \sum_{j=1}^k |G_j| = \sum_{j=1}^k j^2 = \frac{k(k+1)(2k+1)}{6}$.
As $k \to \infty$, $N_k = \frac{2k^3+3k^2+k}{6} \sim \frac{k^3}{3}$.

Let $S_k$ be the sum of all elements up to the end of the $k$-th group.
$S_k = \sum_{j=1}^k (\text{sum of elements in } G_j) = \sum_{j=1}^k \frac{j^2(j^2+1)}{2} = \frac{1}{2} \sum_{j=1}^k (j^4+j^2)$.
We know the formulas for sums of powers:
$\sum_{j=1}^k j^2 = \frac{k(k+1)(2k+1)}{6} = \frac{2k^3+3k^2+k}{6}$.
$\sum_{j=1}^k j^4 = \frac{k(k+1)(2k+1)(3k^2+3k-1)}{30} = \frac{6k^5+15k^4+10k^3-k}{30}$.
So, $S_k = \frac{1}{2} \left( \frac{6k^5+15k^4+10k^3-k}{30} + \frac{2k^3+3k^2+k}{6} \right)$.
$S_k = \frac{1}{2} \left( \frac{6k^5+15k^4+10k^3-k + 5(2k^3+3k^2+k)}{30} \right) = \frac{6k^5+15k^4+10k^3-k + 10k^3+15k^2+5k}{60}$
$S_k = \frac{6k^5+15k^4+20k^3+15k^2+4k}{60} = \frac{k^5}{10} + \frac{k^4}{4} + \frac{k^3}{3} + \frac{k^2}{4} + \frac{k}{15}$.
As $k \to \infty$, $S_k \sim \frac{k^5}{10}$.

We are interested in the limit of $b_n = \frac{A_n}{n^\alpha}$ as $n\to\infty$, where $A_n = \sum_{k=1}^n a_k$.
Let $n$ be a large integer. Then there exists a unique integer $m$ such that $N_{m-1} < n \leq N_m$.
The sum $A_n = \sum_{k=1}^n a_k = \sum_{k=1}^{N_{m-1}} a_k + \sum_{k=N_{m-1}+1}^n a_k = S_{m-1} + \sum_{j=1}^{n-N_{m-1}} a_{N_{m-1}+j}$.
The elements in the $m$-th group are $1, 2, \ldots, m^2$. So $a_{N_{m-1}+j} = j$ for $1 \leq j \leq m^2$.
Let $i = n-N_{m-1}$. Then $1 \leq i \leq N_m - N_{m-1} = m^2$.
$A_n = S_{m-1} + \sum_{j=1}^i j = S_{m-1} + \frac{i(i+1)}{2}$.

We need to determine $\alpha$ and $\beta$ such that $\lim_{n\to\infty} \frac{A_n}{n^\alpha} = \beta > 0$.
As $n \to \infty$, $m \to \infty$.
$n$ is within the range $(N_{m-1}, N_m]$. $N_{m-1} \sim \frac{(m-1)^3}{3} \sim \frac{m^3}{3}$ and $N_m \sim \frac{m^3}{3}$. So $n \sim \frac{m^3}{3}$, which implies $m \sim (3n)^{1/3}$.
$A_n = S_{m-1} + \frac{i(i+1)}{2}$. $S_{m-1} \sim \frac{(m-1)^5}{10} \sim \frac{m^5}{10}$.
Since $1 \leq i \leq m^2$, $\frac{i(i+1)}{2}$ is at most $\frac{m^2(m^2+1)}{2} \sim \frac{m^4}{2}$.
So $A_n \sim \frac{m^5}{10} + O(m^4)$.
For the limit $\lim_{n\to\infty} \frac{A_n}{n^\alpha}$ to be a positive constant, $A_n$ must be proportional to $n^\alpha$.
$A_n \sim \frac{m^5}{10}$. Substitute $m \sim (3n)^{1/3}$: $A_n \sim \frac{((3n)^{1/3})^5}{10} = \frac{3^{5/3} n^{5/3}}{10}$.
This suggests that $\alpha = 5/3$.

Let's check the limit for $\alpha=5/3$.
$\frac{A_n}{n^{5/3}} = \frac{S_{m-1} + i(i+1)/2}{(N_{m-1}+i)^{5/3}}$.
We can bound this ratio using the values at the boundaries of the interval $(N_{m-1}, N_m]$.
For $n \in (N_{m-1}, N_m]$, we have $N_{m-1} < n \leq N_m$ and $S_{m-1} \leq A_n \leq S_m$.
Therefore, $\frac{S_{m-1}}{N_m^{5/3}} \leq \frac{A_n}{n^{5/3}} \leq \frac{S_m}{N_{m-1}^{5/3}}$.

Let's evaluate the limit of the lower bound:
$\lim_{m\to\infty} \frac{S_{m-1}}{N_m^{5/3}}$.
$S_{m-1} = \frac{(m-1)^5}{10} + O((m-1)^4) = \frac{m^5}{10} + O(m^4)$.
$N_m = \frac{m^3}{3} + O(m^2)$.
$N_m^{5/3} = \left(\frac{m^3}{3} + O(m^2)\right)^{5/3} = \left(\frac{m^3}{3}\right)^{5/3} \left(1 + O(m^{-1})\right)^{5/3} = \frac{m^5}{3^{5/3}}(1 + O(m^{-1})) = \frac{m^5}{3^{5/3}} + O(m^4)$.
$\lim_{m\to\infty} \frac{S_{m-1}}{N_m^{5/3}} = \lim_{m\to\infty} \frac{\frac{m^5}{10} + O(m^4)}{\frac{m^5}{3^{5/3}} + O(m^4)} = \lim_{m\to\infty} \frac{m^5(1/10 + O(1/m))}{m^5(1/3^{5/3} + O(1/m))} = \frac{1/10}{1/3^{5/3}} = \frac{3^{5/3}}{10}$.

Let's evaluate the limit of the upper bound:
$\lim_{m\to\infty} \frac{S_m}{N_{m-1}^{5/3}}$.
$S_m = \frac{m^5}{10} + O(m^4)$.
$N_{m-1} = \frac{(m-1)^3}{3} + O((m-1)^2) = \frac{m^3}{3} + O(m^2)$.
$N_{m-1}^{5/3} = \left(\frac{m^3}{3} + O(m^2)\right)^{5/3} = \frac{m^5}{3^{5/3}} + O(m^4)$.
$\lim_{m\to\infty} \frac{S_m}{N_{m-1}^{5/3}} = \lim_{m\to\infty} \frac{\frac{m^5}{10} + O(m^4)}{\frac{m^5}{3^{5/3}} + O(m^4)} = \frac{1/10}{1/3^{5/3}} = \frac{3^{5/3}}{10}$.

Since both the lower and upper bounds converge to the same value $\frac{3^{5/3}}{10}$, by the Squeeze Theorem, the limit exists and $\lim_{n\to\infty} \frac{A_n}{n^{5/3}} = \frac{3^{5/3}}{10}$.
Thus, $\alpha = 5/3$ and $\beta = \frac{3^{5/3}}{10}$.
Both $\alpha=5/3$ and $\beta = \frac{3^{5/3}}{10}$ are positive real numbers.

If $\alpha \neq 5/3$:
If $\alpha < 5/3$, then for $n=N_m$, $\frac{A_{N_m}}{(N_m)^\alpha} \sim \frac{m^5/10}{(m^3/3)^\alpha} = \frac{3^\alpha}{10} m^{5-3\alpha}$. Since $5-3\alpha > 0$, this tends to $\infty$ as $m\to\infty$.
If $\alpha > 5/3$, then for $n=N_m$, $\frac{A_{N_m}}{(N_m)^\alpha} \sim \frac{3^\alpha}{10} m^{5-3\alpha}$. Since $5-3\alpha < 0$, this tends to $0$ as $m\to\infty$.
In neither case is the limit a positive real number $\beta$.
Therefore, $\alpha$ must be $5/3$.

The unique pair $(\alpha, \beta)$ of positive real numbers satisfying the condition is $(5/3, 3^{5/3}/10)$.

The final answer is $\boxed{\left(\frac{5}{3}, \frac{3^{5/3}}{10}\right)}$.