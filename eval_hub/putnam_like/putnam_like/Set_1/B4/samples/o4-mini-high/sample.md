```markdown
**Solution.**  
Let
\[
I_n \;=\;\int_0^1 \frac{\bigl(1-\ln(1-x)\bigr)^n}{n!}\,dx.
\]
Make the change of variable
\[
t \;=\;1-\ln(1-x),
\qquad
x=1-e^{1-t},
\qquad
dx=e^{1-t}\,dt.
\]
When \(x\) goes from \(0\) to \(1\), \(t\) runs from \(1\) to \(\infty\).  Hence
\[
I_n
=\frac1{n!}\int_0^1\bigl(1-\ln(1-x)\bigr)^n\,dx
=\frac{e}{n!}\int_1^\infty t^n e^{-t}\,dt
=e\;\frac{\Gamma(n+1,1)}{\Gamma(n+1)},
\]
where
\(\displaystyle\Gamma(n+1,1)=\int_1^\infty t^n e^{-t}\,dt\)  
is the upper incomplete Gamma‐function.  For integer \(n\) one has the well‐known expansion
\[
\Gamma(n+1,1)
=n!\,e^{-1}\sum_{k=0}^n\frac{1}{k!},
\]
so
\[
I_n
=e\;\frac{n!\,e^{-1}\sum_{k=0}^n\frac1{k!}}{n!}
=\sum_{k=0}^n\frac1{k!}.
\]
Therefore
\[
\lim_{n\to\infty}I_n
=\sum_{k=0}^{\infty}\frac1{k!}
=e.
\]
```