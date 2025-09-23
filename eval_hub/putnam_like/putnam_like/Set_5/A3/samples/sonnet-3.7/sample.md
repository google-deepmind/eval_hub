# Solution

To prove that $\prod_{i<j} (e_i+e_j)^2=1$, where $e_1=1, e_2,\ldots, e_n$ are the $n$-th roots of unity and $n$ is odd, I'll compute an auxiliary product and analyze it from two different angles.

Let's define $S = \prod_{i=1}^{n} \prod_{j=1}^{n} (e_i+e_j)$.

## Angle 1: Computing $S$ directly

For a fixed $i$, consider $\prod_{j=1}^{n} (e_i+e_j)$. This is equivalent to evaluating the polynomial $P(z) = \prod_{j=1}^{n} (z+e_j)$ at $z = e_i$.

To determine $P(z)$, we start with the known polynomial $Q(z) = \prod_{j=1}^{n} (z-e_j) = z^n - 1$ (since $e_j$ are the $n$-th roots of unity).

If we evaluate $Q(-z)$, we get:
$$Q(-z) = (-z)^n - 1 = -z^n - 1$$
since $n$ is odd.

We can also express $Q(-z)$ as:
$$Q(-z) = \prod_{j=1}^{n} (-z-e_j) = (-1)^n \times \prod_{j=1}^{n} (z+e_j) = -\prod_{j=1}^{n} (z+e_j)$$
since $n$ is odd and $(-1)^n = -1$.

Equating these expressions:
$$-\prod_{j=1}^{n} (z+e_j) = -z^n - 1$$
$$\therefore \prod_{j=1}^{n} (z+e_j) = z^n + 1$$

So $P(z) = z^n + 1$, and at $z = e_i$:
$$\prod_{j=1}^{n} (e_i+e_j) = P(e_i) = e_i^n + 1 = 1 + 1 = 2$$
since $e_i^n = 1$ for all $i$.

Therefore, $S = \prod_{i=1}^{n} \prod_{j=1}^{n} (e_i+e_j) = \prod_{i=1}^{n} 2 = 2^n$.

## Angle 2: Rewriting $S$ differently

We can also express $S$ as:
$$S = \prod_{i=1}^{n} \prod_{j=1}^{n} (e_i+e_j) = \prod_{i=1}^{n} [(e_i+e_i) \times \prod_{j \neq i} (e_i+e_j)]$$
$$= \prod_{i=1}^{n} [2e_i \times \prod_{j \neq i} (e_i+e_j)]$$
$$= \prod_{i=1}^{n} 2e_i \times \prod_{i=1}^{n} \prod_{j \neq i} (e_i+e_j)$$
$$= 2^n \times \prod_{i=1}^{n} e_i \times \prod_{i \neq j} (e_i+e_j)$$

From the polynomial $z^n - 1 = \prod_{j=1}^{n} (z-e_j)$, comparing the constant terms, we get $(-1)^n \times \prod_{j=1}^{n} e_j = -1$. Since $n$ is odd, $(-1)^n = -1$, which means $\prod_{j=1}^{n} e_j = 1$.

So:
$$S = 2^n \times 1 \times \prod_{i \neq j} (e_i+e_j) = 2^n \times \prod_{i \neq j} (e_i+e_j)$$

In the product $\prod_{i \neq j} (e_i+e_j)$, each unordered pair $\{i,j\}$ (where $i \neq j$) appears twice: once as $(e_i+e_j)$ and once as $(e_j+e_i)$. Since addition is commutative, $(e_i+e_j) = (e_j+e_i)$, so:
$$\prod_{i \neq j} (e_i+e_j) = \prod_{i<j} (e_i+e_j)^2$$

Therefore:
$$S = 2^n \times \prod_{i<j} (e_i+e_j)^2$$

## Conclusion

Equating our two expressions for $S$:
$$2^n = 2^n \times \prod_{i<j} (e_i+e_j)^2$$

This gives us $\prod_{i<j} (e_i+e_j)^2 = 1$, which completes the proof.