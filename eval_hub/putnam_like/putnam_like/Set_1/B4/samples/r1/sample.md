

To find the limit
$$
\lim_{n\to\infty} \int_0^1 \frac{(1-\ln(1-x))^n}{n!} \, dx,
$$
we start by making the substitution \( u = -\ln(1 - x) \). This transforms the integral limits from \( x = 0 \) to \( x = 1 \) into \( u = 0 \) to \( u = \infty \), and the differential \( dx \) becomes \( e^{-u} \, du \). The integral becomes:
$$
\int_0^\infty \frac{(1 + u)^n e^{-u}}{n!} \, du.
$$

Next, we recognize that this integral can be evaluated exactly using the binomial theorem. Expanding \( (1 + u)^n \) and integrating term-by-term:
$$
\int_0^\infty \frac{(1 + u)^n e^{-u}}{n!} \, du = \sum_{k=0}^n \frac{1}{k!}.
$$

This sum is the partial sum of the series expansion of \( e \). As \( n \to \infty \), the partial sum converges to \( e \). Therefore, the limit is:
$$
\lim_{n\to\infty} \sum_{k=0}^n \frac{1}{k!} = e.
$$

Thus, the final answer is:
$$
\boxed{e}
$$