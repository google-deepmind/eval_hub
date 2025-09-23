```markdown
**Solution.**

Assume \(f:(0,1)\to\R\) is \(\CC^\infty\) and for every \(n\ge0\) the function
\[
x\;\longmapsto\;\frac{f(x)}{x^n}
\]
is increasing on \((0,1)\).  Then for each fixed \(n\) we have
\[
\Bigl(\frac{f(x)}{x^n}\Bigr)'
=\frac{f'(x)\,x^n - n\,x^{n-1}f(x)}{x^{2n}}
=\frac{x\,f'(x)-n\,f(x)}{x^{n+1}}
\;\ge\;0,
\]
so
\[
\boxed{\quad
f'(x)\;\ge\;\frac{n\,f(x)}{x}
\quad\forall\,n\ge0,\;x\in(0,1).
}
\]

Now fix any \(x_0\in(0,1)\).  If \(f(x_0)\neq0\), then letting \(n\to\infty\) forces the right‐hand side
\(\tfrac{n\,f(x_0)}{x_0}\) to diverge (to \(+\infty\) if \(f(x_0)>0\),
or to \(-\infty\) if \(f(x_0)<0\)), which is impossible since \(f'\)
is finite.  Hence
\[
f(x_0)=0
\quad\forall\,x_0\in(0,1),
\]
i.e.\ \(f\equiv0\).  In particular all its derivatives vanish, so
\[
f^{(n)}(x)=0\;\ge0
\quad\text{for every }n\ge0,\;x\in(0,1).
\]
Thus the answer is **yes**, and in fact the only solution is \(f\equiv0\).