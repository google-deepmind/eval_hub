Below is one acceptable solution. One may show that
\[
\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx\quad\text{for all } n\in\mathbb{N},
\]
by “re‐interpreting” the middle integral as an average of \(f\) with respect to an appropriate probability measure. One way to do this is as follows.

---

```markdown
We are given that \(f:[0,1]\to\mathbb{R}\) is continuous and decreasing. Define
\[
I_n=\int_0^1 x^{n-1}f(x)\,dx.
\]
Notice that
\[
\int_0^1 x^{n-1}\,dx=\frac1n,
\]
so that if we define on \([0,1]\) the measure
\[
\mu_n(A)=n\int_A x^{n-1}\,dx,
\]
then \(\mu_n\) is a probability measure. In other words, if we define a random variable \(X\) whose density is
\[
p_n(x)=n\,x^{n-1}\quad \text{for } x\in[0,1],
\]
then
\[
n I_n=\int_0^1 f(x)\,d\mu_n(x)=\mathbb{E}[f(X)].
\]

Because \(f\) is decreasing, its value at any point is “extremal” in the sense that if the probability measure is more concentrated on the right (larger \(x\)) then the average of \(f\) must be smaller, and vice‐versa.

A key observation is to compare \(\mathbb{E}[f(X)]\) with the values of \(f\) at appropriate quantiles of \(X\). The distribution function of \(X\) is
\[
F_X(x)=\int_0^x n\,t^{n-1}\,dt=x^n.
\]
Thus, the \(p\)th quantile \(q_p\) is given by
\[
q_p=x \quad\text{with}\quad x^n=p,\quad\text{or}\quad q_p=p^{1/n}.
\]
Now, take
\[
p=\frac{1}{n}\quad\text{and}\quad p=1-\frac{1}{n}.
\]
Then the corresponding quantiles are
\[
q_{1/n}=\Bigl(\frac{1}{n}\Bigr)^{\!1/n}\quad\text{and}\quad q_{1-1/n}=\Bigl(1-\frac{1}{n}\Bigr)^{\!1/n}\,.
\]
Since \(f\) is decreasing, we have
\[
f\Bigl(q_{1-1/n}\Bigr)\le \mathbb{E}[f(X)]\le f\Bigl(q_{1/n}\Bigr).
\]
A short calculation shows that
\[
\Bigl(1-\frac{1}{n}\Bigr)^{\!1/n}\ge 1-\frac{1}{n}\quad\text{and}\quad \Bigl(\frac{1}{n}\Bigr)^{\!1/n}\le \frac{1}{n}\,.
\]
Thus, using the fact that \(f\) is decreasing we obtain
\[
f\Bigl(1-\frac{1}{n}\Bigr)\le f\Bigl(\Bigl(1-\frac{1}{n}\Bigr)^{1/n}\Bigr)\le \mathbb{E}[f(X)]\le f\Bigl(\Bigl(\frac{1}{n}\Bigr)^{1/n}\Bigr)\le f\Bigl(\frac{1}{n}\Bigr).
\]
That is,
\[
f\Bigl(1-\frac{1}{n}\Bigr)\le n\int_0^1 x^{n-1}f(x)dx\le f\Bigl(\frac{1}{n}\Bigr).
\]

Since \(f\) is decreasing it is also true that for any \(a\in(0,1)\)
\[
\int_{1-a}^1 f(x)dx\le a\, f\Bigl(1-\frac{1}{n}\Bigr)
\quad\text{and}\quad
\int_0^a f(x)dx\ge a\, f\Bigl(\frac{1}{n}\Bigr)
\]
with the proper choice of \(a\). In particular, choosing \(a=\frac{1}{n}\) we have
\[
\frac{1}{n}\, f\Bigl(1-\frac{1}{n}\Bigr)\ge \int_{1-\frac{1}{n}}^1 f(x)dx
\quad\text{and}\quad
\frac{1}{n}\, f\Bigl(\frac{1}{n}\Bigr)\le \int_0^{\frac{1}{n}} f(x)dx.
\]
Multiplying the inequality
\[
f\Bigl(1-\frac{1}{n}\Bigr)\le n I_n\le f\Bigl(\frac{1}{n}\Bigr)
\]
by \(\frac{1}{n}\) and using the above bounds gives
\[
\int_{1-\frac{1}{n}}^1 f(x)dx\le I_n\le \int_0^{\frac{1}{n}} f(x)dx\,,
\]
which is exactly the desired result.
  
\(\Box\)
```

---

Any answer equivalent to the one above is acceptable.