# Solution

I will prove that there does not exist a sequence $(z_n) \subset \mathbb{R}^2$ that satisfies the given conditions.

## Proof by Contradiction

Assume, for contradiction, that there exists a sequence $(z_n) \subset \mathbb{R}^2$ such that:

1. $\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx \to 0$ for every continuous function $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$
2. $B(z_n, 1/n) \cap B(z_m, 1/m) = \emptyset$ for $n \neq m$

I will construct a continuous function $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$ for which condition 1 fails, thereby reaching a contradiction.

For each $n \in \mathbb{N}$, define the function $\phi_n : \mathbb{R}^2 \rightarrow \mathbb{R}$ as follows:
$$\phi_n(x) = n \cdot \max(0, 1 - n|x - z_n|)$$

Note that $\phi_n$ has the following properties:
- $\phi_n$ is continuous on $\mathbb{R}^2$
- $\phi_n(z_n) = n$ (maximum value at the center of the ball)
- $\phi_n(x) = 0$ for all $x$ outside $B(z_n, 1/n)$
- $\phi_n$ decreases linearly from $z_n$ to the boundary of the ball

Now define $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$ as:
$$\varphi(x) = \sum_{n=1}^{\infty} \phi_n(x)$$

This function is well-defined and continuous because, due to the disjointness of the balls, for any point $x \in \mathbb{R}^2$, at most one term in the sum is non-zero.

Let's calculate the value of $\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx$ for any $n$:

$$\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx = \frac{n}{\pi} \int_{B(z_n, 1/n)} \phi_n(x) \, dx$$

The last equality follows from the fact that inside $B(z_n, 1/n)$, only $\phi_n$ is non-zero due to the disjointness of the balls.

Using polar coordinates centered at $z_n$, with $r = |x - z_n|$, we compute:

$$\int_{B(z_n, 1/n)} \phi_n(x) \, dx = \int_0^{2\pi} \int_0^{1/n} n \cdot (1 - nr) \cdot r \, dr \, d\theta$$

$$= 2\pi \cdot n \cdot \int_0^{1/n} (r - nr^2) \, dr$$

$$= 2\pi \cdot n \cdot \left[ \frac{r^2}{2} - \frac{nr^3}{3} \right]_0^{1/n}$$

$$= 2\pi \cdot n \cdot \left[ \frac{1}{2n^2} - \frac{1}{3n^2} \right]$$

$$= 2\pi \cdot \frac{1}{6n} = \frac{\pi}{3n}$$

Therefore:
$$\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx = \frac{n}{\pi} \cdot \frac{\pi}{3n} = \frac{1}{3}$$

This expression equals $\frac{1}{3}$ for all $n$, which does not converge to 0 as $n \to \infty$. This contradicts our assumption that $\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx \to 0$ for every continuous function $\varphi$.

Therefore, there does not exist a sequence $(z_n) \subset \mathbb{R}^2$ satisfying the given conditions.