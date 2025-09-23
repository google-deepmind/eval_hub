```markdown
**Solution.**

Define for each \(n\ge0\) the partial sum
\[
S_n(x)\;=\;\sum_{k=0}^n f^{(k)}(x),
\]
and set
\[
T_n(x)\;=\;S_n(x)\,e^{-x}.
\]
The given condition
\[
\frac{S_n(b_n)}{S_n(a_n)}
\;=\;
\frac{e^{b_n}}{e^{a_n}}
\]
is equivalent to
\[
S_n(b_n)\,e^{-b_n}
\;=\;
S_n(a_n)\,e^{-a_n},
\]
i.e.\ \(T_n(b_n)=T_n(a_n)\). Since \(a_n<b_n\), Rolle’s theorem yields
\(\xi_n\in(a_n,b_n)\) with
\[
T_n'(\xi_n)
\;=\;
0.
\]
Let us compute \(T_n'(x)\). First,
\[
S_n'(x)
=\sum_{k=0}^n f^{(k+1)}(x)
=\sum_{k=1}^{n+1}f^{(k)}(x)
=S_{n+1}(x)-f(x),
\]
hence
\[
T_n'(x)
=\bigl(S_n'(x)-S_n(x)\bigr)\,e^{-x}
=\bigl(S_{n+1}(x)-f(x)-S_n(x)\bigr)\,e^{-x}
=\bigl(f^{(n+1)}(x)-f(x)\bigr)\,e^{-x}.
\]
Thus \(T_n'(\xi_n)=0\) gives
\[
f^{(n+1)}(\xi_n)\;=\;f(\xi_n).
\]
If we shift the index by one, we obtain for each \(n\ge1\) a point
\(\zeta_n=\xi_{n-1}\in(a_{n-1},b_{n-1})\) such that
\[
f^{(n)}(\zeta_n)=f(\zeta_n),
\]
and \(\zeta_n\to c\) as \(n\to\infty\).

Finally, by hypothesis all derivatives of \(f\) are bounded by some \(M\):
\(\bigl|f^{(k)}(x)\bigr|\le M\) for all \(k\) and \(x\).  In particular
\(f^{(n)}\) is Lipschitz with constant \(M\), so
\[
\bigl|f^{(n)}(c)-f(c)\bigr|
\;\le\;
\bigl|f^{(n)}(c)-f^{(n)}(\zeta_n)\bigr|
\;+\;\bigl|f^{(n)}(\zeta_n)-f(\zeta_n)\bigr|
\;+\;\bigl|f(\zeta_n)-f(c)\bigr|.
\]
Here
\[
\bigl|f^{(n)}(c)-f^{(n)}(\zeta_n)\bigr|\le M\,|c-\zeta_n|\to0,
\quad
f^{(n)}(\zeta_n)-f(\zeta_n)=0,
\quad
f(\zeta_n)\to f(c).
\]
Hence \(\,f^{(n)}(c)\to f(c)\,\) as claimed.  
\(\quad\blacksquare\)
```