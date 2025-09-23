```markdown
We start by noting that the sequence \((a_n)_{n=1}^\infty\) is obtained by concatenating blocks of the form
\[
\text{Block } k: 1,2,3,\dots,k^2, \quad k=1,2,3,\dots
\]
Thus, the sequence is
\[
(1,\; 1,2,3,4,\; 1,2,\ldots,9,\; \dots).
\]

For each block \(k\):
- The number of terms is
  \[
  k^2.
  \]
- The sum of the terms in the block is
  \[
  S_k = 1+2+\cdots+k^2 = \frac{k^2(k^2+1)}{2}.
  \]
  For large \(k\) we have
  \[
  S_k \sim \frac{k^4}{2}.
  \]

Let \(m\) be the index of the last complete block when forming the first \(n\) terms of the sequence. Then:

1. The total number of terms up to block \(m\) is
   \[
   N(m)=\sum_{k=1}^{m} k^2 = \frac{m(m+1)(2m+1)}{6}\sim\frac{m^3}{3} \quad \text{as } m\to\infty.
   \]
2. The total sum of terms up to block \(m\) is
   \[
   T(m)=\sum_{k=1}^{m} S_k \sim \sum_{k=1}^{m} \frac{k^4}{2} \sim \frac{1}{2}\cdot\frac{m^5}{5}=\frac{m^5}{10}.
   \]

Now, since \(n\) is the total number of terms, we have (approximately)
\[
n\sim \frac{m^3}{3} \quad\Longrightarrow\quad m\sim (3n)^{1/3}.
\]
Substituting this into the expression for the total sum we obtain
\[
\sum_{k=1}^n a_k \sim T(m)\sim \frac{(3n)^{5/3}}{10}.
\]

The problem defines
\[
b_n=\frac{\sum_{k=1}^n a_k}{n^\alpha},
\]
so we have
\[
b_n\sim \frac{\frac{(3n)^{5/3}}{10}}{n^\alpha}=\frac{3^{5/3}}{10}\,n^{5/3-\alpha}.
\]

For \(\lim_{n\to\infty} b_n\) to be a finite positive number \(\beta\), we need the exponent of \(n\) in the asymptotic expression to vanish:
\[
5/3-\alpha=0 \quad\Longrightarrow\quad \alpha=\frac{5}{3}.
\]
In this case,
\[
\lim_{n\to\infty} b_n=\frac{3^{5/3}}{10}.
\]

Thus, the only pair \((\alpha,\beta)\) of positive real numbers such that
\[
\lim_{n\to\infty}b_n=\beta
\]
with \(\beta>0\) is
\[
\boxed{\left(\alpha,\beta\right)=\left(\frac{5}{3},\frac{3^{5/3}}{10}\right)}.
\]

Note: For \(\alpha<\frac{5}{3}\) the limit is \(+\infty\), and for \(\alpha>\frac{5}{3}\) the limit is \(0\); hence only \(\alpha=\frac{5}{3}\) gives a positive finite \(\beta\).
```