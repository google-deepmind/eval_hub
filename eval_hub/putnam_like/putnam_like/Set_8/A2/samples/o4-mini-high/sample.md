```markdown
**Solution.**  
We look for a conic of the form
\[
F(x,y)\;=\;A x^2 + B\,x y + C y^2 + D x + E y + F \;=\;0
\]
which is tangent to the lines \(y=0\) at \((\alpha,0)\) and \(x=0\) at \((0,\beta)\), and which is a parabola (i.e.\ its discriminant \(B^2-4AC=0\)).

---

1.  Tangency at \((\alpha,0)\) to \(y=0\) means
   - \(F(\alpha,0)=0\), 
   - the tangent‐line condition \(F_x(\alpha,0)=0\),
   - and \(F_y(\alpha,0)\neq0\) (so the tangent is indeed \(y=0\)).  
   Writing these out:
   \[
   F(\alpha,0)=A\alpha^2 + D\alpha + F = 0,\qquad
   F_x(\alpha,0)=2A\alpha + D = 0.
   \]

2.  Tangency at \((0,\beta)\) to \(x=0\) means
   - \(F(0,\beta)=0\),
   - \(F_y(0,\beta)=0\),
   - and \(F_x(0,\beta)\neq0\).  
   That is
   \[
   F(0,\beta)=C\beta^2 + E\beta + F = 0,\qquad
   F_y(0,\beta)=2C\beta + E = 0.
   \]

3.  The parabola condition is
   \[
   B^2 - 4AC \;=\;0.
   \]

---

From 
\[
2A\alpha + D=0\;\Longrightarrow\;D=-2A\alpha,\quad
A\alpha^2+D\alpha+F=0\;\Longrightarrow\;F=A\alpha^2,
\]
and
\[
2C\beta + E=0\;\Longrightarrow\;E=-2C\beta,\quad
C\beta^2+E\beta+F=0\;\Longrightarrow\;F=C\beta^2,
\]
we get \(A\alpha^2=C\beta^2\), so one may set
\[
A=\mu\,\beta^2,\quad C=\mu\,\alpha^2,\quad
D=-2\mu\,\beta^2\alpha,\quad E=-2\mu\,\alpha^2\beta,\quad
F=\mu\,\alpha^2\beta^2,
\]
for some scale factor \(\mu\ne0\).  The remaining free parameter is \(B\).  Imposing
\[
B^2-4AC=0
\quad\Longrightarrow\quad
B^2=4\,A\,C=4\,\mu^2\,\alpha^2\beta^2
\quad\Longrightarrow\quad
B=\pm2\mu\,\alpha\beta,
\]
one finds that—up to an overall scale—the unique solution is
\[
x^2-\frac{2\alpha}{\beta}\,x y+\frac{\alpha^2}{\beta^2}\,y^2
\;-\;2\alpha\,x\;+\;\frac{2\alpha^2}{\beta}\,y\;+\;\alpha^2
\;=\;0.
\]
But this factors at once as a double line:
\[
\boxed{\;\bigl(x-\tfrac{\alpha}{\beta}\,y-\alpha\bigr)^2 \;=\;0\,.}
\]
In other words, the only “parabola’’ meeting those two tangency‐conditions is the **degenerate** one (a doubled straight line).  There is **no** non‑degenerate parabola tangent to \(y=0\) at \((\alpha,0)\) and to \(x=0\) at \((0,\beta)\). 
```

**Answer.**  
The only solution is the degenerate conic  
\[
\bigl(x-\tfrac{\alpha}{\beta}y-\alpha\bigr)^2=0,
\]
so there is no genuine (non‑degenerate) parabola with the prescribed tangencies.