

To solve the problem, we need to determine the pairs \((\alpha, \beta)\) such that \(\lim_{n \to \infty} b_n = \beta\) where \(b_n = \frac{\sum_{k=1}^n a_k}{n^\alpha}\). The sequence \((a_n)\) is structured in blocks where each block \(m\) consists of the numbers from 1 to \(m^2\). 

### Key Steps:

1. **Understanding the Sequence Structure**:
   - Each block \(m\) has \(m^2\) terms.
   - The total number of terms up to block \(M\) is approximately \(\frac{M^3}{3}\) for large \(M\).

2. **Sum of the Sequence**:
   - The sum of the first \(M\) blocks is approximately \(\sum_{m=1}^M \sum_{k=1}^{m^2} k \approx \sum_{m=1}^M \frac{m^4}{2}\).
   - Using the approximation for the sum of fourth powers, \(\sum_{m=1}^M m^4 \approx \frac{M^5}{5}\), the sum of the first \(M\) blocks is \(\frac{M^5}{10}\).

3. **Relating \(M\) to \(n\)**:
   - For large \(n\), the number of terms \(n\) is related to \(M\) by \(M \approx (3n)^{1/3}\).
   - Substituting \(M \approx (3n)^{1/3}\) into the sum, we get \(\sum_{k=1}^n a_k \approx \frac{(3n)^{5/3}}{10}\).

4. **Determining \(\alpha\) and \(\beta\)**:
   - The sum \(\sum_{k=1}^n a_k\) grows as \(n^{5/3}\).
   - For the limit \(b_n = \frac{\sum_{k=1}^n a_k}{n^\alpha}\) to be a positive real number \(\beta\), the exponent \(\alpha\) must be \(\frac{5}{3}\).
   - The constant \(\beta\) is derived from the coefficient of the leading term, resulting in \(\beta = \frac{3^{5/3}}{10}\).

### Final Answer:
The pairs \((\alpha, \beta)\) of positive real numbers such that \(\lim_{n \to \infty} b_n = \beta\) are:

\[
\boxed{\left( \frac{5}{3}, \frac{3^{5/3}}{10} \right)}
\]