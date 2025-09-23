

To determine the probability that all vertex angles of a convex 2025-gon formed by 2025 randomly chosen points on a circle are obtuse, we need to analyze the relationship between the arcs subtended by consecutive points and the interior angles of the polygon.

1. **Interior Angles and Arcs**: For a cyclic polygon, the interior angle at each vertex is half the measure of the arc opposite to that vertex. Specifically, for three consecutive points \(P_{i-1}\), \(P_i\), and \(P_{i+1}\), the interior angle at \(P_i\) is half the measure of the arc from \(P_{i-1}\) to \(P_{i+1}\) not containing \(P_i\). This angle is obtuse if and only if the measure of this arc is greater than 180 degrees, which translates to the sum of the arcs between \(P_{i-1}\) and \(P_i\) and between \(P_i\) and \(P_{i+1}\) being less than half the circumference of the circle.

2. **Spacings Between Points**: The points \(P_1, P_2, \ldots, P_{2025}\) are uniformly and independently distributed on the circle. The spacings between consecutive points (denoted \(X_1, X_2, \ldots, X_{2025}\)) follow a Dirichlet distribution with parameters all equal to 1. The key condition for all angles to be obtuse is that the sum of any two consecutive spacings \(X_i + X_{i+1}\) must be less than 1/2 (considering the circle as a unit circumference).

3. **Probability Analysis**: For large \(n\) (specifically \(n = 2025\)), the spacings between points become very small. The maximum spacing between any two consecutive points is approximately \(\log n / n\), which is extremely small for large \(n\). Consequently, the sum of any two consecutive spacings is also very small, much less than 1/2. This implies that the probability that any two consecutive spacings sum to more than 1/2 is effectively zero.

4. **Conclusion**: Given the large number of sides (2025), the probability that all pairs of consecutive spacings sum to less than 1/2 approaches 1. This is due to the fact that the spacings are highly concentrated around their mean value, making the occurrence of any spacing pair exceeding 1/2 astronomically unlikely.

Thus, the probability that all vertex angles of the convex 2025-gon are obtuse is \(\boxed{1}\).