Solution step (worth 2 points):
Using the second property we can rewrite the first one as follows
$$
\begin{split}
9f(x)-10f(f(x))&=2x \\
\Leftrightarrow 5f(x)-5f(2f(x))&=2x-4f(x) \\
\Leftrightarrow 5(f(x)-f(2f(x))&=2(x-f(2x)).
\end{split}
$$
Assume that the function $f$ exists and put $g(x)=x-f(2x)$, $g:\mathbb{Z}\to\mathbb{Z}$. Then the equation we rewrite as
$$
5g(f(x))=2g(x).
$$

Solution step (worth 6 points):
Fix $y\in \mathbb{Z}$ and define a sequence $(x_n)$ by
$$
x_0=y,\quad x_n=f(x_{n-1}).
$$
Then $g(x_{n-1})=\frac 52 g(f(x_{n-1}))=\frac 52 g(x_n)$, hence by an easy induction
$$
g(y)=g(x_0)=\frac{5^n}{2^n} g(x_n) \Leftrightarrow 2^n g(y) = 5^n g(x_n)
$$
for any $n\geq 1$. The numbers $2$ and $5$ are relatively prime, so we deduce $5^n|g(y)$ for any $n\geq 1$. It implies $g(y)=0$. Since $y$ was taken arbitrary we conclude $g(y)=0$ for any $y\in\mathbb{Z}$.

Solution step (worth 2 points):
Thus $y=f(2y)=2f(y)$ for any $y\in\mathbb{Z}$. This equation cannot hold for odd numbers $y$, therefore we conclude that such function $f$ does not exist.