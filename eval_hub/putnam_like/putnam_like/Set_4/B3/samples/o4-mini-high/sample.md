```markdown
**Solution.**

Define the function
\[
S(a_1,\dots,a_n)\;=\;\sum_{i=1}^n\Bigl(a_i+\tfrac1{a_i}\Bigr)^p,
\]
where \(a_i>0\) and \(\sum_{i=1}^n a_i=1\).  We will show
\[
S(a_1,\dots,a_n)\;\ge\;n\Bigl(\tfrac1n+n\Bigr)^p
\;=\;n^{\,1-p}\,(n^2+1)^p,
\]
with equality precisely when \(a_1=\cdots=a_n=1/n\).

---

### 1. A two–variable “smoothing’’ lemma

Fix two indices \(i\neq j\), set
\[
A\;=\;a_i+a_j\;\le1,
\]
and for \(0<x<A\) define
\[
\phi(x)\;=\;\Bigl(x+\tfrac1{x}\Bigr)^p,
\qquad
F(x)\;=\;\phi(x)+\phi(A-x).
\]
We claim \(F\) is **strictly convex** on \((0,A)\).  Indeed, one computes
\[
F''(x)
=\phi''(x)+\phi''(A-x)
>0
\quad\bigl(\forall\,x\in(0,A)\bigr),
\]
because a direct check shows \(\phi''(y)>0\) for all \(y>0\) when \(p>0\).
Since
\[
F'(x)\Big|_{x=A/2}
=\phi'(A/2)-\phi'(A/2)=0,
\]
the unique minimizer of \(F\) on \((0,A)\) is \(x=A/2\).  Hence
\[
\phi(a_i)+\phi(a_j)
=F(a_i)
\;\ge\;
F\bigl(A/2\bigr)
=\;2\,\phi\!\Bigl(\tfrac{a_i+a_j}2\Bigr).
\]
In other words, replacing the pair \(\{a_i,a_j\}\) by the more equal pair
\(\{\tfrac{A}2,\tfrac{A}2\}\) **decreases** the partial sum
\(\phi(a_i)+\phi(a_j)\).

---

### 2. Conclusion by successive smoothing

Starting from an arbitrary positive \((a_1,\dots,a_n)\) with sum 1,
repeat the above “smoothing’’ step on any pair of unequal coordinates.
Each step lowers (or leaves unchanged) the total
\(\sum_{i=1}^n\phi(a_i)\), and the only way to make **all** coordinates
equal under the constraint \(a_1+\cdots+a_n=1\) is to end up at
\[
a_1=\cdots=a_n=\frac1n.
\]
At this uniform point,
\[
S_{\min}
\;=\;
n\,\phi\!\bigl(\tfrac1n\bigr)
\;=\;
n\Bigl(\tfrac1n+n\Bigr)^p
\;=\;
n^{\,1-p}\,(n^2+1)^p.
\]
Thus for every admissible \((a_1,\dots,a_n)\),
\[
\sum_{i=1}^n\Bigl(a_i+\tfrac1{a_i}\Bigr)^p
\;\ge\;
n^{\,1-p}\,(n^2+1)^p,
\]
with equality exactly when \(a_i=1/n\) for all \(i\).  This completes
the proof.
```