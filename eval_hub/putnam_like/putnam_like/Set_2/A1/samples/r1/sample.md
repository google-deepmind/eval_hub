

The problem asks whether there exist real numbers \( a \) and \( b \), not both zero, such that \( \det(aA + bB) = 0 \), where \( A \) and \( B \) are invertible square matrices of odd size \( 2n+1 \).

**Key Steps and Reasoning:**

1. **Determinant as a Homogeneous Polynomial:**  
   The determinant \( \det(aA + bB) \) is a homogeneous polynomial of degree \( 2n+1 \) in \( a \) and \( b \). This follows because each entry of \( aA + bB \) is linear in \( a \) and \( b \), and the determinant of an \( (2n+1)\times(2n+1) \) matrix is a degree-\( (2n+1) \) polynomial in its entries.

2. **Properties of Homogeneous Polynomials Over \( \mathbb{R} \):**  
   A non-zero homogeneous polynomial \( P(a, b) \) of odd degree in two variables must have at least one non-trivial real root. This is because when restricted to \( b = 1 \), the polynomial becomes a univariate polynomial of odd degree, which always has a real root. Scaling this root gives a solution in homogeneous coordinates \( (a, b) \neq (0,0) \).

3. **Application to the Problem:**  
   Since \( \det(aA + bB) \) is a non-zero homogeneous polynomial of odd degree \( 2n+1 \), it must vanish for some real \( (a, b) \neq (0,0) \). Thus, there exist real numbers \( a \) and \( b \), not both zero, such that \( \det(aA + bB) = 0 \).

**Conclusion:**  
Yes, such real numbers \( a \) and \( b \) always exist.

```markdown
**Answer**

\boxed{Yes}
```