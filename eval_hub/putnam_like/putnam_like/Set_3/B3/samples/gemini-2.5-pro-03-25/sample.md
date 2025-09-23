Solution:
We want to investigate the convergence of the improper integral $I = \int_0^\infty \cos(x)\cos(x^2)\,dx$.

We can use the product-to-sum trigonometric identity $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$.
Applying this identity with $A = x^2$ and $B = x$, we get:
$$ \cos(x) \cos(x^2) = \frac{1}{2} [\cos(x^2 - x) + \cos(x^2 + x)] $$
Thus, the integral becomes:
$$ I = \int_0^\infty \frac{1}{2} [\cos(x^2 - x) + \cos(x^2 + x)] \,dx = \frac{1}{2} \int_0^\infty \cos(x^2 - x) \,dx + \frac{1}{2} \int_0^\infty \cos(x^2 + x) \,dx $$
The convergence of the original integral $I$ depends on the convergence of the two integrals $I_1 = \int_0^\infty \cos(x^2 - x) \,dx$ and $I_2 = \int_0^\infty \cos(x^2 + x) \,dx$. If both $I_1$ and $I_2$ converge, then $I$ converges.

Let's investigate the convergence of $I_2 = \int_0^\infty \cos(x^2 + x) \,dx$.
We can use integration by parts. Let $\phi(x) = x^2 + x$. Then $\phi'(x) = 2x + 1$. For $x \ge 0$, $2x+1 \ge 1$.
We can write $\cos(x^2+x)$ as $\frac{1}{2x+1} (2x+1)\cos(x^2+x) = \frac{1}{2x+1} \frac{d}{dx}(\sin(x^2+x))$.
$$ I_2 = \lim_{b \to \infty} \int_0^b \cos(x^2+x) \,dx = \lim_{b \to \infty} \int_0^b \frac{1}{2x+1} \frac{d}{dx}(\sin(x^2+x)) \,dx $$
We apply integration by parts with $u = \frac{1}{2x+1}$ and $dv = \frac{d}{dx}(\sin(x^2+x)) \,dx$.
Then $du = \frac{-2}{(2x+1)^2} dx$ and $v = \sin(x^2+x)$.
$$ \int_0^b \cos(x^2+x) \,dx = \left[ \frac{\sin(x^2+x)}{2x+1} \right]_0^b - \int_0^b \sin(x^2+x) \left( \frac{-2}{(2x+1)^2} \right) \,dx $$
$$ = \left( \frac{\sin(b^2+b)}{2b+1} - \frac{\sin(0)}{1} \right) + 2 \int_0^b \frac{\sin(x^2+x)}{(2x+1)^2} \,dx $$
$$ = \frac{\sin(b^2+b)}{2b+1} + 2 \int_0^b \frac{\sin(x^2+x)}{(2x+1)^2} \,dx $$
Now, we take the limit as $b \to \infty$:
$$ \lim_{b \to \infty} \frac{\sin(b^2+b)}{2b+1} $$
Since $-1 \le \sin(b^2+b) \le 1$, and $\lim_{b \to \infty} (2b+1) = \infty$, by the Squeeze Theorem, this limit is 0.
$$ \lim_{b \to \infty} \frac{\sin(b^2+b)}{2b+1} = 0 $$
Next, we need to investigate the convergence of the integral $\int_0^\infty \frac{\sin(x^2+x)}{(2x+1)^2} \,dx$. We consider its absolute convergence:
$$ \int_0^\infty \left| \frac{\sin(x^2+x)}{(2x+1)^2} \right| \,dx \le \int_0^\infty \frac{1}{(2x+1)^2} \,dx $$
Let's evaluate the comparison integral:
$$ \int_0^\infty \frac{1}{(2x+1)^2} \,dx $$
Let $u = 2x+1$, then $du = 2 dx$. When $x=0$, $u=1$. As $x \to \infty$, $u \to \infty$.
$$ \int_1^\infty \frac{1}{u^2} \frac{du}{2} = \frac{1}{2} \int_1^\infty u^{-2} du = \frac{1}{2} \left[ \frac{u^{-1}}{-1} \right]_1^\infty = \frac{1}{2} \left[ -\frac{1}{u} \right]_1^\infty = \frac{1}{2} (0 - (-1)) = \frac{1}{2} $$
Since the comparison integral $\int_0^\infty \frac{1}{(2x+1)^2} \,dx$ converges, by the Comparison Test, the integral $\int_0^\infty \frac{\sin(x^2+x)}{(2x+1)^2} \,dx$ converges absolutely.
Therefore, the limit $\lim_{b \to \infty} 2 \int_0^b \frac{\sin(x^2+x)}{(2x+1)^2} \,dx$ exists and is finite.
This implies that $I_2 = \int_0^\infty \cos(x^2+x) \,dx$ converges.

