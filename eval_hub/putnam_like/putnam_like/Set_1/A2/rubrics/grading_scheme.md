Solution step (1 point):
First observe that by changing the order of summation, we get
$$
\sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n  \frac{1}{4^k} {\ell \choose 2k} = \sum_{\ell = 1}^n \sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} \frac{1}{4^k} {\ell \choose 2k}.
$$

Solution step (1 point):
Let $x \in \mathbb{R}$. Recall that
$$
(1+x)^\ell = \sum_{k=0}^\ell {\ell \choose k} x^k
$$
and
$$
(1-x)^\ell = \sum_{k=0}^\ell {\ell \choose k} (-1)^k x^k.
$$

Solution step (8 points):
Hence, taking the sum of these two identities and after re-indexing the sum we obtain
$$
2 \sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} {\ell \choose 2k} x^{2k} = (1+x)^\ell + (1-x)^\ell
$$
or equivalently
$$
\sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} {\ell \choose 2k} x^{2k} = \frac12 \left( (1+x)^\ell + (1-x)^\ell \right).
$$
In particular, for $x = \frac12$, we get 
$$
\sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} \frac{1}{4^k} {\ell \choose 2k} = \frac12 \left( \left( \frac{3}{2} \right)^\ell + \left( \frac12 \right)^\ell \right).
$$
Thus
$$
\begin{aligned}
\sum_{\ell = 1}^n \sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} \frac{1}{4^k} {\ell \choose 2k} &= \sum_{\ell = 1}^n \frac12 \left( \left( \frac{3}{2} \right)^\ell + \left( \frac12 \right)^\ell \right) \\
&= \frac12 \left( \frac{3}{2} \frac{\left(\frac{3}{2}\right)^n - 1}{\frac12} + \frac12 \frac{1 - \left(\frac{1}{2}\right)^n}{\frac12} \right) \\
&= \frac12 \left( 3 \frac{3^n}{2^n} - 3 + 1 - \frac{1}{2^n} \right) = \frac{3^{n+1} - 1}{2^{n+1}} - 1.
\end{aligned}
$$