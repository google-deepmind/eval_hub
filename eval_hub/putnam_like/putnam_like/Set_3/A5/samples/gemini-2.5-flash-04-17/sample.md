```markdown
# Problem Statement
Show that
\begin{equation*}
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=0.
\end{equation*}

# Solution
Let the integral be denoted by $I(y)$.
$$I(y) = \int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx$$
We can express $\cos(yx)$ using Euler's formula: $\cos(yx) = \text{Re}(e^{iyx})$.
Thus, the integral can be written as the real part of a complex integral:
$$I(y) = \text{Re}\left(\int_{-\infty}^{\infty}e^{-x^2/2}e^{iyx}dx\right)$$
Let's evaluate the complex integral $J(y) = \int_{-\infty}^{\infty}e^{-x^2/2}e^{iyx}dx$.
The exponent of the integrand is $-\frac{x^2}{2} + i yx$. We complete the square with respect to $x$:
$$-\frac{x^2}{2} + i yx = -\frac{1}{2}(x^2 - 2iyx) = -\frac{1}{2}(x^2 - 2iyx + (iy)^2 - (iy)^2) = -\frac{1}{2}(x-iy)^2 - \frac{y^2}{2}$$
So the integral becomes:
$$J(y) = \int_{-\infty}^{\infty} e^{-\frac{1}{2}(x-iy)^2 - \frac{y^2}{2}} dx = e^{-y^2/2} \int_{-\infty}^{\infty} e^{-\frac{1}{2}(x-iy)^2} dx$$
Let's evaluate the integral $K(y) = \int_{-\infty}^{\infty} e^{-\frac{1}{2}(x-iy)^2} dx$.
Consider the function $f(z) = e^{-z^2/2}$, which is an entire function in the complex plane. We integrate $f(z)$ over a rectangular contour $C_R$ with vertices at $-R, R, R-iy, -R-iy$. By Cauchy's Integral Theorem, since $f(z)$ is entire, the integral over this closed contour is zero:
$$\oint_{C_R} e^{-z^2/2} dz = 0$$
The contour $C_R$ consists of four line segments:
1. $C_1$: From $-R$ to $R$ along the real axis ($z=x$). The integral is $\int_{-R}^R e^{-x^2/2} dx$.
2. $C_2$: From $R$ to $R-iy$ ($z=R+it$, $t$ from $0$ to $-y$). The integral is $\int_0^{-y} e^{-(R+it)^2/2} i dt$.
3. $C_3$: From $R-iy$ to $-R-iy$ ($z=x-iy$, $x$ from $R$ to $-R$). The integral is $\int_R^{-R} e^{-(x-iy)^2/2} dx = -\int_{-R}^R e^{-(x-iy)^2/2} dx$.
4. $C_4$: From $-R-iy$ to $-R$ ($z=-R+it$, $t$ from $-y$ to $0$). The integral is $\int_{-y}^0 e^{-(-R+it)^2/2} i dt$.

The sum of these integrals is zero:
$$\int_{-R}^R e^{-x^2/2} dx + \int_0^{-y} e^{-(R+it)^2/2} i dt - \int_{-R}^R e^{-(x-iy)^2/2} dx + \int_{-y}^0 e^{-(-R+it)^2/2} i dt = 0$$
We analyze the integrals over the vertical segments $C_2$ and $C_4$ as $R \to \infty$.
For $C_2$, $|e^{-(R+it)^2/2}| = |e^{-(R^2+2iRt-t^2)/2}| = |e^{-R^2/2} e^{-iRt} e^{t^2/2}| = e^{-R^2/2} e^{t^2/2}$.
The length of the path is $|y|$. If $y>0$, $t \in [0, -y]$, so $t \in [-y, 0]$, and $t^2 \in [0, y^2]$. The maximum value of $e^{t^2/2}$ is $e^{y^2/2}$.
The magnitude of the integral over $C_2$ is bounded by $|y| \max_{t \in [0,-y]} |e^{-(R+it)^2/2}| = |y| e^{-R^2/2} \max_{t \in [0,-y]} e^{t^2/2} = |y| e^{-R^2/2} e^{y^2/2}$.
As $R \to \infty$, $e^{-R^2/2} \to 0$, so $|y| e^{y^2/2} e^{-R^2/2} \to 0$ for fixed $y$.
Similarly, the integral over $C_4$ goes to zero as $R \to \infty$.

Taking the limit $R \to \infty$, the equation becomes:
$$\int_{-\infty}^\infty e^{-x^2/2} dx - \int_{-\infty}^\infty e^{-(x-iy)^2/2} dx = 0$$
The first integral is a standard Gaussian integral: $\int_{-\infty}^\infty e^{-x^2/2} dx = \sqrt{2\pi}$.
Therefore, $\int_{-\infty}^\infty e^{-(x-iy)^2/2} dx = \sqrt{2\pi}$. This is $K(y)$.

Substituting $K(y)$ back into the expression for $J(y)$:
$$J(y) = e^{-y^2/2} K(y) = \sqrt{2\pi} e^{-y^2/2}$$
Now, we find the real part of $J(y)$ to get $I(y)$:
$$I(y) = \text{Re}(J(y)) = \text{Re}(\sqrt{2\pi} e^{-y^2/2})$$
Since $y$ is a real variable, $y^2$ is real, $e^{-y^2/2}$ is real, and $\sqrt{2\pi}$ is real.
Thus, $I(y) = \sqrt{2\pi} e^{-y^2/2}$.

Finally, we evaluate the limit as $y \to \infty$:
$$\lim_{y\to\infty} I(y) = \lim_{y\to\infty} \sqrt{2\pi} e^{-y^2/2}$$
As $y \to \infty$, $y^2 \to \infty$, which implies $-y^2/2 \to -\infty$.
Therefore, $e^{-y^2/2} \to 0$ as $y \to \infty$.
$$\lim_{y\to\infty} \sqrt{2\pi} e^{-y^2/2} = \sqrt{2\pi} \cdot 0 = 0$$

Thus, we have shown that $\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=0$.

Alternatively, this result can be obtained directly by recognizing the integral as the Fourier transform of $e^{-x^2/2}$. The Fourier transform of $f(x) = e^{-ax^2}$ is $\hat{f}(\omega) = \sqrt{\frac{\pi}{a}} e^{-\omega^2/(4a)}$. For $f(x) = e^{-x^2/2}$, we have $a=1/2$, so $\hat{f}(\omega) = \sqrt{\frac{\pi}{1/2}} e^{-\omega^2/(4(1/2))} = \sqrt{2\pi} e^{-\omega^2/2}$. Using the convention $\hat{f}(\omega) = \int_{-\infty}^\infty f(x) e^{-i\omega x} dx$.
The integral $\int_{-\infty}^{\infty} e^{-x^2/2}\cos(yx)dx = \int_{-\infty}^{\infty} e^{-x^2/2} \frac{e^{iyx} + e^{-iyx}}{2} dx = \frac{1}{2} \left(\int_{-\infty}^{\infty} e^{-x^2/2} e^{-i(-y)x} dx + \int_{-\infty}^{\infty} e^{-x^2/2} e^{-iyx} dx \right) = \frac{1}{2} (\hat{f}(-y) + \hat{f}(y))$.
Since $f(x) = e^{-x^2/2}$ is real and even, $\hat{f}$ is real and even, so $\hat{f}(-y) = \hat{f}(y)$. The integral is $\hat{f}(y)$.
By the Riemann-Lebesgue Lemma, if $f \in L^1(\mathbb{R})$, then $\lim_{|\omega|\to\infty} \hat{f}(\omega) = 0$.
Since $f(x) = e^{-x^2/2}$ is in $L^1(\mathbb{R})$, we have $\lim_{y\to\infty} \hat{f}(y) = 0$.
Thus, $\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \lim_{y\to\infty} \hat{f}(y) = 0$.

The final answer is $\boxed{0}$.
```