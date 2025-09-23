This step is worth 4 points.
First we show that
$$
f_n(x)=\prod_{i=1}^n\cos((2i-1)x) = 2^{-n}\sum\left\{\cos\left(\sum_{i=1}^{n} s_i(2i-1)x \right)\,:\, s_1,s_2,\ldots,s_n\in\{-1,1\}\right\}.
$$
We use the induction. For $n=1$ it is obvious. Assume that the above equity holds true for some natural $n$. Observe that
$$
\begin{split}
\cos\Big(\sum_{i=1}^{n} s_i(2i-1)x &+ (2n+1)x\Big) + \cos\left(\sum_{i=1}^{n} s_i(2i-1)x - (2n+1)x\right) \\
&= 2 \cos\left(\sum_{i=1}^{n} s_i(2i-1)x \right) \cos((2n+1)x).	
\end{split}
$$
Summing up the above over all combinations $s_1,s_2,\ldots,s_n\in\{-1,1\}$ and using the inductive assumption we see that
$$
\begin{aligned}
&\quad \sum\left\{\cos\left(\sum_{i=1}^{n} s_i(2i-1)x \right)\,:\, s_1,s_2,\ldots,s_n\in\{-1,1\}\right\}\\
& = 2\cdot 2^nf_n(x)\cdot\cos((2n+1)x)=2^{n+1}f_{n+1}(x),
\end{aligned}
$$
which completes the proof.

This step is worth 3 points.
We see that
$$
\int_0^{2\pi}f_n(x)dx = 2^{-n}\sum\left\{\int_0^{2\pi}\cos\left(\sum_{i=1}^{n} s_i(2i-1)x \right)dx\,:\, s_1,s_2,\ldots,s_n\in\{-1,1\}\right\}.
$$
Moreover, 
$$
\int_0^{2\pi}\cos(\alpha x)dx =\begin{cases}
2\pi, & \alpha=0\\
0, & \alpha \neq 0.
\end{cases}
$$
Therefore
$$
\int_0^{2\pi}f_n(x)dx = 2^{-n-1}\cdot\pi N(n), 
$$
where $N(n)=\sharp\left\{(s_1,s_2,\ldots,s_n)\in\{-1,1\}^n\,:\, \sum_{i=1}^{n} s_i(2i-1) = 0\right\}.$  Hence $\int_0^{2\pi}f_n(x)dx=0$ if and only if $N(n)=0$.

This step is worth 2 points.
Note that 
$$
\sum_{i=1}^n(2i-1) = n^2
$$
which is odd when $n$ is odd. If we change a sign in the above sum (in which $s_i=1$ for $i=1,2,\ldots,n$), we reduce $S$ by an even number. That’s why, if $S$ is odd, then for any system of signs $(s_1, s_2,\ldots, s_n)$, the sum $\sum_{i=1}^ns_i(2i-1)\neq 0$.

This step is worth 1 point.
Summing up, 
$$
0\leq \liminf_{n\to\infty}\int_0^{2\pi}f_n(x)dx \leq \lim_{n\to\infty}\int_0^{2\pi}f_{2n+1}(x)dx = 0,
$$ 
and hence $\liminf_{n\to\infty}\int_0^{2\pi}f_n(x)dx=0.$