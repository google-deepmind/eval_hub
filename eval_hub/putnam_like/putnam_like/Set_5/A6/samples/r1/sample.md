

To solve the problem of finding the infimum of the circumradius \( r(P, Q) \) of triangle \( PQR \) where \( P \) and \( Q \) are points on the hyperbola \( \mathcal{H} = \left\{ (x, y) \in \mathbb{R}^2 : y = \frac{1}{x}, x > 0, y > 0 \right\} \), and \( R \) is the intersection of the tangents at \( P \) and \( Q \):

1. **Parameterize Points**: Let \( P = (a, \frac{1}{a}) \) and \( Q = (b, \frac{1}{b}) \) with \( a \neq b \).
2. **Tangent Equations**: The tangent at \( P \) is \( y = -\frac{x}{a^2} + \frac{2}{a} \) and at \( Q \) is \( y = -\frac{x}{b^2} + \frac{2}{b} \).
3. **Intersection Point \( R \)**: Solving the tangent equations, \( R \) is found to be \( \left( \frac{2ab}{a + b}, \frac{2}{a + b} \right) \).
4. **Symmetry Consideration**: Assume \( P = (a, \frac{1}{a}) \) and \( Q = (\frac{1}{a}, a) \), reflecting symmetry over \( y = x \).
5. **Circumradius Calculation**: Using coordinates of \( P, Q, R \), compute the distances and area. The circumradius formula for three points shows that the radius simplifies to \( \frac{\sqrt{2}}{2a} \cdot \frac{1 + a^4}{a^2 + 1} \).
6. **Minimization**: Analyze the behavior as \( a \to 1 \), leading to the conclusion that the infimum is achieved in the symmetric case as \( a \) approaches 1, yielding the minimal radius.

**Final Answer**:
\[
\boxed{\sqrt{2}}
\]