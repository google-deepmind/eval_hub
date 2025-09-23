Below is one complete solution using series expansions and known formulas for integrals involving powers of sine.

```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}

We wish to show that
\begin{equation*}
\int_0^{\pi/2} e^{\sin x}\,dx=\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)
+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!},
\end{equation*}
where by convention $0!!=1$ and $0!=1$.

\paragraph{Step 1. Expand the Exponential Function.}

Recall the power series expansion of the exponential function:
\[
e^{\sin x}=\sum_{n=0}^{\infty}\frac{(\sin x)^n}{n!}.
\]
Then, by interchanging summation and integration (which is justified by the uniform convergence of the series on the interval),
\[
\int_0^{\pi/2} e^{\sin x}\,dx=\sum_{n=0}^{\infty}\frac{1}{n!}\int_0^{\pi/2} (\sin x)^n\,dx.
\]

\paragraph{Step 2. Split into Even and Odd Powers.}

It is convenient to separate the sum into even and odd powers. Write $n=2k$ and $n=2k+1$ respectively:
\[
\int_0^{\pi/2} e^{\sin x}\,dx=\sum_{k=0}^{\infty}\frac{1}{(2k)!}\int_0^{\pi/2} (\sin x)^{2k}\,dx
+\sum_{k=0}^{\infty}\frac{1}{(2k+1)!}\int_0^{\pi/2} (\sin x)^{2k+1}\,dx.
\]

\paragraph{Step 3. Use Known Integrals for Powers of Sine.}

We use the standard formulas:
\[
\int_0^{\pi/2} (\sin x)^{2k}\,dx=\frac{(2k-1)!!}{(2k)!!}\frac{\pi}{2},
\]
\[
\int_0^{\pi/2} (\sin x)^{2k+1}\,dx=\frac{(2k)!!}{(2k+1)!!}.
\]
Here the double factorial is defined by
\[
n!!=\begin{cases}
n(n-2)\cdots 2, & \text{if } n \text{ is even,}\\[1ex]
n(n-2)\cdots 1, & \text{if } n \text{ is odd,}
\end{cases}
\]
with $0!!=(-1)!!=1$.

Substituting these results into the series, we obtain:
\[
\int_0^{\pi/2} e^{\sin x}\,dx=\sum_{k=0}^{\infty}\frac{1}{(2k)!}\left(\frac{(2k-1)!!}{(2k)!!}\frac{\pi}{2}\right)
+\sum_{k=0}^{\infty}\frac{1}{(2k+1)!}\frac{(2k)!!}{(2k+1)!!}.
\]

\paragraph{Step 4. Recognize the Separated Terms.}

Note that when \( k=0 \) in the first sum we have:
\[
\frac{1}{0!}\left(\frac{(-1)!!}{0!!}\frac{\pi}{2}\right)=\frac{\pi}{2},
\]
since by convention \((-1)!!=0!!=1\).

Thus, we may write the first sum as
\[
\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right).
\]

Therefore, we have shown that
\[
\int_0^{\pi/2} e^{\sin x}\,dx = \frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)
+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!},
\]
which is the desired result.

\end{document}
```

This solution expands \( e^{\sin x} \) in its power series, interchanges summation and integration, uses the standard integrals for \(\sin^n x\) on \(\left[0,\frac{\pi}{2}\right]\), and finally separates the terms into even and odd parts to obtain the stated identity.