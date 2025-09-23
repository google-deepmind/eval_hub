# Solution

I'll solve this problem by finding the minimum value of the left-hand side expression.

Let's set $f(a_1, a_2, \ldots, a_n) = \sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p$, which we want to minimize subject to the constraint $a_1 + a_2 + \ldots + a_n = 1$ where $a_i > 0$ for all $i$.

## Using Lagrange Multipliers

I'll use the method of Lagrange multipliers to find the minimum value. The Lagrangian is:

$$L(a_1, a_2, \ldots, a_n, \lambda) = \sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p - \lambda \left( \sum_{i=1}^n a_i - 1 \right)$$

Taking the partial derivative with respect to each $a_i$ and setting it equal to zero:

$$\frac{\partial L}{\partial a_i} = p \left( a_i + \frac{1}{a_i} \right)^{p-1} \cdot \left( 1 - \frac{1}{a_i^2} \right) - \lambda = 0$$

This gives us:

$$p \left( a_i + \frac{1}{a_i} \right)^{p-1} \cdot \left( 1 - \frac{1}{a_i^2} \right) = \lambda$$

For convenience, let's define $h(a) = p \left( a + \frac{1}{a} \right)^{p-1} \cdot \left( 1 - \frac{1}{a^2} \right)$.

## Analyzing the Function $h(a)$

Let's examine the behavior of $h(a)$ for $a > 0$:

1. When $a = 1$: $h(1) = p \cdot 2^{p-1} \cdot 0 = 0$
2. When $a > 1$: Both $\left( a + \frac{1}{a} \right)^{p-1} > 0$ and $\left( 1 - \frac{1}{a^2} \right) > 0$, so $h(a) > 0$
3. When $0 < a < 1$: We have $\left( a + \frac{1}{a} \right)^{p-1} > 0$ but $\left( 1 - \frac{1}{a^2} \right) < 0$, so $h(a) < 0$

This shows that $h(a)$ is a strictly increasing function for $a > 0$, crossing zero at $a = 1$.

## Finding the Critical Point

Since $h(a)$ is strictly increasing, the equation $h(a_i) = \lambda$ for all $i$ implies that all $a_i$ must be equal. Given the constraint $\sum_{i=1}^n a_i = 1$, we have $a_i = \frac{1}{n}$ for all $i$.

## Verifying this is a Minimum

The strict monotonicity of $h(a)$ ensures that this critical point is the unique minimum of our constrained optimization problem.

## Computing the Minimum Value

When $a_i = \frac{1}{n}$ for all $i$, we have:

$$f\left(\frac{1}{n}, \frac{1}{n}, \ldots, \frac{1}{n}\right) = \sum_{i=1}^n \left( \frac{1}{n} + \frac{1}{\frac{1}{n}} \right)^p = n \cdot \left( \frac{1}{n} + n \right)^p = n \cdot \left( \frac{1+n^2}{n} \right)^p = \frac{(1+n^2)^p}{n^{p-1}}$$

## Conclusion

Thus, we have shown that:

$$\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p \geq \frac{(n^2+1)^p}{n^{p-1}}$$

with equality if and only if $a_i = \frac{1}{n}$ for all $i$.