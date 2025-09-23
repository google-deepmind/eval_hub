# Solution

I need to find the supremum of 
$$
\frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}}
$$
over all continuous functions $f$ on $[0,1]$ with $f(0) = 0$.

## Step 1: Establish an upper bound

By the Cauchy-Schwarz inequality, for any integrable functions $g$ and $h$:
$$\left|\int g(x)h(x)\,dx\right|^2 \leq \int |g(x)|^2\,dx \cdot \int |h(x)|^2\,dx$$

Taking $g(x) = |f(x)|$ and $h(x) = 1$ on $[0,1]$:
$$\left(\int_0^1 |f(x)|\,dx\right)^2 \leq \int_0^1 |f(x)|^2\,dx \cdot \int_0^1 1^2\,dx = \int_0^1 |f(x)|^2\,dx$$

Taking the square root of both sides:
$$\int_0^1 |f(x)|\,dx \leq \left(\int_0^1 |f(x)|^2\,dx\right)^{1/2}$$

This implies that for any $f \in \mathcal{F}$:
$$\frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}} \leq 1$$

## Step 2: Show the bound is tight

To prove that $\sup_{f \in \mathcal{F}} = 1$, I'll construct a sequence of functions in $\mathcal{F}$ whose ratio approaches 1.

Consider the sequence of functions:
$$
f_n(x) = 
\begin{cases} 
nx & \text{if } 0 \leq x \leq \frac{1}{n} \\
1 & \text{if } \frac{1}{n} < x \leq 1 
\end{cases}
$$

Each $f_n$ is continuous on $[0,1]$ and satisfies $f_n(0) = 0$, so $f_n \in \mathcal{F}$.

Let's compute the numerator:
$$
\int_{0}^{1} |f_n(x)| \, dx = \int_{0}^{\frac{1}{n}} nx \, dx + \int_{\frac{1}{n}}^{1} 1 \, dx = n\frac{x^2}{2}\bigg|_0^{1/n} + x\bigg|_{1/n}^1 = \frac{1}{2n} + \left(1 - \frac{1}{n}\right) = 1 - \frac{1}{2n}
$$

Now for the denominator:
$$
\int_0^1 |f_n(x)|^2 \, dx = \int_{0}^{\frac{1}{n}} (nx)^2 \, dx + \int_{\frac{1}{n}}^{1} 1^2 \, dx = n^2\frac{x^3}{3}\bigg|_0^{1/n} + x\bigg|_{1/n}^1 = \frac{1}{3n} + \left(1 - \frac{1}{n}\right) = 1 - \frac{2}{3n}
$$

Using the binomial expansion for large $n$:
$$\left(1 - \frac{2}{3n}\right)^{1/2} = 1 - \frac{1}{3n} + O\left(\frac{1}{n^2}\right)$$

Therefore:
$$
R(f_n) = \frac{1 - \frac{1}{2n}}{1 - \frac{1}{3n} + O\left(\frac{1}{n^2}\right)} = 1 - \frac{1}{6n} + O\left(\frac{1}{n^2}\right)
$$

As $n \to \infty$, we have $R(f_n) \to 1$.

## Conclusion

Since we've shown that:
1. $R(f) \leq 1$ for all $f \in \mathcal{F}$
2. There exists a sequence $f_n \in \mathcal{F}$ such that $\lim_{n \to \infty} R(f_n) = 1$

We can conclude that $\sup_{f \in \mathcal{F}} R(f) = 1$.