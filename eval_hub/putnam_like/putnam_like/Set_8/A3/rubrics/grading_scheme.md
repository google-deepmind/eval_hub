This step is worth 2 points.
Since all terms of $(x_n)$ are positive,
$$0<\sum_{n=0}^{\infty}x_n^3 < \left(\sum_{n=0}^{\infty}x_n\right)^3 = c^3.$$
Hence $Y\subset(0,c^3)$. We show that $Y=(0,c^3)$.

This step is worth 5 points.
Let $h\in(0,1)$. We show that there exists a geometric sequence $(x_n)\in X$ such that $\sum_{n=0}^{\infty}x_n^3 = hc^3$. 

Let $q\in(0,1)$. Put $x_0=c(1-q)$ and $x_n=c(1-q)q^n$ for $n\in\mathbb{N}$. Obviously $\sum_{n=0}^\infty x_n = \frac{c(1-q)}{1-q}=c$.
Moreover
$$ \sum_{n=0}^\infty x_n^3 = \frac{c^3(1-q)^3}{1-q^3} = c^3\frac{1-2q+q^2}{1+q+q^2}.$$
To complete the proof it suffices to show that there exists $q\in(0,1)$ such that $\frac{1-2q+q^2}{1+q+q^2} = h$.

This step is worth 3 points.
Note that the latter equality is equivalent to the following
$$1-h = \frac{3q}{1+q+q^2}.$$
Consider a function $f(x)=\frac{3q}{1+q+q^2}$. Note that $f(0)=0$, $f(1)=1$ and $f$ is increasing on $(0,1)$, since
$$f'(q)=\frac{3-3q^3}{(1+q+q^2)^2} > 0,\qquad q\in(0,1).$$
Therefore, by Darboux's theorem, there exists $q\in(0,1)$ such that $f(q)=1-h$ and desired result follows.