

To find all symmetric matrices \( A \in M_{n \times n}(\mathbb{R}) \) that satisfy the equation:
\[
A^{4m+1} + A^{4m} + A^{2m+1} + A^{2m} + A + I = 0,
\]
we start by noting that symmetric matrices are diagonalizable with real eigenvalues. Therefore, we consider the eigenvalues \(\lambda\) of \(A\) which must satisfy the scalar equation:
\[
\lambda^{4m+1} + \lambda^{4m} + \lambda^{2m+1} + \lambda^{2m} + \lambda + 1 = 0.
\]

Factoring the polynomial, we get:
\[
(\lambda + 1)(\lambda^{4m} + \lambda^{2m} + 1) = 0.
\]

For real \(\lambda\), the term \(\lambda^{4m} + \lambda^{2m} + 1\) is always positive because \(\lambda^{4m}\) and \(\lambda^{2m}\) are non-negative for any real \(\lambda\). Thus, the only real solution is \(\lambda = -1\).

Since all eigenvalues of \(A\) must be \(-1\), the matrix \(A\) must be similar to \(-I\). However, because \(A\) is symmetric, it can be diagonalized by an orthogonal matrix, leading to \(A = -I\). Verifying, substituting \(A = -I\) into the original equation confirms it satisfies the equation.

Thus, the only solution is:
\[
\boxed{-I}
\]