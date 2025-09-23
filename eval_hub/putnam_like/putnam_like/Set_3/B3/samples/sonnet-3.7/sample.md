# Solution: Convergence of $\int_0^\infty \cos(x)\cos(x^2)\,dx$

To investigate if the integral $\int_0^\infty \cos(x)\cos(x^2)\,dx$ is convergent, I'll use the product-to-sum formula for cosines:

$$\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$$

Applying this formula to our integrand:

$$\cos(x)\cos(x^2) = \frac{1}{2}[\cos(x+x^2) + \cos(x-x^2)]$$

Thus, our integral becomes:

$$\int_0^\infty \cos(x)\cos(x^2)\,dx = \frac{1}{2}\int_0^\infty [\cos(x+x^2) + \cos(x-x^2)]\,dx$$

I'll analyze each term separately:

## First term: $\int_0^\infty \cos(x+x^2)\,dx$

For oscillatory integrals of the form $\int_0^\infty \cos(f(x))\,dx$, a key criterion for convergence is that $f'(x)$ is eventually monotonic and its absolute value tends to infinity as $x \to \infty$. This ensures rapid oscillations that lead to cancellations.

For the function $f_1(x) = x+x^2$, we have $f_1'(x) = 1+2x$, which is:
- Always positive for $x > 0$
- Strictly increasing 
- Grows without bound as $x \to \infty$

This means the integrand oscillates more and more rapidly as $x$ increases, ensuring that $\int_0^\infty \cos(x+x^2)\,dx$ converges.

## Second term: $\int_0^\infty \cos(x-x^2)\,dx$

For the function $f_2(x) = x-x^2$, we have $f_2'(x) = 1-2x$.
- For $x > \frac{1}{2}$, $f_2'(x)$ is negative
- The absolute value $|f_2'(x)| = |1-2x| = 2x-1$ for $x > \frac{1}{2}$
- This absolute value grows without bound as $x \to \infty$

Again, the integrand oscillates more and more rapidly as $x$ increases, ensuring that $\int_0^\infty \cos(x-x^2)\,dx$ also converges.

## Conclusion

Since both $\int_0^\infty \cos(x+x^2)\,dx$ and $\int_0^\infty \cos(x-x^2)\,dx$ are convergent, their sum $\int_0^\infty \cos(x)\cos(x^2)\,dx$ is also convergent.