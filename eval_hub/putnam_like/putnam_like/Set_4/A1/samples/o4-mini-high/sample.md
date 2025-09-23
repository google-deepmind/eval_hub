```markdown
**Solution.**

Define the auxiliary function
\[
u(x)\;=\;f(x)\,e^{g(x)}.
\]
A direct computation gives
\[
u'(x)
= f'(x)e^{g(x)} + f(x)\,g'(x)\,e^{g(x)}
= e^{g(x)}\bigl[f'(x)+f(x)g'(x)\bigr]
= e^{g(x)}\,g'(x)\,\Bigl(\frac{f'(x)}{g'(x)}+f(x)\Bigr).
\]
By hypothesis,
\[
\lim_{x\to\infty}\Bigl(\frac{f'(x)}{g'(x)}+f(x)\Bigr)=0.
\]
Hence for any \(\varepsilon>0\) there exists \(X\) such that
\(\bigl|\tfrac{f'(t)}{g'(t)}+f(t)\bigr|<\varepsilon\) for all \(t\ge X\).  
For \(x\ge X\) we integrate from \(X\) to \(x\):
\[
u(x)-u(X)
= \int_X^x u'(t)\,dt
= \int_X^x e^{g(t)}\,g'(t)\,\Bigl(\tfrac{f'(t)}{g'(t)}+f(t)\Bigr)\,dt
= \int_X^x \Bigl(\tfrac{f'(t)}{g'(t)}+f(t)\Bigr)\,d\!\bigl(e^{g(t)}\bigr).
\]
Since \(\bigl|\tfrac{f'(t)}{g'(t)}+f(t)\bigr|<\varepsilon\) on \([X,x]\), it follows
\[
\bigl|u(x)-u(X)\bigr|
\le \varepsilon\;\bigl|\,e^{g(x)}-e^{g(X)}\bigr|.
\]
Hence
\[
|f(x)|\,e^{g(x)} = |u(x)|
\le |u(X)| + \varepsilon\bigl|e^{g(x)}-e^{g(X)}\bigr|
\le \varepsilon\,e^{g(x)} + \bigl(|u(X)|+\varepsilon\,e^{g(X)}\bigr).
\]
Dividing by \(e^{g(x)}\) and letting \(x\to\infty\) (so that the constant term over \(e^{g(x)}\) vanishes) gives
\[
|f(x)| \;\le\; \varepsilon + o(1).
\]
Since \(\varepsilon>0\) was arbitrary, we conclude
\[
\lim_{x\to\infty}f(x)\;=\;0.
\]
```