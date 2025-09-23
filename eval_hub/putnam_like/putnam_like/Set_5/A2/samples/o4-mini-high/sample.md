```markdown
## Solution

First, note that the hypothesis  
\[
a_{n+1}\le \tfrac12\,a_n
\]
implies exponential decay \(a_n=O(2^{-n})\).  In particular all the infinite sums below converge absolutely, so term–by–term manipulations are justified.

---

### 1. Rewrite the sum

We want to compute
\[
\sum_{n=1}^\infty n\,b_n
\quad\text{where}\quad
b_n = a_n \;-\;3a_{n+1}\;+\;3a_{n+2}\;-\;a_{n+3}.
\]
Break it into four series:
\[
\sum_{n=1}^\infty n\,b_n
=
\sum_{n=1}^\infty n\,a_n
\;-\;3\sum_{n=1}^\infty n\,a_{n+1}
\;+\;3\sum_{n=1}^\infty n\,a_{n+2}
\;-\;\sum_{n=1}^\infty n\,a_{n+3}.
\]
Call these sums \(S_0,S_1,S_2,S_3\) respectively:
\[
S_k \;=\;\sum_{n=1}^\infty n\,a_{n+k}, 
\qquad k=0,1,2,3.
\]

---

### 2. Shift the indices

For each \(k\), set \(m=n+k\).  Then \(n=m-k\) and as \(n\) runs from \(1\) to \(\infty\), \(m\) runs from \(k+1\) to \(\infty\).  Hence
\[
S_k
=\sum_{n=1}^\infty n\,a_{n+k}
=\sum_{m=k+1}^\infty (m-k)\,a_m.
\]
Thus
\[
\sum_{n=1}^\infty n\,b_n
=\sum_{m=1}^\infty 
\Bigl[
\underbrace{(m-0)}_{S_0}
\;-\;3\underbrace{(m-1)}_{S_1}
\;+\;3\underbrace{(m-2)}_{S_2}
\;-\;\underbrace{(m-3)}_{S_3}
\Bigr]\,a_m,
\]
where in each bracket the terms \((m-k)\) only actually appear for \(m\ge k+1\).  Define the coefficient
\[
C(m)
\;=\;
\bigl[m\bigr]
\;-\;3\bigl[m-1\bigr]
\;+\;3\bigl[m-2\bigr]
\;-\;\bigl[m-3\bigr].
\]
One checks directly:
- For \(m\ge4\), 
  \[
    C(m)
    =m-3(m-1)+3(m-2)-(m-3)
    =0.
  \]
- For \(m=3\), only the first three terms appear and again they sum to \(0\).
- For \(m=2\), 
  \[
    C(2)=2-3\cdot1= -1.
  \]
- For \(m=1\), only the first term appears:
  \[
    C(1)=1.
  \]
Hence the infinite sum collapses to just two terms:
\[
\sum_{n=1}^\infty n\,b_n
=\sum_{m=1}^\infty C(m)\,a_m
= C(1)\,a_1 \;+\;C(2)\,a_2
= a_1 - a_2.
\]

---

### Conclusion

\[
\boxed{\sum_{n=1}^\infty n\,b_n \;=\; a_1 - a_2.}
\]
This completes the proof.
```