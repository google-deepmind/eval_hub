```markdown
**Solution.**  
Let 
\[
\Psi(s)\;=\;\ln\Bigl(\!\int_{\R^n}|f(x)|^s\,dx\Bigr), 
\qquad s\in[p,q].
\]
We give two proofs of the convexity of $\Psi$.

---

### Proof 1: Hölder’s inequality

Fix $s_1,s_2\in[p,q]$ and $t\in[0,1]$.  Write
\[
s = t\,s_1 + (1-t)\,s_2.
\]
Then
\[
\int_{\R^n}|f|^s
=\int_{\R^n}\bigl(|f|^{s_1}\bigr)^t\,\bigl(|f|^{s_2}\bigr)^{1-t}.
\]
Applying Hölder’s inequality with exponents $\tfrac1t$ and $\tfrac1{1-t}$ gives
\[
\int_{\R^n}|f|^s
\;\le\;
\Bigl(\int_{\R^n}|f|^{s_1}\Bigr)^{t}\,
\Bigl(\int_{\R^n}|f|^{s_2}\Bigr)^{1-t}.
\]
Taking logarithms,
\[
\Psi\bigl(t\,s_1+(1-t)s_2\bigr)
=\ln\!\Bigl(\int|f|^s\Bigr)
\;\le\;
t\,\ln\!\Bigl(\!\int|f|^{s_1}\Bigr)
\;+\;(1-t)\,\ln\!\Bigl(\!\int|f|^{s_2}\Bigr)
\;=\;
t\,\Psi(s_1)+(1-t)\,\Psi(s_2).
\]
This is exactly the definition of convexity of $\Psi$.

---

### Proof 2: Second‐derivative test

Assume for the moment that we may differentiate under the integral sign.  Set
\[
I(s)=\int_{\R^n}|f(x)|^s\,dx,
\]
so that $\Psi(s)=\ln I(s)$.  Then
\[
\Psi'(s)
=\frac{I'(s)}{I(s)},
\quad
\Psi''(s)
=\frac{I''(s)\,I(s)-\bigl(I'(s)\bigr)^2}{I(s)^2}.
\]
We compute
\[
I'(s)
=\int|f|^s\ln|f|
\quad\text{and}\quad
I''(s)
=\int|f|^s(\ln|f|)^2.
\]
Hence
\[
\Psi''(s)
=\frac{\displaystyle\int|f|^s(\ln|f|)^2\;\;\displaystyle\int|f|^s
\;-\;\Bigl(\displaystyle\int|f|^s\ln|f|\Bigr)^2}
{\bigl(\displaystyle\int|f|^s\bigr)^2}
\;=\;
\operatorname{Var}_{\mu_s}\!(\ln|f|)\;\ge0,
\]
where $\mu_s$ is the probability measure
\[
d\mu_s(x)=\frac{|f(x)|^s\,dx}{\int|f|^s}.
\]
Since variances are nonnegative, $\Psi''(s)\ge0$, and $\Psi$ is convex.

---

In either approach, we conclude that $\Psi\colon[p,q]\to\R$ is convex, as required.
```