

To solve the problem, we analyze the given power series \( f(x) = \sum_{i=0}^\infty a_i x^i \) with \( a_i \in \{0,1\} \) and use the rationality of \( f\left(\frac{1}{2^n}\right) \) to deduce properties of \( f\left(\frac{2}{q}\right) \) for odd \( q \geq 3 \).

### Key Steps and Proof

1. **Rationality Implies Periodicity**:
   - Given \( f\left(\frac{1}{2^n}\right) \in \mathbb{Q} \), the series \( \sum_{i=0}^\infty \frac{a_i}{2^{ni}} \) represents a rational number in base \( 2^n \).
   - A number is rational if and only if its expansion in any integer base is eventually periodic. Thus, the coefficients \( \{a_i\} \) must be eventually periodic.

2. **Rational Function Representation**:
   - The eventual periodicity of \( \{a_i\} \) implies \( f(x) \) is a rational function, i.e., \( f(x) = \frac{P(x)}{Q(x)} \) where \( P(x), Q(x) \in \mathbb{Z}[x] \) are polynomials with integer coefficients.

3. **Evaluating at \( x = \frac{2}{q} \)**:
   - Substitute \( x = \frac{2}{q} \):  
     \[
     f\left(\frac{2}{q}\right) = \frac{P\left(\frac{2}{q}\right)}{Q\left(\frac{2}{q}\right)}.
     \]
   - Let \( d = \max(\deg P, \deg Q) \). Multiply numerator and denominator by \( q^d \) to clear denominators:
     \[
     f\left(\frac{2}{q}\right) = \frac{q^d P\left(\frac{2}{q}\right)}{q^d Q\left(\frac{2}{q}\right)}.
     \]
     Both numerator and denominator become integers, hence \( f\left(\frac{2}{q}\right) \in \mathbb{Q} \).

4. **Denominator Analysis**:
   - The denominator \( q^d Q\left(\frac{2}{q}\right) \) is an integer. Since \( q \) is odd, all terms in \( Q\left(\frac{2}{q}\right) \) (when expanded) have denominators that are powers of \( q \), which remain odd after multiplication by \( q^d \).
   - Reducing the fraction \( \frac{\alpha}{\beta} \), the denominator \( \beta \) divides \( q^d Q\left(\frac{2}{q}\right) \). As \( q \) is odd and no factors of 2 are introduced by \( Q(x) \), \( \beta \) must be odd.

### Conclusion

For every odd \( q \geq 3 \), \( f\left(\frac{2}{q}\right) \) is rational. When expressed in lowest terms \( \frac{\alpha}{\beta} \), the denominator \( \beta \) is odd. This follows from the periodicity of \( \{a_i\} \) induced by the rationality of \( f\left(\frac{1}{2^n}\right) \) and the structure of the rational function evaluation at \( \frac{2}{q} \).

```markdown
\boxed{f\left(\frac{2}{q}\right) \in \mathbb{Q} \text{ and } \beta \text{ is odd for } f\left(\frac{2}{q}\right) = \frac{\alpha}{\beta} \text{ with } \gcd(\alpha, \beta) = 1.}
```