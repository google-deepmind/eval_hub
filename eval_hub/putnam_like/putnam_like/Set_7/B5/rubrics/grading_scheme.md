Solution step (1 point)
First, we claim that $g$ is an injection. Indeed, suppose that $g(x) = g(y)$ for some $x,y \in \mathbb{R}$. Then, clearly
$$
\frac12 g(x) + \frac12 x = g(g(x)) = g(g(y)) = \frac12 g(y) + \frac12 y = \frac12 g(x) + \frac12 {y}
$$
and therefore $x=y$.

Solution step (1 point)
In particular, as $g$ is continuous, it has to be strictly monotone. Hence the limits $\lim_{x\to\infty} g(x)$ and $\lim_{x\to-\infty} g(x)$ exist (but may be infinite). Suppose that $\lim_{x\to\infty} g(x) = L$ is finite. Then
$$
\infty = \lim_{x\to\infty} \frac12 x = \lim_{x\to\infty} g(g(x)) - \frac12 g(x) = g(L)-\frac12 L,
$$
which is a contradiction. Similarly with the limit at $-\infty$. Hence both limits are infinite. Hence, $g$ is a surjection.

Solution step (1 point)
For fixed $x_0 = x$ define the sequence $x_{n+1} := g(x_n)$. Then $(x_n)$ satisfies
$$
x_{n+2} = \frac12 x_{n+1} + \frac12 x_n.
$$
The characteristic polynomial of this recurrence relation is
$$
\lambda^2 - \frac12 \lambda - \frac12 = \left( \lambda + \frac12 \right) (\lambda - 1)
$$
and therefore
$$
x_n = c_1 \left(- \frac12 \right)^n + c_2.
$$
Note that $x_n \to c_2$ as $n \to \infty$. Then, passing to the limit in
$$
g(x_{n+1}) = \frac12 x_{n+1} + \frac12 x_n
$$
we obtain that
$$
g(c_2) = c_2
$$
and therefore $g$ has a fixed point. Call this point $p \in \mathbb{R}$ and define the function
$$
h(x) := g(x+p)-p.
$$

Solution step (6 points)
Then $h(0) = 0$ and $g(x) = h(x-p) + p$. Hence, substituting it to the equation we get
$$
h(h(x-p)+p - p) + p = \frac12 (h(x-p)+p) + \frac12 x
$$
or equivalently
$$\tag{1}
h(h(x)) = \frac12 h(x) + \frac12 x.
$$
Suppose first that $h$ is decreasing. Then $\frac{h(x)}{x} < 0$ for every $x \neq 0$. Then consider $x_0 = x \in \mathbb{R} \setminus \{0\}$ and the sequence $x_{n+1} := h(x_n)$. From previous computations we know that
$$
x_n = c_1 \left( - \frac12 \right)^n + c_2.
$$
Suppose that $c_2 \neq 0$. Then
$$
\frac{h(x_n)}{x_n} = \frac{x_{n+1}}{x_n} =  \frac{c_1 \left( - \frac12 \right)^{n+1} + c_2}{c_1 \left( - \frac12 \right)^n + c_2} \to 1 > 0,
$$
which is a contradiction. Hence $c_2 = 0$ and $x_n = c_1 \left(-\frac12 \right)^n$. Since $x_0 = x$, we get $c_1 = x$ and then $h(x) = h(x_0) = x_1 = -\frac12 x$ and therefore $h(x) = -\frac12 x$. From here we get
$$
g(x) = h(x-p)+p = -\frac12 (x-p) + p = - \frac12 x + \frac32 p.
$$
Now, consider the case when $h$ is increasing. We will show that $h(x) = x$. Indeed, suppose by contradiction that for some $x$ we have $h(x) \neq x$. If $h(x) > x$, then from (1) we get
$$
h(x) < h(h(x)) = \frac12 h(x) + \frac12 x
$$
and therefore $h(x) < x$, which is a contradiction. Similarly we get a contradiction if $h(x) < x$. Hence $h(x) = x$. Noting that all $x \in \mathbb{R}$ are fixed points of $h$, we clearly see that the unique $g$ is then
$$
g(x) = x.
$$

Solution step (1 point)
To summarize, all the solutions are of the form $g(x) = -\frac12 x + c$ for $c \in \mathbb{R}$, $g(x) = x$. It is easy to check that these functions solve the problem.