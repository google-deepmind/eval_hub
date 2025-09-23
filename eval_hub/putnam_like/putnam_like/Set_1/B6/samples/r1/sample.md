

To solve the problem, we analyze the given recursive sequence \( x_{n+1} = \beta x_n + \lfloor \alpha x_n \rfloor \) and aim to find the limit \( \lim_{n \to \infty} \frac{x_n}{(\alpha + \beta)^n} \).

1. **Key Observations**:
   - The sequence can be approximated by \( x_{n+1} \approx (\alpha + \beta)x_n \) for large \( n \), but the floor function introduces a small error term \( e_n = \{ \alpha x_n \} \).
   - The error term \( e_n \) follows the recurrence \( e_{n+1} = \{ (\beta - \alpha) e_n \} \) due to the given conditions \( \beta - \alpha \in (0,1) \) and \( \alpha^2 \in \mathbb{N} \).

2. **Sum of Error Terms**:
   - The sequence \( e_n \) decays exponentially because \( \beta - \alpha \) is a contraction mapping.
   - The sum of the error terms \( S = \sum_{k=0}^{\infty} \frac{e_k}{(\alpha + \beta)^{k+1}} \) converges and is found to be \( S = \frac{\{ \alpha x_0 \}}{2 \alpha} \).

3. **Final Limit Calculation**:
   - Using the relation \( \lim_{n \to \infty} \frac{x_n}{(\alpha + \beta)^n} = x_0 - S \), we substitute the sum \( S \) and simplify the expression.

4. **Result**:
   - The limit is derived to be the average of \( x_0 \) and \( \frac{\lfloor \alpha x_0 \rfloor}{\alpha} \), leading to the final result.

The final answer is:

\[
\boxed{\dfrac{x_0}{2} + \dfrac{\lfloor \alpha x_0 \rfloor}{2 \alpha}}
\]