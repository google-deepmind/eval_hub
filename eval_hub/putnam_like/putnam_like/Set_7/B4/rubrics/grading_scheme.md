Solution step (2 points):
Observe that
$$
\mathbb{O} = \left\{ \frac{p^m - 1}{p-1} \ : \ m \geq 1 \right\}.
$$
Note that if we put
$$\tag{1}
g(n) = (p-1) f \left( \frac{n-1}{p-1} \right) + 1,
$$
then $f(\mathbb{O}) \subset \mathbb{O}$ if and only if $g(\{ p^m \}_m ) \subset  \{ p^m \}_m$.

Solution step (7 points):
We will show that $g$ has to be of the form $g(x) = p^k x^n$ for $n \geq 0$ and $k \geq 1 - n$. Clearly $g$ of this form satisfies the above condition. On the other hand, suppose that the leading term $g(x)$ has the form $a x^n$, where $a > 0$. Then $\lim_{x\to\infty} \frac{g(x)}{x^n} = a$. But for $x = p^m$, $\frac{g(x)}{x^n}$ is again a power of $p$, and since we consider $x \to \infty$, such a subsequence doesn't have finite, positive limit points. Thus for $x = p^m$ we have $\frac{g(x)}{x^n} = a$. In particular $a = p^k$ for some $k \geq 1 - n$. Then we see that $g(x) - ax^n = g(x) - p^k x^n$ has infinitely many roots, so $g(x) = p^k x^n$.

Solution step (1 point):
Hence, from (1), all the polynomials $f$ have the form
$$
f(x) = \frac{1}{p-1} \left( p^k ( (p-1)x + 1)^n - 1 \right)
$$
for $n \geq 0$ and $k \geq 1-n$.