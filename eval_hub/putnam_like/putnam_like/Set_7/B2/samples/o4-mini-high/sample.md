```markdown
**Solution.**  
Let
\[
R(f)\;=\;\frac{\displaystyle\int_0^1|f(x)|\,dx}
{\displaystyle\Bigl(\int_0^1|f(x)|^2\,dx\Bigr)^{1/2}}.
\]
By the Cauchy–Schwarz inequality with the constant function \(1\), we have
\[
\int_0^1|f(x)|\,dx
\;=\;\int_0^1 1\cdot |f(x)|\,dx
\;\le\;\Bigl(\int_0^1 1^2\,dx\Bigr)^{1/2}
\Bigl(\int_0^1|f(x)|^2\,dx\Bigr)^{1/2}
=1\cdot\Bigl(\!\int_0^1|f(x)|^2\,dx\Bigr)^{1/2}.
\]
Hence
\[
R(f)\;\le\;1
\quad\text{for every }f\in\Cal C([0,1])\text{ with }f(0)=0.
\]
It remains to show the supremum is actually \(1\).  For each integer \(n\ge1\), define the continuous function
\[
f_n(x)
=\begin{cases}
n\,x,&0\le x\le\frac1n,\\
1,&\frac1n\le x\le1,
\end{cases}
\]
so that \(f_n(0)=0\).  Then
\[
\int_0^1|f_n|\,dx
=\int_0^{1/n}n\,x\,dx+\int_{1/n}^1 1\,dx
=\frac{1}{2n}+1-\frac1n
=1-\frac{1}{2n},
\]
and
\[
\int_0^1|f_n|^2\,dx
=\int_0^{1/n}n^2x^2\,dx+\int_{1/n}^1 1\,dx
=\frac{1}{3n}+1-\frac1n
=1-\frac{2}{3n}.
\]
Therefore
\[
R(f_n)
=\frac{1-\tfrac1{2n}}{\sqrt{\,1-\tfrac{2}{3n}\,}}
\;\longrightarrow\;1
\quad\text{as }n\to\infty.
\]
We conclude
\[
\sup_{f\in\Cal F}R(f)=1.
\]
```