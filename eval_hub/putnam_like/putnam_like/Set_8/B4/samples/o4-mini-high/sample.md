```markdown
**Solution**

Let
\[
U = -\ln X,\qquad V = -\ln Y.
\]
Since \(X,Y\sim\mathrm{Uniform}(0,1)\) independently, \(U\) and \(V\) are i.i.d. \(\mathrm{Exp}(1)\).  Note
\[
\frac{\ln X}{\ln Y}
=\frac{-U}{-V}
=\frac{U}{V}.
\]
We seek
\[
P\bigl(\lfloor U/V\rfloor\text{ is even}\bigr)
=\sum_{k=0}^\infty P\bigl(U/V\in[2k,2k+1)\bigr).
\]
The density of \(R=U/V\) is
\[
f_R(r)=\int_0^\infty w\,e^{-(r+1)w}\,dw
=\frac1{(1+r)^2},\quad r\ge0.
\]
Hence
\[
P\bigl(U/V\in[2k,2k+1)\bigr)
=\int_{2k}^{2k+1}\frac{dr}{(1+r)^2}
=\frac1{2k+1}-\frac1{2k+2}.
\]
Summing over \(k\ge0\) gives a telescoping series:
\[
\sum_{k=0}^\infty\Bigl(\frac1{2k+1}-\frac1{2k+2}\Bigr)
=\ln2.
\]
Therefore the desired probability is
\[
\boxed{\ln2}.
\]
```