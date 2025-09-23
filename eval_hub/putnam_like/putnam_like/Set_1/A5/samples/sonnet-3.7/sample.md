# Solution

I'll find the limit of $\displaystyle\lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right)$.

For large values of $n$, the arguments inside the sine function become small. This allows me to use the small-angle approximation: $\sin(θ) \approx θ$ when $θ$ is close to zero.

First, let me examine the argument inside the sine function:

$$\frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)}$$

Let's check the maximum value of this argument:
- When $k = n$ (maximum value), we get: $\frac{\pi}{2} \cdot \frac{n+2n-1}{n(n-1)} = \frac{\pi}{2} \cdot \frac{3n-1}{n(n-1)} \approx \frac{3\pi}{2n}$ for large $n$

This confirms that as $n \to \infty$, the arguments inside all sine terms approach zero.

Using the small-angle approximation, I can write:

$$\sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) \approx \sum_{k=1}^n \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)}$$

Computing this sum:

$$\frac{\pi}{2} \cdot \sum_{k=1}^n \frac{n+2k-1}{n(n-1)} = \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \sum_{k=1}^n (n+2k-1)$$

$$= \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \left[n^2 + 2\sum_{k=1}^n k - n\right]$$

Using the formula $\sum_{k=1}^n k = \frac{n(n+1)}{2}$:

$$= \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \left[n^2 + n(n+1) - n\right]$$

$$= \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \left[n^2 + n^2 + n - n\right]$$

$$= \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \cdot 2n^2 = \frac{\pi}{2} \cdot \frac{2n}{n-1}$$

As $n \to \infty$, we have $\frac{2n}{n-1} \to 2$, so:

$$\lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) = \frac{\pi}{2} \cdot 2 = \pi$$

The error in using the small-angle approximation is of order $\frac{1}{n^2}$, which vanishes as $n \to \infty$.

Therefore, the value of the limit is $\pi$.