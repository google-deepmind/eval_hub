This step is worth 3 points.
The function $\cos(x)\cos(x^2)$ is continuous on $[0,\pi]$ so the integral $\int_0^{\pi} \cos(x)\cos(x^2)\,dx$ is finite. To study $\int_{\pi}^k \cos(x)\cos(x^2)\,dx$ we integrate by parts:
$$
\begin{split}
\int_\pi^k \cos(x)\cos(x^2)\,dx &=\int_\pi^k \frac{\cos(x)}{2x} d(\sin(x^2))\,dx\\
&= \left. \frac{\cos(x)\sin(x^2)}{2x}\right|_\pi^k -\int_\pi^k \sin(x^2)\left(\frac{-\sin(x)}{2x}-\frac{\cos(x)}{2x^2}\right)\,dx\\
&=\frac{\cos(k)\sin(k^2)}{2k^2}+\frac{\sin(\pi^2)}{2\pi}\\
&+\int_\pi^k \frac{\sin(x)\sin(x^2)}{2x}\,dx +\int_\pi^k\frac{\sin(x^2)\cos(x)}{2x^2}\,dx
\end{split}
$$

This step is worth 6 points.
Obviously $\lim_{k\to\infty} \frac{\cos(k)\sin(k^2)}{2k^2}=0$. The last integral converges in the limit $k\to\infty$ since
$$
\int_\pi^\infty\frac{|\sin(x^2)\cos(x)|}{2x^2}\,dx\leq \int_\pi^\infty \frac{1}{2x^2}\,dx <\infty.
$$
To study $\int_\pi^k \frac{\sin(x)\sin(x^2)}{2x}\,dx$ we integrate by parts again
$$
\begin{split}
&\quad \int_\pi^k \frac{\sin(x)\sin(x^2)}{2x}\,dx=\int_\pi^k \frac{-\sin(x)}{4x^2} d(\cos(x^2))=\\
&=\left.\frac{-\sin(x)\cos(x^2)}{4x^2}\right|_\pi^k-\left(\int_\pi^k \frac{\cos(x^2)(-\cos(x))}{4x^2}\,dx+\int_\pi^k \frac{\cos(x^2)(-\sin(x))}{-8x^3}\,dx\right).\\
&=-\frac{\sin{k}\cos{k^2}}{4k^2}-\left(\int_\pi^k \frac{\cos(x^2)(-\cos(x))}{4x^2}\,dx+\int_\pi^k \frac{\cos(x^2)(-\sin(x))}{-8x^3}\,dx\right).
\end{split}
$$

Here we have the convergence of integrals the same way as above i.e. by the comparision test and the obvious limit of the first summand.

This step is worth 1 point.
We have shown that terms are finite and therefore the integral $\int_0^\infty \cos(x)\cos(x^2)\,dx$ is convergent.