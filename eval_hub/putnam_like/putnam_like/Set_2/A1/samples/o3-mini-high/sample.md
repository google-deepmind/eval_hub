```markdown
We want to show that there exist real numbers \(a\) and \(b\), not both zero (i.e. \(a^2+b^2\neq 0\)), such that
\[
\det(aA+bB)=0,
\]
where \(A\) and \(B\) are invertible square matrices of size \(2n+1\) (with \(n\geq 1\)).

A convenient way to prove this is to consider the one-parameter family of matrices obtained by setting \(b=1\) and writing
\[
M(t) = tA + B,
\]
where \(t\) runs through the real numbers. Since both \(A\) and \(B\) are fixed matrices, the function
\[
p(t) = \det(tA + B)
\]
is a polynomial in the parameter \(t\).

Recall that the determinant is a homogeneous polynomial of degree equal to the size of the matrix. Since \(tA+B\) is a linear combination of \(A\) and \(B\), it follows that
\[
p(t)
\]
is a polynomial of degree \(2n+1\). In particular, the degree is odd.

An important property of real polynomials is that any real polynomial of odd degree must have at least one real root. Thus, there exists some
\[
t_0 \in \mathbb{R}
\]
such that
\[
p(t_0) = \det(t_0A+B)=0.
\]

Setting \(a=t_0\) and \(b=1\), we have found real numbers \(a\) and \(b\) (with \(a^2+b^2 \neq 0\)) for which
\[
\det(aA+bB)=0.
\]

Alternatively, one may notice that the determinant function
\[
(a,b) \mapsto \det(aA+bB)
\]
is homogeneous of degree \(2n+1\) and satisfies the property
\[
\det(-aA-bB)=(-1)^{2n+1}\det(aA+bB)=-\det(aA+bB).
\]
Thus, if we restrict our attention to the unit circle in \(\mathbb{R}^2\),
\[
S^1=\{(a,b)\in \mathbb{R}^2 : a^2+b^2=1\},
\]
this function is odd. The intermediate value theorem (or more generally, topological arguments like the Borsuk-Ulam theorem) then ensures that the function must vanish for some \((a,b)\in S^1\). This again shows that there exist \(a\) and \(b\), not both zero, such that \(\det(aA+bB)=0\).

Thus, the answer to the problem is:

Yes, there exist real numbers \(a\) and \(b\) with \(a^2+b^2\neq 0\) such that \(\det(aA+bB)=0\).
```