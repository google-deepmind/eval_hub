We want to show that
\begin{equation*}
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=0.
\end{equation*}

Let $I(y) = \int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx$. We can solve this problem using several methods.

**Method 1: Direct Calculation using Fourier Transform**

The integral $I(y)$ is related to the Fourier transform of the Gaussian function $f(x) = e^{-x^2/2}$. Recall the Fourier transform definition $\hat{f}(k) = \int_{-\infty}^{\infty} f(x) e^{-ikx} dx$.
The integral we are interested in is the real part of the Fourier transform evaluated at $k=-y$ (or $k=y$, since $\cos(yx)$ is even in $y$):
\begin{equation*}
I(y) = \int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \text{Re} \left( \int_{-\infty}^{\infty} e^{-x^2/2} e^{iyx} dx \right)
\end{equation*}
Let's compute the complex integral $J(y) = \int_{-\infty}^{\infty} e^{-x^2/2} e^{iyx} dx$.
The exponent is $-\frac{x^2}{2} + iyx$. We complete the square for $x$:
\begin{align*} -\frac{x^2}{2} + iyx &= -\frac{1}{2}(x^2 - 2iyx) \\ &= -\frac{1}{2}( (x - iy)^2 - (iy)^2 ) \\ &= -\frac{1}{2}( (x - iy)^2 + y^2 ) \\ &= -\frac{(x-iy)^2}{2} - \frac{y^2}{2} \end{align*}
So, the integral becomes:
\begin{equation*}
J(y) = \int_{-\infty}^{\infty} e^{-\frac{(x-iy)^2}{2}} e^{-y^2/2} dx = e^{-y^2/2} \int_{-\infty}^{\infty} e^{-\frac{(x-iy)^2}{2}} dx
\end{equation*}
Let $u = x - iy$. Then $du = dx$. The path of integration is shifted to the line $\text{Im}(u) = -y$ in the complex plane. However, due to the rapid decay of the Gaussian function $e^{-u^2/2}$ as $\text{Re}(u) \to \pm \infty$, and the fact that it is analytic, we can shift the contour back to the real axis using Cauchy's Integral Theorem.
\begin{equation*}
\int_{-\infty}^{\infty} e^{-\frac{(x-iy)^2}{2}} dx = \int_{-\infty}^{\infty} e^{-u^2/2} du
\end{equation*}
This is the standard Gaussian integral, $\int_{-\infty}^{\infty} e^{-u^2/2} du = \sqrt{2\pi}$.
Therefore,
\begin{equation*}
J(y) = e^{-y^2/2} \sqrt{2\pi} = \sqrt{2\pi} e^{-y^2/2}
\end{equation*}
Since $J(y)$ is real, $I(y) = \text{Re}(J(y)) = J(y)$.
\begin{equation*}
I(y) = \int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \sqrt{2\pi} e^{-y^2/2}
\end{equation*}
Now we take the limit as $y \to \infty$:
\begin{equation*}
\lim_{y\to\infty} I(y) = \lim_{y\to\infty} \sqrt{2\pi} e^{-y^2/2}
\end{assuming}
As $y \to \infty$, $y^2 \to \infty$, so $-y^2/2 \to -\infty$. Thus, $e^{-y^2/2} \to 0$.
\begin{equation*}
\lim_{y\to\infty} I(y) = \sqrt{2\pi} \cdot 0 = 0
\end{equation*}

**Method 2: Integration by Parts**

