```markdown
**Solution.**

We write
\[
P_1(x)=d\,x+e,\qquad P_2(x)=a\,x^2+b\,x+c,
\]
where \(a,b,c,d,e\in\Bbb R\) and by hypothesis \(P_2(k)\neq0\) for all \(k\in\Bbb Z\).

---

### (a) Existence of \(P\) with \(k^2\,P(1/k)=P_2(k)\)

Set
\[
P(t)\;:=\;a\;+\;b\,t\;+\;c\,t^2.
\]
Then for any integer \(k\neq0\),
\[
k^2\,P\!\bigl(1/k\bigr)
=\;k^2\Bigl(a+\frac b{k}+\frac c{k^2}\Bigr)
=\;a\,k^2+b\,k+c
=\;P_2(k).
\]
Thus a suitable polynomial \(P\) of degree 2 exists (and is unique).

---

### (b) Non‑existence of \(Q\) with \(\tfrac1k\,Q(1/k)=P_1(k)/P_2(k)\)

We seek \(Q\in\Bbb R[x]\) such that
\[
\frac1k\,Q\!\bigl(1/k\bigr)
=\frac{P_1(k)}{P_2(k)}
\quad\Longleftrightarrow\quad
Q\!\bigl(1/k\bigr)
=\frac{k\,(d\,k+e)}{a\,k^2+b\,k+c}
\quad(\forall\,k\in\Bbb Z\setminus\{0\}).
\]
Put \(t=1/k\).  The right side becomes
\[
\frac{k\,(d\,k+e)}{a\,k^2+b\,k+c}
=\frac{\frac d{t^2}+\frac e{t}}{\frac a{t^2}+\frac b{t}+c}
=\frac{d+e\,t}{\,a+b\,t+c\,t^2\,}.
\]
Hence one would need
\[
Q(t)\;=\;\frac{d+e\,t}{a+b\,t+c\,t^2},
\]
which is a rational function of degree \(-1\) (numerator deg 1, denominator deg 2).  Such a function can never be a polynomial unless the quadratic \(a+b\,t+c\,t^2\) is constant.  But \(\deg(a+b\,t+c\,t^2)=2\) by hypothesis, and the only way to make it constant would force \(b=c=0\), giving \(P_2(x)=a\,x^2\) and hence \(P_2(0)=0\), contradicting \(0\notin P_2(\Bbb Z)\).  

Therefore **no** polynomial \(Q\) with the stated property can exist.

---

**Answer.**  
(a) Yes, one can take \(P(t)=a+b\,t+c\,t^2\).  
(b) No, under \(0\notin P_2(\Bbb Z)\) there is no polynomial \(Q\) satisfying \(\tfrac1k\,Q(1/k)=P_1(k)/P_2(k)\).  
```