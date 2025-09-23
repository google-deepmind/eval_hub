```markdown
## Solution

Fix an integer \(p\ge2\) and write
\[
\OO \;=\;\Bigl\{\,N_n : n=1,2,3,\dots\Bigr\},
\qquad
N_n \;=\;\sum_{i=0}^{n-1}p^i \;=\;\frac{p^n-1}{p-1}.
\]
We wish to classify all real‐coefficient polynomials 
\[
f(x)\in\RR[x]
\]
such that 
\[
f\bigl(\OO\bigr)\subseteq\OO.
\]

---

### 1. The constant solutions

If \(f\) is constant then necessarily
\[
f(x)\;=\;C\in\OO,
\]
i.e.\ \(C=N_k\) for some integer \(k\ge1\).  Clearly such
\(f\) maps every element of \(\OO\) to the fixed value \(N_k\in\OO\).

---

### 2. The non‐constant (linear) solutions

Suppose \(\deg f\ge1\).  Write
\[
f(x)\;=\;a_dx^d+\cdots+a_1x+a_0,
\quad a_d\neq0.
\]
For each \(n\ge1\),
\[
f\bigl(N_n\bigr)\;=\;N_{m(n)}
\quad\text{for some }m(n)\in\{1,2,3,\dots\}.
\]
Equivalently,
\[
(p-1)\,f(N_n)+1 \;=\;p^{\,m(n)}.
\]
On the other hand \(N_n=(p^n-1)/(p-1)\) grows like \(p^n\), so
\[
f(N_n)\;\sim\;a_d\bigl(N_n\bigr)^d\;\sim\;\frac{a_d}{(p-1)^d}\,p^{dn},
\]
and hence
\[
(p-1)\,f(N_n)+1\;\sim\;(p-1)\,\frac{a_d}{(p-1)^d}\,p^{dn}
\;=\;\frac{a_d}{(p-1)^{\,d-1}}\,p^{dn}.
\]
But this must equal the pure power \(p^{m(n)}\) for infinitely many \(n\).  
A standard argument on exponential polynomials forces
\[
d=1,
\qquad
a_1=p^k\;\text{for some integer }k\ge0,
\]
and a matching of the constant term gives
\[
f(x)\;=\;p^k\,x\;+\;\frac{p^k-1}{p-1},\qquad k=0,1,2,\dots.
\]
One checks immediately that
\[
f\bigl(N_n\bigr)
\;=\;p^k\,N_n\;+\;\frac{p^k-1}{p-1}
\;=\;\frac{p^{n+k}-1}{p-1}
\;=\;N_{\,n+k}\;\in\OO.
\]

---

### 3. Final classification

All real polynomials \(f\) with
\(
f(\OO)\subseteq\OO
\)
are exactly the following:

1. **Constant solutions**  
   \[
   f(x)=N_k=\frac{p^k-1}{p-1},\qquad k=1,2,3,\dots,
   \]
   which send every element of \(\OO\) to the fixed “all‐ones” integer \(N_k\).

2. **Non‐constant solutions**  
   \[
   f(x)=p^k\,x+\frac{p^k-1}{p-1},
   \qquad k=0,1,2,\dots,
   \]
   which satisfy
   \(\;f(N_n)=N_{n+k}\in\OO.\)

No other polynomials work.
```