Let $I(y) = \int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx$. We can use integration by parts. Note that $\cos(yx) = \frac{1}{y} \frac{d}{dx}(\sin(yx))$ for $y \neq 0$.
\begin{align*} I(y) &= \int_{-\infty}^{\infty}e^{-x^2/2} \left(\frac{1}{y} \frac{d}{dx}(\sin(yx))\right) dx \\ &= \frac{1}{y} \left[ e^{-x^2/2} \sin(yx) \right]_{-\infty}^{\infty} - \frac{1}{y} \int_{-\infty}^{\infty} \frac{d}{dx}(e^{-x^2/2}) \sin(yx) dx \\ &= \frac{1}{y} \left[ e^{-x^2/2} \sin(yx) \right]_{-\infty}^{\infty} - \frac{1}{y} \int_{-\infty}^{\infty} (-x e^{-x^2/2}) \sin(yx) dx \end{align*}
The boundary terms vanish because $e^{-x^2/2}$ decays to 0 much faster than $\sin(yx)$ oscillates (it is bounded by 1) as $x \to \pm \infty$.
\begin{equation*}
\lim_{x\to\pm\infty} e^{-x^2/2} \sin(yx) = 0
\end{equation*}
So,
\begin{equation*}
I(y) = \frac{1}{y} \int_{-\infty}^{\infty} x e^{-x^2/2} \sin(yx) dx
\end{equation*}
We can apply integration by parts again. Note that $\sin(yx) = -\frac{1}{y} \frac{d}{dx}(\cos(yx))$.
\begin{align*} I(y) &= \frac{1}{y} \int_{-\infty}^{\infty} x e^{-x^2/2} \left(-\frac{1}{y} \frac{d}{dx}(\cos(yx))\right) dx \\ &= -\frac{1}{y^2} \int_{-\infty}^{\infty} x e^{-x^2/2} \frac{d}{dx}(\cos(yx)) dx \\ &= -\frac{1}{y^2} \left[ x e^{-x^2/2} \cos(yx) \right]_{-\infty}^{\infty} + \frac{1}{y^2} \int_{-\infty}^{\infty} \frac{d}{dx}(x e^{-x^2/2}) \cos(yx) dx \end{align*}
The boundary terms $\lim_{x\to\pm\infty} x e^{-x^2/2} \cos(yx)$ are 0 because $e^{-x^2/2}$ decays faster than $x$ grows.
We compute the derivative $\frac{d}{dx}(x e^{-x^2/2}) = 1 \cdot e^{-x^2/2} + x \cdot (-x e^{-x^2/2}) = (1-x^2)e^{-x^2/2}$.
So,
\begin{equation*}
I(y) = \frac{1}{y^2} \int_{-\infty}^{\infty} (1-x^2)e^{-x^2/2} \cos(yx) dx
\end{equation*}
Now, let's consider the magnitude of $I(y)$:
\begin{align*} |I(y)| &= \left| \frac{1}{y^2} \int_{-\infty}^{\infty} (1-x^2)e^{-x^2/2} \cos(yx) dx \right| \\ &\le \frac{1}{y^2} \int_{-\infty}^{\infty} |(1-x^2)e^{-x^2/2} \cos(yx)| dx \\ &\le \frac{1}{y^2} \int_{-\infty}^{\infty} |1-x^2|e^{-x^2/2} |\cos(yx)| dx \\ &\le \frac{1}{y^2} \int_{-\infty}^{\infty} |1-x^2|e^{-x^2/2} dx \end{align*}
The integral $M = \int_{-\infty}^{\infty} |1-x^2|e^{-x^2/2} dx$ converges because the integrand decays like $x^2 e^{-x^2/2}$ for large $|x|$, which is integrable. For instance, $\int_{-\infty}^{\infty} x^2 e^{-x^2/2} dx = \sqrt{2\pi}$ (related to the variance of a standard normal distribution). The integral $\int_{-\infty}^{\infty} e^{-x^2/2} dx = \sqrt{2\pi}$. Thus, $M$ is a finite positive constant.
So we have:
\begin{equation*}
|I(y)| \le \frac{M}{y^2}
\end{equation*}
As $y \to \infty$, $\frac{M}{y^2} \to 0$. By the Squeeze Theorem, since $0 \le |I(y)| \le \frac{M}{y^2}$, we must have:
\begin{equation*}
\lim_{y\to\infty} |I(y)| = 0
\end{equation*}
which implies
\begin{equation*}
\lim_{y\to\infty} I(y) = 0
\end{equation*}

**Method 3: Riemann-Lebesgue Lemma**

The Riemann-Lebesgue Lemma states that if $f \in L^1(\mathbb{R})$ (i.e., $\int_{-\infty}^{\infty} |f(x)| dx < \infty$), then its Fourier transform $\hat{f}(y) = \int_{-\infty}^{\infty} f(x) e^{-iyx} dx$ satisfies $\lim_{|y|\to\infty} \hat{f}(y) = 0$.

Let $f(x) = e^{-x^2/2}$. We check if $f(x)$ is in $L^1(\mathbb{R})$:
\begin{equation*}
\int_{-\infty}^{\infty} |f(x)| dx = \int_{-\infty}^{\infty} |e^{-x^2/2}| dx = \int_{-\infty}^{\infty} e^{-x^2/2} dx = \sqrt{2\pi}
\end{equation*}
Since $\sqrt{2\pi} < \infty$, $f(x) = e^{-x^2/2}$ is in $L^1(\mathbb{R})$.
The integral in question is
\begin{equation*}
I(y) = \int_{-\infty}^{\infty} e^{-x^2/2} \cos(yx) dx
\end{equation*}
We can write $\cos(yx) = \frac{e^{iyx} + e^{-iyx}}{2}$.
\begin{align*} I(y) &= \int_{-\infty}^{\infty} e^{-x^2/2} \frac{e^{iyx} + e^{-iyx}}{2} dx \\ &= \frac{1}{2} \int_{-\infty}^{\infty} e^{-x^2/2} e^{iyx} dx + \frac{1}{2} \int_{-\infty}^{\infty} e^{-x^2/2} e^{-iyx} dx \end{align*}
Let $\hat{f}(k) = \int_{-\infty}^{\infty} e^{-x^2/2} e^{-ikx} dx$. Then $I(y) = \frac{1}{2} (\hat{f}(-y) + \hat{f}(y))$.
By the Riemann-Lebesgue Lemma, since $f \in L^1(\mathbb{R})$, we have:
\begin{equation*}
\lim_{y\to\infty} \hat{f}(y) = 0 \quad \text{and} \quad \lim_{y\to\infty} \hat{f}(-y) = \lim_{z\to-\infty} \hat{f}(z) = 0
\end{equation*}
Therefore,
\begin{equation*}
\lim_{y\to\infty} I(y) = \frac{1}{2} (0 + 0) = 0
\end{equation*}
Alternatively, $I(y) = \text{Re}(\int_{-\infty}^{\infty} e^{-x^2/2} e^{iyx} dx) = \text{Re}(\hat{f}(-y))$. Since $\lim_{y\to\infty} \hat{f}(-y) = 0$, its real part must also tend to 0.

All three methods confirm the result.

Final Answer: The final answer is $\boxed{0}$