Of course. This is a classic problem in mathematical analysis, often related to the theory of Fourier transforms. The result is an example of the Riemann-Lebesgue Lemma. I will present two detailed methods to prove this.

### Problem Statement
Show that
\begin{equation*}
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=0.
\end{equation*}

---

### Method 1: Direct Calculation via Fourier Transform

This is the most elegant method. We will first compute the integral for a general `y` and then take the limit. The integral is the real part of the Fourier transform of a Gaussian function.

**Step 1: Express the integral using complex exponentials.**
We use Euler's formula, $e^{i\theta} = \cos(\theta) + i\sin(\theta)$, to write $\cos(yx) = \text{Re}(e^{iyx})$.
\begin{align*}
\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx &= \int_{-\infty}^{\infty}e^{-x^2/2}\text{Re}(e^{iyx})dx \\
&= \text{Re}\left(\int_{-\infty}^{\infty}e^{-x^2/2}e^{iyx}dx\right)
\end{align*}
Let's define the complex-valued integral $I(y)$:
\begin{equation*}
I(y) = \int_{-\infty}^{\infty}e^{-x^2/2}e^{iyx}dx = \int_{-\infty}^{\infty}e^{-x^2/2 + iyx}dx
\end{equation*}
Our goal is to compute $I(y)$ and then take its real part.

**Step 2: Complete the square in the exponent.**
The exponent is $-x^2/2 + iyx$. We complete the square with respect to $x$:
\begin{align*}
-\frac{x^2}{2} + iyx &= -\frac{1}{2}(x^2 - 2iyx) \\
&= -\frac{1}{2}\left( (x - iy)^2 - (iy)^2 \right) \\
&= -\frac{1}{2}\left( (x - iy)^2 - i^2y^2 \right) \\
&= -\frac{1}{2}\left( (x - iy)^2 + y^2 \right) \\
&= -\frac{(x-iy)^2}{2} - \frac{y^2}{2}
\end{align*}

**Step 3: Substitute the completed square back into the integral.**
\begin{equation*}
I(y) = \int_{-\infty}^{\infty} \exp\left(-\frac{(x-iy)^2}{2} - \frac{y^2}{2}\right)dx
\end{equation*}
The term $e^{-y^2/2}$ is constant with respect to $x$, so we can pull it out of the integral:
\begin{equation*}
I(y) = e^{-y^2/2} \int_{-\infty}^{\infty} e^{-(x-iy)^2/2}dx
\end{equation*}

**Step 4: Evaluate the remaining integral.**
Let $z = x - iy$. Then $dz = dx$. The integral becomes $\int_{-\infty-iy}^{\infty-iy} e^{-z^2/2}dz$. This is an integral in the complex plane along a line parallel to the real axis. We can show that this integral is equal to the standard Gaussian integral along the real axis by using contour integration and Cauchy's Integral Theorem.

Consider the integral of $f(z) = e^{-z^2/2}$ over a rectangular contour $C$ with vertices at $-R, R, R-iy, -R-iy$.
\begin{equation*}
\oint_C e^{-z^2/2} dz = 0
\end{equation*}
since $f(z)$ is analytic inside the contour. The integral breaks down into four parts:
\begin{equation*}
\int_{-R}^{R} e^{-x^2/2}dx + \int_{0}^{-y} e^{-(R+it)^2/2}i dt + \int_{R}^{-R} e^{-(x-iy)^2/2}dx + \int_{-y}^{0} e^{-(-R+it)^2/2}i dt = 0
\end{equation*}
As $R\to\infty$, the integrals over the vertical sides (the second and fourth terms) vanish. For example, for the side at $x=R$:
$|e^{-(R+it)^2/2}| = |e^{-(R^2-t^2+2iRt)/2}| = e^{-R^2/2}e^{t^2/2}$. Since $y$ is fixed, $t$ is bounded, and the term $e^{-R^2/2}$ drives the integral to 0.

This leaves us with:
\begin{equation*}
\int_{-\infty}^{\infty} e^{-x^2/2}dx - \int_{-\infty}^{\infty} e^{-(x-iy)^2/2}dx = 0
\end{equation*}
Therefore,
\begin{equation*}
\int_{-\infty}^{\infty} e^{-(x-iy)^2/2}dx = \int_{-\infty}^{\infty} e^{-x^2/2}dx
\end{equation*}
This is the famous Gaussian integral, whose value is $\sqrt{2\pi}$.

**Step 5: Finalize the calculation of I(y).**
Substituting this result back into our expression for $I(y)$:
\begin{equation*}
I(y) = e^{-y^2/2} \cdot \sqrt{2\pi} = \sqrt{2\pi}e^{-y^2/2}
\end{equation*}
The original integral is the real part of $I(y)$. Since $I(y)$ is purely real, we have:
\begin{equation*}
\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \sqrt{2\pi}e^{-y^2/2}
\end{equation*}

**Step 6: Take the limit as y → ∞.**
Now we can evaluate the limit:
\begin{equation*}
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \lim_{y\to\infty} \left(\sqrt{2\pi}e^{-y^2/2}\right)
\end{equation*}
As $y \to \infty$, $y^2 \to \infty$, so $-y^2/2 \to -\infty$. Consequently, $e^{-y^2/2} \to 0$.
\begin{equation*}
\lim_{y\to\infty} \left(\sqrt{2\pi}e^{-y^2/2}\right) = \sqrt{2\pi} \cdot 0 = 0
\end{equation*}
This completes the proof using the first method.

