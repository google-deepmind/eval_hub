```markdown
**Solution.**

Let \(f\in L^1(\mathbb{R})\) and define
\[
g(x)=\int_x^{x+1}f(y)\,dy\,.
\]
We will show (i) \(g\) is measurable and integrable, and (ii)
\(\displaystyle\int_{-\infty}^{\infty}g(x)\,dx
=\int_{-\infty}^{\infty}f(x)\,dx\).

---

### 1. Measurability of \(g\)

For each fixed \(x\), the map
\[
y\;\longmapsto\;f(y)\,1_{[x,x+1]}(y)
\]
is measurable in \(y\).  Since pointwise integrals of measurable functions are measurable in the parameter \(x\), it follows that
\[
g(x)=\int_\mathbb{R}f(y)\,1_{[x,x+1]}(y)\,dy
\]
is a measurable function of \(x\).

---

### 2. Integrability of \(g\)

First note the pointwise estimate
\[
\lvert g(x)\rvert 
\;=\;\Bigl\lvert\int_x^{x+1}f(y)\,dy\Bigr\rvert
\;\le\;\int_x^{x+1}\lvert f(y)\rvert\,dy.
\]
Hence
\[
\int_{-\infty}^{\infty}\lvert g(x)\rvert\,dx
\;\le\;\int_{-\infty}^{\infty}
\Bigl(\int_x^{x+1}\lvert f(y)\rvert\,dy\Bigr)\,dx.
\]
By Tonelli’s theorem we may interchange the order of integration:
\[
\int_{-\infty}^{\infty}\!\int_x^{x+1}\lvert f(y)\rvert\,dy\,dx
=
\int_{-\infty}^{\infty}\!\int_{y-1}^{y}\lvert f(y)\rvert\,dx\,dy
=
\int_{-\infty}^{\infty}\lvert f(y)\rvert
\Bigl(\int_{y-1}^{y}dx\Bigr)dy
=\int_{-\infty}^{\infty}\lvert f(y)\rvert\,dy<\infty.
\]
Thus \(g\in L^1(\mathbb{R})\).

---

### 3. Equality of the integrals

We now compute
\[
\int_{-\infty}^{\infty}g(x)\,dx
=\int_{-\infty}^{\infty}\!\Bigl(\int_x^{x+1}f(y)\,dy\Bigr)\,dx.
\]
Again by Fubini–Tonelli,
\[
\int_{-\infty}^{\infty}\!\int_x^{x+1}f(y)\,dy\,dx
=\int_{-\infty}^{\infty}\!\int_{y-1}^{y}f(y)\,dx\,dy
=\int_{-\infty}^{\infty}f(y)
\Bigl(\int_{y-1}^{y}dx\Bigr)dy
=\int_{-\infty}^{\infty}f(y)\,dy.
\]
Hence
\[
\boxed{
\int_{-\infty}^{\infty}g(x)\,dx
=\int_{-\infty}^{\infty}f(x)\,dx
}\,.
\]
This completes the proof. \(\blacksquare\)
```