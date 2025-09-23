```markdown
## Solution

We start by using the power‐series expansion of the exponential,
\[
e^{\sin x}
=\sum_{n=0}^{\infty}\frac{\sin^n x}{n!},
\]
and then integrate term by term over \(x\in[0,\tfrac\pi2]\):
\[
\int_0^{\pi/2}e^{\sin x}\,dx
=\sum_{n=0}^{\infty}\frac{1}{n!}\int_0^{\pi/2}\sin^n x\,dx.
\]

Recall the standard integrals of powers of sine:
\[
\int_0^{\pi/2}\sin^n x\,dx
=\begin{cases}
\dfrac{(2k-1)!!}{(2k)!!}\,\dfrac\pi2,
&n=2k,\\[1em]
\dfrac{(2k)!!}{(2k+1)!!},
&n=2k+1,
\end{cases}
\]
where by convention \(0!!=1\) and \((-1)!!=1\).  Thus we split the sum into even and odd terms.

1. **Even terms** \(n=2k\).  For \(k\ge0\),
\[
\int_0^{\pi/2}\sin^{2k}x\,dx
=\frac{(2k-1)!!}{(2k)!!}\,\frac\pi2,
\]
so their contribution is
\[
\sum_{k=0}^{\infty}\frac{1}{(2k)!}
\cdot\frac{(2k-1)!!}{(2k)!!}\,\frac\pi2
=\frac\pi2\sum_{k=0}^{\infty}\frac{(2k-1)!!}{(2k)!\,(2k)!!}.
\]
Since \(({-1})!!=1\), the \(k=0\) term of this sum is \(1\).

2. **Odd terms** \(n=2k+1\).  For \(k\ge0\),
\[
\int_0^{\pi/2}\sin^{2k+1}x\,dx
=\frac{(2k)!!}{(2k+1)!!},
\]
so their contribution is
\[
\sum_{k=0}^{\infty}\frac{1}{(2k+1)!}
\cdot\frac{(2k)!!}{(2k+1)!!}
=\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!\,(2k+1)!!}.
\]

Putting these two pieces together gives
\[
\int_0^{\pi/2}e^{\sin x}\,dx
=\frac\pi2\sum_{k=0}^{\infty}\frac{(2k-1)!!}{(2k)!\,(2k)!!}
\;+\;\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!\,(2k+1)!!}.
\]
Noting that the \(k=0\) term in the first sum is \(1\), we can rewrite it as
\[
\frac\pi2\Bigl(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!\,(2k)!!}\Bigr)
\;+\;\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!\,(2k+1)!!},
\]
which is exactly the desired result.
```