---

### Method 2: Integration by Parts

This method is more general and illustrates the cancellation effect of the rapid oscillations of $\cos(yx)$. It does not require knowing the exact value of the integral.

**Step 1: Set up the integral and apply Integration by Parts.**
Let the integral be $J(y)$:
\begin{equation*}
J(y) = \int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx
\end{equation*}
We use integration by parts, $\int u \, dv = uv - \int v \, du$. Let:
\begin{itemize}
    \item $u = e^{-x^2/2}$
    \item $dv = \cos(yx)dx$
\end{itemize}
Then we have:
\begin{itemize}
    \item $du = -x e^{-x^2/2}dx$
    \item $v = \frac{1}{y}\sin(yx)$
\end{itemize}
Applying the formula, we get:
\begin{equation*}
J(y) = \left[ e^{-x^2/2} \cdot \frac{\sin(yx)}{y} \right]_{-\infty}^{\infty} - \int_{-\infty}^{\infty} \frac{\sin(yx)}{y} (-x e^{-x^2/2})dx
\end{equation*}

**Step 2: Evaluate the boundary term.**
The boundary term is evaluated at $x\to\infty$ and $x\to-\infty$:
\begin{equation*}
\lim_{x\to\pm\infty} \left( \frac{e^{-x^2/2}\sin(yx)}{y} \right)
\end{equation*}
Since $|\sin(yx)| \leq 1$, the term is bounded by $\frac{e^{-x^2/2}}{y}$. As $x\to\pm\infty$, $x^2\to\infty$, so $e^{-x^2/2} \to 0$. The exponential decay is much faster than any polynomial growth, so the boundary term is zero.
\begin{equation*}
\left[ e^{-x^2/2} \frac{\sin(yx)}{y} \right]_{-\infty}^{\infty} = 0 - 0 = 0
\end{equation*}

**Step 3: Simplify the remaining integral.**
The expression for $J(y)$ simplifies to:
\begin{equation*}
J(y) = \frac{1}{y} \int_{-\infty}^{\infty} x e^{-x^2/2} \sin(yx) dx
\end{equation*}

**Step 4: Show that the remaining integral is bounded.**
To find the limit of $J(y)$ as $y\to\infty$, we need to analyze the behavior of the integral $\int_{-\infty}^{\infty} x e^{-x^2/2} \sin(yx) dx$. Let's bound its absolute value:
\begin{align*}
\left| \int_{-\infty}^{\infty} x e^{-x^2/2} \sin(yx) dx \right| &\leq \int_{-\infty}^{\infty} |x e^{-x^2/2} \sin(yx)| dx \\
&\leq \int_{-\infty}^{\infty} |x| e^{-x^2/2} |\sin(yx)| dx
\end{align*}
Since $|\sin(yx)| \leq 1$ for all $x, y$:
\begin{equation*}
\left| \int_{-\infty}^{\infty} x e^{-x^2/2} \sin(yx) dx \right| \leq \int_{-\infty}^{\infty} |x| e^{-x^2/2} dx
\end{equation*}
The integral $\int_{-\infty}^{\infty} |x| e^{-x^2/2} dx$ is a constant, finite value. We can compute it:
\begin{align*}
\int_{-\infty}^{\infty} |x| e^{-x^2/2} dx &= 2 \int_{0}^{\infty} x e^{-x^2/2} dx \\
&= 2 \left[ -e^{-x^2/2} \right]_{0}^{\infty} \quad (\text{using substitution } u = x^2/2) \\
&= 2 \left( - \lim_{x\to\infty} e^{-x^2/2} - (-e^0) \right) \\
&= 2(0 - (-1)) = 2
\end{align*}
So, the integral is bounded by 2. Let $C = \int_{-\infty}^{\infty} |x| e^{-x^2/2} dx = 2$.

**Step 5: Apply the Squeeze Theorem.**
We now have an upper bound for the absolute value of $J(y)$:
\begin{equation*}
|J(y)| = \left| \frac{1}{y} \int_{-\infty}^{\infty} x e^{-x^2/2} \sin(yx) dx \right| \leq \frac{1}{|y|} \int_{-\infty}^{\infty} |x| e^{-x^2/2} dx = \frac{C}{|y|} = \frac{2}{|y|}
\end{equation*}
This gives us the inequality:
\begin{equation*}
0 \leq |J(y)| \leq \frac{2}{|y|}
\end{equation*}
Taking the limit as $y \to \infty$:
\begin{equation*}
\lim_{y\to\infty} 0 \leq \lim_{y\to\infty} |J(y)| \leq \lim_{y\to\infty} \frac{2}{y}
\end{equation*}
\begin{equation*}
0 \leq \lim_{y\to\infty} |J(y)| \leq 0
\end{equation*}
By the Squeeze Theorem, $\lim_{y\to\infty} |J(y)| = 0$, which implies that $\lim_{y\to\infty} J(y) = 0$.

### Conclusion
Both methods conclusively show that
\begin{equation*}
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=0.
\end{equation*}
The first method provides an exact expression for the integral, from which the limit is obvious. The second method demonstrates a more general technique for proving that integrals of this type (an integrable function multiplied by a rapidly oscillating function) tend to zero, a principle formalized by the Riemann-Lebesgue Lemma.