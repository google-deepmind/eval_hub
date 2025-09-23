```markdown
## Solution

We first describe the block‐structure of the sequence.  The terms of \((a_n)\) are arranged in blocks of lengths \(1^2,2^2,3^2,\dots\), namely
\[
\underbrace{1}_{1^2},\;
\underbrace{1,2,3,4}_{2^2},\;
\underbrace{1,2,\dots,9}_{3^2},\;\dots
\]
In the \(k\)-th block we list the integers \(1,2,\dots,k^2\).

Let
\[
S_k=\sum_{i=1}^k i^2=\frac{k(k+1)(2k+1)}6
\]
be the total number of terms in the first \(k\) blocks.  For any large \(n\), choose \(k\) so that
\[
S_{k-1}<n\le S_k,
\]
and set \(t=n-S_{k-1}\), where \(1\le t\le k^2\).  Then
\[
\sum_{m=1}^n a_m
=\sum_{i=1}^{k-1}\sum_{r=1}^{i^2}r
+\sum_{r=1}^t r
=\frac12\sum_{i=1}^{k-1}\bigl(i^4+i^2\bigr)\;+\;\frac{t(t+1)}2.
\]
As \(k\to\infty\),
\[
S_k=\frac{k^3}3+O(k^2), 
\quad
\sum_{i=1}^k i^4=\frac{k^5}5+O(k^4),
\]
so that
\[
n=S_{k-1}+t\sim\frac{k^3}3,
\qquad
\sum_{m=1}^n a_m\sim\frac1{2}\,\frac{k^5}5=\frac{k^5}{10}.
\]
Hence
\[
b_n=\frac{\sum_{m=1}^n a_m}{n^\alpha}
\sim\frac{\frac{k^5}{10}}{\bigl(\tfrac{k^3}3\bigr)^{\!\alpha}}
=\frac{3^\alpha}{10}\;k^{5-3\alpha}
\sim\frac{3^\alpha}{10}\;\bigl(3n\bigr)^{\frac{5-3\alpha}3}
=\frac{3^{5/3}}{10}\;n^{\frac53-\alpha}.
\]
  
– If \(\alpha<\tfrac53\), then \(b_n\to+\infty\).  
  
– If \(\alpha>\tfrac53\), then \(b_n\to0\).  
  
– If \(\alpha=\tfrac53\), then
\[
\lim_{n\to\infty}b_n
=\frac{3^{5/3}}{10}\,,
\]
which is a positive real number.

Therefore the only choice of \(\alpha,\beta>0\) for which
\(\lim_{n\to\infty}b_n=\beta\) is
\[
\boxed{\;\alpha=\tfrac53,\quad\beta=\frac{3^{5/3}}{10}\;.}
\]
```