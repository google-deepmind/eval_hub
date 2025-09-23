

To prove that $\prod_{i<j} (e_i+e_j)^2 = 1$ where $n$ is an odd number and $e_1 = 1, e_2, \ldots, e_n$ are the $n$-th roots of unity, we can use properties of roots of unity and polynomials.

1. **Roots of Unity and Polynomial**: The roots of unity $e_1, e_2, \ldots, e_n$ satisfy the polynomial equation $x^n - 1 = 0$. The product of all roots of unity is $(-1)^{n+1}$ multiplied by the constant term of the polynomial. For $x^n - 1$, the product of all roots is $1$ since $n$ is odd.

2. **Product of Sums**: Consider the product $\prod_{i \neq j} (e_i + e_j)$. For each root $e_i$, the product $\prod_{j \neq i} (e_i + e_j)$ can be related to the polynomial $Q_i(x) = \prod_{j \neq i} (x - e_j)$. Evaluating $Q_i(x)$ at $x = -e_i$ gives:
   \[
   Q_i(-e_i) = \prod_{j \neq i} (-e_i - e_j) = (-1)^{n-1} \prod_{j \neq i} (e_i + e_j)
   \]
   Since $n$ is odd, $(-1)^{n-1} = 1$. The polynomial $Q_i(x)$ is also the derivative of $x^n - 1$ evaluated at $x = e_i$, leading to $Q_i(-e_i) = \frac{1}{e_i}$.

3. **Simplifying the Product**: Thus, $\prod_{j \neq i} (e_i + e_j) = \frac{1}{e_i}$. Multiplying this over all $i$ gives:
   \[
   \prod_{i=1}^n \prod_{j \neq i} (e_i + e_j) = \prod_{i=1}^n \frac{1}{e_i} = \frac{1}{\prod_{i=1}^n e_i}
   \]
   Since the product of all roots $\prod_{i=1}^n e_i = 1$, we have:
   \[
   \prod_{i \neq j} (e_i + e_j) = 1
   \]

4. **Final Step**: The original product $\prod_{i<j} (e_i + e_j)^2$ is the square of the product over all pairs $i < j$:
   \[
   \prod_{i<j} (e_i + e_j)^2 = \left( \prod_{i<j} (e_i + e_j) \right)^2 = \left( \sqrt{\prod_{i \neq j} (e_i + e_j)} \right)^2 = 1
   \]

Thus, the product $\prod_{i<j} (e_i + e_j)^2$ is indeed equal to $1$.

\[
\boxed{1}
\]