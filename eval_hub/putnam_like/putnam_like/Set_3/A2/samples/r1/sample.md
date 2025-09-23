

To solve the problem, we analyze the structure of the function and use induction to establish the required properties.

**Step-by-Step Explanation and Proof:**

1. **Function and Derivatives:**
   Given \( f(x) = \frac{1}{x^k + 1} \), we need to compute the \( n \)-th derivative \( f^{(n)}(x) \) and study \( p(x) = (x^k + 1)^{n+1} f^{(n)}(x) \).

2. **Base Case (\( n = 1 \)):**
   - First derivative: \( f'(x) = -\frac{k x^{k-1}}{(x^k + 1)^2} \)
   - \( p(x) = (x^k + 1)^2 \cdot f'(x) = -k x^{k-1} \)
   - At \( x = k-1 \): \( p(k-1) = -k(k-1)^{k-1} \)
   - This is an integer and divisible by \( k \).

3. **Inductive Step:**
   Assume for \( n \), \( p_n(x) = (x^k + 1)^{n+1} f^{(n)}(x) \) is a polynomial with integer coefficients, each term divisible by \( k \). For \( n + 1 \):
   - Differentiate \( p_n(x)/(x^k + 1)^{n+1} \) to get \( f^{(n+1)}(x) \).
   - Multiply by \( (x^k + 1)^{n+2} \): 
     \[
     p_{n+1}(x) = (x^k + 1)^{n+2} f^{(n+1)}(x)
     \]
   - Differentiation introduces terms with factors of \( k \) from \( \frac{d}{dx}(x^k) = kx^{k-1} \), preserving divisibility by \( k \).

4. **General Argument:**
   - Each derivative of \( f(x) \) introduces a factor of \( k \) via the chain rule.
   - Multiplying by \( (x^k + 1)^{n+1} \) clears denominators, yielding a polynomial \( p(x) \).
   - Coefficients in \( p(x) \) are integers due to derivative operations and polynomial multiplication preserving integrality.
   - Each term in \( p(x) \) contains at least one factor of \( k \), as differentiation introduces \( k \) repeatedly.

5. **Evaluation at \( x = k-1 \):**
   - \( p(k-1) \) is a sum of terms, each an integer multiplied by \( k \).
   - Hence, \( p(k-1) \in \mathbb{Z} \) and \( k \mid p(k-1) \).

**Conclusion:**
By induction, \( p(x) \) is a polynomial with integer coefficients where each term is divisible by \( k \). Evaluating at \( x = k-1 \) yields an integer divisible by \( k \).

```markdown
**Final Answer**

\boxed{p(k-1) \in \mathbb{Z} \text{ and } k \mid p(k-1)}
```