```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}

We wish to evaluate the limit
\[
\lim_{n\to\infty} S_n, \quad \text{where} \quad S_n = \sum_{k=1}^n \sin\!\left(\frac{\pi}{2}\cdot \frac{n+2k-1}{n(n-1)}\right).
\]
Since for large \( n \) the angle
\[
\theta_{n,k} = \frac{\pi}{2}\cdot \frac{n+2k-1}{n(n-1)}
\]
is small, we may use the small-angle approximation
\[
\sin \theta \sim \theta \quad \text{as } \theta\to 0.
\]
Thus, for large \( n \) we have
\[
\sin\!\left(\frac{\pi}{2}\cdot \frac{n+2k-1}{n(n-1)}\right) \sim \frac{\pi}{2}\cdot \frac{n+2k-1}{n(n-1)}.
\]
Therefore, the sum can be approximated by
\[
S_n \sim \frac{\pi}{2} \cdot \frac{1}{n(n-1)} \sum_{k=1}^n (n+2k-1).
\]

Let us compute the inner sum:
\[
\sum_{k=1}^n (n+2k-1) = \sum_{k=1}^n \bigl[(n-1) + 2k\bigr] 
= n(n-1) + 2\sum_{k=1}^n k.
\]
Since
\[
\sum_{k=1}^n k = \frac{n(n+1)}{2},
\]
it follows that
\[
\sum_{k=1}^n (n+2k-1) = n(n-1) + 2\cdot \frac{n(n+1)}{2} 
= n(n-1) + n(n+1) 
= 2n^2.
\]

Substituting back into the expression for \( S_n \), we obtain
\[
S_n \sim \frac{\pi}{2} \cdot \frac{2n^2}{n(n-1)} 
= \pi \cdot \frac{n}{n-1}.
\]
Taking the limit as \( n \to \infty \) gives
\[
\lim_{n\to\infty} S_n = \pi \lim_{n\to\infty} \frac{n}{n-1} = \pi.
\]

Thus, the desired limit is
\[
\boxed{\pi}.
\]

\end{document}
```