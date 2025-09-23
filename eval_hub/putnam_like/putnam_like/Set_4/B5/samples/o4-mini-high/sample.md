```markdown
**Solution.**

We shall show that any solution of
\[
f\bigl(f(z_1)+z_2\bigr)=z_1+f(z_2)
\qquad\forall\,z_1,z_2\in V
\tag{*}
\]
is a \(\mathbb{Q}\)‑linear involution, and conversely that every such involution satisfies \((*)\).

1. Bijectivity and \(f(0)=0\).  
   –  Setting \(z_2=0\) in \((*)\) gives
   \[
     f\bigl(f(z_1)\bigr)=z_1+f(0).
   \]
   –  Setting \(z_1=0\) in \((*)\) gives
   \[
     f\bigl(f(0)+z_2\bigr)=f(z_2).
   \]
   Injectivity then forces \(f(0)=0\), and hence
   \[
     f\bigl(f(z)\bigr)=z,
   \]
   so \(f\) is bijective and involutive.

2. Additivity.  
   Replace \(z_1\) by \(f(z_1)\) in \((*)\):
   \[
     f\bigl(f(f(z_1))+z_2\bigr)
     =f(z_1)+f(z_2).
   \]
   Since \(f(f(z_1))=z_1\), this yields
   \[
     f(z_1+z_2)=f(z_1)+f(z_2),
   \]
   i.e.\ \(f\) is additive.

3. \(\mathbb{Q}\)‑homogeneity.  
   By additivity one checks by induction
   \(\;f(n\,x)=n\,f(x)\) for \(n\in\mathbb{Z}\).  Since \(V\) is a
   \(\mathbb{Q}\)‑space, for \(n\neq0\) one writes
   \(\,x=\;n\cdot\bigl(\tfrac1n x\bigr)\) and finds
   \[
     f\Bigl(\tfrac1n x\Bigr)=\tfrac1n f(x),
     \quad
     f\Bigl(\tfrac m n x\Bigr)=\tfrac m n\,f(x).
   \]
   Hence \(f\) is \(\mathbb{Q}\)‑linear.

4. Conclusion.  
   Combining involutivity \(f(f(x))=x\) with \(\mathbb{Q}\)‑linearity
   shows immediately
   \[
     f\bigl(f(z_1)+z_2\bigr)
     =f(f(z_1))+f(z_2)
     =z_1+f(z_2),
   \]
   so every \(\mathbb{Q}\)‑linear involution is a solution.  Conversely,
   any solution must satisfy the above steps.

**Answer.**  
The general solution is
\[
\boxed{
\text{\(f:V\to V\) is any \(\mathbb{Q}\)‑linear map with }f^2=\mathrm{id}_V.
}
\]
Equivalently, choosing a direct‑sum decomposition \(V=U\oplus W\), one may write
\[
  f(u+w)=u-w,
  \quad u\in U,\;w\in W,
\]
which indeed satisfies \((*)\).
```