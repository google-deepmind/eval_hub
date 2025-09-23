Let the given sum be $S_n$. The sum is
$$
S_n = \sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n  \frac{1}{4^k} {\ell \choose 2k}.
$$
We can separate the term for $k=0$ from the sum, as the lower limit for $\ell$ depends on $k$.

For $k=0$:
The term is $\frac{1}{4^0} \sum_{\ell = \max\{1, 0\}}^n \binom{\ell}{0} = 1 \cdot \sum_{\ell=1}^n \binom{\ell}{0}$.
Since $\binom{\ell}{0} = 1$ for $\ell \ge 0$, this sum is $\sum_{\ell=1}^n 1$.
If $n \ge 1$, $\sum_{\ell=1}^n 1 = n$.
If $n=0$, the sum is $\sum_{\ell=1}^0 1$, which is an empty sum, equal to 0. The value of $n$ is also 0.
So, the term for $k=0$ is $n$.

For $k > 0$:
The range for $k$ is $1 \le k \le \lfloor n/2 \rfloor$. This implies $k \ge 1$, so $2k \ge 2$.
The lower limit for $\ell$ is $\max\{1, 2k\} = 2k$.
The inner sum is $\sum_{\ell=2k}^n \binom{\ell}{2k}$.
For the binomial coefficient $\binom{\ell}{2k}$ to be non-zero, we must have $\ell \ge 2k$. The summation starts at $2k$, so all terms are potentially non-zero.
We can use the Hockey-stick identity: $\sum_{i=r}^m \binom{i}{r} = \binom{m+1}{r+1}$.
Let $i=\ell$, $r=2k$, and $m=n$. The sum is $\sum_{\ell=2k}^n \binom{\ell}{2k} = \binom{n+1}{2k+1}$.
This identity holds for $m \ge r$. Since $k \le \lfloor n/2 \rfloor$, we have $k \le n/2$, so $2k \le n$. Thus $n \ge 2k$, and the identity applies.
The term for $k > 0$ is $\frac{1}{4^k} \binom{n+1}{2k+1}$.

Combining the $k=0$ term and the terms for $k>0$:
$S_n = n + \sum_{k=1}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1}$.

We can rewrite the $k=0$ term $n$ using $\binom{n+1}{1} = n+1$. So $n = \binom{n+1}{1} - 1$.
$S_n = \binom{n+1}{1} - 1 + \sum_{k=1}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1}$.
This can be written as:
$S_n = \left( \binom{n+1}{1} + \sum_{k=1}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1} \right) - 1$.

Let's consider the sum $T_m = \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \frac{1}{4^k} \binom{m}{2k+1}$.
Let $m=n+1$. Then $\lfloor (m-1)/2 \rfloor = \lfloor n/2 \rfloor$.
$T_{n+1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1}$.
The sum inside the parenthesis for $S_n$ is $\binom{n+1}{1} + \sum_{k=1}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1}$.
The $k=0$ term in $T_{n+1}$ is $\frac{1}{4^0} \binom{n+1}{2(0)+1} = \binom{n+1}{1}$.
So $T_{n+1} = \frac{1}{4^0} \binom{n+1}{1} + \sum_{k=1}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1} = \binom{n+1}{1} + \sum_{k=1}^{\lfloor n/2 \rfloor} \frac{1}{4^k} \binom{n+1}{2k+1}$.
Thus, $S_n = T_{n+1} - 1$.

Now we evaluate $T_m = \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \frac{1}{4^k} \binom{m}{2k+1}$.
Consider the binomial expansion of $(1+x)^m$ and $(1-x)^m$:
$(1+x)^m = \sum_{j=0}^m \binom{m}{j} x^j$
$(1-x)^m = \sum_{j=0}^m \binom{m}{j} (-x)^j$
Subtracting the two expansions, we get:
$(1+x)^m - (1-x)^m = \sum_{j=0}^m \binom{m}{j} (x^j - (-x)^j)$.
If $j$ is even, $x^j - (-x)^j = x^j - x^j = 0$.
If $j$ is odd, $x^j - (-x)^j = x^j - (-1)^j x^j = x^j - (-x^j) = 2x^j$.
So, $(1+x)^m - (1-x)^m = 2 \sum_{j \text{ odd}, 0 \le j \le m} \binom{m}{j} x^j$.
Let $j=2k+1$. As $j$ takes odd values from $1$ up to $m$ (or $m-1$ if $m$ is even), $k$ takes integer values starting from $0$. $2k+1 \le m \implies 2k \le m-1 \implies k \le (m-1)/2$. Since $k$ is an integer, $k \le \lfloor (m-1)/2 \rfloor$.
$\frac{(1+x)^m - (1-x)^m}{2} = \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} x^{2k+1}$.

We want the term $\frac{1}{4^k} \binom{m}{2k+1}$.
The expression on the right side is $\sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} x^{2k+1} = \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} x \cdot (x^2)^k$.
We want this to match $\sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} \frac{1}{4^k}$.
If we set $x = 1/2$:
$x=1/2$, $x^2 = 1/4$.
$\sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} (1/2)^{2k+1} = \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} \frac{1}{2^{2k+1}} = \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} \frac{1}{2 \cdot 4^k} = \frac{1}{2} \sum_{k=0}^{\lfloor (m-1)/2 \rfloor} \binom{m}{2k+1} \frac{1}{4^k} = \frac{1}{2} T_m$.

So, $\frac{1}{2} T_m = \frac{(1+1/2)^m - (1-1/2)^m}{2} = \frac{(3/2)^m - (1/2)^m}{2}$.
$\frac{1}{2} T_m = \frac{\frac{3^m}{2^m} - \frac{1}{2^m}}{2} = \frac{3^m-1}{2^m} \cdot \frac{1}{2} = \frac{3^m-1}{2^{m+1}}$.
Multiplying by 2, $T_m = \frac{3^m-1}{2^m}$.

Substitute $m=n+1$:
$T_{n+1} = \frac{3^{n+1}-1}{2^{n+1}}$.

Finally, $S_n = T_{n+1} - 1$.
$S_n = \frac{3^{n+1}-1}{2^{n+1}} - 1$.

The sum is $\frac{3^{n+1}-1-2^{n+1}}{2^{n+1}}$.

The final answer is $\boxed{\frac{3^{n+1}-1}{2^{n+1}}-1}$.