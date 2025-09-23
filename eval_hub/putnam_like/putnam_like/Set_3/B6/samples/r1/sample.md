

To prove that the matrix \( A \) has a non-real eigenvalue, we focus on its determinant and properties of eigenvalues.

**Step-by-Step Explanation:**

1. **Matrix Structure:**
   \( A \) is a \( 2n \times 2n \) matrix with 1s on the subdiagonal and the last column entries:
   \[
   \begin{pmatrix}
   n-1, & n-2, & \ldots, & 0, & 0, & -1, & \ldots, & -(n-1)
   \end{pmatrix}^\top
   \]
   All other entries are zero.

2. **Determinant Calculation:**
   The determinant of \( A \) is computed by expanding along the first row. The first row has only one non-zero entry \( (n-1) \) in the last column. The minor \( M_{1,2n} \) (matrix after removing row 1 and column \( 2n \)) is the identity matrix of size \( (2n-1) \times (2n-1) \), whose determinant is 1. Thus:
   \[
   \det(A) = (n-1) \cdot (-1)^{1+2n} \cdot \det(M_{1,2n}) = -(n-1)
   \]
   For \( n \geq 2 \), \( \det(A) = -(n-1) < 0 \).

3. **Eigenvalues and Determinant:**
   - The determinant of a matrix is the product of its eigenvalues.
   - Real eigenvalues of a real matrix must come in even multiplicities if complex (as complex conjugate pairs).
   - Since \( \det(A) < 0 \), the product of eigenvalues is negative. This implies an odd number of negative real eigenvalues if all were real. However, the total number of eigenvalues (even for \( 2n \times 2n \)) contradicts this parity.

4. **Conclusion:**
   The contradiction arises if all eigenvalues are real. Hence, \( A \) must have at least one pair of non-real eigenvalues.

**Final Answer:**

\boxed{\sigma(A) \setminus \mathbb{R} \neq \emptyset}