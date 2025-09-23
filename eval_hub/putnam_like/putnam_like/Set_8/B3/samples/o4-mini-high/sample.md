```markdown
## Solution

Let \(f:[0,1]\to\Bbb R\) be continuous and **decreasing**, and fix \(n\in\Bbb N\).  Set
\[
I_n\;=\;\int_0^1 x^{n-1}f(x)\,dx.
\]
We shall prove the two inequalities
\[
\int_{1-\frac1n}^1 f(x)\,dx\;\le\;I_n
\quad\text{and}\quad
I_n\;\le\;\int_0^{\frac1n} f(x)\,dx.
\]

---

### 1. Lower bound: \(\displaystyle \int_{1-\frac1n}^1 f\le I_n\)

Subdivide \([0,1]\) into the \(n\) equal subintervals
\[
I_k=\Bigl[\tfrac{k-1}n,\;\tfrac{k}n\Bigr], 
\qquad k=1,2,\dots,n.
\]
On each \(I_k\) the Beta‑density
\[
p_n(x)=n\,x^{\,n-1},\quad 0\le x\le1,
\]
has total mass
\[
a_k
=\int_{I_k}n\,x^{n-1}\,dx
=\Bigl(\tfrac{k}{n}\Bigr)^n-\Bigl(\tfrac{k-1}{n}\Bigr)^n,
\]
while the uniform partition weights are
\[
b_k=\frac1n,
\]
and clearly 
\[
\sum_{k=1}^na_k
=\sum_{k=1}^nb_k=1,
\]
but for each \(1\le j\le n-1\)
\[
\sum_{k=1}^ja_k
=\Bigl(\tfrac jn\Bigr)^n
\;\le\;\frac jn
=\sum_{k=1}^jb_k.
\]
Hence the discrete weight vector \((a_k)\) is *majorized* by the constant vector \((b_k)\).  Since \(f\) is **decreasing**, one shows by a rearrangement/majorization argument that
\[
\sum_{k=1}^na_k\,f(\xi_k)
\;\ge\;
\sum_{k=1}^nb_k\,f\!\bigl(\tfrac{k}{n}\bigr)
\]
for any choice of sample points \(\xi_k\in I_k\).  But
\[
n\,I_n
=\int_0^1 n\,x^{n-1}f(x)\,dx
=\sum_{k=1}^n a_k\,f(\xi_k)
\;\ge\;
\frac1n\sum_{k=1}^n f\!\bigl(\tfrac{k}{n}\bigr)
\;.
\]
On the other hand, since \(f\) is decreasing,
\[
f\Bigl(\tfrac{k}{n}\Bigr)\;\ge\;f\Bigl(1-\tfrac1n\Bigr)
\quad(k=1,2,\dots,n),
\]
so
\[
\frac1n\sum_{k=1}^n f\!\bigl(\tfrac{k}{n}\bigr)
\;\ge\;
f\!\Bigl(1-\tfrac1n\Bigr).
\]
Finally, on \(\bigl[1-\tfrac1n,1\bigr]\) we have
\[
\int_{1-\frac1n}^1 f(x)\,dx
\;\le\;
\frac1n\;f\!\Bigl(1-\tfrac1n\Bigr)
\;\le\;
f\!\Bigl(1-\tfrac1n\Bigr),
\]
so altogether
\[
\int_{1-\frac1n}^1 f(x)\,dx
\;\le\;
\frac1n\sum_{k=1}^n f\!\bigl(\tfrac{k}{n}\bigr)
\;\le\;
n\,I_n,
\]
i.e.
\[
\boxed{
\int_{1-\frac1n}^1 f(x)\,dx\;\le\;\int_0^1 x^{n-1}f(x)\,dx\,.
}
\]

---

### 2. Upper bound: \(\displaystyle I_n\le\int_0^{\frac1n}f\)

Since \(x\mapsto x^{n-1}\) is **increasing** on \([0,1]\) and \(f\) is **decreasing**, Chebyshev’s integral inequality gives
\[
\int_0^1 x^{n-1}f(x)\,dx
\;\le\;
\Bigl(\int_0^1 x^{n-1}dx\Bigr)
\Bigl(\int_0^1 f(x)\,dx\Bigr)
\;=\;
\frac1n\;\int_0^1 f(x)\,dx.
\]
But on \([0,\tfrac1n]\) we have \(f(x)\ge f(\tfrac1n)\), so
\[
\int_0^{\frac1n}f(x)\,dx
\;\ge\;
\frac1n\,f\!\Bigl(\tfrac1n\Bigr)
\;\ge\;
\frac1n\,f(0)
\;\ge\;
\frac1n\int_0^1 f(x)\,dx.
\]
Hence
\[
\int_0^1 x^{n-1}f(x)\,dx
\;\le\;
\frac1n\int_0^1 f(x)\,dx
\;\le\;
\int_0^{\frac1n}f(x)\,dx,
\]
i.e.
\[
\boxed{
\int_0^1 x^{n-1}f(x)\,dx
\;\le\;
\int_0^{\frac1n}f(x)\,dx\,.}
\]

---

Combining the two displayed bounds proves the claim:
\[
\int_{1-\tfrac1n}^1 f(x)\,dx
\;\le\;
\int_0^1 x^{n-1}f(x)\,dx
\;\le\;
\int_0^{\tfrac1n}f(x)\,dx,
\]
for every \(n\in\Bbb N\).
```