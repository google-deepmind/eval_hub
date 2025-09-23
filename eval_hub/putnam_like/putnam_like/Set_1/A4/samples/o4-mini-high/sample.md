```markdown
# Solution

We claim that the group
\[
G \;=\;\bigl\langle x,\,y \mid x^n=e,\;y^2=e,\;xyxy=e\bigr\rangle,
\]
with \(n\ge3\), is isomorphic to the dihedral group of order \(2n\).  In particular \(\lvert G\rvert=2n\) and \(G\) is non‑abelian.

---

## 1. Deriving the “reflection–rotation” relation

From the relation
\[
xyxy \;=\; e,
\]
multiply on the right by \(y\) to get
\[
xyx\,=\;y^{-1}\;=\;y,
\]
since \(y^2=e\).  Hence
\[
xyx \;=\; y.
\]
Now multiply on the left by \(y\):
\[
y\,(xyx)
\;=\;
yx\;=\;
(yxy)\,x
\;=\;
x^{-1}\,x
\;=\;
e.
\]
Equivalently,
\[
y\,x\,y \;=\; x^{-1}.
\]
Rewriting gives the familiar dihedral relation
\[
y\,x \;=\; x^{-1}\,y.
\]

---

## 2. A normal‐form argument

Using the relations
\[
x^n=e,\quad y^2=e,\quad yx=x^{-1}y,
\]
any word in \(x,y\) can be rewritten (by moving each \(y\) past all \(x\)'s at the cost of inverting those \(x\)'s) into **exactly one** of the following two forms:
\[
x^k
\quad\text{or}\quad
y\,x^k,
\qquad
k=0,1,2,\dots,n-1.
\]
Thus there are **at most** \(2n\) distinct elements in \(G\).

---

## 3. Distinctness of the normal forms

Suppose, for contradiction, that for some \(0\le i,j<n\) one had
\[
x^i \;=\; y\,x^j.
\]
Then multiplying on the left by \(y\) and using \(y^2=e\) gives
\[
y\,x^i \;=\; x^j.
\]
But the left side is of the form “\(yx^\text{something}\)” while the right side is a pure power of \(x\); by uniqueness of normal forms this forces \(y\) to be trivial, contradiction.  Hence all \(2n\) normal forms are distinct, and
\[
|G|\;=\;2n.
\]

---

## 4. Non‑abelianness

Since \(n\ge3\), \(x\neq x^{-1}\).  From
\[
yx \;=\; x^{-1}y
\]
we see
\[
yx \;\neq\; xy,
\]
so \(G\) is non‑abelian.

---

## 5. Conclusion: the dihedral group

The presentation
\[
\langle x,y : x^n=e,\;y^2=e,\;yxy=x^{-1}\rangle
\]
is the standard one for the dihedral group \(D_{2n}\).  Hence
\[
G\;\cong\;D_{2n},
\]
a non‑abelian group of order \(2n\), as required.  ■