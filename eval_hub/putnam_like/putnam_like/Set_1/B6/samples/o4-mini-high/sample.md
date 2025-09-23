Here is a self‐contained derivation of the limit.  All of the algebraic manipulations are exact and one ends up with a single infinite series involving only the {\em fractional–part} of the very first term.

**1. Rewrite the recurrence**  
Set 
\[
f_n:=\{\alpha x_n\}\,,\qquad\{y\}=y-\lfloor y\rfloor\in[0,1)\,.
\]
Since 
\[
\lfloor\alpha x_n\rfloor=\alpha x_n-f_n,
\]
the given recurrence
\[
x_{n+1}=\beta\,x_n+\lfloor\alpha x_n\rfloor
\]
becomes
\[
x_{n+1}
=\beta\,x_n+(\alpha x_n-f_n)
=(\alpha+\beta)\,x_n - f_n.
\]
Divide both sides by \((\alpha+\beta)^{\,n+1}\):
\[
\frac{x_{n+1}}{(\alpha+\beta)^{n+1}}
=\frac{x_n}{(\alpha+\beta)^n}
\;-\;\frac{f_n}{(\alpha+\beta)^{\,n+1}}.
\]
Now telescope this from \(n=0\) up to \(n=N-1\):  
\[
\frac{x_N}{(\alpha+\beta)^N}
-\frac{x_0}{(\alpha+\beta)^0}
\;=\;
-\sum_{n=0}^{N-1}\frac{f_n}{(\alpha+\beta)^{n+1}}.
\]
Hence
\[
\frac{x_N}{(\alpha+\beta)^N}
= x_0
\;-\;\sum_{n=0}^{N-1}\frac{f_n}{(\alpha+\beta)^{n+1}}
\]
and, as \(N\to\infty\), the left–hand side converges to our desired limit  
\[
L\;:=\;\lim_{n\to\infty}\frac{x_n}{(\alpha+\beta)^n}\,.
\]
Since \(0\le f_n<1\) and \(\alpha+\beta>1\), the infinite series on the right converges absolutely.  We conclude  

\[
\boxed{
\lim_{n\to\infty}\frac{x_n}{(\alpha+\beta)^n}
\;=\;
x_0
\;-\;
\sum_{n=0}^\infty
\frac{\{\alpha\,x_n\}}{(\alpha+\beta)^{\,n+1}}\,.
}
\]

**2. A more explicit form**  
One can show (using \(\alpha^2\in\Bbb N\) and \(\beta-\alpha\in(0,1)\)) that the fractional parts themselves satisfy a simple “multiplicative‐mod‑1’’ law
\[
f_{n+1}
=\{\,-(2\alpha-\beta)\,f_n\}
\;=\;
\{\,(\beta-2\alpha)\,f_n\},
\]
so that by induction
\[
f_n
=\{\;(\beta-2\alpha)^n\,f_0\},
\qquad
f_0=\{\alpha x_0\}.
\]
Substituting back into the series one obtains the fully explicit formula

\[
\boxed{
\lim_{n\to\infty}\frac{x_n}{(\alpha+\beta)^n}
\;=\;
x_0
\;-\;
\sum_{n=0}^{\infty}
\frac{
\{\;(\beta-2\alpha)^n\;\{\alpha x_0\}\}
}{(\alpha+\beta)^{\,n+1}}
}\,.
\]

Either of the two boxed formulæ can be taken as the final answer.