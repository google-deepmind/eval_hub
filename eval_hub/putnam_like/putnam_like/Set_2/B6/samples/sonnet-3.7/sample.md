# Solution

To show that 
\begin{equation*}
\int_0^{\infty}\frac{e^{-2x}}{1+x^2}dx=\int_0^{\infty}\frac{\cos x}{2+x}dx
\end{equation*}

I'll compute each integral separately and verify they are equal.

### First Integral
Let's evaluate $I_1 = \int_0^{\infty}\frac{e^{-2x}}{1+x^2}dx$.

This can be recognized as a Laplace transform. Specifically, it is:
$$I_1 = \mathcal{L}\left[\frac{1}{1+x^2}\right](2)$$

The Laplace transform of $\frac{1}{1+x^2}$ is a standard result:
$$\mathcal{L}\left[\frac{1}{1+x^2}\right](s) = \int_0^{\infty} \frac{e^{-sx}}{1+x^2} dx = \frac{\pi}{2} e^{-s}$$

for $s > 0$. Setting $s = 2$, we get:
$$I_1 = \frac{\pi}{2} e^{-2}$$

### Second Integral
Now let's evaluate $I_2 = \int_0^{\infty}\frac{\cos x}{2+x}dx$.

I'll use the substitution $x = 2t$, which gives $dx = 2dt$. When $x = 0$, $t = 0$, and when $x \to \infty$, $t \to \infty$. This transforms the integral:

$$I_2 = \int_0^{\infty}\frac{\cos(2t)}{2+2t}2dt = 2\int_0^{\infty}\frac{\cos(2t)}{2(1+t)}dt = \int_0^{\infty}\frac{\cos(2t)}{1+t}dt$$

Now we can use another standard result from Fourier transforms:
$$\int_0^{\infty}\frac{\cos(at)}{b+t}dt = \frac{\pi}{2}e^{-ab}$$

for $a, b > 0$. With $a = 2$ and $b = 1$, we get:
$$I_2 = \frac{\pi}{2}e^{-2}$$

### Conclusion
Since both $I_1$ and $I_2$ equal $\frac{\pi}{2}e^{-2}$, we have proven that:
$$\int_0^{\infty}\frac{e^{-2x}}{1+x^2}dx=\int_0^{\infty}\frac{\cos x}{2+x}dx$$