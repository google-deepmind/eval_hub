# Solution

Let's analyze the given integral and determine whether it converges or diverges.

## Approach

Given:
- $\alpha > 0$
- $f:[0,\infty)\to\mathbb{R}$ is strictly decreasing and continuous
- $\lim_{x\to\infty}f(x)=0$

We need to prove that $\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx = \infty$.

First, we'll define a helpful function $h(x) = -\log(f(x))$ for $x \geq 0$. Since $f$ is strictly decreasing and approaches 0 as $x \to \infty$, we know that $h$ is strictly increasing and $\lim_{x\to\infty}h(x) = \infty$.

## Establishing a Lower Bound

Using the function $h$, we can rewrite the integrand as:

$$\frac{f(x-\alpha)-f(x+\alpha)}{f(x)} = \frac{e^{-h(x-\alpha)}-e^{-h(x+\alpha)}}{e^{-h(x)}} = e^{h(x)-h(x-\alpha)} - e^{h(x)-h(x+\alpha)}$$

Since $h$ is strictly increasing, for $x > \alpha$, we have:
$$h(x-\alpha) < h(x) < h(x+\alpha)$$

Let's denote:
- $A(x) = h(x) - h(x-\alpha) > 0$
- $B(x) = h(x+\alpha) - h(x) > 0$

The integrand becomes:
$$e^{A(x)} - e^{-B(x)}$$

Using the properties of the exponential function:
- For all $x > 0$, $e^x > 1 + x$
- For all $x > 0$, $e^{-x} < 1$

Thus:
$$e^{A(x)} - e^{-B(x)} > (1 + A(x)) - 1 = A(x) = h(x) - h(x-\alpha)$$

Therefore:
$$\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx > \int_\alpha^\infty [h(x) - h(x-\alpha)]dx$$

## Evaluating the Lower Bound

Let's compute this integral over a finite interval $[\alpha, T]$ first, and then take the limit as $T \to \infty$:

$$\int_\alpha^T [h(x) - h(x-\alpha)]dx = \int_\alpha^T h(x)dx - \int_\alpha^T h(x-\alpha)dx$$

Using the substitution $u = x-\alpha$ for the second integral:
$$\int_\alpha^T h(x-\alpha)dx = \int_0^{T-\alpha} h(u)du$$

Therefore:
$$\int_\alpha^T [h(x) - h(x-\alpha)]dx = \int_\alpha^T h(x)dx - \int_0^{T-\alpha} h(u)du$$

Rewriting with consistent variables and breaking up the integral:
$$\int_\alpha^T [h(x) - h(x-\alpha)]dx = \int_\alpha^T h(x)dx - \left(\int_0^\alpha h(x)dx + \int_\alpha^{T-\alpha} h(x)dx\right)$$

$$= \int_\alpha^T h(x)dx - \int_0^\alpha h(x)dx - \int_\alpha^{T-\alpha} h(x)dx$$

$$= \int_{T-\alpha}^T h(x)dx - \int_0^\alpha h(x)dx$$

## Completing the Proof

Since $\lim_{x\to\infty}h(x) = \infty$, for any constant $K > 0$, there exists $M_K$ such that for all $x \geq M_K$, we have $h(x) \geq K$.

For $T > M_K + \alpha$:
$$\int_{T-\alpha}^T h(x)dx \geq \int_{T-\alpha}^T K dx = K\alpha$$

As $K$ can be chosen arbitrarily large, the integral $\int_{T-\alpha}^T h(x)dx$ grows without bound as $T \to \infty$.

The term $\int_0^\alpha h(x)dx$ is constant, so:
$$\lim_{T\to\infty}\int_\alpha^T [h(x) - h(x-\alpha)]dx = \infty$$

Therefore, the original integral diverges to infinity:
$$\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx = \infty$$