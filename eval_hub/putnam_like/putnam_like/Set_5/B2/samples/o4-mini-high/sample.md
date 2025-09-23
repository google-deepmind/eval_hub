```markdown
# Solution

We are given two invertible \(n\times n\) matrices \(A\) and \(B\) such that
\[
A + B = I,
\qquad
A^4 + B^4 = I.
\]
Set
\[
B = I - A.
\]
Then
\[
A^4 + (I - A)^4 = I.
\]
Expand \((I-A)^4\):
\[
(I - A)^4
= I - 4A + 6A^2 - 4A^3 + A^4.
\]
Hence
\[
A^4 + \bigl(I - 4A + 6A^2 - 4A^3 + A^4\bigr) \;=\; I
\;\Longrightarrow\;
2A^4 - 4A^3 + 6A^2 - 4A = 0.
\]
Divide by 2:
\[
A^4 - 2A^3 + 3A^2 - 2A = 0
\;\Longrightarrow\;
A\bigl(A^3 - 2A^2 + 3A - 2I\bigr)=0.
\]
Since \(A\) is invertible, we may cancel \(A\):
\[
A^3 - 2A^2 + 3A - 2I = 0.
\]
Factor the cubic polynomial:
\[
A^3 - 2A^2 + 3A - 2I
= (A - I)\,(A^2 - A + 2I)
= 0.
\]
Again, \(B=I-A\) is invertible, so \(A-I\) is invertible.  Hence
\[
A^2 - A + 2I = 0
\;\Longrightarrow\;
A^2 - A = -2I.
\]
But
\[
AB = A\,(I - A) = A - A^2 = 2I.
\]
Therefore
\[
\det(AB) = \det(2I) = 2^n.
\]
Answer:  
\[
\boxed{\det(AB) = 2^n.}
\]
```