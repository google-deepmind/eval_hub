

To determine the expected number of tosses \( E[N] \) to get the first heads when the probability \( p \) of heads is uniformly distributed on \([0,1]\), we use the **law of total expectation**:

\[
E[N] = E_p\left[ E[N \mid p] \right]
\]

For a fixed \( p \), the number of tosses follows a geometric distribution with expectation \( E[N \mid p] = \frac{1}{p} \). Since \( p \) is uniformly distributed, its probability density function (PDF) is \( f(p) = 1 \) for \( p \in [0,1] \). Thus,

\[
E[N] = \int_{0}^{1} \frac{1}{p} \cdot 1 \, dp = \int_{0}^{1} \frac{1}{p} \, dp
\]

This integral is **improper** at \( p = 0 \). Evaluating the limit,

\[
\int_{0}^{1} \frac{1}{p} \, dp = \lim_{\epsilon \to 0^+} \int_{\epsilon}^{1} \frac{1}{p} \, dp = \lim_{\epsilon \to 0^+} \left[ \ln p \right]_{\epsilon}^{1} = \lim_{\epsilon \to 0^+} ( \ln 1 - \ln \epsilon ) = 0 - (-\infty) = \infty
\]

Since the integral diverges to infinity, the expected number of tosses \( E[N] \) is infinite. This occurs because the contribution from \( p \to 0 \) (where the expected number of tosses grows unboundedly) dominates the integral.

```markdown
**Final Answer**
The expected number of tosses to get the first heads is \boxed{\infty}.
```