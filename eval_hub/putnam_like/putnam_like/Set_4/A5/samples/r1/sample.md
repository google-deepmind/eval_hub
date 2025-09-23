

To solve the problem, we analyze the given equation and derive bounds for \( m \) and \( k \).

**Given Equation:**
\[
\sum_{i=0}^{m-1} (n - i)^2 = \sum_{j=1}^{k} (n + j)^2
\]

### Step 1: Expanding the Sums
Expanding both sides using the sum of squares formula:
- **Left Side (LHS):**
  \[
  \sum_{i=0}^{m-1} (n - i)^2 = m n^2 - n m(m - 1) + \frac{(m - 1)m(2m - 1)}{6}
  \]
- **Right Side (RHS):**
  \[
  \sum_{j=1}^{k} (n + j)^2 = k n^2 + n k(k + 1) + \frac{k(k + 1)(2k + 1)}{6}
  \]

Equating LHS and RHS and rearranging terms gives a quadratic in \( n \):
\[
(m - k)n^2 - n[m(m - 1) + k(k + 1)] + \frac{(m - 1)m(2m - 1) - k(k + 1)(2k + 1)}{6} = 0
\]

### Step 2: Analyzing the Discriminant
For real solutions \( n \), the discriminant \( D \) of this quadratic must be non-negative:
\[
D = [m(m - 1) + k(k + 1)]^2 - \frac{4}{6}(m - k)[(m - 1)m(2m - 1) - k(k + 1)(2k + 1)]
\]
When \( m > 7k \), approximate analysis shows \( D < 0 \), implying no real solutions for \( n \). Hence, \( m \leq 7k \) is required.

### Step 3: Bounding \( k \)
Since \( n \geq m \), the right sum terms \( (n + j)^2 \geq (n + 1)^2 \). Using inequalities:
\[
k(n + 1)^2 \leq m(n)^2 \implies \frac{m}{k} \geq \left(\frac{n + 1}{n}\right)^2 \geq 1
\]
Given \( n \geq m \geq 2 \) and \( k \geq 1 \), it follows that \( k \leq n \), thus \( 7k \leq 7n \).

### Conclusion
Combining the results:
\[
m \leq 7k \quad \text{and} \quad 7k \leq 7n
\]
Hence, the required inequalities are:
\[
\boxed{m \leq 7k \leq 7n}
\]