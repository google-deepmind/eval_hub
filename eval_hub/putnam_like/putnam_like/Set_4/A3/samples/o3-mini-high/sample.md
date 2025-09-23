```markdown
We will show that the “if and only if” statement fails over the finite field. In fact, one may prove that

  “If all eigenvalues of a symmetric matrix A (with eigenvalues in ℱₚ) are positive (i.e. squares in ℱₚ), then every leading principal minor of A is positive (a square in ℱₚ),”

but the converse implication is false.

Below we explain both directions.

---

Step 1. Suppose that all eigenvalues of A are positive in ℱₚ.

Since A is symmetric and (by assumption) its characteristic polynomial splits over ℱₚ, a spectral theorem applies. (Note that by “positive” we mean that for every eigenvalue λ there is some y in ℱₚ for which λ = y².) Thus, there exists an invertible matrix P such that

\[
A = P\, \mathrm{diag}(\lambda_1,\lambda_2,\dots,\lambda_n)\,P^T,
\]

with each \(\lambda_i\) a square in ℱₚ. One may then show (using for example an LDLᵀ or Cholesky factorization, which is available when all “pivot” values are squares) that every leading principal submatrix of A is congruent to a diagonal matrix whose diagonal entries are products of the square pivots. In particular, the k-th leading principal minor is a product of squares so that

\[
\Delta_k = \det\bigl(A_{[1:k,1:k]}\bigr)
\]

is also a square in ℱₚ. (This is the analogue of Sylvester’s criterion for positive‐definiteness in ℝ.)

---

Step 2. Now we show that the reverse implication does not hold. In other words, it is not true in general that if every leading principal minor of A is positive (a square in ℱₚ), then all the eigenvalues of A are positive.

For example, let us work in the field \(\F_7\) (here the nonzero squares are \(1,2,\) and \(4\); remember that in any field \(\F_p\) with \(p\) odd, exactly half of the nonzero elements are squares). Consider the symmetric matrix

\[
A = \begin{pmatrix} 1 & 1 \\[1mm] 1 & 3 \end{pmatrix} \in M_2(\F_7).
\]

We first check the leading principal minors:
• The 1×1 minor is \(a_{11} = 1\), which is a square in \(\F_7\) (since \(1=1^2\)).

• The 2×2 minor is the determinant
\[
\det A = (1)(3) - (1)(1) = 2.
\]
Since \(2 = 3^2\) in \(\F_7\) (indeed, \(3^2 = 9 \equiv 2 \pmod{7}\) ), the determinant is also a square in \(\F_7\).

Thus, all the leading principal minors of A are positive.

Now we compute the eigenvalues of A. Its characteristic polynomial is
\[
\lambda^2 - (1+3)\lambda + (1\cdot3-1\cdot1) = \lambda^2 - 4\lambda + 2.
\]
The discriminant is
\[
\Delta = 4^2 - 4\cdot2 = 16 - 8 = 8 \equiv 1\pmod{7}.
\]
Thus the eigenvalues are
\[
\lambda = \frac{4\pm 1}{2}.
\]
Since 2 is invertible in \(\F_7\) (its inverse is 4 because \(2\cdot 4=8\equiv 1 \pmod{7}\) ) these eigenvalues are:
\[
\lambda_1 = \frac{5}{2} = 5\cdot 4=20\equiv 6 \pmod{7}, \quad \lambda_2 = \frac{3}{2} = 3\cdot 4=12\equiv 5 \pmod{7}.
\]
In \(\F_7\) the squares are \(\{1,2,4\}\); hence neither 5 nor 6 is a square in \(\F_7\). Thus, even though all leading principal minors of A are positive, its eigenvalues are not all positive.

---

Conclusion

The counter‐example above shows that while “all eigenvalues are positive ⟹ all leading principal minors are positive” still holds, the converse (i.e. “all leading principal minors are positive ⟹ all eigenvalues are positive”) does not hold in \(\F_p\) when positivity is defined by “being a square.”

So the answer to the problem is: No, the equivalence fails; the implication from “all leading principal minors are positive” to “all eigenvalues are positive” is false.
```