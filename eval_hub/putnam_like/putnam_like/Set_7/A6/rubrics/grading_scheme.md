Solution step (1 point).
Fix $x,y > 0$. Note that the following limit exists
$$\tag{1}
\begin{aligned}
\lim_{z \to 0^+} f(z) &= \lim_{z \to 0^+} f(zf(x+y)) \\
&= \lim_{z \to 0^+} \left(2 + f(x+y+z) - f(x f(y+z)) - f(yf(x+z))  \right) \nonumber \\
&= 2 + f(x+y) - f(xf(y)) - f(y f(x)). 
\end{aligned}
$$
Thus, denote $\lim_{x \to 0^+} f(x) = L \geq 0$. In particular, $\lim_{x \to 0^+} x f(2x) = 0 \cdot L = 0$. Taking $x=y=z$ we get 
$$
f(xf(2x)) + f(xf(2x)) + f(xf(2x)) = 2 + f(3x)
$$
and passing to the limit with $x \to 0^+$ we obtain
$$
3L = 2 + L
$$
and therefore $L=1$. 

Solution step (1 point).
Using now (1) we obtain that for every $x,y > 0$ we have
$$
1 = 2 + f(x+y) - f(xf(y)) - f(y f(x)),
$$
or equivalently
$$\tag{2}
1 + f(x+y) = f(xf(y)) + f(y f(x)).
$$

Solution step (7 points)
Clearly $f(x) \equiv 1$ is the unique constant solution. Hence, from now on, we will assume that $f$ is nonconstant. Define
$$
S := f^{-1} (\{1\}).
$$
Suppose that $f(x) \geq 1$ for some $x > 0$. Then either $f(x) = 1$ and $x \in S$ or, if we take $y = \frac{x}{f(x)-1}$ in (2), we get $f(xf(y))=1$ and $xf(y) \in S$. In both cases, $S \neq \emptyset$. Suppose now that $f(x)=f(y)=1$. Then from (2) we find
$$
1 + f(x+y) = f(x)+f(y) = 2.
$$
Thus 
$$\tag{3}
x,y \in S \quad \Longrightarrow \quad x+y \in S.
$$
Define $m := \inf S$. Note that, since $f$ is nonconstant, $S$ is not dense in $(0,\infty)$. Then $m > 0$, because of \eqref{eq:additive}. Indeed, if $m = 0$, there exists a sequence $(x_n) \subset S$, $x_n \to 0^+$. But then one can easily show that $S$ is dense. Fix a number $a \in (0,\infty)$ and $\varepsilon > 0$. Choose $n$ so large that $x_n < \varepsilon$. Then, from the Archimedean property one can find $m=m_n \in \mathbb{N}$ such that $a \in (m x_n, (m+1) x_n)$ and $m x_n, (m+1) x_n \in S$ and $\mathrm{dist} (a, S) < \varepsilon$. Thus $m > 0$. From continuity $f(m)=1$ and $m \in S$.

Now, taking $x = y = \frac{m}{2}$ in (2) we get
$$
2 = 1 + f(m) = 2 f \left( \frac{m}{2} f \left( \frac{m}{2} \right) \right).
$$
Hence $\frac{m}{2} f \left( \frac{m}{2} \right) \in S$. Hence $\frac{m}{2} f \left( \frac{m}{2} \right) \geq m$ and $f \left( \frac{m}{2} \right) \geq 2$. Then, from the continuity, there is $x_0 \in (0,m)$ such that $f(x_0) = 1 + \frac{x_0}{m}$. But then, from (2) applied to $x=x_0$ and $y=m$ we get
$$
1+f(x_0+m) = f(x_0 f(m)) + f(m f(x_0)) = f(x_0) + f(m + x_0)
$$
and $f(x_0) = 1$, which is a contradiction. This means that $f(x) < 1$ for every $x \in (0,\infty)$.

Let $I = \inf_{x > 0} f(x)$. Choose $\varepsilon \in \left(0, \frac{1-I}{2} \right)$ and $y > 0$ such that $f(y) < I + \varepsilon$. Then, if for some $x$ there holds $x f(x) = y$, we get
$$
1+I \leq 1 + f(2x) = 2f(y) < 2I + 2 \varepsilon,
$$
which is a contradiction. Hence $xf(x) \neq y$. On the other hand $\lim_{x \to 0^+} x f(x) = 0 \cdot 1 = 0$. Hence, from the continuity, $\sup_{x > 0} xf(x) < \infty$.

Note that if $f$ is a solution to our problem, then $f(c \cdot)$ is also a solution. Hence, without loss of generality we can assume that $f(1) = \frac12$ and that $f(x) > \frac12$ for $x \in (0,1)$. 

Then, repeating a similar calculation
$$\tag{4}
f(xf(x))= \frac12 (1+f(2x)) > \frac12 = f(1)
$$
yields that $xf(x) \neq 1$ for all $x > 0$ and therefore $xf(x) < 1$ for all $x > 0$. Then, from (4),
$$
\lim_{x\to\infty} f(xf(x)) = \frac12.
$$
Now, setting $y = xy$ in (2) we get
$$
f(xf(xy))+f(xyf(x))=1+f(x+xy)
$$
and taking the limit as $x \to \infty$ we arrive at
$$
f \left( \frac{1}{y} \right) + f(y) = 1
$$
for all $y > 0$. Thus
$$
\begin{aligned}
1 &= \lim_{x \to \infty} (xf(y)) f(xf(y)) = \lim_{x\to\infty} \left( xf(y) f(x+y) + xf(y) f \left( \frac{1}{yf(x)} \right) \right) \\
&= f(y) \lim_{x\to\infty} \left( (x+y) f(x+y) - y f(x+y) \right) + y f(y) \lim_{x\to\infty} \left( xf(x)   \frac{1}{yf(x)}     f \left( \frac{1}{yf(x)} \right) \right) \\
&= f(y) + yf(y)
\end{aligned}
$$
and therefore $f(y) = \frac{1}{1+y}$ for any $y > 0$. Taking into account the scaling, we get $f(x) = \frac{1}{1+cx}$ is a solution for any $c > 0$. To include also the constant solution, it is enough to consider $f(x) = \frac{1}{1+cx}$ for $c \geq 0$.

Solution step (1 point)
It is easy to check that such functions satisfy the equation. Hence, all solutions are $f(x) = \frac{1}{1+cx}$ for $c \geq 0$.