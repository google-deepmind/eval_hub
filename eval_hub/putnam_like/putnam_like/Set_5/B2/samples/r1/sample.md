

To solve the problem, we start with the given conditions \( A + B = I \) and \( A^4 + B^4 = I \), where \( A \) and \( B \) are invertible \( n \times n \) matrices. We need to compute \( \det(AB) \).

1. **Express \( B \) in terms of \( A \)**:
   \[
   B = I - A
   \]

2. **Substitute \( B = I - A \) into \( A^4 + B^4 = I \)**:
   \[
   A^4 + (I - A)^4 = I
   \]

3. **Expand \( (I - A)^4 \) using the binomial theorem** (noting that \( A \) and \( I \) commute):
   \[
   (I - A)^4 = I - 4A + 6A^2 - 4A^3 + A^4
   \]

4. **Combine terms**:
   \[
   A^4 + I - 4A + 6A^2 - 4A^3 + A^4 = I
   \]
   Simplifying, we get:
   \[
   2A^4 - 4A^3 + 6A^2 - 4A = 0
   \]

5. **Factor out \( 2A \)**:
   \[
   2A(A^3 - 2A^2 + 3A - 2I) = 0
   \]
   Since \( A \) is invertible, \( 2A \neq 0 \), so:
   \[
   A^3 - 2A^2 + 3A - 2I = 0
   \]

6. **Factor the polynomial**:
   \[
   (A - I)(A^2 - A + 2I) = 0
   \]
   As \( A \) is invertible, \( A \neq I \). Thus, the minimal polynomial is:
   \[
   A^2 - A + 2I = 0 \implies A^2 = A - 2I
   \]

7. **Compute \( AB \)** using \( B = I - A \):
   \[
   AB = A(I - A) = A - A^2
   \]
   Substitute \( A^2 = A - 2I \):
   \[
   AB = A - (A - 2I) = 2I
   \]

8. **Determine the determinant**:
   \[
   \det(AB) = \det(2I) = 2^n
   \]

Thus, the determinant of \( AB \) is \(\boxed{2^n}\).