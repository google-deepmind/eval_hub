This step is worth 5 points.
Note that $q_n$ is a probability that $\hat X_n$ is some permutation of $(2n-1,2n,2n+1)$. Let $u_n$ be a probability that $\hat X_n$ is equal to some permutation of $(2n-2,2n+1,2n+1)$ or $(2n+2, 2n-1,2n-1)$.

Assume that $\hat X_n$ is a permutation of $(2n-1,2n,2n+1)$. Then there is exactly one possible value of $X_{n+1}$, for which $\hat R_{n+1}=\hat S_{n+1}=\hat T_{n+1}$, two possible values for which $\hat X_{n+1}$ is a permutation of $(2n+1,2n+2,2n+3)$ and two possible values for which $\hat X_{n+1}$ is a permutation of  $(2n,2n+3,2n+3)$ or $(2n+4, 2n+1,2n+1)$. For the last possible value of $X_{n+1}$, $\hat X_{n+1}$ is a permutation of $(2n,2n+2,2n+4)$.

If $\hat R_n=\hat S_n=\hat T_n$, then always $\hat X_{n+1}$ is a permutation of $(2n+1,2n+2,2n+3)$. Moreover, if $\hat X_n$ is a permutation of $(2n-2,2n,2n+2)$, then there are two values of $X_{n+1}$, for which $\hat X_{n+1}$ is a permutation of $(2n+1,2n+2,2n+3)$.

Summarizing the above and using the law of total probability we have
$$
\begin{cases}
p_{n+1} = \frac{q_n}{6},\\
q_{n+1} \geq p_n + \frac{q_n}{3} + \frac{u_n}{3},\\
u_{n+1} \geq \frac{q_n}{3},
\end{cases}
$$
where the inequalities follows from the fact, that we skipped some possibilities on the right hand side.

This step is worth 4 points.
Assume that $4p_n\geq q_n$. Using the above system of inequalities we deduce that
$$
q_{n+1}\geq \frac{q_n}{4} + \frac{q_n}{3} + \frac{q_{n-1}}{9} = \frac{7q_n}{12} + \frac{2p_n}{3} \geq \frac{7q_n}{12} + \frac{q_n}{6} = \frac{9q_n}{12} = \frac{9p_{n+1}}{2} > 4 p_{n+1}.
$$
This shows that for each $n$ we have $4p_n<q_n$ or $4p_{n+1}<q_{n+1}$.

This step is worth 1 point.
Obviously for each pair of indexes $(2k-1,2k)$, $k\in\mathbb{N}$ we have $4p_{2k-1}<q_{2k-1}$ or $4p_{2k}<q_{2k}$. Since there is infinitely many $k\in\mathbb{N}$, the desired result follows.