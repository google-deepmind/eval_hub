```markdown
# Problem Statement

Suppose that $f : \mathbb{R} \rightarrow \mathbb{R}$ is Lebesgue integrable. Show that the function $g : \mathbb{R} \rightarrow \mathbb{R}$ given by
$$
g(x) = \int_x^{x+1} f(y) \, dy
$$
is Lebesgue integrable and that
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx.
$$

# Solution

Let $f : \mathbb{R} \rightarrow \mathbb{R}$ be a Lebesgue integrable function. This means $f$ is measurable and $\int_{-\infty}^\infty |f(x)| \, dx < \infty$.
The function $g : \mathbb{R} \rightarrow \mathbb{R}$ is defined by
$$
g(x) = \int_x^{x+1} f(y) \, dy.
$$
Since $f$ is measurable and $\int |f| dx < \infty$, for any finite interval $[a, b]$, the function $f \cdot \mathbb{1}_{[a, b]}$ is Lebesgue integrable because $|f(y) \mathbb{1}_{[a, b]}(y)| \le |f(y)|$, and $\int |f(y)| dy < \infty$. Thus, the integral $\int_a^b f(y) \, dy$ is well-defined for any finite $a < b$. In particular, $g(x) = \int_x^{x+1} f(y) \, dy$ is well-defined for every $x \in \mathbb{R}$.

We want to show that $g$ is Lebesgue integrable and that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.

First, let's express $g(x)$ as a convolution. The integral $\int_x^{x+1} f(y) \, dy$ can be written as $\int_{-\infty}^\infty f(y) \mathbb{1}_{[x, x+1]}(y) \, dy$, where $\mathbb{1}_{[x, x+1]}$ is the indicator function of the interval $[x, x+1]$.
We observe that $\mathbb{1}_{[x, x+1]}(y) = 1$ if and only if $x \le y \le x+1$.
Let $h(z) = \mathbb{1}_{[-1, 0]}(z)$. Then $h(x-y) = \mathbb{1}_{[-1, 0]}(x-y)$. The condition $-1 \le x-y \le 0$ is equivalent to $0 \le y-x \le 1$, which is $x \le y \le x+1$.
Thus, $\mathbb{1}_{[x, x+1]}(y) = \mathbb{1}_{[-1, 0]}(x-y)$.
So, $g(x) = \int_{-\infty}^\infty f(y) \mathbb{1}_{[-1, 0]}(x-y) \, dy$.
This is the definition of the convolution of $f$ and $h$, where $h(y) = \mathbb{1}_{[-1, 0]}(y)$. That is, $g(x) = (f * h)(x)$.

Now we show that $g$ is Lebesgue integrable.
The function $h(y) = \mathbb{1}_{[-1, 0]}(y)$ is measurable. Its $L^1$ norm is
$$
\|h\|_1 = \int_{-\infty}^\infty |h(y)| \, dy = \int_{-\infty}^\infty \mathbb{1}_{[-1, 0]}(y) \, dy = \int_{-1}^0 1 \, dy = [y]_{-1}^0 = 0 - (-1) = 1.
$$
Since $\|h\|_1 < \infty$, $h \in L^1(\mathbb{R})$.
We are given that $f$ is Lebesgue integrable, which means $f \in L^1(\mathbb{R})$.
A standard result in the theory of Lebesgue integration and convolution states that if $f \in L^1(\mathbb{R})$ and $h \in L^1(\mathbb{R})$, then their convolution $f * h$ is defined almost everywhere and belongs to $L^1(\mathbb{R})$. This implies that $f*h$ is measurable and $\int |f*h| dx < \infty$.
Since $g = f * h$ with $f \in L^1(\mathbb{R})$ and $h \in L^1(\mathbb{R})$, we conclude that $g \in L^1(\mathbb{R})$.
This means $g$ is a Lebesgue integrable function.

Next, we show that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.
Another standard result for convolutions of $L^1$ functions states that if $f, h \in L^1(\mathbb{R})$, then
$$
\int_{-\infty}^\infty (f * h)(x) \, dx = \left( \int_{-\infty}^\infty f(x) \, dx \right) \left( \int_{-\infty}^\infty h(x) \, dx \right).
$$
Using this property with $g = f * h$ where $h(x) = \mathbb{1}_{[-1, 0]}(x)$:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty (f * \mathbb{1}_{[-1, 0]})(x) \, dx = \left( \int_{-\infty}^\infty f(x) \, dx \right) \left( \int_{-\infty}^\infty \mathbb{1}_{[-1, 0]}(x) \, dx \right).
$$
We have already calculated the integral of $h(x) = \mathbb{1}_{[-1, 0]}(x)$:
$$
\int_{-\infty}^\infty \mathbb{1}_{[-1, 0]}(x) \, dx = 1.
$$
Substituting this into the equation:
$$
\int_{-\infty}^\infty g(x) \, dx = \left( \int_{-\infty}^\infty f(x) \, dx \right) \cdot 1 = \int_{-\infty}^\infty f(x) \, dx.
$$

Therefore, we have shown that the function $g$ is Lebesgue integrable and that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.
```