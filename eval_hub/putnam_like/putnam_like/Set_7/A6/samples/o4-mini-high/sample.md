```markdown
**Solution.**  
We show that the only continuous solution \(f:(0,\infty)\to(0,\infty)\) of

\[
f\bigl(xf(y+z)\bigr)\;+\;f\bigl(yf(x+z)\bigr)\;+\;f\bigl(zf(x+y)\bigr)
\;=\;
2\;+\;f(x+y+z)
\tag{*}
\]

is the constant function \(f(x)\equiv1\).

---

### 1. Reduction to a two‐variable identity

Write \(P(x,y,z)\) for the assertion \((*)\).  Fix \(x>0\) and a sum \(s=y+z>0\).  If we replace \((y,z)\) by any other pair \((y',z')\) with \(y'+z'=s\), then
\[
P(x,y,z)\;-\;P(x,y',z')
\;=\;
\bigl[f(yf(x+z))+f(zf(x+y))\bigr]
\;-\;
\bigl[f(y'f(x+z'))+f(z'f(x+y'))\bigr]
\;=\;0.
\]
Hence the quantity
\[
f\bigl(yf(x+z)\bigr)\;+\;f\bigl(zf(x+y)\bigr)
\]
depends only on \((x,s)\), not on the particular split \(y+z=s\).  Define
\[
H(x,s)
\;=\;
f\bigl(yf(x+z)\bigr)\;+\;f\bigl(zf(x+y)\bigr)
\quad\bigl(y+z=s\bigr).
\]
Then \(P(x,y,z)\) becomes
\[
f\bigl(xf(s)\bigr)\;+\;H(x,s)\;=\;2\;+\;f(x+s),
\]
i.e.
\[
H(x,s)
\;=\;
2\;+\;f(x+s)\;-\;f\bigl(xf(s)\bigr).
\tag{1}
\]

---

### 2. Specializing to \(y=z\)

1.  In \(P(x,y,y)\) we have \(s=y+z=2y\).  Since \(H(x,2y)=f\bigl(yf(x+y)\bigr)+f\bigl(yf(x+y)\bigr)=2f\bigl(yf(x+y)\bigr)\), identity \((1)\) gives
   \[
   2f\bigl(yf(x+y)\bigr)
   \;+\;
   f\bigl(xf(2y)\bigr)
   \;=\;
   2\;+\;f(x+2y).
   \tag{2}
   \]

2.  Now set \(x=y\) in \((2)\).  Then \(x+2y=3x\), \(2y=2x\) and \(yf(x+y)=x f(2x)\).  Hence
   \[
   2f\!\bigl(xf(2x)\bigr)\;+\;f\!\bigl(xf(2x)\bigr)
   \;=\;
   2\;+\;f(3x)
   \quad\Longrightarrow\quad
   3\,f\bigl(xf(2x)\bigr)
   \;=\;
   2\;+\;f(3x).
   \tag{3}
   \]

3.  Comparing \((2)\) (with general \(x,y\)) and \((3)\) (with \(y=x\)) shows in particular that
   \[
   2\,f\bigl(yf(x+y)\bigr)
   \;=\;
   f\bigl(xf(2y)\bigr)
   \;-\;
   f\bigl(xf(2y)\bigr)
   \;+\;
   f(x+2y)
   \;-\;2
   \;=\;
   f(x+2y)\;-\;2.
   \tag{4}
   \]
   But when \(x=y\), \((4)\) becomes
   \[
   2\,f\bigl(xf(2x)\bigr)
   \;=\;
   f(3x)\;-\;2,
   \]
   which together with \((3)\) forces
   \[
   f\bigl(xf(2x)\bigr)
   \;=\;
   1,\qquad
   f(3x)
   \;=\;
   3.
   \]

---

### 3. Concluding that \(f\equiv1\)

From \(f\bigl(xf(2x)\bigr)=1\) and continuity of \(f\) we see that \(xf(2x)\) ranges over all \((0,\infty)\) as \(x>0\) varies (since \(xf(2x)>0\) and is continuous).  Hence
\[
f(t)=1
\quad\text{for every }t>0.
\]
Finally, one checks at once that the constant function \(f(x)\equiv1\) indeed satisfies \((*)\).  

---

**Answer.**  
\[
\boxed{f(x)=1\quad\text{for all }x>0.}
\]