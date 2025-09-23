```markdown
**Solution.**  
Set 
\[
A = 2 + \sqrt{5}, 
\quad B = 2 - \sqrt{5}.
\]
Then \(A+B=4\) and \(AB=-1\), and one checks easily that the sequence
\[
U_k \;=\; A^k + B^k
\]
satisfies the integer recurrence
\[
U_k \;=\; 4\,U_{k-1} + U_{k-2}, 
\quad U_0=2,\;U_1=4,
\]
hence \(U_k\in\mathbb{Z}\) for all \(k\).  Moreover, since 
\[
|B| = |2-\sqrt5| < 1,
\]
we have \(0 < B^{2n} < 1\) for every positive integer \(n\).  It follows that
\[
A^{2n} = U_{2n} - B^{2n}
\]
is strictly less than the integer \(U_{2n}\) but greater than \(U_{2n}-1\).  Therefore the smallest integer exceeding \(A^{2n}\) is
\[
\bigl\lceil A^{2n}\bigr\rceil \;=\; U_{2n}
\;=\; A^{2n} + B^{2n}
\;=\; (2+\sqrt5)^{2n} + (2-\sqrt5)^{2n}.
\]
In conclusion,

\[
\boxed{\;
\bigl\lceil (\sqrt5+2)^{2n}\bigr\rceil
\;=\;
(2+\sqrt5)^{2n} + (2-\sqrt5)^{2n}.
\;} 
\]
```