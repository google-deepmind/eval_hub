This step is worth 2 points.
Define $f : (0,\infty) \rightarrow (0,\infty)$ by
$$
f(x) = \left( x + \frac{1}{x} \right)^p.
$$
Suppose first that $p > 1$. Then
$$
f'(x) = p \left(x + \frac{1}{x} \right)^{p-1} \left(1 - \frac{1}{x^2} \right)
$$
and
$$
\begin{aligned}
f''(x) &= p (p-1) \left(x + \frac{1}{x} \right)^{p-2} \left(1 - \frac{1}{x^2} \right) \left(1 - \frac{1}{x^2} \right) + p \left(x + \frac{1}{x} \right)^{p-1} \frac{2}{x^3} \\
&= p (p-1) \left(x + \frac{1}{x} \right)^{p-2} \left(1 - \frac{1}{x^2} \right)^2 + 2 p \left(x + \frac{1}{x} \right)^{p-1} \frac{1}{x^3}.
\end{aligned}
$$
Hence $f''(x) \geq 0$ for all $x \in (0,\infty)$ and $f$ is convex. If $p = 1$, clearly the function is constant, so it is convex as well. 

This step is worth 5 points.
If $p \in (0,1)$, consider $x \in (0,1)$. Then
$$
\begin{aligned}
f''(x) &= p (p-1) \left(x + \frac{1}{x} \right)^{p-2} \left(1 - \frac{1}{x^2} \right)^2 + 2 p \left(x + \frac{1}{x} \right)^{p-1} \frac{1}{x^3} \\
&=  p \left( x + \frac{1}{x} \right)^{p-2} \left( (p-1) \left(1-\frac{1}{x^2}\right)^2 + 2 \left(x + \frac{1}{x} \right) \frac{1}{x^3} \right) \\
&= p \left( x + \frac{1}{x} \right)^{p-2} \left( (p-1) \left(1  - \frac{2}{x^2} + \frac{1}{x^4}\right) + 2 \left(\frac{1}{x^2} + \frac{1}{x^4} \right) \right) \\
&= p \left( x + \frac{1}{x} \right)^{p-2} \left( p - \frac{2p}{x^2} + \frac{p}{x^4} - 1 + \frac{2}{x^2} - \frac{1}{x^4} + \frac{2}{x^2} + \frac{2}{x^4} \right) \\
&= p \left( x + \frac{1}{x} \right)^{p-2} \left( p-1 + \frac{4-2p}{x^2} + \frac{p+1}{x^4} \right) \\
&\geq p \left( x + \frac{1}{x} \right)^{p-2} \left( p-1 + \frac{4-2p}{1} + \frac{p+1}{1} \right) \\
&= p \left( x + \frac{1}{x} \right)^{p-2} (p-1+4-2p+p+1) \\
&= p \left( x + \frac{1}{x} \right)^{p-2} 4 \geq 0.
\end{aligned}
$$
Hence $f$ is convex on $(0,1)$ for each $p > 0$. 

This step is worth 1 point.
Since all $a_i \in (0,1)$, from Jensen's inequality we get
$$
\frac1n f(a_1) + \ldots + \frac1n f(a_n) \geq f \left( \frac{1}{n} a_1 + \ldots + \frac{1}{n} a_n \right) = f \left( \frac{1}{n} \right).
$$

This step is worth 2 points.
Hence
$$
\begin{aligned}
\sum_{i=1}^n f(a_i) &\geq n f \left( \frac{1}{n} \right), \\
\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p &\geq n  \left( n + \frac1n \right)^p, \\
\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p &\geq \frac{(n^2+1)^p}{n^{p-1}}.
\end{aligned}
$$