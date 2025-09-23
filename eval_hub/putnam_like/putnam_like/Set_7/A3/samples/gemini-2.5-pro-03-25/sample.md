Let $S = \sum_{i=1}^n a_i$. Since $a_i \ge 1$ for all $i$ and $n \ge 2$, we have $S \ge n \ge 2$.
The inequality we want to prove is
$$
\frac{S^S}{S!} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n a_i!}
$$
We can rewrite this inequality by multiplying both sides by $S! \prod_{i=1}^n a_i!$ (which is positive):
$$
S^S \prod_{i=1}^n a_i! > S! \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Let's divide by $S!$ (which is positive):
$$
\frac{S^S \prod_{i=1}^n a_i!}{S!} > \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Let $LHS = \frac{S^S \prod_{i=1}^n a_i!}{S!}$ and $RHS_\sigma = \prod_{i=1}^n a_i^{a_{\sigma(i)}}$. We want to show $LHS > RHS_\sigma$.
Let $P_1 = \prod_{i=1}^n a_i^{a_i}$. This corresponds to the case where $\sigma$ is the identity permutation.

Step 1: Show that $LHS > P_1$.
Consider the multinomial theorem for $(a_1 + \dots + a_n)^S$:
$$
S^S = (a_1 + \dots + a_n)^S = \sum_{k_1+\dots+k_n=S, k_i \ge 0} \binom{S}{k_1, \dots, k_n} a_1^{k_1} \dots a_n^{k_n}
$$
where $\binom{S}{k_1, \dots, k_n} = \frac{S!}{k_1! \dots k_n!}$ is the multinomial coefficient.
Since $a_i \ge 1$, all $a_i$ are positive integers. The terms $a_1^{k_1} \dots a_n^{k_n}$ are positive integers for any non-negative integers $k_i$. The multinomial coefficients are positive integers. Thus, the sum consists of positive terms.
One of the terms in the sum corresponds to the choice $(k_1, \dots, k_n) = (a_1, \dots, a_n)$. Note that $\sum a_i = S$ and $a_i \ge 1$, so this is a valid tuple with non-negative integer entries.
The term is $\binom{S}{a_1, \dots, a_n} a_1^{a_1} \dots a_n^{a_n} = \frac{S!}{a_1! \dots a_n!} \prod_{i=1}^n a_i^{a_i} = \frac{S!}{\prod_{i=1}^n a_i!} P_1$.
Since $n \ge 2$ and $a_i \ge 1$, we have $S = \sum a_i \ge n \ge 2$.
Are there other terms in the sum? Consider the tuple $(S, 0, \dots, 0)$. This tuple satisfies $k_1+\dots+k_n = S$ and $k_i \ge 0$.
Is this tuple different from $(a_1, \dots, a_n)$? Yes, because $a_n \ge 1$, so $a_n \neq 0$.
The term corresponding to $(S, 0, \dots, 0)$ is $\binom{S}{S, 0, \dots, 0} a_1^S a_2^0 \dots a_n^0 = \frac{S!}{S! 0! \dots 0!} a_1^S = a_1^S$. Since $a_1 \ge 1$, this term is positive ($a_1^S \ge 1$).
Therefore, the multinomial sum $S^S$ consists of the term $\frac{S!}{\prod a_i!} P_1$ plus at least one other positive term (e.g., $a_1^S$).
$$
S^S = \frac{S!}{\prod_{i=1}^n a_i!} P_1 + \sum_{(k_1, \dots, k_n) \neq (a_1, \dots, a_n)} \binom{S}{k_1, \dots, k_n} a_1^{k_1} \dots a_n^{k_n}
$$
Since the sum on the right is non-empty and contains positive terms, we have
$$
S^S > \frac{S!}{\prod_{i=1}^n a_i!} P_1
$$
Now, we multiply this inequality by $\frac{\prod_{i=1}^n a_i!}{S!}$ (which is positive):
$$
\frac{S^S \prod_{i=1}^n a_i!}{S!} > P_1
$$
So, $LHS > P_1$.

Step 2: Show that $P_1 \ge RHS_\sigma$.
We want to show that $\prod_{i=1}^n a_i^{a_i} \ge \prod_{i=1}^n a_i^{a_{\sigma(i)}}$.
Taking the natural logarithm of both sides, we want to show:
$$
\log \left( \prod_{i=1}^n a_i^{a_i} \right) \ge \log \left( \prod_{i=1}^n a_i^{a_{\sigma(i)}} \right)
$$
$$
\sum_{i=1}^n a_i \log a_i \ge \sum_{i=1}^n a_{\sigma(i)} \log a_i
$$
This inequality is an application of the Rearrangement Inequality.
Let $(x_1, \dots, x_n) = (\log a_1, \dots, \log a_n)$ and $(y_1, \dots, y_n) = (a_1, \dots, a_n)$.
Let $\pi \in S_n$ be a permutation that sorts the sequence $(a_i)$ in non-decreasing order: $a_{\pi(1)} \le a_{\pi(2)} \le \dots \le a_{\pi(n)}$.
Since the logarithm function is increasing, the sequence $(\log a_i)$ is sorted in the same order: $\log a_{\pi(1)} \le \log a_{\pi(2)} \le \dots \le \log a_{\pi(n)}$.
Let $x'_i = \log a_{\pi(i)}$ and $y'_i = a_{\pi(i)}$. Both sequences $(x'_i)$ and $(y'_i)$ are non-decreasing.
The Rearrangement Inequality states that for any permutation $\tau \in S_n$,
$$
\sum_{i=1}^n x'_i y'_{\tau(i)} \le \sum_{i=1}^n x'_i y'_i
$$
Let's express these sums in terms of the original sequences.
The right-hand side is:
$$
\sum_{i=1}^n x'_i y'_i = \sum_{i=1}^n (\log a_{\pi(i)}) a_{\pi(i)} = \sum_{j=1}^n (\log a_j) a_j = \log P_1
$$
(by letting $j = \pi(i)$ and summing over $j$).
The left-hand side is:
$$
\sum_{i=1}^n x'_i y'_{\tau(i)} = \sum_{i=1}^n (\log a_{\pi(i)}) a_{\pi(\tau(i))}
$$
Let $j = \pi(i)$, so $i = \pi^{-1}(j)$. The sum becomes:
$$
\sum_{j=1}^n (\log a_j) a_{\pi(\tau(\pi^{-1}(j)))}
$$
Let $\sigma = \pi \tau \pi^{-1}$. As $\tau$ ranges over all permutations in $S_n$, $\sigma$ also ranges over all permutations in $S_n$.
The sum is $\sum_{j=1}^n (\log a_j) a_{\sigma(j)} = \sum_{j=1}^n a_{\sigma(j)} \log a_j = \log(RHS_\sigma)$.
So the Rearrangement Inequality implies $\log(RHS_\sigma) \le \log P_1$.
Exponentiating both sides gives $RHS_\sigma \le P_1$.

Step 3: Conclusion.
We have shown that $LHS > P_1$ in Step 1, and $P_1 \ge RHS_\sigma$ in Step 2.
Combining these two inequalities, we get:
$$
LHS > P_1 \ge RHS_\sigma
$$
Therefore, $LHS > RHS_\sigma$.
This means
$$
\frac{S^S \prod_{i=1}^n a_i!}{S!} > \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
which is equivalent to the desired inequality:
$$
\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}
$$

Final Answer: The final answer is $\boxed{\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}}$