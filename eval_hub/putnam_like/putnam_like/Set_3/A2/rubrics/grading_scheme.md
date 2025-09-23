Solution step (3 points):
$p_n(x)=(x^k+1)^{n+1}f^{(n)}(x)$. By differentiating the equation $f^{(n)}(x)=\frac{p_n(x)}{(x^k+1)^{n+1}}$ 
we get
$$
f^{(n+1)}(x)=\frac{p'_n(x)(x^k+1)^{n+1}-p_n(x)(n+1)(x^k+1)^n \cdot kx^{k-1}}{(x^k+1)^{2n+2}}=\frac{p'_n(x)(x^k+1)-p_n(x)(n+1)kx^{k-1}}{(x^k+1)^{n+2}},
$$
so
$$
p_{n+1}(x)=p'_n(x)(x^k+1)-p_n(x)(n+1)kx^{k-1}.
$$

Solution step (6 points):
Note that $p_1(x)=(x^k+1)^2\cdot \frac{-kx^{k-1}}{(x^k+1)^2}=-kx^{k-1}$ so $p_1(x)=kq_1(x)$ where $q_1(x)$ is a polynomial in $\mathbb{Z}[x]$. 

When the polynomial has the form $P=kQ$, where $Q$ is in $\mathbb{Z}[x]$, $k$ is in $\mathbb{Z}$, its derivative has the same form. Therefore using the recurrence relation, for any $n\geq 1$ we get $p_{n+1}(x)=kq_{n+1}(x)$ for some $q_{n+1}(x)$ in $\mathbb{Z}[x]$. 

Solution step (1 point):
Thus, $p(k-1)=p_n(k-1)$ is an integer and $p(k-1)=k\cdot q_n(k-1)$, so $k|p(k-1)$, since $q_n(k-1)$ is an integer.
