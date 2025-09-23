This step is worth 3 points.
Let $U_n$ be a number of heads in $n$-th toss. We see that $P(U_n=1|p)=p$ and $P(U_n=0|p)=1-p.$ Moreover, random variables $U_n$ are conditionally independent when $p$ is fixed.

Let $N=\min\{n\in\mathbb{N}\,:\, U_n=1\}$ be the number of tosses up to getting the first heads. Then $P(N=n|p)=(1-p)^{n-1}p$.

This step is worth 4 points.
We know that $P(N=n)=EP(N=n|p)$. Hence
$$
P(N=n)=\int_0^1 (1-p)^{n-1}p\,dp = \int_0^{1} q^{n-1}(1-q)dq = \frac{1}{n}-\frac{1}{n+1},
$$
where we changed variables in the integral substituting $q=1-p$.

This step is worth 3 points.
Finally we have
$$
EN = \sum_{n=1}^{\infty}nP(N=n)=\sum_{n=1}^\infty \frac{1}{n+1}=\infty.
$$