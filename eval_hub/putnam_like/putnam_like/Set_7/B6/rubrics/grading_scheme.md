Solution step (1 point):
Note that for $n = 0$ the result is clear and therefore we can consider only $n \geq 1$.

Solution step (2 points):
Then we rewrite the problem as
$$
\sum_{k=1}^n (-1)^{\left\lfloor k (\sqrt{3}-1) \right\rfloor} \geq 0.
$$
To simplify the notation, we introduce $a_k := \left\lfloor k (\sqrt{3}-1) \right\rfloor$ and $b_k := (-1)^{a_k}$ for $k \geq 1$. Then, the first terms of $b_k$ are given by
$$
b_1 = 1, \ b_2 = -1, \ b_3 = 1, \ b_4 = 1, \ b_5 = -1, \ b_6 = 1, \ b_7 = -1.
$$
Let $c_k$ be the sequence of lengths of consecutive clusters of $1$'s and $(-1)$'s in $(b_k)$, namely
$$
c_1 = 1, \ c_2 = 1, \ c_3 = 2, \ c_4 = 1, \ c_5=1, \ \ldots.
$$
Then, clearly the sum $c_1 + c_2 + \ldots + c_i$ equals to the number of positive integers $k$ such that $k (\sqrt{3}-1) < i$. It is equivalent to $k < i \frac{\sqrt{3}+1}{2}$. Hence 
$$
c_1 + c_2 + \ldots + c_i = \left\lfloor i \frac{\sqrt{3}+1}{2} \right\rfloor
$$
and therefore, for $i \geq 2$ we have
$$
\begin{aligned}
c_i &= \left(c_1 + c_2 + \ldots + c_i\right) - \left(c_1 + c_2 + \ldots + c_{i-1}\right) = \left\lfloor i \frac{\sqrt{3}+1}{2} \right\rfloor - \left\lfloor (i-1) \frac{\sqrt{3}+1}{2} \right\rfloor \\
&= \left\lfloor i \frac{\sqrt{3}-1}{2} + i \right\rfloor - \left\lfloor (i-1) \frac{\sqrt{3}-1}{2} + (i-1) \right\rfloor \\
&= 1 + \left\lfloor i \frac{\sqrt{3}-1}{2} \right\rfloor - \left\lfloor (i-1) \frac{\sqrt{3}-1}{2} \right\rfloor.
\end{aligned}
$$
Note that, since $\frac{\sqrt{3}-1}{2} < \frac12$, we know that $\left\lfloor i \frac{\sqrt{3}-1}{2} \right\rfloor - \left\lfloor (i-1) \frac{\sqrt{3}-1}{2} \right\rfloor \in \{0,1\}$ and it is equal to $1$ only if there is an integer in the interval $\left[ (i-1) \frac{\sqrt{3}-1}{2}, i \frac{\sqrt{3}-1}{2} \right]$. In other words, it is equal to $1$ if and only if there is $j \in \mathbb{Z}$ such that $(i-1) \frac{\sqrt{3}-1}{2} < j < i \frac{\sqrt{3}-1}{2}$. We can rewrite this condition equivalently as $i-1 < j (\sqrt{3}+1) < i$. In other words, $i = \left\lfloor j (\sqrt{3}+1) \right\rfloor + 1$. Hence we obtain that
$$
c_i = \begin{cases}
2 &\quad \text{if } i = \left\lfloor j (\sqrt{3}+1) \right\rfloor + 1 \text{ for some positive integer } j,\\
1 &\quad \text{otherwise}
\end{cases}
$$
for $i \geq 2$. For $i=1$ we have $c_1=1$ and the above formula works as well, since $\left\lfloor j (\sqrt{3}+1) \right\rfloor + 1 \geq 1$ for each positive $j$.

Solution step (7 points):
To show that 
$$
\sum_{k=1}^n b_k \geq 0
$$
we will use the mathematical induction. Easy computation shows that the statement holds for $n \in \{1,2,3\}$. Suppose now that there is $N$ such that the above inequality holds for every $n \leq N$, with $N \geq 3$, and we will show that it holds for every $n \leq 2N$. For that purpose it is enough to show that
$$
\sum_{k=1}^m (-1)^{k+1} c_k \geq 0
$$
for every $m$ such that $c_1 + \ldots + c_m < 2N + 2$ (then for sure we cover in the sum all the clusters of $1$'s and $(-1)$'s in the sum up to $2N$ summands). Observe that, since $c_i \geq 1$, we get that $m < 2N+2$. Suppose that $m$ is even. Then
$$
\begin{aligned}
\sum_{k=1}^m (-1)^{k+1} c_k &= \sum_{k=1}^m (-1)^{k+1} (c_k - 1) = \sum_{j > 0 \ : \ j(\sqrt{3}+1) +1 < m} (-1)^{\left\lfloor j (\sqrt{3}+1)) \right\rfloor + 2} \\
&= \sum_{j \geq 1 \ : \ j < \frac12 (m-1) (\sqrt{3}-1)} (-1)^{\left\lfloor j (\sqrt{3}+1)) \right\rfloor} \\
&= \sum_{j \geq 1 \ : \ j < \frac12 (m-1) (\sqrt{3}-1)} (-1)^{\left\lfloor j (\sqrt{3}-1)) \right\rfloor} \\
&= \sum_{j \geq 1 \ : \ j < \frac12 (m-1) (\sqrt{3}-1)} b_j.
\end{aligned}
$$
Now, observe that
$$
\frac12 (m-1) (\sqrt{3}-1) < \frac{\sqrt{3}-1}{2} (2N+2) = (\sqrt{3}-1) (N+1) \leq N
$$
for $N \geq 3$. Hence $\sum_{j \geq 1 \ : \ j < \frac12 (m-1) (\sqrt{3}-1)} b_j \geq 0$ by the induction assumption. Thus $\sum_{k=1}^m (-1)^{k+1} c_k \geq 0$. Suppose now that $m$ is odd. Then, repeating similar calculation as above,
$$
\sum_{k=1}^m (-1)^{k+1} c_k = c_m + \sum_{k=1}^{m-1} (-1)^{k+1} c_k = c_m + \sum_{j \geq 1 \ : \ j < \frac12 (m-2) (\sqrt{3}-1)} b_j.
$$
Note that
$$
\frac12 (m-2) (\sqrt{3}-1) \leq \frac12 (m-1) (\sqrt{3}-1) \leq N
$$
for $N \geq 3$ and again, by the induction assumption, $\sum_{j \geq 1 \ : \ j < \frac12 (m-2) (\sqrt{3}-1)} b_j \geq 0$ and then $\sum_{k=1}^m (-1)^{k+1} c_k \geq 0$. Hence the proof is completed.