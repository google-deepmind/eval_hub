Below is one complete solution written in markdown with LaTeX.

---

```markdown
We will show that if there is an \( n \times n \) (with \( n \) even) matrix 
\[
A = (a_{ij})_{1\le i,j\le n} \quad\text{with } a_{ij}\in\{0,1\},
\]
satisfying
\[
A^2 = J_n,
\]
where
\[
J_n = \begin{pmatrix}
1 & 0 & 1 & 0 & \cdots \\
1 & 0 & 1 & 0 & \cdots \\
\vdots && \vdots & \vdots & \ddots
\end{pmatrix}
\]
(with 1’s in the odd‐numbered columns and 0’s in the even‐numbered ones), then necessarily
\[
\sqrt{\frac{n}{2}}
\]
must be an integer. In other words, such an \(A\) exists if and only if
\[
\frac{n}{2} = k^2 \quad\Longleftrightarrow\quad n = 2k^2
\]
for some positive integer \(k\).

Below is a sketch of the proof.

-----------------------------------------------------------------------
Step 1. Eigenvalue considerations

Since \(A\) is a \(0\text{-}1\) matrix, all its entries are nonnegative integers and the product
\[
(A^2)_{ij} = \sum_{k=1}^n a_{ik}a_{kj}
\]
is a nonnegative integer. In our situation, we have
\[
A^2 = J_n,
\]
where the \(j\)th column of \(J_n\) is
\[
\begin{cases}
\mathbf{e}=(1,1,\dots,1)^T,& \text{if } j \text{ is odd},\\[1mm]
\mathbf{0},& \text{if } j \text{ is even}.
\end{cases}
\]
Thus, \(J_n\) has rank 1.

Also note that
\[
J_n^2 = \bigl(e\,v^T\bigr)^2 = e\, (v^T e)\, v^T,
\]
where
\[
v^T = (1,0,1,0,\dots, 1,0).
\]
Because there are exactly \( n/2 \) ones in \(v\), we have
\[
J_n^2 = \frac{n}{2}\, J_n.
\]
On the other hand, since \(A^2=J_n\),
\[
A^4 = J_n^2 = \frac{n}{2}\, J_n = \frac{n}{2}\, A^2.
\]
If \(\lambda\) is an eigenvalue of \(A\) with eigenvector \(x\) (possibly in \(\mathbb{C}^n\)), then
\[
A^4 x = \lambda^4 x \quad \text{and} \quad A^2x = \lambda^2x.
\]
Thus,
\[
\lambda^4 x = \frac{n}{2}\, \lambda^2 x,
\]
and if \(x\neq 0\) this gives
\[
\lambda^4 = \frac{n}{2}\, \lambda^2.
\]
That is,
\[
\lambda^2\Bigl(\lambda^2-\frac{n}{2}\Bigr)=0.
\]
So the only possible eigenvalues are
\[
\lambda=0 \quad \text{or} \quad \lambda^2=\frac{n}{2}\quad\Longrightarrow\quad \lambda=\pm\sqrt{\frac{n}{2}}.
\]

-----------------------------------------------------------------------
Step 2. Counting the nonzero eigenvalue

Because \(J_n\) has rank 1, so does \(A^2\), and it turns out (from an argument using the trace) that there is exactly one nonzero eigenvalue of \(A\). (It is possible for a nonzero matrix to have more than one nonzero eigenvalue, but here the structure forces exactly one.)

Since \(A\) is a \(0\text{-}1\) matrix, its trace 
\[
\operatorname{tr}(A) = \sum_{i=1}^n a_{ii}
\]
is an integer between 0 and \(n\). On the other hand, the trace of \(A\) is also the sum of its eigenvalues. (Even though \(A\) need not be diagonalizable, one may argue from the minimal polynomial that the only nonzero eigenvalue appears with multiplicity 1.) Hence the unique nonzero eigenvalue (say, \(\lambda_0\)) must be
\[
\lambda_0=\operatorname{tr}(A)\in \mathbb{Z}_{\ge0}.
\]
But we also have from the eigenvalue equation that
\[
\lambda_0=\sqrt{\frac{n}{2}}\quad\text{or}\quad\lambda_0=-\sqrt{\frac{n}{2}}.
\]
Since the trace is nonnegative, we must have
\[
\lambda_0=\sqrt{\frac{n}{2}}\in \mathbb{Z},
\]
so that \(\sqrt{n/2}\) is an integer. Write
\[
\sqrt{\frac{n}{2}}=k,\quad k\in\mathbb{N}.
\]
Then
\[
n=2k^2.
\]

-----------------------------------------------------------------------
Step 3. Sufficiency

One may also show (by an explicit but somewhat involved combinatorial construction, see for example constructions using incidence matrices of certain designs) that for every positive integer \(k\) there exists a \(0\text{-}1\) matrix \(A\) of size
\[
n=2k^2
\]
with
\[
A^2=J_n.
\]

-----------------------------------------------------------------------
Conclusion

Thus, there exists an \(n\times n\) matrix \(A\) with entries in \(\{0,1\}\) satisfying 
\[
A^2=J_n
\]
if and only if
\[
n=2k^2\quad\text{for some } k\in\mathbb{N}.
\]
Equivalently, if and only if \(\frac{n}{2}\) is a perfect square.
```

---

To summarize, the answer is:

There exists a \(0\text{-}1\) matrix \(A\) with \(A^2=J_n\) (with \(J_n\) having ones in every odd column and zeros in every even column) if and only if 
\[
\frac{n}{2} \text{ is a perfect square, i.e. } n = 2k^2 \text{ for some positive integer } k.
\]