Now let's investigate the convergence of $I_1 = \int_0^\infty \cos(x^2 - x) \,dx$.
Let $\psi(x) = x^2 - x$. Then $\psi'(x) = 2x - 1$. Note that $2x-1 = 0$ when $x=1/2$. The integration by parts technique used above involves division by $2x-1$, so we need to be careful around $x=1/2$. We can split the integral:
$$ I_1 = \int_0^1 \cos(x^2 - x) \,dx + \int_1^\infty \cos(x^2 - x) \,dx $$
The first integral $\int_0^1 \cos(x^2 - x) \,dx$ is a proper integral of a continuous function over a finite interval, so it is finite. We only need to check the convergence of the second integral $\int_1^\infty \cos(x^2 - x) \,dx$.
For $x \ge 1$, $2x-1 \ge 1$. We can write $\cos(x^2-x) = \frac{1}{2x-1} \frac{d}{dx}(\sin(x^2-x))$.
$$ \int_1^\infty \cos(x^2-x) \,dx = \lim_{b \to \infty} \int_1^b \frac{1}{2x-1} \frac{d}{dx}(\sin(x^2-x)) \,dx $$
Apply integration by parts with $u = \frac{1}{2x-1}$ and $dv = \frac{d}{dx}(\sin(x^2-x)) \,dx$.
Then $du = \frac{-2}{(2x-1)^2} dx$ and $v = \sin(x^2-x)$.
$$ \int_1^b \cos(x^2-x) \,dx = \left[ \frac{\sin(x^2-x)}{2x-1} \right]_1^b - \int_1^b \sin(x^2-x) \left( \frac{-2}{(2x-1)^2} \right) \,dx $$
$$ = \left( \frac{\sin(b^2-b)}{2b-1} - \frac{\sin(1^2-1)}{2(1)-1} \right) + 2 \int_1^b \frac{\sin(x^2-x)}{(2x-1)^2} \,dx $$
$$ = \frac{\sin(b^2-b)}{2b-1} - \frac{\sin(0)}{1} + 2 \int_1^b \frac{\sin(x^2-x)}{(2x-1)^2} \,dx $$
$$ = \frac{\sin(b^2-b)}{2b-1} + 2 \int_1^b \frac{\sin(x^2-x)}{(2x-1)^2} \,dx $$
Take the limit as $b \to \infty$:
$$ \lim_{b \to \infty} \frac{\sin(b^2-b)}{2b-1} = 0 $$
by the Squeeze Theorem, since $-1 \le \sin(b^2-b) \le 1$ and $\lim_{b \to \infty} (2b-1) = \infty$.
Now consider the integral $\int_1^\infty \frac{\sin(x^2-x)}{(2x-1)^2} \,dx$. Check absolute convergence:
$$ \int_1^\infty \left| \frac{\sin(x^2-x)}{(2x-1)^2} \right| \,dx \le \int_1^\infty \frac{1}{(2x-1)^2} \,dx $$
Let's evaluate the comparison integral:
$$ \int_1^\infty \frac{1}{(2x-1)^2} \,dx $$
Let $u = 2x-1$, then $du = 2 dx$. When $x=1$, $u=1$. As $x \to \infty$, $u \to \infty$.
$$ \int_1^\infty \frac{1}{u^2} \frac{du}{2} = \frac{1}{2} \int_1^\infty u^{-2} du = \frac{1}{2} \left[ -\frac{1}{u} \right]_1^\infty = \frac{1}{2} (0 - (-1)) = \frac{1}{2} $$
Since the comparison integral $\int_1^\infty \frac{1}{(2x-1)^2} \,dx$ converges, by the Comparison Test, the integral $\int_1^\infty \frac{\sin(x^2-x)}{(2x-1)^2} \,dx$ converges absolutely.
Therefore, the limit $\lim_{b \to \infty} 2 \int_1^b \frac{\sin(x^2-x)}{(2x-1)^2} \,dx$ exists and is finite.
This implies that $\int_1^\infty \cos(x^2-x) \,dx$ converges.
Since $\int_0^1 \cos(x^2 - x) \,dx$ is finite and $\int_1^\infty \cos(x^2 - x) \,dx$ converges, the integral $I_1 = \int_0^\infty \cos(x^2 - x) \,dx$ converges.

Since both $I_1 = \int_0^\infty \cos(x^2 - x) \,dx$ and $I_2 = \int_0^\infty \cos(x^2 + x) \,dx$ converge, their sum multiplied by $1/2$ also converges.
Therefore, the integral $I = \int_0^\infty \cos(x)\cos(x^2)\,dx$ is convergent.

Final Answer: The final answer is $\boxed{The\ integral\ is\ convergent}$