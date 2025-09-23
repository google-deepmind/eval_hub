```markdown
**Solution.**  
Let 
\[
\zeta = e^{2\pi i/n}, 
\qquad e_k = \zeta^{\,k-1}, 
\quad k=1,2,\dots,n,
\]
so that the $n$th roots of unity are $1=\zeta^0,\zeta^1,\dots,\zeta^{n-1}$.  We wish to show
\[
P \;=\;\prod_{1\le i<j\le n}(e_i+e_j)
\]
satisfies $P^2=1$.

1.  Rewrite the product in terms of powers of $\zeta$.  Since
\[
e_i+e_j=\zeta^{i-1}+\zeta^{j-1}
=\zeta^{\,i-1}\bigl(1+\zeta^{\,j-i}\bigr),
\]
we get
\[
P = \prod_{0\le i<j\le n-1}\bigl(\zeta^i+\zeta^j\bigr)
    = \prod_{0\le i<j\le n-1}\zeta^i
      \;\cdot\;
      \prod_{0\le i<j\le n-1}\bigl(1+\zeta^{\,j-i}\bigr).
\]
The exponent of $\zeta$ in the first factor is
\[
\sum_{0\le i<j\le n-1}i 
\;=\;\sum_{i=0}^{n-1} i\,(n-1-i)
\;=\;\frac{n(n^2-1)}6,
\]
which is divisible by $n$ as long as $n$ is odd.  Hence that factor is $\zeta^{n\cdot(\cdots)}=1$, and
\[
P \;=\;
\prod_{0\le i<j\le n-1}\bigl(1+\zeta^{\,j-i}\bigr)
\;=\;
\prod_{k=1}^{n-1}\bigl(1+\zeta^k\bigr)^{\,\#\{(i,j):j-i=k\}}
\;=\;
\prod_{k=1}^{n-1}\bigl(1+\zeta^k\bigr)^{\,n-k}\!.
\]

2.  Pair up the factors $k$ and $n-k$.  For $1\le k\le\frac{n-1}2$ set $m=(n-1)/2$.  Then
\[
P 
= \prod_{k=1}^{n-1}(1+\zeta^k)^{n-k}
= \prod_{k=1}^{m}(1+\zeta^k)^{n-k}\,(1+\zeta^{n-k})^{k}.
\]
But $\;1+\zeta^{n-k}=1+\zeta^{-k}=\zeta^{-k}(1+\zeta^k)\,$, so
\[
(1+\zeta^k)^{n-k}\,(1+\zeta^{n-k})^{k}
= (1+\zeta^k)^{\,n-k}\,\bigl[\zeta^{-k}(1+\zeta^k)\bigr]^{k}
= \zeta^{-k^2}\,(1+\zeta^k)^n.
\]
Hence
\[
P
= \prod_{k=1}^m \zeta^{-k^2}\;\;\times\;\;
\prod_{k=1}^m (1+\zeta^k)^n
= \Bigl(\prod_{k=1}^m \zeta^{\,k^2}\Bigr)^{-1}\;\bigl(\!\prod_{k=1}^m(1+\zeta^k)\bigr)^{n}.
\]
One checks directly (using $\sum_{k=1}^m k^2 = \tfrac{n(n^2-1)}{24}$) that 
$\prod_{k=1}^m\zeta^{k^2}=\zeta^{\,n\cdot(\cdots)}=1$.  Thus
\[
P = S^n,
\qquad
\text{where }
S=\prod_{k=1}^m(1+\zeta^k).
\]

3.  Finally observe that
\[
x^n-1=\prod_{j=0}^{n-1}(x-\zeta^j)
\;\Longrightarrow\;
(-1)^n-1
=\prod_{j=0}^{n-1}(-1-\zeta^j)
=\;(-1)^n\prod_{j=0}^{n-1}(1+\zeta^j).
\]
Since $n$ is odd, $(-1)^n-1=-2$, and $-1-\zeta^0=-2$, so
\[
\prod_{j=1}^{n-1}(1+\zeta^j)
=\frac{(-1)^n-1}{-1-\zeta^0}
= \frac{-2}{-2}=1.
\]
Pairing again shows
\[
\prod_{j=1}^{n-1}(1+\zeta^j)
=\prod_{k=1}^m(1+\zeta^k)(1+\zeta^{n-k})
=\prod_{k=1}^m\frac{(1+\zeta^k)^2}{\zeta^k}
=1,
\]
hence
\[
\prod_{k=1}^m(1+\zeta^k)^2
=\prod_{k=1}^m \zeta^k
=\zeta^{\,\frac{m(m+1)}2}
\quad\Longrightarrow\quad
S^2=\zeta^{\,\frac{m(m+1)}2}.
\]
But then
\[
P^2=(S^n)^2=(S^2)^n
=\zeta^{\,\frac{n\,m(m+1)}2}
=\bigl(\zeta^n\bigr)^{\,\frac{m(m+1)}2}
=1.
\]
This completes the proof that
\[
\boxed{\;\prod_{1\le i<j\le n}(e_i+e_j)^2 \;=\;1\quad\text{for odd }n.}
\]
```