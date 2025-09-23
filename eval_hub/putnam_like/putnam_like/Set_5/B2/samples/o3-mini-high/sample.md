```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

We are given that \(A\) and \(B\) are invertible \(n \times n\) matrices satisfying:
\[
A + B = I \quad \text{and} \quad A^4 + B^4 = I,
\]
where \(I\) is the identity matrix. We wish to compute \(\det(AB)\).

\textbf{Step 1. Express \(B\) in terms of \(A\):}

Since
\[
A + B = I,
\]
we have 
\[
B = I - A.
\]

\textbf{Step 2. Substitute \(B\) into the second equation:}

Substitute \(B = I-A\) into
\[
A^4 + B^4 = I \quad \Longrightarrow \quad A^4 + (I-A)^4 = I.
\]
Expanding \((I-A)^4\) using the binomial theorem:
\[
(I-A)^4 = I - 4A + 6A^2 - 4A^3 + A^4.
\]
Thus,
\[
A^4 + \left( I - 4A + 6A^2 - 4A^3 + A^4 \right) = I.
\]
Combine like terms:
\[
2A^4 - 4A^3 + 6A^2 - 4A + I = I.
\]
Subtract \(I\) from both sides:
\[
2A^4 - 4A^3 + 6A^2 - 4A = 0.
\]
Factoring out \(2A\) (note that \(A\) is invertible, so we can safely divide by it later):
\[
2A\left( A^3 - 2A^2 + 3A - 2I \right) = 0.
\]
Since \(A\) is invertible, we multiply on the left by \(A^{-1}\) to obtain:
\[
A^3 - 2A^2 + 3A - 2I = 0.
\]

\textbf{Step 3. Determine the eigenvalues of \(A\):}

Let \(\lambda\) be an eigenvalue of \(A\). Then \(\lambda\) satisfies the scalar equation:
\[
\lambda^3 - 2\lambda^2 + 3\lambda - 2 = 0.
\]
Notice that \(\lambda = 1\) is a solution since:
\[
1^3 - 2\cdot 1^2 + 3\cdot 1 - 2 = 1 - 2 + 3 - 2 = 0.
\]
Thus, factor out \((\lambda - 1)\):
\[
\lambda^3 - 2\lambda^2 + 3\lambda - 2 = (\lambda - 1)(\lambda^2 - \lambda + 2) = 0.
\]
Hence, the eigenvalues satisfy either:
\[
\lambda - 1 = 0 \quad \text{or} \quad \lambda^2 - \lambda + 2 = 0.
\]

However, if \(\lambda = 1\) is an eigenvalue of \(A\), then for the corresponding eigenvector \(v\) we have
\[
Bv = (I-A)v = v - Av = (1-\lambda)v = 0,
\]
which contradicts the invertibility of \(B\). Therefore, \(\lambda = 1\) is not allowed. 

Thus every eigenvalue of \(A\) must satisfy:
\[
\lambda^2 - \lambda + 2 = 0.
\]
The solutions are:
\[
\lambda = \frac{1 \pm i\sqrt{7}}{2}.
\]

\textbf{Step 4. Compute the eigenvalues of \(AB\):}

Since 
\[
B = I-A,
\]
if \(v\) is an eigenvector of \(A\) corresponding to eigenvalue \(\lambda\), then:
\[
Bv = (I-A)v = (1-\lambda)v.
\]
Hence, 
\[
ABv = A(Bv) = A[(1-\lambda)v] = (1-\lambda)Av = \lambda(1-\lambda)v.
\]
In other words, the eigenvalues of \(AB\) are given by:
\[
\mu = \lambda(1-\lambda).
\]
Substituting \(\lambda = \frac{1 \pm i\sqrt{7}}{2}\), we compute:
\[
\lambda(1-\lambda) = \left(\frac{1 \pm i\sqrt{7}}{2}\right)
\left(1 - \frac{1 \pm i\sqrt{7}}{2}\right)
= \left(\frac{1 \pm i\sqrt{7}}{2}\right)
\left(\frac{1 \mp i\sqrt{7}}{2}\right).
\]
Simplify using the difference of squares:
\[
\left(\frac{1 \pm i\sqrt{7}}{2}\right)
\left(\frac{1 \mp i\sqrt{7}}{2}\right)
= \frac{1^2 + (\sqrt{7})^2}{4} = \frac{1 + 7}{4} = \frac{8}{4} = 2.
\]
Thus, every eigenvalue \(\mu\) of \(AB\) is equal to 2.

\textbf{Step 5. Compute the determinant:}

Since \(\det(AB)\) is the product of the eigenvalues of \(AB\) (counting algebraic multiplicity) and there are \(n\) of them, we have:
\[
\det(AB) = 2^n.
\]

\[
\boxed{\det(AB) = 2^n.}
\]

\end{document}
```