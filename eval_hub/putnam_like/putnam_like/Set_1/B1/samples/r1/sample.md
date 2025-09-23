

To solve the equation \(6^{x^2} + 5^{x^2} - 10^{x^2} = 1\), we start by substituting \(t = x^2\), which transforms the equation into:

\[
6^t + 5^t - 10^t = 1 \quad \text{where} \quad t \geq 0.
\]

Define \(f(t) = 6^t + 5^t - 10^t - 1\). We analyze \(f(t)\) for \(t \geq 0\):

1. **At \(t = 0\)**:
   \[
   f(0) = 6^0 + 5^0 - 10^0 - 1 = 1 + 1 - 1 - 1 = 0.
   \]
   Thus, \(t = 0\) is a solution, corresponding to \(x = 0\).

2. **At \(t = 1\)**:
   \[
   f(1) = 6^1 + 5^1 - 10^1 - 1 = 6 + 5 - 10 - 1 = 0.
   \]
   Hence, \(t = 1\) is a solution, corresponding to \(x = \pm 1\).

3. **Behavior for \(t > 1\)**:
   For large \(t\), \(10^t\) dominates, making \(f(t)\) negative (e.g., \(f(2) = -40\)). Thus, no solutions exist for \(t > 1\).

4. **Behavior between \(t = 0\) and \(t = 1\)**:
   The function \(f(t)\) starts at \(0\) when \(t = 0\), reaches a maximum (e.g., \(f(0.5) \approx 0.524\)), then decreases back to \(0\) at \(t = 1\). Since \(f(t) > 0\) in this interval except at the endpoints, there are no additional roots here.

**Conclusion**: The only solutions are \(t = 0\) and \(t = 1\), leading to \(x^2 = 0\) or \(x^2 = 1\). Therefore, the real solutions are:

\[
\boxed{-1, 0, 1}
\]