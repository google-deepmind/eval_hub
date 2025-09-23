```markdown
Here is one correct solution.

We begin by defining, for each \( n\in\mathbb{N} \), the function
\[
F_n(x)=f(x)+f'(x)+\cdots+f^{(n)}(x).
\]
Then the hypothesis is that there exist numbers \(a_n,b_n\in(-1,1)\) with \(a_n<b_n\) such that
\[
\frac{F_n(b_n)}{F_n(a_n)}=\frac{e^{b_n}}{e^{a_n}}.
\]
This equation may be rewritten as
\[
\frac{F_n(b_n)}{e^{b_n}}=\frac{F_n(a_n)}{e^{a_n}}.
\]
Thus if we set
\[
G_n(x)=\frac{F_n(x)}{e^x},
\]
then for each \( n \) we have
\[
G_n(a_n)=G_n(b_n).
\]

Since \(G_n\) is a smooth function on \((-1,1)\) and \(a_n<b_n\), the Mean Value (or Rolle’s) Theorem implies that there exists some point \(c_n\) between \(a_n\) and \(b_n\) (that is, \(c_n\in(a_n,b_n)\)) such that
\[
G_n'(c_n)=0.
\]

Let us now compute the derivative \(G_n'(x)\). By the quotient rule we have
\[
G_n'(x)=\frac{F_n'(x)e^x-F_n(x)e^x}{e^{2x}}=\frac{F_n'(x)-F_n(x)}{e^x}.
\]
Recall that
\[
F_n(x)=\sum_{k=0}^n f^{(k)}(x)
\]
so that its derivative is
\[
F_n'(x)=\sum_{k=0}^n f^{(k+1)}(x)=\sum_{k=1}^{n+1} f^{(k)}(x).
\]
Therefore,
\[
F_n'(x)-F_n(x)=\Biggl(\sum_{k=1}^{n+1} f^{(k)}(x)\Biggr)-\Biggl(\sum_{k=0}^{n} f^{(k)}(x)\Biggr)
=\;f^{(n+1)}(x)-f(x).
\]
Inserting this into the expression for \(G_n'(x)\), we find that for the point \(c_n\) we have
\[
G_n'(c_n)=\frac{f^{(n+1)}(c_n)-f(c_n)}{e^{c_n}}=0.
\]
Since \(e^{c_n}\neq 0\) we deduce that
\[
f^{(n+1)}(c_n)=f(c_n).
\]
It is given that
\[
\lim_{n\to\infty}a_n=\lim_{n\to\infty}b_n=c\quad \text{with } c\in(-1,1).
\]
Because \(c_n\) lies between \(a_n\) and \(b_n\), it follows that
\[
\lim_{n\to\infty}c_n=c.
\]
Moreover, since \(f\) is smooth (in fact, \(C^\infty\)) with all its derivatives uniformly bounded, we may pass to the limit in the identity
\[
f^{(n+1)}(c_n)=f(c_n)
\]
to obtain
\[
\lim_{n\to\infty} f^{(n+1)}(c_n) = \lim_{n\to\infty} f(c_n)=f(c).
\]
Finally, by reindexing (or noticing that the index “\(n+1\)” plays no essential role), we conclude that
\[
\boxed{\lim_{n\to\infty} f^{(n)}(c) = f(c).}
\]

Thus, under the given hypothesis, if the endpoints \(a_n\) and \(b_n\) tend to \(c\), then the \(n\)th derivative of \(f\) at \(c\) converges to \(f(c)\).
```