Let the given limit be $L$. The expression is
\[ L = \lim_{n\to\infty} \frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}. \]
Let $S_n = \sum_{k=1}^n\sum_{l=1}^k e^{l/k}$.
The inner sum is $S_k = \sum_{l=1}^k e^{l/k}$. This is a geometric series with first term $a=e^{1/k}$, common ratio $r=e^{1/k}$, and $k$ terms. The sum is
\[ S_k = e^{1/k} \frac{(e^{1/k})^k - 1}{e^{1/k} - 1} = e^{1/k} \frac{e - 1}{e^{1/k} - 1}. \]
We need to evaluate $\lim_{n\to\infty} \frac{1}{n^2} \sum_{k=1}^n S_k$.
Let's analyze the term $S_k$ for large $k$. Let $x=1/k$. As $k\to\infty$, $x\to 0$.
We use the Taylor series expansion of $e^x$ around $x=0$: $e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + O(x^4)$.
$e^x-1 = x + \frac{x^2}{2} + \frac{x^3}{6} + O(x^4)$.
$\frac{1}{e^x-1} = \frac{1}{x(1+x/2+x^2/6+O(x^3))} = \frac{1}{x} \left( 1 - \left(\frac{x}{2}+\frac{x^2}{6}\right) + \left(\frac{x}{2}\right)^2 + O(x^3) \right)$
$= \frac{1}{x} \left( 1 - \frac{x}{2} - \frac{x^2}{6} + \frac{x^2}{4} + O(x^3) \right) = \frac{1}{x} \left( 1 - \frac{x}{2} + \frac{x^2}{12} + O(x^3) \right) = \frac{1}{x} - \frac{1}{2} + \frac{x}{12} + O(x^2)$.
Now consider $\frac{e^x}{e^x-1} = (1+x+x^2/2+O(x^3)) \left(\frac{1}{x} - \frac{1}{2} + \frac{x}{12} + O(x^2)\right)$
$= \left(\frac{1}{x} - \frac{1}{2} + \frac{x}{12}\right) + \left(1 - \frac{x}{2}\right) + \frac{x}{2} + O(x^2)$
$= \frac{1}{x} + \left(1 - \frac{1}{2}\right) + \left(\frac{1}{12} - \frac{1}{2} + \frac{1}{2}\right)x + O(x^2)$
$= \frac{1}{x} + \frac{1}{2} + \frac{x}{12} + O(x^2)$.
Substitute $x=1/k$:
\[ \frac{e^{1/k}}{e^{1/k}-1} = k + \frac{1}{2} + \frac{1}{12k} + O(1/k^2). \]
So, $S_k = (e-1) \left( k + \frac{1}{2} + \frac{1}{12k} + O(1/k^2) \right)$ for $k \ge 1$. The $O(1/k^2)$ term is uniform for $k \ge 1$.

Now we sum $S_k$ from $k=1$ to $n$:
\[ S_n = \sum_{k=1}^n S_k = \sum_{k=1}^n (e-1) \left( k + \frac{1}{2} + \frac{1}{12k} + R_k \right), \]
where $R_k = O(1/k^2)$ means $|R_k| \le C/k^2$ for some constant $C$ for $k \ge 1$.
\[ S_n = (e-1) \left( \sum_{k=1}^n k + \sum_{k=1}^n \frac{1}{2} + \sum_{k=1}^n \frac{1}{12k} + \sum_{k=1}^n R_k \right). \]
We know the sums:
$\sum_{k=1}^n k = \frac{n(n+1)}{2} = \frac{n^2}{2} + \frac{n}{2}$.
$\sum_{k=1}^n \frac{1}{2} = \frac{n}{2}$.
$\sum_{k=1}^n \frac{1}{k} = H_n$, the $n$-th harmonic number. $H_n = \log n + \gamma + O(1/n)$, where $\gamma$ is the Euler-Mascheroni constant. So $\sum_{k=1}^n \frac{1}{k} = O(\log n)$.
$\sum_{k=1}^n R_k$: Since $|R_k| \le C/k^2$, the series $\sum_{k=1}^\infty R_k$ converges because $\sum_{k=1}^\infty 1/k^2$ converges. Thus, $\sum_{k=1}^n R_k$ is bounded as $n\to\infty$, which means $\sum_{k=1}^n R_k = O(1)$.

Substituting these into the expression for $S_n$:
\[ S_n = (e-1) \left( \frac{n^2}{2} + \frac{n}{2} + \frac{n}{2} + \frac{1}{12} O(\log n) + O(1) \right) \]
\[ S_n = (e-1) \left( \frac{n^2}{2} + n + O(\log n) \right). \]
Now, we compute the limit:
\[ L = \lim_{n\to\infty} \frac{1}{n^2} S_n = \lim_{n\to\infty} \frac{1}{n^2} (e-1) \left( \frac{n^2}{2} + n + O(\log n) \right) \]
\[ L = \lim_{n\to\infty} (e-1) \left( \frac{n^2}{2n^2} + \frac{n}{n^2} + \frac{O(\log n)}{n^2} \right) \]
\[ L = \lim_{n\to\infty} (e-1) \left( \frac{1}{2} + \frac{1}{n} + O\left(\frac{\log n}{n^2}\right) \right). \]
As $n\to\infty$, $\frac{1}{n} \to 0$ and $\frac{\log n}{n^2} \to 0$.
Thus, the limit is
\[ L = (e-1) \left( \frac{1}{2} + 0 + 0 \right) = \frac{e-1}{2}. \]

The final answer is $\boxed{\frac{e-1}{2}}$.