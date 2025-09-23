This step is worth 6 points.
Let $g_n(x)=e^{-x}(f(x)+f'(x)+\ldots + f^{(n)}(x))$. Then
$$
\frac{g(b_n)}{g(a_n)}=e^{a_n-b_n}\frac{f(b_n)+f'(b_n)+\ldots + f^{(n)}(b_n)}{f(a_n)+f'(a_n)+\ldots + f^{(n)}(a_n)} = 1.
$$
By Mean Value Theorem we know that there exist $c_n\in(a_n,b_n)$ such that
$$
0 = g'(c_n) = e^{-c_n}(f^{(n+1)}(c_n)-f(c_n)).
$$
Hence
$$
f^{(n+1)}(c_n)=f(c_n),\qquad n\in\mathbb{N}.
$$

This step is worth 1 point.
Since $a_n<c_n<b_n$, $\lim_{n\to\infty} c_n = c$. Hence
$$
f(c) = \lim_{n\to\infty} f^{(n)}(c_{n-1}).
$$

This step is worth 3 points.
Finally observe that
$$
|f^{(n)}(c_{n-1})-f^{(n)}(c)|\leq \sup_{d\in(-1,1)}|f^{(n+1)}(d)|\cdot |c_{n-1}-c|,
$$
and hence
$$
f(c) = \lim_{n\to\infty} f^{(n)}(c).
$$