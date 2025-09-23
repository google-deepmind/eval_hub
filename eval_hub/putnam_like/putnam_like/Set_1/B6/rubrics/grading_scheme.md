Solution step (1 point):
Observe that from the reccurence relation, we have $x_n \in \mathbb{N}$ for all $n \geq 0$. Hence, since $\beta$ is irrational, 
$$0 < \alpha x_n - \left\lfloor \alpha x_n \right\rfloor < 1.$$

Solution step (7 points):
From that, using the reccurence relation, we get
$$x_{n+1} - \beta x_n = \left\lfloor \alpha x_n \right\rfloor < \alpha x_n < \left\lfloor \alpha x_n \right\rfloor + 1 = x_{n+1} - \beta x_n + 1.$$
Thus
$$(\alpha + \beta) x_n - 1 < x_{n+1} < (\alpha + \beta) x_n.$$
Multiplying this inequality by $\beta - \alpha$ we get
$$(\beta^2 - \alpha^2) x_n - (\beta - \alpha) < (\beta - \alpha) x_{n+1} < (\beta^2 - \alpha^2) x_n.$$
Hence
$$\beta x_{n+1} - (\beta^2 - \alpha^2) x_n < \alpha x_{n+1} < \beta x_{n+1} - (\beta^2 - \alpha^2) x_n + (\beta - \alpha)$$
Since $\beta - \alpha \in (0,1)$ and $\beta x_{n+1} - (\beta^2 - \alpha^2) x_n \in \mathbb{Z}$, we obtain that
$$\left\lfloor \alpha x_{n+1} \right\rfloor = \beta x_{n+1} - (\beta^2 - \alpha^2) x_n, \quad n \geq 0$$
or equivalently
$$\left\lfloor \alpha x_{n} \right\rfloor = \beta x_{n} - (\beta^2 - \alpha^2) x_{n-1}, \quad n \geq 1.$$
Putting this to the reccurence relation we obtain that
$$x_{n+1} = \beta x_n + \left\lfloor \alpha x_n \right\rfloor = 2\beta x_{n} - (\beta^2 - \alpha^2) x_{n-1}, \quad n \geq 1.$$
The characteristic polynomial for this reccurence relation is
$$p(\lambda) = \lambda^2 - 2 \beta \lambda + (\beta^2 - \alpha^2).$$
From Vieta's formulas one can immediatelly see that
$$p(\lambda) = (\lambda - (\beta-\alpha) ) (\lambda - (\beta+\alpha)).$$
Hence, for some $A, B \in \mathbb{R}$ we have
$$x_n = A (\beta-\alpha)^n + B (\beta + \alpha)^n.$$

Solution step (1 point):
Putting $n = 0$ and $n=1$ into this relation we obtain the following system of equations
$$
\begin{cases}
x_0 = A + B, \\
x_1 = A (\beta-\alpha) + B(\beta + \alpha).
\end{cases}
$$
Solving it we find that
$$
\begin{cases}
A = \frac{x_0 (\beta + \alpha) - x_1}{2\alpha}, \\
B = x_0 - \frac{x_0 (\beta + \alpha) - x_1}{2\alpha}.
\end{cases}
$$
Observe that
$$\lim_{n\to\infty} \frac{x_n}{(\alpha+\beta)^n} = \lim_{n\to\infty} A \left( \frac{\beta-\alpha}{\beta+\alpha} \right)^n + B = B.$$

Solution step (1 point):
Hence it is enough to compute $B$. Note that from the original reccurence relation $x_1 = \beta x_0 + \left\lfloor \alpha x_0 \right\rfloor$. Hence
$$B = x_0 - \frac{x_0 (\beta + \alpha) - x_1}{2\alpha} = \frac{2\alpha x_0 - \beta x_0 - \alpha x_0 + \beta x_0 + \left\lfloor \alpha x_0 \right\rfloor}{2\alpha} = \frac{\alpha x_0 + \left\lfloor \alpha x_0 \right\rfloor}{2\alpha}.$$
To summarize
$$\lim_{n\to\infty} \frac{x_n}{(\alpha+\beta)^n} = \frac{\alpha x_0 + \left\lfloor \alpha x_0 \right\rfloor}{2\alpha}.$$