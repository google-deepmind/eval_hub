Solution step (8 points):
First, we will attempt to calculate the integral:
$$
\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx,
$$
for all  $y\in \mathbb{R}$. To this end, we will define an auxiliary function $I: \mathbb{R}\to \mathbb{R}$ as follows:
$$
I(y)=\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx.
$$
Since the integrand is an even function, the following equality holds:
$$
I(y)=2\int_{0}^{\infty}e^{-x^2/2}\cos(yx)\, dx.
$$
To calculate the derivative of the function above, we often use Leibniz's rule or the Dominated Convergence Theorem, which allow us to interchange differentiation and integration. For this purpose, we need to check that the function above satisfies all the necessary conditions of Leibniz's rule.
Namely, $I(y)$ has the following properties:

*   The integrand $e^{-x^2/2} \cos(yx)$ is continuously differentiable with respect to $y$. Since $\cos(yx)$ is smooth and $e^{-x^2/2}$ does not depend on $y$.
*   The partial derivative of the integrand with respect to $y$,
$$
\frac{\partial}{\partial y} \left( e^{-x^2/2} \cos(yx) \right) = -x e^{-x^2/2} \sin(yx),
$$
is absolutely integrable over the domain $x \in [0, \infty)$.  Indeed, we have
$$
\begin{aligned}
\int_0^{\infty}\left|\frac{\partial}{\partial y} \left( e^{-x^2/2} \cos(yx) \right)\right|dx
&=\int_0^{\infty}|-x e^{-x^2/2} \sin(yx)|dx\\
&\leq \int_0^{\infty}|x e^{-x^2/2}|dx\\
&=\int_0^{\infty}x e^{-x^2/2}dx\\
&=\int_0^{\infty}e^{-u}du=1.
\end{aligned}
$$
*   The improper integral
$$
\int_0^{\infty} x e^{-x^2/2} \sin(yx)\, dx
$$
converges uniformly with respect to $y\in \mathbb{R}$ on the interval $[0,\infty)$, i.e., for every $\varepsilon>0$ there exists $M>0$ such that for all
$y\in \mathbb{R}$ and for all $T>M$, the following holds:
$$
\left|\int_T^{\infty} x e^{-x^2/2} \sin(yx)\, dx\right|<\varepsilon.
$$
Indeed, the above property follows from the following estimations:
$$
\begin{aligned}
\left|\int_T^{\infty} x e^{-x^2/2} \sin(yx)\, dx\right|&\leq \int_T^{\infty} \left|x e^{-x^2/2} \sin(yx)\right| \, dx\\
&\leq \int_T^{\infty} |x e^{-x^2/2}|\cdot  |\sin(yx)| \, dx\\
&\leq \int_T^{\infty} |x e^{-x^2/2}| \, dx\\
&= \int_T^{\infty} x e^{-x^2/2} \, dx\\
&= \int_{T^2/2}^{\infty}  e^{-u} \, du\quad (u:=x^2/2)\\
&=e^{-T^2/2}.
\end{aligned}
$$
*   Under these conditions, the function $I(y)$ is differentiable with respect to $y$, and the derivative can be computed as:
$$
\begin{aligned}
I'(y)&=\frac{d}{dy} \left( 2 \int_{0}^{\infty} e^{-x^2/2} \cos(yx) \, dx \right) = 2 \int_{0}^{\infty} \frac{\partial}{\partial y} \left( e^{-x^2/2} \cos(yx) \right) \, dx.\\
&=-2\int_0^{\infty} e^{-x^2/2} x\sin(yx)\,dx.
\end{aligned}
$$


Applying the integration by parts formula, we get
$$
\int_0^{\infty} e^{-x^2/2} x \sin(yx) \, dx = \left[ -\sin(yx) e^{-x^2/2} \right]_{x=0}^{x=\infty} +
\int_0^\infty e^{-x^2/2} y \cos(yx) \, dx.
$$
Since $e^{-x^2/2} \to 0$ as $x \to \infty$ and $\sin(yx)$ is bounded at infinity with
$\sin(0) = 0$, the first term evaluates to:
$$
\left[ -\sin(yx) e^{-x^2/2} \right]_0^\infty = 0.
$$
Thus, we are left with:
$$
y \int_0^\infty e^{-x^2/2} \cos(yx) \, dx.
$$
Now, we reach the conclusion:
$$
I'(y)=-yI(y).
$$
It is a differential equation with separable variables, and its solution has the form:
$$
I(y)=Ce^{-y^2/2}.
$$

Solution step (2 points):
In this step we calculate the required limit. Namely, we have
$$
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=\lim_{y\to\infty}Ce^{-y^2/2}=0,
$$
where
$$
C=I(0)=\int_{-\infty}^{\infty}e^{-x^2/2}dx<\infty.
$$
This completes the solution.
