```markdown
**Solution.**

Define the auxiliary function
\[
g(x)\;=\;f(x)-f(0).
\]
Then \(g(0)=0\) and for every \(x\in\R\),
\[
|g'(x)| \;=\;|f'(x)| \;\le\;|f(x)-f(0)| \;=\;|g(x)|.
\]

We split the proof into two parts, for \(x\ge0\) and \(x\le0\).

---

### 1. Case \(x\ge0\)

Set
\[
H(x)\;=\;\int_0^x |g(t)|\,dt.
\]
Then \(H(0)=0\) and by the Fundamental Theorem of Calculus \(H'(x)=|g(x)|\).  The inequality \(|g'(x)|\le|g(x)|\) implies
\[
H'(x)\;\le\;H(x),
\]
or equivalently
\[
\bigl(e^{-x}H(x)\bigr)' \;=\;e^{-x}\bigl(H'(x)-H(x)\bigr)\;\le\;0.
\]
Hence \(x\mapsto e^{-x}H(x)\) is nonincreasing on \([0,\infty)\).  But at \(x=0\) we have
\[
e^{-0}H(0)=0,
\]
so for all \(x\ge0\),
\[
e^{-x}H(x)\le0
\quad\Longrightarrow\quad
H(x)\le0.
\]
Since by definition \(H(x)\ge0\), we conclude \(H(x)=0\) for all \(x\ge0\).  Therefore
\[
|g(x)| \;=\;H'(x)\;=\;0,
\]
and thus \(g(x)=0\) for every \(x\ge0\).  Equivalently,
\[
f(x)=f(0),\qquad x\ge0.
\]

---

### 2. Case \(x\le0\)

Define \(\tilde g(x)=g(-x)\).  Then \(\tilde g(0)=0\) and
\[
\tilde g'(x)=-\,g'(-x),
\]
so
\[
|\tilde g'(x)| \;=\;|g'(-x)|\;\le\;|g(-x)| \;=\;|\tilde g(x)|,
\]
for all \(x\).  By exactly the same argument as in the first case (now on \([0,\infty)\) for \(\tilde g\)) we deduce \(\tilde g(x)=0\) for \(x\ge0\).  Hence
\[
g(x)=0
\quad
\text{for all }x\le0,
\]
i.e.\ \(f(x)=f(0)\) for \(x\le0\).

---

### Conclusion

Combining both cases shows
\[
f(x)\;=\;f(0)
\quad\text{for all }x\in\R.
\]
Therefore \(f\) is constant, as required.
```