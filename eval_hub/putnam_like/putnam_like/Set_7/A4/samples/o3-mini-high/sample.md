```markdown
We will show that no real \(2\times2\) matrix \(A\) exists such that
\[
\cos A = \begin{pmatrix} 1 & 2025 \\ 0 & 1 \end{pmatrix},
\]
where
\[
\cos A = \sum_{n=0}^\infty (-1)^n \frac{A^{2n}}{(2n)!}.
\]

1. **Spectral Considerations:**

   Let \(\lambda\) be any eigenvalue of \(A\). By the analytic functional calculus (or the spectral mapping theorem), the eigenvalues of \(\cos A\) are given by \(\cos \lambda\). Since
   \[
   \cos A = \begin{pmatrix} 1 & 2025 \\ 0 & 1 \end{pmatrix},
   \]
   its only eigenvalue is 1 (with algebraic multiplicity 2). Hence, for every eigenvalue \(\lambda\) of \(A\) we must have
   \[
   \cos \lambda = 1.
   \]
   The scalar equation \(\cos \lambda = 1\) has solutions
   \[
   \lambda = 2\pi k, \quad k\in\mathbb{Z}.
   \]

2. **Diagonalizable Case:**

   Suppose first that \(A\) is diagonalizable. Then there exists an invertible matrix \(P\) and integers \(k_1, k_2\) such that
   \[
   A = P \begin{pmatrix} 2\pi k_1 & 0 \\ 0 & 2\pi k_2 \end{pmatrix} P^{-1}.
   \]
   Applying the cosine function, we have
   \[
   \cos A = P \begin{pmatrix} \cos(2\pi k_1) & 0 \\ 0 & \cos(2\pi k_2) \end{pmatrix} P^{-1}
   = P \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} P^{-1} = I.
   \]
   This gives
   \[
   \cos A = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
   \]
   which clearly does not equal \(\begin{pmatrix} 1 & 2025 \\ 0 & 1 \end{pmatrix}\).

3. **Non-diagonalizable Case:**

   Next, suppose \(A\) is not diagonalizable. Then \(A\) must have a single eigenvalue \(\lambda = 2\pi k\) (for some \(k \in \mathbb{Z}\)) and is similar to a Jordan block. That is, 
   \[
   A = 2\pi k\, I + N,
   \]
   where \(N\) is nilpotent with \(N \neq 0\) and \(N^2 = 0\) (since the size of the matrix is 2). For any analytic function \(f\), we have
   \[
   f(2\pi k\, I + N) = f(2\pi k)I + f'(2\pi k)N.
   \]
   In our case, \(f(x) = \cos x\) so that
   \[
   \cos A = \cos(2\pi k)I - \sin(2\pi k)N.
   \]
   Since
   \[
   \cos(2\pi k) = 1 \quad \text{and} \quad \sin(2\pi k) = 0,
   \]
   it follows that
   \[
   \cos A = I - 0\cdot N = I.
   \]
   Again, we get \(\cos A = I\) rather than the given matrix.

4. **Conclusion:**

   In either case, whether \(A\) is diagonalizable or not, we necessarily obtain
   \[
   \cos A = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
   \]
   which does not match
   \[
   \begin{pmatrix} 1 & 2025 \\ 0 & 1 \end{pmatrix}.
   \]
   Therefore, there is no matrix \(A \in \mathbb{M}_{2\times 2}(\mathbb{R})\) that satisfies the given equation.

**Answer:** No, such a matrix \(A\) does not exist.
```