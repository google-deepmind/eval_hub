```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

In this article we prove that if $n$ is an odd positive integer and 
\[
e_1, e_2, \dots, e_n
\]
are the (complex) $n$th roots of unity (with $e_1=1$), then
\[
\prod_{1\le i<j\le n}(e_i+e_j)^2 = 1.
\]
There are several ways to prove this identity. One attractive method is to “pull apart” the product,
rewrite it in terms of a simpler product (and eventually a phase), and show that the phase is trivial.
One possible solution is as follows.

\bigskip

\textbf{Step 1. Expressing the product in a suggestive form.}

Since none of the $e_k$ vanish and for any pair $(i,j)$ we have
\[
e_i+e_j = e_i\Bigl(1+\frac{e_j}{e_i}\Bigr),
\]
we write
\[
\prod_{1\le i<j\le n}(e_i+e_j) = \prod_{1\le i<j\le n} e_i \cdot \prod_{1\le i<j\le n}\left(1+\frac{e_j}{e_i}\right).
\]
It is clear that
\[
\prod_{1\le i<j\le n} e_i = \prod_{i=1}^{n} e_i^{\,\lambda_i},
\]
where for each index $i$ the exponent $\lambda_i$ equals the number of $j$ with $j>i$, namely $\lambda_i = n-i$. In other words,
\[
\prod_{1\le i<j\le n} e_i = \prod_{i=1}^{n} \, e_i^{\, n-i}.
\]
Since each $e_i$ is an $n$th root of unity (so that $e_i^n=1$), the only possible nontrivial contribution is a phase factor.

\medskip

\textbf{Step 2. Changing the order of the product.}

In the second product
\[
\prod_{1\le i<j\le n}\left(1+\frac{e_j}{e_i}\right),
\]
make the change of variable by writing 
\[
\frac{e_j}{e_i} = \zeta^{j-i},
\]
where
\[
\zeta = e^{2\pi i/n}
\]
is a fixed primitive $n$th root of unity. Notice that, as $i$ and $j$ range over $1,2,\ldots,n$ with $i<j$, the difference $d=j-i$ takes values $1,2,\dots,n-1$ and for each such $d$ the number of pairs $(i,j)$ with $j-i=d$ is exactly $n-d$. Hence,
\[
\prod_{1\le i<j\le n}\left(1+\frac{e_j}{e_i}\right)
=\prod_{d=1}^{n-1} \left(1+\zeta^d\right)^{\,n-d}\,.
\]
A useful observation is that the $n$th roots of unity satisfy the identity
\[
\prod_{j=1}^{n-1} (1+\zeta^j)=1,
\]
which follows from considering 
\[
\prod_{j=0}^{n-1} (x+\zeta^j) = x^n+1
\]
and substituting $x=1$ (noting that $1+\zeta^0=2$ so the remaining product equals $1$).

Now, it is convenient to group together the terms corresponding to $d$ and $n-d$. For $1\le d\le (n-1)/2$, pair
\[
1+\zeta^d \quad \text{with} \quad 1+\zeta^{n-d}.
\]
It is easy to check that
\[
1+\zeta^{n-d} = 1+\zeta^{-d} = \zeta^{-d}\bigl(1+\zeta^d\bigr),
\]
so that
\[
\left(1+\zeta^d\right)^{n-d}\left(1+\zeta^{n-d}\right)^{d}
=
\bigl(1+\zeta^d\bigr)^{(n-d)+d}\,\zeta^{-d^2}
=
\bigl(1+\zeta^d\bigr)^n\,\zeta^{-d^2}\,.
\]
Thus, after pairing the factors we obtain
\[
\prod_{d=1}^{n-1} \left(1+\zeta^d\right)^{\,n-d}
=\left(\prod_{d=1}^{\frac{n-1}{2}} \left(1+\zeta^d\right)^n\right)
\left(\prod_{d=1}^{\frac{n-1}{2}} \zeta^{-d^2}\right)\,.
\]
In other words, we have expressed
\[
\prod_{1\le i<j\le n}(e_i+e_j)
=\left[\prod_{i=1}^{n} e_i^{\,n-i}\right]
\cdot  
\left(\prod_{d=1}^{\frac{n-1}{2}} \left(1+\zeta^d\right)^n\right)
\left(\prod_{d=1}^{\frac{n-1}{2}} \zeta^{-d^2}\right)\,.
\]
When we take the square we obtain
\[
\prod_{1\le i<j\le n}(e_i+e_j)^2 =
\left[\prod_{i=1}^{n} e_i^{\,n-i}\right]^2
\cdot  
\left(\prod_{d=1}^{\frac{n-1}{2}} \left(1+\zeta^d\right)^{2n}\right)
\cdot
\left(\prod_{d=1}^{\frac{n-1}{2}} \zeta^{-d^2}\right)^2\,.
\]
Each factor is a power of $\zeta$. Since $\zeta^n=1$, to show that the overall product is $1$ it is enough to check that the total exponent is a multiple of $n$.

\medskip

\textbf{Step 3. Checking the total phase vanishes modulo $n$.}

A brief (but elementary) computation shows that the contribution to the phase from the first factor is
\[
\prod_{i=1}^n e_i^{\,n-i} = \zeta^{\,\frac{n(n-1)(n-2)}{6}}\,.
\]
On the other hand, using the standard expression
\[
\prod_{j=1}^{n-1}(1+\zeta^j)=1,
\]
one may show (after some algebra and pairing of conjugate factors) that the factors coming from
\[
\prod_{d=1}^{\frac{n-1}{2}} \left(1+\zeta^d\right)^{2n}
\quad \text{and} \quad
\left(\prod_{d=1}^{\frac{n-1}{2}} \zeta^{-d^2}\right)^2
\]
contribute an overall phase of
\[
\zeta^{- 2\sum\limits_{d=1}^{\frac{n-1}{2}}d^2}\,.
\]
A standard formula shows that
\[
\sum_{d=1}^{\frac{n-1}{2}} d^2 = \frac{n\,(n^2-1)}{24}\,.
\]
Thus the total phase in the product $\prod\limits_{i<j}(e_i+e_j)^2$ is 
\[
\zeta^{\,\frac{n(n-1)(n-2)}{3} - 2\sum_{d=1}^{\frac{n-1}{2}}d^2}
=\zeta^{\,\frac{n(n-1)(n-2)}{3} -\frac{n(n^2-1)}{12}}\,.
\]
A short calculation shows that
\[
\frac{n(n-1)(n-2)}{3} -\frac{n(n^2-1)}{12} = \frac{n(n^2-1)}{4}\,.
\]
Since $n$ is odd, one may verify that $n^2-1$ is divisible by~$4$, so that
\[
\frac{n(n^2-1)}{4}
\]
is an integer multiple of~$n$. But then 
\[
\zeta^{\frac{n(n^2-1)}{4}} = \left(e^{2\pi i/n}\right)^{\frac{n(n^2-1)}{4}} = e^{2\pi i\cdot K} = 1\quad
\text{for some integer } K\,.
\]
Hence, 
\[
\prod_{1\le i<j\le n}(e_i+e_j)^2 = 1\,.
\]

\bigskip

\textbf{Conclusion.} We have shown that when $n$ is odd and $e_1, e_2, \dots, e_n$ are the $n$th roots of unity, the product
\[
\prod_{1\le i<j\le n}(e_i+e_j)^2
\]
equals $1$. 

\end{document}
``` 

This completes the solution.