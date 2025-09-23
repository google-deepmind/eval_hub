```markdown
# Solution

We recognize the given identity

\[
\Bigl(\int_a^b g(x)\,f(x)^2\,dx\Bigr)^2
=
\Bigl(\int_a^b f(x)^2\,dx\Bigr)\,
\Bigl(\int_a^b g(x)^2\,f(x)^2\,dx\Bigr)
\]

as the equality case in the Cauchy–Schwarz inequality in the weighted space \(L^2([a,b],w\,dx)\) with weight
\[
w(x)=f(x)^2\ge0.
\]
Indeed, Cauchy–Schwarz gives
\[
\Bigl\langle g,w\Bigr\rangle^2
\;\le\;
\|g\|^2\,\|w\|^2
\;\Longleftrightarrow\;
\Bigl(\!\int_a^b g\,w\Bigr)^2
\le
\Bigl(\!\int_a^b g^2\,w\Bigr)
\Bigl(\!\int_a^b w\Bigr),
\]
and equality holds precisely when \(g\) and \(w\) are linearly dependent almost everywhere:
\[
g(x)\,w(x) = C\,w(x)
\quad\text{for some constant }C.
\]

Since \(w(x)=f(x)^2=0\) exactly on the set \(\{x:f(x)=0\}\), the condition
\[
g(x)\,w(x)=C\,w(x)
\]
is equivalent to
\[
\boxed{%
g(x)=C,\quad\forall\,x\text{ with }f(x)\neq0.
}
\]
On the zero–set \(\{x:f(x)=0\}\) the identity places no further integral constraint, but continuity of \(g\) on \([a,b]\) forces
\[
g(x)=C
\quad
\text{at every boundary point of }\{f=0\}.
\]
Inside any open interval on which \(f\equiv0\), the function \(g\) may be chosen arbitrarily (subject only to matching the value \(C\) at the ends).

---

## Final Description of All Continuous Solutions

All continuous functions \(g:[a,b]\to\Bbb R\) satisfying  
\[
\Bigl(\int_a^b g\,f^2\Bigr)^2
=
\Bigl(\int_a^b f^2\Bigr)\,
\Bigl(\int_a^b g^2\,f^2\Bigr)
\]
are exactly those of the form
\[
\boxed{%
g(x)=C+h(x),
}
\]
where
- \(C\in\Bbb R\) is an arbitrary constant,  
- \(h\in C([a,b])\) satisfies  
  \[
    h(x)=0\quad\text{for all }x\text{ such that }f(x)\neq0.
  \]
Equivalently,
\[
g(x)=C\text{ on }\{f\neq0\},
\]
and on each connected component of \(\{f=0\}\) one may let \(g\) vary continuously so long as it takes the value \(C\) at the endpoints of that component.
```