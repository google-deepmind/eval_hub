

To evaluate the limit
$$
\lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right),
$$
we approximate the sum by leveraging the small-angle approximation for sine and convert the sum into an integral.

**Step-by-Step Explanation:**

1. **Simplify the Argument of Sine:**
   For large \( n \), the term inside the sine can be approximated:
   $$
   \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \approx \frac{\pi}{2} \cdot \frac{2k}{n^2} = \frac{\pi k}{n^2}.
   $$

2. **Small-Angle Approximation:**
   Since each term \( \theta_k = \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \) is small as \( n \to \infty \), we use \( \sin(\theta_k) \approx \theta_k \). The error term \( O(\theta_k^3) \) sums to zero because:
   $$
   \sum_{k=1}^n \theta_k^3 \approx \sum_{k=1}^n \left(\frac{\pi k}{n^2}\right)^3 = O\left(\frac{1}{n^3}\right) \to 0.
   $$

3. **Sum the Approximated Terms:**
   Substitute \( \sin(\theta_k) \approx \theta_k \):
   $$
   \sum_{k=1}^n \theta_k = \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \sum_{k=1}^n (n + 2k - 1).
   $$
   Compute the summation:
   $$
   \sum_{k=1}^n (n + 2k - 1) = n(n - 1) + 2 \cdot \frac{n(n+1)}{2} = 2n^2.
   $$

4. **Evaluate the Limit:**
   Substitute back:
   $$
   \sum_{k=1}^n \theta_k = \frac{\pi}{2} \cdot \frac{2n^2}{n(n-1)} = \pi \cdot \frac{n}{n-1} \xrightarrow{n\to\infty} \pi.
   $$

**Final Answer:**
The limit is
$$
\boxed{\pi}.
$$