**Solution.**

We show that the only continuous \(f:\Bbb R^+\to\Bbb R^+\) satisfying
\[
\frac{f(x)+f(y)}{f(xy)} \;=\;\frac1{f(x+y)} \;-\;2xy
\]
is 
\[
f(x)=\frac1{x^2}.
\]

---

1.  **Reduction to an auxiliary function.**  
    Set 
    \[
      h(x)=x^2\,f(x)\,,\qquad x>0.
    \]
    Then
    \[
      f(x)=\frac{h(x)}{x^2},\quad
      f(y)=\frac{h(y)}{y^2},\quad
      f(xy)=\frac{h(xy)}{x^2y^2},
    \]
    so
    \[
      \frac{f(x)+f(y)}{f(xy)}
      =\frac{\tfrac{h(x)}{x^2}+\tfrac{h(y)}{y^2}}{\tfrac{h(xy)}{x^2y^2}}
      =\frac{x^2\,h(y)+y^2\,h(x)}{h(xy)}.
    \]
    On the other hand,
    \[
      \frac1{f(x+y)}-2xy
      =\frac{(x+y)^2}{h(x+y)}-2xy.
    \]
    Hence the functional equation becomes
    \[
      \frac{x^2h(y)+y^2h(x)}{h(xy)}
      =\frac{(x+y)^2}{h(x+y)}-2xy,
    \]
    or equivalently
    \[
      h(x+y)\,\bigl[x^2h(y)+y^2h(x)+2xy\,h(xy)\bigr]
      =(x+y)^2\,h(xy).
    \]

2.  **Specializing \(y=x\).**  
    Put \(y=x\).  Then
    \[
      h(2x)\,\bigl[2x^2h(x)+2x^2h(x)\bigr]
      =(2x)^2\,h(x^2)
      \;\Longrightarrow\;
      4x^2\,h(x)\,h(2x)
      =4x^2\,h(x^2)\,h(2x).
    \]
    Since \(x>0\) and \(h(2x)>0\), we conclude
    \[
      h(x^2)=h(x)\quad\text{for all }x>0.
    \]
    By continuity this forces \(h\) to be constant, say \(h(x)\equiv k>0\).

3.  **Determining the constant.**  
    If \(h(x)\equiv k\) then \(f(x)=k/x^2\).  Substituting into the original equation gives
    \[
       \frac{\tfrac k{x^2}+\tfrac k{y^2}}{\tfrac k{x^2y^2}}
       =x^2+y^2,\quad
       \frac1{f(x+y)}-2xy=(x+y)^2-2xy=x^2+y^2,
    \]
    so both sides agree if and only if \(k=1\).  

Hence the unique continuous solution is
\[
\boxed{f(x)=\frac1{x^2}\quad(x>0).}
\]