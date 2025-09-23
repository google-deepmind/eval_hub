This step is worth 1 point.
The sequence consists of parts of the length $k^2$ so take $N_n=1^2+2^2+\ldots+n^2=\frac{n(n+1)(2n+1)}6$. In the one part of the length $k^2$ the sum of elements is $1+2+\ldots+k^2=\frac{k^2(k^2+1)}2$. Recall that
$$
\sum_{i=1}^n i^4 = \frac{n(n+1)(2n+1)(3n^2+3n-1)}{30}.
$$
This formula is not widely known, but one can prove it by a simple induction: for $n=1$ the equality is trivial. Assuming the formula is true for $n$ we have:
$$
\begin{split}
\sum_{i=1}^{n+1} i^4 &=\left(\sum_{i=1}^{n} i^4\right)+(n+1)^4
= \frac{n(n+1)(2n+1)(3n^2+3n-1)}{30}+(n+1)^4\\
&= \frac{n+1}{30}\left(n(2n+1)(3n^2+3n-1)+30(n+1)^3\right)\\
&=  \frac{n+1}{30}\left((6n^4+9n^3+n^2-n)+30(n^3+3n^2+3n+1)\right)\\
&=\frac{n+1}{30} \left(6n^4+39n^3+91n^2+89n+30\right).
\end{split}
$$
On the other hand we expect the formula:
$$
\begin{split}
&\frac{(n+1)(n+2)(2(n+1)+1)(3(n+1)^2+3(n+1)-1)}{30}=\frac{n+1}{30} (n+2)(2n+3)(3n^2+9n+5)\\
=& \frac{n+1}{30} (2n^2+7n+6)(3n^2+9n+5)=\frac{n+1}{30} \left(6n^4+39n^3+91n^2+89n+30\right),
\end{split}
$$
so the formulas agree.


This step is worth 4 points.
We compute
$$
\begin{split}
b_{N_n}&=\frac{\sum_{k=1}^{N_n} a_k}{N_n^{\alpha}}=\frac{\sum_{k=1}^{n} \frac{k^2(k^2+1)}2}{N_n^{\alpha}}
=\frac{\sum_{k=1}^{n} (k^4+k^2)}{2\cdot 6^{-\alpha}n^{\alpha}(n+1)^{\alpha}(2n+1)^{\alpha}}=\\
&=\frac{6^\alpha}2\cdot\frac{\sum k^4+\sum k^2}{n^{\alpha}(n+1)^{\alpha}(2n+1)^{\alpha}}
=\frac{6^\alpha}2\frac{\frac{n(n+1)(2n+1)(3n^2+3n-1)}{30}+\frac{n(n+1)(2n+1)}6}{n^{\alpha}(n+1)^{\alpha}(2n+1)^{\alpha}}=\\
&= \frac{6^{\alpha}}2 \cdot\frac{n(n+1)(2n+1)}{30}\cdot \frac{3n^2+3n-1+5}{n^{\alpha}(n+1)^{\alpha}(2n+1)^{\alpha}}=\frac{6^{\alpha-1}}{10} \cdot\frac{(2n+1)(3n^2+3n+4)}{n^{\alpha-1}(n+1)^{\alpha-1}(2n+1)^{\alpha}}.
\end{split}
$$
Computing further
$$
b_{N_n}=\frac{6^{\alpha-1}}{10} \cdot\frac{6n^3\left(1+\frac{1}{2n}\right)\left(1+\frac{1}{n}+\frac{4}{3n^2}\right)}{2^{\alpha}n^{3\alpha-2}(1+\frac 1n)^{\alpha-1}(1+\frac{1}{2n})^{\alpha}}=\frac{3^{\alpha}}{10} \cdot\frac{n^3\left(1+\frac{1}{2n}\right)\left(1+\frac{1}{n}+\frac{4}{3n^2}\right)}{n^{3\alpha-2}(1+\frac 1n)^{\alpha-1}(1+\frac{1}{2n})^{\alpha}}.
$$

This step is worth 2 points.
The limit of this sequence exists, is finite and non-zero if $3=3\alpha-2 \Leftrightarrow\alpha=\frac 53$. Then
$$
\lim_{n\to\infty} b_{N_n}= \frac{3^{5/3}}{10}.
$$
Hence the only pair that could satisfy the condition is $(\alpha,\beta)=(\frac 53,\frac{3^{5/3}}{10})$.

This step is worth 3 points.
Let $N$ be an integer in $[N_n,N_{n+1}]$ i.e. $N=N_n+m$. Then
$$
b_N=\frac{\sum_{k=1}^{N_n} \frac{k(k+1)(2k+1)}6+1+2+\ldots+m}{(N_n+m)^{\alpha}}
$$
and we estimate
$$
b_{N_n}\cdot\frac{N_n^{\alpha}}{N_{n+1}^{\alpha}}=\frac{\sum_{k=1}^{N_n} \frac{k(k+1)(2k+1)}6}{N_{n+1}^{\alpha}}<b_N<\frac{\sum_{k=1}^{N_{n+1}} \frac{k(k+1)(2k+1)}6}{N_n^{\alpha}}=b_{N_{n+1}}\cdot\frac{N_{n+1}^{\alpha}}{N_{n}^{\alpha}}.
$$
Since $\lim_{n\to\infty} \frac{N_n}{N_{n+1}}=1$ by the squeeze theorem we get $\lim_{N\to\infty}b_N=\beta$.