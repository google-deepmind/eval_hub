This step is worth 7 points.
To show that $g$ is integrable, we use the Fubini's theorem
$$
\begin{aligned}
\int_{-\infty}^\infty |g(x)| \, dx &= \int_{-\infty}^\infty \left| \int_x^{x+1} f(y) \, dy \right| \, dx \leq \int_{-\infty}^\infty \int_x^{x+1} |f(y)| \, dy \, dx \\
&= \int_{-\infty}^{\infty} \int_{y-1}^y |f(y)| \, dx \, dy = \int_{-\infty}^\infty |f(y)| \, dx < \infty.
\end{aligned}
$$

This step is worth 3 points.
Hence, we can compute
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \int_x^{x+1} f(y) \, dy \, dx = \int_{-\infty}^{\infty} \int_{y-1}^y f(y) \, dx \, dy = \int_{-\infty}^{\infty} f(y) \, dy.
$$