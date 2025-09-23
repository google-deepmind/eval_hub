```markdown
# Solution

Suppose, to the contrary, that \(P\) has a rational root
\[
r = \frac{p}{q}
\]
in lowest terms, so \(\gcd(p,q)=1\).  By the Rational Root Theorem,
\[
p\mid a_0=3^v,\quad q\mid a_n=5^u,
\]
hence
\[
p=\pm3^i,\quad q=5^j
\]
for some nonnegative integers \(i,j\).  In particular \(p\) and \(q\) are odd.

Consider
\[
q^n\,P\!\bigl(\tfrac pq\bigr)
\;=\;\sum_{k=0}^n a_k\,p^k\,q^{\,n-k}
\;=\;0.
\]
Reducing this congruence modulo 2, we observe that since \(p\) and \(q\) are odd,
\[
p^k\,q^{\,n-k}\equiv1\pmod2\quad\text{for each }k,
\]
hence
\[
0 \equiv \sum_{k=0}^n a_k
\;\equiv\;P(1)\pmod2.
\]
On the other hand, we are given that
\[
P(-1)=\sum_{k=0}^n a_k(-1)^k
\]
is odd.  But
\[
P(1)+P(-1)
=\sum_{k=0}^n a_k\bigl(1+(-1)^k\bigr)
=2\sum_{k\text{ even}}a_k
\equiv0\pmod2,
\]
so
\[
P(1)\equiv P(-1)\equiv1\pmod2.
\]
This contradicts the fact that \(P(1)\) must be even.  Therefore \(P\) has no rational roots.
```