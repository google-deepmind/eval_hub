```markdown
**Solution.**

We want to show
\[
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx
\;=\;0.
\]

### 1. Using the known Fourier transform of the Gaussian

It is a standard result that
\[
\int_{-\infty}^{\infty}e^{-x^2/2}\,e^{i y x}\,dx
\;=\;\sqrt{2\pi}\,e^{-y^2/2}.
\]
Taking real parts gives
\[
\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx
=\Re\!\Bigl(\sqrt{2\pi}\,e^{-y^2/2}\Bigr)
=\sqrt{2\pi}\,e^{-y^2/2}.
\]
Since \(e^{-y^2/2}\to0\) as \(y\to\infty\), the desired limit is \(0\).

---

### 2. By the Riemann–Lebesgue lemma

The function
\[
f(x)=e^{-x^2/2}
\]
is integrable on \(\Bbb R\).  The Riemann–Lebesgue lemma asserts that
\[
\int_{-\infty}^\infty f(x)\,e^{i y x}\,dx
\;\longrightarrow\;0
\quad(y\to\infty).
\]
Taking real parts yields
\[
\int_{-\infty}^\infty e^{-x^2/2}\cos(yx)\,dx
\;\longrightarrow\;0.
\]

---

### 3. By an elementary integration‐by‐parts estimate

Split the integral at some large \(A>0\):
\[
\int_{-\infty}^\infty e^{-x^2/2}\cos(yx)\,dx
=\int_{-A}^A\!e^{-x^2/2}\cos(yx)\,dx
\;+\;\int_{|x|>A}\!e^{-x^2/2}\cos(yx)\,dx.
\]
1.  The tail \(\int_{|x|>A}e^{-x^2/2}\,dx\) can be made arbitrarily small by choosing \(A\) large, since \(e^{-x^2/2}\) is integrable.  
2.  On \([-A,A]\) integrate by parts once: for \(x\in[0,A]\),
   \[
   \int_0^A e^{-x^2/2}\cos(yx)\,dx
   =\Bigl[\frac{e^{-x^2/2}\sin(yx)}{y}\Bigr]_0^A
    +\frac1y\int_0^A x\,e^{-x^2/2}\sin(yx)\,dx,
   \]
   so its absolute value is \(O(1/y)\).  A similar estimate holds on \([-A,0]\).  
Putting these together shows the whole integral tends to \(0\) as \(y\to\infty\).
```

**Therefore,** in any of these approaches one concludes
\[
\boxed{\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx = 0.}
\]
