```markdown
We are given a symmetric matrix \( A \in M_{n\times n}(\mathbb{R}) \) satisfying
\[
A^{4m+1} + A^{4m} + A^{2m+1} + A^{2m} + A + I = 0,
\]
where \( m \in \mathbb{N} \) and \( I \) is the \( n \times n \) identity matrix.

Since \( A \) is symmetric, it is diagonalizable with real eigenvalues. Let \( \lambda \) be an eigenvalue of \( A \) and \( v \) a corresponding eigenvector. Then, multiplying the above equation by \( v \) gives:
\[
\lambda^{4m+1} v + \lambda^{4m} v + \lambda^{2m+1} v + \lambda^{2m} v + \lambda v + v = 0.
\]
Since \( v \neq 0 \), it follows that
\[
\lambda^{4m+1} + \lambda^{4m} + \lambda^{2m+1} + \lambda^{2m} + \lambda + 1 = 0.
\]

Notice that we can factor the polynomial as follows:
\[
\lambda^{4m+1} + \lambda^{4m} + \lambda^{2m+1} + \lambda^{2m} + \lambda + 1 = (\lambda+1)(\lambda^{4m} + \lambda^{2m} + 1).
\]

For any real number \( \lambda \), the terms \( \lambda^{4m} \) and \( \lambda^{2m} \) are nonnegative (since \(4m\) and \(2m\) are even exponents). Hence,
\[
\lambda^{4m} + \lambda^{2m} + 1 \ge 1,
\]
and this factor can never be zero.

Thus, the only solution to the equation is
\[
\lambda+1=0 \quad \Longrightarrow \quad \lambda=-1.
\]

Since every eigenvalue of \( A \) must equal \(-1\) and \( A \) is diagonalizable, we conclude that
\[
A = -I.
\]

Therefore, the only symmetric matrix \( A \) that satisfies
\[
A^{4m+1}+A^{4m}+A^{2m+1}+A^{2m}+A+I=0
\]
is
\[
\boxed{A = -I.}
\]
```