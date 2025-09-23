```markdown
**Solution.**  
Denote by \(A\) the \(2n\times2n\) matrix described in the problem.  We will show that its eigenvalues cannot all be real by computing
\[
\mathrm{tr}(A^2)\;=\;\sum_{i=1}^{2n}\lambda_i^2
\]
and observing it is strictly negative (or gives a contradiction when \(n=2\)).

---

## 1. Structure of \(A\)

Label the rows and columns of \(A\) from \(1\) to \(2n\).  The only nonzero entries of \(A\) are

1.  Ones on the subdiagonal:
   \[
     A_{i+1,i}=1,
     \quad i=1,2,\dots,2n-1,
   \]
2.  The last column (column \(2n\)) has the entries
   \[
     A_{i,2n}=
     \begin{cases}
       n-1,\;n-2,\;\dots,\;1,\;0,\,0,\;-1,\,-2,\;\dots,\,-(n-2),\,-(n-1)
       & i=1,2,\dots,2n,
     \end{cases}
   \]
   in that order.  In particular
   \[
     A_{2n,2n-1}=1,\qquad
     A_{2n-1,2n}=-(n-2).
   \]

All other entries of \(A\) are zero.

---

## 2. Computation of \(\mathrm{tr}(A^2)\)

By definition
\[
(A^2)_{ii} \;=\;\sum_{k=1}^{2n}A_{i,k}\,A_{k,i}.
\]
But each row \(i\) of \(A\) has at most two nonzero entries, namely
\[
  A_{i,i-1}=1\quad(\text{if }i>1),
  \quad
  A_{i,2n}\;=\;\text{(the given last‐column entry)}.
\]
Similarly, each column \(i\) has at most two nonzero spots.  Hence
\[
  (A^2)_{ii}
  = A_{i,i-1}\,A_{i-1,i}\;+\;A_{i,2n}\,A_{2n,i}.
\]
But \(A_{i-1,i}=0\) (there are no superdiagonal ones), and \(A_{2n,i}\neq0\)
only when \(i=2n-1\), in which case \(A_{2n,2n-1}=1\).  Therefore all diagonal
entries of \(A^2\) vanish except
\[
  (A^2)_{2n-1,2n-1}
  = A_{2n-1,2n}\;A_{2n,2n-1}
  =\bigl(-(n-2)\bigr)\cdot1
  =-(n-2).
\]
It follows that
\[
  \mathrm{tr}(A^2)
  =\sum_{i=1}^{2n}(A^2)_{ii}
  =-(n-2).
\]

---

## 3. Concluding the existence of a non‐real eigenvalue

If all the eigenvalues \(\lambda_1,\dots,\lambda_{2n}\) of \(A\) were real, then
\[
  \sum_{i=1}^{2n}\lambda_i^2
  = \mathrm{tr}(A^2)
  =-(n-2).
\]
1.  If \(n\ge3\), the right‐hand side \(-(n-2)\) is strictly negative, which is
    impossible for a sum of real squares.  
2.  If \(n=2\), then \(\mathrm{tr}(A^2)=0\), so real eigenvalues would force
    \(\lambda_i=0\) for all \(i\), contradicting
    \(\mathrm{tr}(A)=\sum_i\lambda_i\neq0\).  

In either case we reach a contradiction, showing that **\(A\) must have at least
one non‐real eigenvalue**.  Hence
\(\sigma(A)\setminus\Bbb R\neq\varnothing\), as desired.  \(\boxed{}\)
```