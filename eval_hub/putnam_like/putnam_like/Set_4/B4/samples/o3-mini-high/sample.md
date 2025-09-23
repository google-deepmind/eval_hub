```markdown
We wish to show that for any \( k\ge1 \) the following inequality holds:
\[
\int_{B(0,1)} |x_1|^{2k} \, dx \ge \frac{\omega_n}{n^{k}(2k+n)},
\]
where \( B(0,1) \) is the unit ball in \(\mathbb{R}^n\) and \(\omega_n\) denotes the surface area of the \((n-1)\)-dimensional unit sphere \( S^{n-1} \).

### Step 1. Write the Integral in Spherical Coordinates

In \(\mathbb{R}^n\) we can express the integral in spherical coordinates. Writing
\[
x = r\theta, \quad r\in [0,1],\quad \theta \in S^{n-1},
\]
the volume element becomes
\[
dx = r^{n-1} \, dr\, dS(\theta).
\]
Thus, we have
\[
\int_{B(0,1)} |x_1|^{2k} \, dx = \int_0^1 \int_{S^{n-1}} |r\theta_1|^{2k} \, r^{n-1} \, dS(\theta) \, dr.
\]
Since \( |r\theta_1|^{2k} = r^{2k} |\theta_1|^{2k} \), we can separate the integrals:
\[
\int_{B(0,1)} |x_1|^{2k} \, dx = \left(\int_0^1 r^{n-1+2k}\, dr\right) \left(\int_{S^{n-1}} |\theta_1|^{2k}\, dS(\theta)\right).
\]

### Step 2. Evaluate the Radial Part

The radial integral is straightforward:
\[
\int_0^1 r^{n-1+2k}\, dr = \frac{1}{n+2k}.
\]
Thus, the integral becomes
\[
\int_{B(0,1)} |x_1|^{2k} \, dx = \frac{1}{n+2k} \int_{S^{n-1}} |\theta_1|^{2k}\, dS(\theta).
\]

### Step 3. Bound the Angular Integral

It remains to show that
\[
\int_{S^{n-1}} |\theta_1|^{2k}\, dS(\theta) \ge \frac{\omega_n}{n^k}.
\]
We can interpret the normalized integral over the sphere as the expected value of \(|\theta_1|^{2k}\) when \(\theta\) is uniformly distributed over \( S^{n-1} \):
\[
\mathbb{E}[|\theta_1|^{2k}] = \frac{1}{\omega_n}\int_{S^{n-1}} |\theta_1|^{2k}\, dS(\theta).
\]

#### Using Symmetry

By symmetry, the coordinates of \(\theta\) are identically distributed, and it is a well-known fact that when \(\theta\) is uniformly distributed over \(S^{n-1}\), one has
\[
\mathbb{E}[\theta_1^2] = \frac{1}{n}.
\]

#### Using Jensen’s Inequality

Since the function \( x \mapsto x^k \) on \([0,\infty)\) is convex for \( k \ge 1 \), Jensen's inequality gives:
\[
\mathbb{E}\left[(\theta_1^2)^k\right] \ge \bigl(\mathbb{E}[\theta_1^2]\bigr)^k.
\]
That is,
\[
\mathbb{E}[|\theta_1|^{2k}] \ge \left(\frac{1}{n}\right)^k.
\]
Multiplying both sides by \(\omega_n\) yields:
\[
\int_{S^{n-1}} |\theta_1|^{2k}\, dS(\theta) \ge \frac{\omega_n}{n^k}.
\]

### Step 4. Conclude the Result

Returning to our expression for the integral over the unit ball, we obtain:
\[
\int_{B(0,1)} |x_1|^{2k} \, dx = \frac{1}{n+2k} \int_{S^{n-1}} |\theta_1|^{2k}\, dS(\theta) \ge \frac{1}{n+2k} \cdot \frac{\omega_n}{n^k} = \frac{\omega_n}{n^k (n+2k)}.
\]

Thus, we have shown that
\[
\boxed{\int_{B(0,1)} |x_1|^{2k} \, dx \ge \frac{\omega_n}{n^k (2k+n)}.}
\]
This completes the proof.
```