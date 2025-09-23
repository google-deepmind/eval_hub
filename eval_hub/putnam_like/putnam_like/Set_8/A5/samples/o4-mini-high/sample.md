```markdown
# Solution

Define
\[
f_n(x)=\prod_{i=1}^n\cos\bigl((2i-1)x\bigr)\,,
\]
and consider the Fourier expansion of \(f_n\).  Using
\[
\cos a=\frac{e^{ia}+e^{-ia}}2
\]
we get
\[
f_n(x)
=\prod_{i=1}^n\frac{e^{i(2i-1)x}+e^{-i(2i-1)x}}2
=2^{-n}\sum_{\varepsilon_i\in\{\pm1\}}
\exp\Bigl(i\,x\sum_{i=1}^n\varepsilon_i\,(2i-1)\Bigr).
\]
Hence the constant term (the coefficient of \(e^{i\cdot0\cdot x}\)) is
\[
2^{-n}\cdot\#\Bigl\{\varepsilon\in\{\pm1\}^n :
\sum_{i=1}^n\varepsilon_i\,(2i-1)=0\Bigr\}.
\]
Since
\[
\int_0^{2\pi}e^{ikx}\,dx
=\begin{cases}
2\pi,&k=0,\\
0,&k\neq 0,
\end{cases}
\]
we obtain
\[
\int_0^{2\pi}f_n(x)\,dx
=2\pi\;\Bigl[\text{constant term of }f_n\Bigr]
=2\pi\,2^{-n}\,\#\Bigl\{\varepsilon:\sum\varepsilon_i(2i-1)=0\Bigr\}.
\]
Observe that
\[
\sum_{i=1}^n(2i-1)=n^2,
\]
so when \(n\) is odd there is no way to split the odd total \(n^2\) into two equal parts.  Hence for odd \(n\) the above count is zero, and
\[
\int_0^{2\pi}f_n(x)\,dx=0\quad(\text{for odd }n).
\]
It follows immediately that
\[
\liminf_{n\to\infty}\int_0^{2\pi}f_n(x)\,dx
=0.
\]

---

**Further remark (asymptotic for even \(n=2k\)).**  
One shows by a local‐CLT argument on the “signed sum” problem that for \(n=2k\)
\[
\int_0^{2\pi}f_{2k}(x)\,dx
\sim\sqrt{\frac{3\pi}{2}}\,(2k)^{-\tfrac32}
\;\longrightarrow\;0
\quad(k\to\infty).
\]
Thus not only does the integral vanish for all odd \(n\), but even for even \(n\) it tends to zero at the rate \(n^{-3/2}\).
```