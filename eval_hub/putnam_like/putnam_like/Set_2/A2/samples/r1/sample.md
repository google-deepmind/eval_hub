

To solve the problem, we analyze the given integral equation using the Cauchy-Schwarz inequality and consider the continuity of the functions involved.

**Problem Statement:**  
Find all continuous functions \( g: [a, b] \to \mathbb{R} \) that satisfy:
\[
\left(\int_{a}^b g(x)f(x)^2\ dx\right)^2 = \left(\int_{a}^b f(x)^2\ dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\ dx\right).
\]

**Solution:**

1. **Cauchy-Schwarz Inequality Insight:**  
   The given equation resembles the equality condition in the Cauchy-Schwarz inequality. For functions \( u, v \in L^2([a,b]) \), equality \( \left(\int u v \, dx\right)^2 = \left(\int u^2 \, dx\right)\left(\int v^2 \, dx\right) \) holds if and only if \( u \) and \( v \) are linearly dependent (i.e., one is a scalar multiple of the other).

2. **Applying to the Given Equation:**  
   Let \( u(x) = g(x)f(x) \) and \( v(x) = f(x) \). Substituting into the equation:
   \[
   \left(\int_{a}^b u(x)v(x) \, dx\right)^2 = \left(\int_{a}^b v(x)^2 \, dx\right)\left(\int_{a}^b u(x)^2 \, dx\right).
   \]
   By the Cauchy-Schwarz equality condition, \( u(x) = \lambda v(x) \) for some \( \lambda \in \mathbb{R} \). Thus:
   \[
   g(x)f(x) = \lambda f(x) \quad \forall x \in [a,b].
   \]

3. **Implications for \( g(x) \):**  
   - If \( f(x) \neq 0 \), then \( g(x) = \lambda \).
   - If \( f(x) = 0 \), the equation holds regardless of \( g(x) \).

4. **Continuity of \( g \):**  
   Since \( g \) is continuous on \([a, b]\), if \( f \) is not identically zero, the constant \( \lambda \) must hold across the entire interval. Specifically:
   - If \( f \) has any point where it is non-zero, \( g \) must be \( \lambda \) there. By continuity, \( g \) must equal \( \lambda \) at all points where \( f \) is zero to prevent discontinuities.

5. **Special Case:**  
   - If \( f \) is identically zero, the original equation reduces to \( 0 = 0 \), which holds for any continuous \( g \).

**Conclusion:**  
- **If \( f \) is identically zero**, every continuous function \( g \) satisfies the equation.  
- **If \( f \) is not identically zero**, the only solutions are constant functions \( g(x) = \lambda \).

**Final Answer:**

\boxed{
\text{All solutions are constant functions if } f \neq 0 \text{, and any continuous } g \text{ if } f \equiv 0.}
}
Specifically:
- If \( f \equiv 0 \), all continuous \( g \) satisfy the equation.
- If \( f \not\equiv 0 \), the solutions are \( g(x) = \lambda \) for some constant \( \lambda \in \mathbb{R} \).