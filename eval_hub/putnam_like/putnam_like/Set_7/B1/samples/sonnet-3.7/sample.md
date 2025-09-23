# Solution

Given that $f : \mathbb{R} \rightarrow \mathbb{R}$ is Lebesgue integrable, we need to show that the function $g(x) = \int_x^{x+1} f(y) \, dy$ is also Lebesgue integrable and that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.

## Part 1: Showing $g$ is Lebesgue integrable

Since $f$ is Lebesgue integrable, we know that $\int_{-\infty}^\infty |f(x)| \, dx < \infty$.

For any $x \in \mathbb{R}$, by the properties of absolute value and the Lebesgue integral:
$$|g(x)| = \left|\int_x^{x+1} f(y) \, dy\right| \leq \int_x^{x+1} |f(y)| \, dy$$

To show that $g$ is Lebesgue integrable, we need to prove that $\int_{-\infty}^\infty |g(x)| \, dx < \infty$. Using the inequality above:

$$\int_{-\infty}^\infty |g(x)| \, dx \leq \int_{-\infty}^\infty \int_x^{x+1} |f(y)| \, dy \, dx$$

To evaluate this double integral, we'll use Fubini's theorem to change the order of integration. For fixed $y$, the variable $x$ must satisfy $x \leq y \leq x+1$, which is equivalent to $y-1 \leq x \leq y$. So the region of integration can be described as:
$$\{(x,y) : x \leq y \leq x+1, -\infty < x < \infty\} = \{(x,y) : y-1 \leq x \leq y, -\infty < y < \infty\}$$

Thus, by Fubini's theorem:
$$\int_{-\infty}^\infty \int_x^{x+1} |f(y)| \, dy \, dx = \int_{-\infty}^\infty \int_{y-1}^y |f(y)| \, dx \, dy$$

Since $|f(y)|$ is constant with respect to $x$, the inner integral becomes:
$$\int_{y-1}^y |f(y)| \, dx = |f(y)| \cdot (y-(y-1)) = |f(y)|$$

Therefore:
$$\int_{-\infty}^\infty \int_{y-1}^y |f(y)| \, dx \, dy = \int_{-\infty}^\infty |f(y)| \, dy < \infty$$

This proves that $g$ is Lebesgue integrable.

## Part 2: Showing $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$

Using the definition of $g$ and applying Fubini's theorem in the same way as above:

$$\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \int_x^{x+1} f(y) \, dy \, dx = \int_{-\infty}^\infty \int_{y-1}^y f(y) \, dx \, dy$$

Since $f(y)$ is constant with respect to $x$, the inner integral evaluates to:
$$\int_{y-1}^y f(y) \, dx = f(y) \cdot 1 = f(y)$$

Therefore:
$$\int_{-\infty}^\infty \int_{y-1}^y f(y) \, dx \, dy = \int_{-\infty}^\infty f(y) \, dy = \int_{-\infty}^\infty f(x) \, dx$$

Thus, we have shown that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.