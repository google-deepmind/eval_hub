This step is worth 4 points.
Let $b$, $N$ be positive integers such that $b<N$. For now assume that each box contains $b$ black balls, and $N-b$ white balls. By induction we show that probability of drawing the black ball from every box is the same.

Obviously, probability of drawing a black ball from the first box is equal to $\frac{b}{N}$.

Assume that for some $k<n$ probability of drawing the black ball from the $k$-th box is equal to $\frac{b}{N}$. Let $B_{k}, B_{k+1}$ mean drawing a black ball from the $k$-th and $(k+1)$-th box, respectively. Then, by the inductive assumption and the law of total probability we see that
$$
\begin{aligned}
P(B_{k+1})&=P(B_{k+1}|B_k)P(B_k)+P(B_{k+1}|B'_k)P(B_k')\\
&=\frac{b+1}{N+1}\cdot\frac{b}{N} + \frac{b}{N+1}\cdot\frac{N-b}{N} = \frac{b}{N}.
\end{aligned}
$$
Therefore, probability of drawing the black ball from each box is equal to $\frac{b}{N}$.

This step is worth 3 points.
Fix $k\in\{1,2,\ldots,m\}$. Let us color all the balls with number $k$ black and other numbers color white. Then applying step 1 with $b=k$ we see that probability of getting $k$ on final ball is equal to $\frac{k}{N}$, where $N=\frac{m(m+1)}{2}$.

This step is worth 3 points.
Let $K$ be the number on the last ball. We know that $P(K=k)=\frac{2k}{m(m+1)}$ for $k=1,2,\ldots,m$. Then 
$$
EK=\sum_{k=1}^{m}kP(K=k) = \sum_{k=1}^m \frac{2k^2}{m(m+1)} = \frac{2}{m(m+1)}\sum_{k=1}^mk^2.
$$
Since $\sum_{k=1}^mk^2 = \frac{m(m+1)(2m+1)}{6}$, it follows that
$$
EK = \frac{2m+1}{3}.
$$
This number is an integer if $2m+1$ is an odd number divisible by 3, hence $m=3p+1$ for some nonnegative integer $p$.