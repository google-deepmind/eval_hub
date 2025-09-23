```markdown
**Solution.**

We wish to show that
\[
t\;\longmapsto\;\|x(t)\|
\]
is (non‑strictly) increasing for every nonzero solution \(x(t)\) of
\[
\dot x(t)=A(t)\,x(t),\qquad x(0)\neq0,
\]
where
\[
A(t)=\begin{pmatrix}
1+\sin^2t & -1 & -1\\
1 & \dfrac1{1+\sin^2t} & -1\\
1 & 1 & 1+\cos^2t
\end{pmatrix}.
\]

1.  **Derivative of the norm squared.**  Recall
    \[
    \frac{d}{dt}\|x(t)\|^2
    \;=\;2\bigl\langle x(t),\,\dot x(t)\bigr\rangle
    \;=\;2\bigl\langle x(t),\,A(t)\,x(t)\bigr\rangle.
    \]
    Hence
    \[
    \frac{d}{dt}\|x(t)\|
    =\frac{1}{2\|x(t)\|}\,\frac{d}{dt}\|x(t)\|^2
    =\frac{\bigl\langle x(t),\,A(t)\,x(t)\bigr\rangle}{\|x(t)\|}.
    \]

2.  **Symmetric part of \(A(t)\).**  Let
    \[
    S(t)\;=\;\frac{A(t)+A(t)^{T}}2
    \]
    be the symmetric part of \(A(t)\).  A direct calculation shows
    \[
    S(t)
    =\frac12\begin{pmatrix}
      1+\sin^2t & -1+1 & -1+1\\[6pt]
      1-1 & \dfrac1{1+\sin^2t}+\dfrac1{1+\sin^2t} & -1+1\\[6pt]
      1-1 & 1-1 & 1+\cos^2t + 1+\cos^2t
    \end{pmatrix}
    =\begin{pmatrix}
      1+\sin^2t & 0 & 0\\
      0 & \dfrac1{1+\sin^2t} & 0\\
      0 & 0 & 1+\cos^2t
    \end{pmatrix}.
    \]
    Since \(1+\sin^2t>0\), \(1+\cos^2t>0\) and \(\frac1{1+\sin^2t}>0\) for all \(t\), the matrix \(S(t)\) is positive‐definite.  Therefore for any \(x\neq0\),
    \[
    \bigl\langle x,\,A(t)\,x\bigr\rangle
    =\bigl\langle x,\,S(t)\,x\bigr\rangle
    \;\ge\;0.
    \]

3.  **Conclusion.**  From step 1 and step 2 we deduce
    \[
    \frac{d}{dt}\|x(t)\|\;=\;\frac{\langle x(t),A(t)x(t)\rangle}{\|x(t)\|}\;\ge\;0,
    \]
    so \(t\mapsto\|x(t)\|\) is non‑decreasing on \(\Bbb R\).  This completes the proof. \(\quad\blacksquare\)
```