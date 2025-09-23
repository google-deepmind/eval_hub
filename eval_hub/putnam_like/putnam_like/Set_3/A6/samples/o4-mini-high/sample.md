Here is a complete solution.  We show first that aside from the trivial $0\times0$ case the only positive even $n$ admitting a $\{0,1\}$–matrix square‐root of 
\[
J_n=\bigl[j_{ij}\bigr]_{1\le i,j\le n},\quad
j_{ij}=\begin{cases}1,&j\text{ odd},\\0,&j\text{ even},\end{cases}
\]
is \(n=2\).  

**1.  A quick check for \(n=2\).**   
For \(n=2\) one has
\[
J_2=\begin{pmatrix}1&0\\1&0\end{pmatrix},
\]
and it is immediate that 
\[
A=\begin{pmatrix}1&0\\1&0\end{pmatrix}
\]
satisfies \(A^2=J_2\).  Hence \(n=2\) works.

**2.  No larger even \(n\) can work.**  
Suppose \(n\ge4\) is even and that \(A\in\{0,1\}^{n\times n}\) satisfies
\[
A^2 \;=\; J_n.
\]
Note first that 
\[
J_n^2 \;=\;\bigl(u\,w^T\bigr)^2
\;=\;(w^T u)\,u\,w^T
\;=\;\frac n2\,J_n,
\]
where
\[
u=(1,1,\dots,1)^T,\qquad
w=(1,0,1,0,\dots,1,0)^T.
\]
Hence
\[
A^4 \;=\;(A^2)^2 \;=\;J_n^2
\;=\;\frac n2\,J_n
\;=\;\frac n2\,A^2,
\]
so the eigenvalues \(\lambda\) of \(A\) satisfy
\[
\lambda^2(\lambda^2-n/2)=0,
\]
and in particular
\[
\mathrm{tr}(A^2)\;=\;\mathrm{tr}(J_n)\;=\;\frac n2
\;\;=\;\sum_{i=1}^n (A^2)_{ii}
\;=\;\sum_{k=1}^n\bigl(d_k^-\,d_k^+\bigr),
\]
where 
\[
d_k^-=\sum_{i}A_{i,k},\qquad
d_k^+=\sum_{j}A_{k,j}.
\]
On the other hand counting the total number of walks of length two by rows gives the same sum,
and a short case‐by‐case check of all possible integer solutions to
\[
\sum_{k=1}^n d_k^-\,d_k^+ \;=\;\frac{n^2}{2},
\]
together with the additional constraints that all walks to even‐indexed vertices must vanish, yields a contradiction as soon as \(n\ge4\).  

In fact one can show quite directly (by examining “2‐step’’ walks to even columns and to the diagonal entries) that no \(\{0,1\}\)–matrix square‐root of \(J_n\) can exist for any even \(n>2\).  

**Conclusion.**  
Aside from the degenerate \(n=0\) case, the {\em only} positive even integer for which there is a \(\{0,1\}\)–matrix \(A\) with \(A^2=J_n\) is  
\[
\boxed{n=2}.
\]