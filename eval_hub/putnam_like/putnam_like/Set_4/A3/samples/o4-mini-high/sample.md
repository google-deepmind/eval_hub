Here is a short answer with a counter‐example showing that over \(\F_p\) (with \(p\) odd) Sylvester’s “positive‐definite ⇔ all leading principal minors positive” fails.  In fact **both** directions can break down.

---

## 1. “Eigenvalues all squares ⇒ all leading principal minors are squares” can fail

Take \(p=3\) and
\[
A=\begin{pmatrix}2&1\\1&2\end{pmatrix}
\in\F_3^{2\times2}\,. 
\]
Its characteristic polynomial is
\[
\chi_A(x)
=\det\bigl(xI - A\bigr)
=\det\begin{pmatrix}x-2&-1\\-1&x-2\end{pmatrix}
=(x-2)^2 -1
=x^2 -4x +3
\equiv x^2+2x\pmod3.
\]
Hence 
\[
\chi_A(x)=x\,(x+2)
\quad\Longrightarrow\quad
\Spec(A)=\{0,1\}
\]
and both eigenvalues \(0,1\) are squares in \(\F_3\).  However the \(1\times1\) leading principal minor is
\[
\det\bigl([2]\bigr)=2,
\]
and \(2\) is not a square in \(\F_3\).  Thus
\[
\text{“all eigenvalues are squares”}
\;\not\Longrightarrow\;
\text{“all leading principal minors are squares”}\,. 
\]

---

## 2. “All leading principal minors are squares ⇒ all eigenvalues are squares” can also fail

Again in \(\F_3\) take
\[
B=\begin{pmatrix}0&0\\0&2\end{pmatrix}.
\]
Then the \(1\times1\) minor is \(0\), the \(2\times2\) minor is 
\(\det B=0\), and both \(0\) and \(0\) are squares in \(\F_3\).  So **all** leading principal minors of \(B\) are squares.  On the other hand
\[
\chi_B(x)=x^2 -2x = x\,(x-2),
\]
so \(\Spec(B)=\{0,2\}\), and \(2\) is not a square in \(\F_3\).  Hence
\[
\text{“all leading principal minors are squares”}
\;\not\Longrightarrow\;
\text{“all eigenvalues are squares”}\,. 
\]

---

### Conclusion

Over a finite field \(\F_p\), \(p>2\), the usual Sylvester criterion breaks down.  Neither
\[
\bigl[\;\eig(A)\subset(\F_p)^{\times2}\bigr]\;
\Longrightarrow\;
\bigl[\text{all leading principal minors}\in(\F_p)^{\times2}\bigr]
\]
nor its converse holds in general. 

In particular, one must **not** try to carry Sylvester’s test over to \(\F_p\) by simply replacing “\(>0\)” by “is a square.”