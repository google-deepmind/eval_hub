This step is worth 2 points.
Fix any positive integers $a_1, \ldots, a_n$ and a permutation $\sigma \in S_n$. Denote
$$m := \sum_{i=1}^n a_i.$$
Then, from multinomial formula we get
$$
\begin{aligned}
\left( \sum_{i=1}^n a_i \right)^m &= \sum_{k_1+k_2+\ldots+k_n = m} {m \choose k_1, k_2, \ldots, k_n} a_{1}^{k_1} a_{2}^{k_2} \ldots a_{n}^{k_n} \\
&= \sum_{k_1+k_2+\ldots+k_n = m} \frac{m!}{k_1! k_2! \ldots k_n!} a_{1}^{k_1} a_{2}^{k_2} \ldots a_{n}^{k_n}.
\end{aligned}
$$

This step is worth 8 points.
Since
$$a_{\sigma(1)} + a_{\sigma(2)} + \ldots + a_{\sigma(n)} = a_1 + a_2 + \ldots + a_n = m$$
we can consider in the above sum $k_1 = a_{\sigma(1)}$, $k_2 = a_{\sigma(2)}$, ..., $k_n = a_{\sigma(n)}$. Hence
$$
\left( \sum_{i=1}^n a_i \right)^m > \frac{m!}{a_{\sigma(1)}! a_{\sigma(2)}! \ldots a_{\sigma(n)}!} a_1^{\sigma(1)} a_2^{\sigma(2)} \ldots a_n^{\sigma(n)} = \frac{m!}{a_1 ! a_2 ! \ldots a_n !} a_1^{\sigma(1)} a_2^{\sigma(2)} \ldots a_n^{\sigma(n)}.
$$
Recalling that $m = \sum_{i=1}^n a_i$ we can rewrite the above inequality as
$$
\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}
$$
and the proof is completed.