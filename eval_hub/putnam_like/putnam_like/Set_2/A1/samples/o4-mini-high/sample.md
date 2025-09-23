```markdown
**Solution.**  
Let \(A,B\in M_{2n+1}(\Bbb R)\) be invertible.  We consider the homogeneous polynomial
\[
P(a,b)\;=\;\det\bigl(aA + bB\bigr)\,,
\]
in the real variables \((a,b)\).  Since \(\det\) is multilinear in the rows and there are \(2n+1\) rows, \(P(a,b)\) is a homogeneous polynomial of degree \(2n+1\), which is odd.

To see that \(P\) must vanish for some real \((a,b)\neq(0,0)\), we argue in one of two equivalent ways:

1. **Projective‐line / Antipodal argument.**  
   Restrict \(P\) to the unit circle \(\{(a,b)\colon a^2+b^2=1\}\).  Define
   \[
     g(a,b)=P(a,b)\quad\text{with}\;a^2+b^2=1.
   \]
   Since \(P\) is homogeneous of odd degree,
   \[
     g(-a,-b)\;=\;P(-a,-b)\;=\;(-1)^{2n+1}P(a,b)\;=\;-\,P(a,b)\;=\;-\,g(a,b).
   \]
   Hence \(g\) takes opposite values at antipodal points on the circle.  By continuity, there must be some \((a_0,b_0)\) on the circle with
   \[
     g(a_0,b_0)\;=\;0,
   \]
   i.e. \(\det(a_0A + b_0B)=0\) and \(a_0^2+b_0^2=1\neq0\).

2. **One‐variable polynomial argument.**  
   If \(a\neq0\), set \(t=\tfrac b a\).  Then
   \[
     \det(aA+bB)
     \;=\;a^{2n+1}\,\det\!\bigl(A + tB\bigr)
     \;=\;a^{2n+1}\,f(t),
   \]
   where
   \[
     f(t)=\det\bigl(A+tB\bigr)
   \]
   is a real polynomial of degree \(2n+1\).  Any real polynomial of odd degree has at least one real root \(t_0\).  For that \(t_0\) we get
   \(\det(A+t_0B)=0,\) so choosing \(a=1\), \(b=t_0\) gives
   \(\det(A + t_0B)=0\) with \(1+t_0^2\neq0\).

In either approach we have found real numbers \(a,b\), not both zero, such that
\[
  \det\bigl(aA + bB\bigr)\;=\;0.
\]
Thus **yes**, such \(a,b\) always exist when \(\dim A=2n+1\) is odd.
```