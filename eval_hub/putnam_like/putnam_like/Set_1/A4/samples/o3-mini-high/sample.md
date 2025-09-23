```latex
\documentclass{article}
\usepackage{amsmath,amssymb}
\begin{document}

We want to show that the group
\[
G=\langle x,y : x^n=e,\; y^2=e,\; xyxy=e\rangle,
\]
with \( n\ge3 \), is a non-abelian group of order \( 2n \).

\textbf{Step 1. Simplifying the relations.}

First, note that
\[
xyxy=(xy)^2=e,
\]
so the element \( xy \) is an involution (i.e. it has order 2).

Next, we manipulate the relation \( xyxy=e \) to obtain a relation between \( x \) and \( y \). Multiply on the left by \( x^{-1} \) and on the right by \( y \):
\[
x^{-1}(xyxy)y = x^{-1}ey \quad \Longrightarrow \quad yx = x^{-1}y.
\]
This relation can be rewritten as:
\[
yx = x^{-1}y \quad \Longrightarrow \quad yxy^{-1} = x^{-1},
\]
since \( y^{-1}=y \) (because \( y^2=e \)). This is exactly the relation that appears in the standard presentation of the dihedral group.

\textbf{Step 2. Recognizing the dihedral group.}

Recall that the dihedral group of order \( 2n \) has the presentation
\[
D_{2n}=\langle r,s : r^n=e,\; s^2=e,\; srs=r^{-1}\rangle.
\]
If we set \( x=r \) and \( y=s \), the relation \( srs=r^{-1} \) becomes
\[
yxy = x^{-1},
\]
which, as we saw, is equivalent to \( yx=x^{-1}y \). Thus, we have established that
\[
G \cong D_{2n}.
\]

\textbf{Step 3. Counting the elements.}

We now show that every element of \( G \) can be written in the form
\[
x^i \quad \text{or} \quad x^iy, \quad \text{with } 0\le i < n.
\]
\textit{Proof:} Consider an arbitrary word in the generators \( x \) and \( y \). Whenever a subword of the form \( yx \) appears, we can use the relation
\[
yx=x^{-1}y
\]
to move \( y \) to the right. Repeating this process and using that \( y^2=e \), any word can be reduced to one of the above forms. Since the representations \( x^i \) (the rotations) and \( x^iy \) (the reflections) are standard and distinct in the dihedral group, there are exactly \( n+n = 2n \) elements in \( G \).

\textbf{Step 4. Non-abelianness.}

Finally, we show that \( G \) is non-abelian. Since
\[
yx=x^{-1}y,
\]
we see that if \( G \) were abelian we would need \( x^{-1}=x \), forcing \( x^2=e \). However, \( x^n=e \) with \( n\ge3 \) prevents this from happening (unless \( n=2 \), which is excluded). Thus, \( G \) is non-abelian.

\textbf{Conclusion.} We have demonstrated that
\[
G \cong D_{2n},
\]
which is a non-abelian group of order \( 2n \).

\end{document}
```