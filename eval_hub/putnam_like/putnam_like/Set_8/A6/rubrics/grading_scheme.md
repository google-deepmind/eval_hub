This step is worth 2 points.
First observe that
$$
\begin{aligned}
\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx 
&> \int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x-\alpha)}dx \\
&= \int_0^\infty \frac{f(x)-f(x+2\alpha)}{f(x)}dx.
\end{aligned}
$$
We show that the latter integral diverges.

This step is worth 3 points.
Assume that $\int_0^\infty \frac{f(x)-f(x+2\alpha)}{f(x)}dx$ converges. Since $\frac{f(x)-f(x+2\alpha)}{f(x)} = 1-\frac{f(x+2\alpha)}{f(x)}$, we see that $\liminf_{x\to\infty}\frac{f(x+2\alpha)}{f(x)}>0$.

Moreover, observe that for $y>0$ we have
$$
0<\frac{f(y+2\alpha)}{f(y)} < \frac{1}{2\alpha f(y)} \int_y^{y+2\alpha} f(x)dx.
$$

This step is worth 5 points.
Since $\int_{y}^{y+2\alpha} f(x+2n\alpha)dx = \int_{y+2x\alpha}^{y+(2n+1)\alpha}f(x)dx$, 
$$
\int_y^{y+2\alpha} f(x)dx = \int_y^{\infty} (f(x) - f(x+2\alpha))\,dx.
$$
Hence
$$
0<\frac{f(y+2\alpha)}{f(y)} < \frac{1}{2\alpha f(y)} \int_y^{\infty} (f(x) - f(x+2\alpha))\,dx < \frac{1}{\alpha}\int_y^\infty \frac{f(x)-f(x+2\alpha)}{f(x)}dx.
$$
Letting $y\to\infty$ we see that $\frac{f(y+2\alpha)}{f(y)}\to 0$ and hence $\int_0^\infty \frac{f(x)-f(x+2\alpha)}{f(x)}dx$ diverges.

Applying this fact to inequality in step 1 we get the desired result.