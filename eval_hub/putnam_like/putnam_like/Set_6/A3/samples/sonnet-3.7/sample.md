# Solution

I'll solve this problem by analyzing the relationship between $f$ and the exponential function.

## Approach

Let's define $S_n(t) = f(t) + f'(t) + \cdots + f^{(n)}(t)$ for each $n \in \mathbb{N}$.

The given condition can be rewritten as:
$$\frac{S_n(b_n)}{S_n(a_n)} = \frac{e^{b_n}}{e^{a_n}}$$

This is equivalent to:
$$\frac{S_n(b_n)}{e^{b_n}} = \frac{S_n(a_n)}{e^{a_n}}$$

Let $G_n(t) = \frac{S_n(t)}{e^t}$. Then $G_n(a_n) = G_n(b_n)$.

## Application of Mean Value Theorem

By the Mean Value Theorem, there exists $\xi_n \in (a_n, b_n)$ such that $G_n'(\xi_n) = 0$.

Computing the derivative:
$$G_n'(t) = \frac{S_n'(t) \cdot e^t - S_n(t) \cdot e^t}{e^{2t}} = \frac{S_n'(t) - S_n(t)}{e^t}$$

Since $G_n'(\xi_n) = 0$, we have $S_n'(\xi_n) = S_n(\xi_n)$.

Now:
$$S_n'(t) = f'(t) + f''(t) + \cdots + f^{(n+1)}(t)$$
$$S_n(t) = f(t) + f'(t) + \cdots + f^{(n)}(t)$$

Therefore:
$$f'(\xi_n) + f''(\xi_n) + \cdots + f^{(n+1)}(\xi_n) = f(\xi_n) + f'(\xi_n) + \cdots + f^{(n)}(\xi_n)$$

Simplifying:
$$f^{(n+1)}(\xi_n) = f(\xi_n)$$

## Finding the Limit

Since $a_n, b_n \to c$ as $n \to \infty$, and $\xi_n \in (a_n, b_n)$, we have $\xi_n \to c$.

By continuity of $f$, we know $f(\xi_n) \to f(c)$ as $n \to \infty$. Thus:
$$\lim_{n \to \infty} f^{(n+1)}(\xi_n) = f(c)$$

Now, using the Mean Value Theorem and the uniform boundedness of derivatives:
For each $n$, there exists $\eta_n$ between $\xi_n$ and $c$ such that:
$$f^{(n+1)}(\xi_n) - f^{(n+1)}(c) = f^{(n+2)}(\eta_n) \cdot (\xi_n - c)$$

Since all derivatives are uniformly bounded, there exists $M > 0$ such that $|f^{(k)}(t)| \leq M$ for all $k \in \mathbb{N}$ and $t \in (-1, 1)$. Thus:
$$|f^{(n+1)}(\xi_n) - f^{(n+1)}(c)| \leq M \cdot |\xi_n - c|$$

As $n \to \infty$, $\xi_n \to c$, so $|\xi_n - c| \to 0$. Therefore:
$$\lim_{n \to \infty} f^{(n+1)}(\xi_n) = \lim_{n \to \infty} f^{(n+1)}(c)$$

Combining with our earlier result:
$$\lim_{n \to \infty} f^{(n+1)}(c) = f(c)$$

By reindexing (setting $m = n+1$), we conclude:
$$\lim_{m \to \infty} f^{(m)}(c) = f(c)$$

which is what we needed to prove.