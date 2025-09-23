This step was worth 2 points.
Observe that, using the coarea formula and changing the variables $r=|x|$,
$$
\frac{m_{i_1, \ldots, i_k}^{2N+i_1+\ldots+i_k-1}}{i_1 + \ldots + i_k + N} = m_{i_1, \ldots, i_k}^{N-1} \int_0^{m_{i_1, \ldots, i_k}} r^{i_1 + \ldots + i_k} \cdot r^{N-1} \, dr = \frac{1}{\omega_N} \int_{B(0, m_{i_1, \ldots, i_k})} |x|^{i_1 + \ldots + i_k} \, dx,
$$
where $B(0, R)$ denotes the ball of radius $R$ in $R^N$ and $\omega_{N}$ is the surface area of a unit, $(N-1)$-dimensional sphere in $R^N$. Thus, we can rewrite the sum given in the statement as
$$
\sum_{k=1}^n \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k} \frac{m_{i_1, \ldots, i_k}^{2N+i_1+\ldots+i_k-1}}{i_1 + \ldots + i_k + N} = \frac{1}{\omega_N} \sum_{k=1}^n \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k}  \int_{B(0, m_{i_1, \ldots, i_k})} |x|^{i_1 + \ldots + i_k} \, dx = (*).
$$

This step was worth 8 points.
Define a family of functions $\{f_i\}_{i=1}^n$ by
$$
f_i (x) := -\chi_{B(0, r_i)} (x) |x|^{i}, \quad x \in R^N,
$$
where $\chi_A$ denotes the characteristic function of a set $A \subset R^N$.
Then
$$
(-1)^{k}  \int_{B(0, m_{i_1, \ldots, i_k})} |x|^{i_1 + \ldots + i_k} \, dx = \int_{B(0, m_{i_1, \ldots, i_k})} (-1)^{k} |x|^{i_1 + \ldots + i_k} \, dx =  \int_{B(0, m_{i_1, \ldots, i_k})} (-|x|^{i_1}) (-|x|^{i_2}) \ldots (-|x|^{i_k}) \, dx = \int_{R^N} f_{i_1}(x) f_{i_2}(x) \ldots f_{i_k}(x) \, dx.
$$
Hence
$$
(*) = \frac{1}{\omega_N} \sum_{k=1}^n \sum_{1 \leq i_1 < \ldots < i_k \leq n} \int_{R^N} f_{i_1}(x) f_{i_2}(x) \ldots f_{i_k}(x) \, dx = \frac{1}{\omega_N} \int_{R^N} \sum_{k=1}^n \sum_{1 \leq i_1 < \ldots < i_k \leq n} f_{i_1}(x) f_{i_2}(x) \ldots f_{i_k}(x) \, dx = \frac{1}{\omega_N} \int_{R^N} (1+f_1(x)) (1+f_2(x)) \ldots (1+f_n(x)) - 1 \, dx = (**).
$$
Observe that, since $r_i < 1$ for all $i$, we have that $|1-f_i(x)| \leq 1$ for all $x \in R^N$. Indeed, if $x \not\in B(0, r_i)$, $f_i(x) = 0$ and the inequality is clear. Otherwise it reads as $\left| 1 - |x|^i \right| \leq 1$ which is equivalent that $|x|^i \leq 2$. It is clear, since $|x| < r_i < 1$ and $|x|^i < 1$. Hence, for every $x \in R^N$,
$$
(1+f_1(x)) (1+f_2(x)) \ldots (1+f_n(x)) - 1 \leq 0
$$
and therefore $(**) \leq 0$ and the proof is complete.