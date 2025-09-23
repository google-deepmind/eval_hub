# Solution

I need to compute the sum
$$
\sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n  \frac{1}{4^k} {\ell \choose 2k}
$$

Let me start by evaluating the inner sum separately for $k=0$ and $k \geq 1$.

For $k=0$, the inner sum is:
$$
\sum_{\ell = \max\{1, 0\}}^n \frac{1}{4^0} {\ell \choose 0} = \sum_{\ell = 1}^n 1 = n
$$

For $k \geq 1$, we have $\max\{1, 2k\} = 2k$, so the inner sum is:
$$
\sum_{\ell = 2k}^n \frac{1}{4^k} {\ell \choose 2k}
$$

I'll use the hockey-stick identity (also known as the upper summation formula):
$$
\sum_{j=r}^n {j \choose r} = {n+1 \choose r+1}
$$

This gives us:
$$
\sum_{\ell = 2k}^n {\ell \choose 2k} = {n+1 \choose 2k+1}
$$

Therefore, for $k \geq 1$, the inner sum equals:
$$
\frac{1}{4^k} {n+1 \choose 2k+1}
$$

Combining the results for all values of $k$:
$$
\sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n \frac{1}{4^k} {\ell \choose 2k} = n + \sum_{k=1}^{\left\lfloor \frac{n}{2} \right\rfloor} \frac{1}{4^k} {n+1 \choose 2k+1}
$$

To evaluate this further, I'll use the binomial identity:
$$(1+x)^{n+1} - (1-x)^{n+1} = 2x\sum_{k=0}^{\lfloor \frac{n}{2} \rfloor} {n+1 \choose 2k+1}x^{2k}$$

Setting $x = \frac{1}{2}$, we get:
$$\left(1+\frac{1}{2}\right)^{n+1} - \left(1-\frac{1}{2}\right)^{n+1} = 2 \cdot \frac{1}{2} \sum_{k=0}^{\lfloor \frac{n}{2} \rfloor} {n+1 \choose 2k+1}\left(\frac{1}{2}\right)^{2k} = \sum_{k=0}^{\lfloor \frac{n}{2} \rfloor} {n+1 \choose 2k+1}\frac{1}{4^k}$$

This means:
$$\sum_{k=0}^{\lfloor \frac{n}{2} \rfloor} {n+1 \choose 2k+1}\frac{1}{4^k} = \left(\frac{3}{2}\right)^{n+1} - \left(\frac{1}{2}\right)^{n+1}$$

Hence:
$$\sum_{k=1}^{\lfloor \frac{n}{2} \rfloor} {n+1 \choose 2k+1}\frac{1}{4^k} = \left(\frac{3}{2}\right)^{n+1} - \left(\frac{1}{2}\right)^{n+1} - (n+1)$$

Therefore, our final answer is:
$$\sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n \frac{1}{4^k} {\ell \choose 2k} = n + \left(\frac{3}{2}\right)^{n+1} - \left(\frac{1}{2}\right)^{n+1} - (n+1) = \left(\frac{3}{2}\right)^{n+1} - \left(\frac{1}{2}\right)^{n+1} - 1$$