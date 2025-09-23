

To determine whether there exists a real matrix \( A \in \mathbb{M}_{2 \times 2}(\mathbb{R}) \) such that 

\[
\cos A = \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix},
\]

we analyze the properties of the matrix cosine function and the given matrix.

### Key Observations:
1. **Eigenvalues of \( \cos A \):**  
   The given matrix is upper triangular with eigenvalues \( 1 \). For any matrix \( A \), the eigenvalues of \( \cos A \) are \( \cos \lambda \), where \( \lambda \) are the eigenvalues of \( A \). Thus, the eigenvalues of \( A \) must satisfy \( \cos \lambda = 1 \), implying \( \lambda = 2\pi k \) for integers \( k \).

2. **Structure of \( \cos A \):**  
   If \( A \) is upper triangular with eigenvalues \( 2\pi k \) and \( 2\pi m \), then \( \cos A \) is also upper triangular. The diagonal entries of \( \cos A \) are \( \cos(2\pi k) = 1 \) and \( \cos(2\pi m) = 1 \). However, the off-diagonal entry of \( \cos A \) depends on the structure of \( A \):
   - **Case 1 (\( k \neq m \)):**  
     The upper-right entry of \( \cos A \) is \( \frac{b(\cos(2\pi k) - \cos(2\pi m))}{2\pi(k - m)} = 0 \), contradicting the requirement of \( 2025 \).
   - **Case 2 (\( k = m \)):**  
     If \( A \) is a Jordan block \( \begin{bmatrix} 2\pi k & b \\ 0 & 2\pi k \end{bmatrix} \), then \( \cos A = I - \sin(2\pi k)N \) where \( N \) is nilpotent. Since \( \sin(2\pi k) = 0 \), \( \cos A = I \), again failing to match the required upper-right entry.

3. **Nilpotent Component Analysis:**  
   The given matrix \( C = I + N \) (where \( N^2 = 0 \)) cannot be expressed as \( \cos A \) for any real \( A \). If \( A \) were such that \( A^2 \propto N \), the series expansion of \( \cos A \) would still yield \( \cos A = I \), as higher powers vanish, leaving no contribution to the upper-right entry.

4. **Double-Angle Identity:**  
   Applying \( \cos(2A) = 2\cos^2 A - I \) leads to \( \cos(2A) = \begin{bmatrix} 1 & 8100 \\ 0 & 1 \end{bmatrix} \). Repeating the analysis recursively shows the same contradiction: the required off-diagonal term cannot arise from \( \sin(4\pi k) = 0 \).

### Conclusion:
The matrix \( \cos A \) must have zero off-diagonal entries if \( A \) has eigenvalues \( 2\pi k \), as the sine terms vanish. The non-zero entry \( 2025 \) in the given matrix is incompatible with the properties of the matrix cosine function. Therefore, **no such real matrix \( A \) exists**.

**Answer**
\boxed{\text{No}}