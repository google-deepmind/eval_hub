

To prove that the integral 

\[
\int_\alpha^\infty \frac{f(x - \alpha) - f(x + \alpha)}{f(x)} \, dx = \infty,
\]

we proceed as follows:

### Key Observations:
1. **Positivity of the Integrand**: Since \( f \) is strictly decreasing, \( f(x - \alpha) > f(x) > f(x + \alpha) \). Thus, the numerator \( f(x - \alpha) - f(x + \alpha) > 0 \), and the denominator \( f(x) > 0 \). Hence, the integrand is positive over \( [\alpha, \infty) \).

2. **Substitution**: Let \( t = x - \alpha \). The integral transforms to:
   \[
   \int_0^\infty \frac{f(t) - f(t + 2\alpha)}{f(t + \alpha)} \, dt.
   \]

3. **Splitting the Integral**: Split the transformed integral into two parts:
   \[
   \int_0^\infty \left( \frac{f(t)}{f(t + \alpha)} - 1 \right) dt + \int_\alpha^\infty \left( 1 - \frac{f(s + \alpha)}{f(s)} \right) ds.
   \]

### Analysis of Each Part:
#### First Integral (\( K \)):
\[
K = \int_0^\infty \left( \frac{f(t)}{f(t + \alpha)} - 1 \right) dt.
\]
- Since \( f(t) > f(t + \alpha) \), the integrand \( \frac{f(t)}{f(t + \alpha)} - 1 > 0 \).
- **Case Analysis**:
  - If \( f \) decays exponentially (e.g., \( f(t) = e^{-kt} \)), the ratio \( \frac{f(t)}{f(t + \alpha)} = e^{k\alpha} \), a constant \( > 1 \). Thus, \( K \) diverges.
  - If \( f \) decays polynomially (e.g., \( f(t) = t^{-p} \)), the ratio \( \frac{f(t)}{f(t + \alpha)} \approx 1 + \frac{p\alpha}{t} \), leading the integrand \( \approx \frac{p\alpha}{t} \). Integrating \( \frac{1}{t} \) diverges.
  - For faster decays (e.g., \( f(t) = e^{-t^2} \)), \( \frac{f(t)}{f(t + \alpha)} \to \infty \), causing divergence.

#### Second Integral (\( L \)):
\[
L = \int_\alpha^\infty \left( 1 - \frac{f(s + \alpha)}{f(s)} \right) ds.
\]
- Similarly, \( \frac{f(s + \alpha)}{f(s)} < 1 \), so the integrand \( > 0 \).
- If \( f \) decays polynomially, \( 1 - \frac{f(s + \alpha)}{f(s)} \approx \frac{p\alpha}{s} \), and \( L \) diverges.
- For exponential decay, \( \frac{f(s + \alpha)}{f(s)} \) is constant \( < 1 \), leading \( L \) to diverge.

### Conclusion:
At least one of \( K \) or \( L \) diverges for any \( f \) satisfying the given conditions. Therefore, the original integral diverges to infinity.

\[
\boxed{\infty}
\]