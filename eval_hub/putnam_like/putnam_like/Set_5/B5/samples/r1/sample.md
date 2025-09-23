

To find the number of zeros of the polynomial \( P(z) = z^8 - 5z^3 + 10 \) in the set \( A = \{ z \in \mathbb{C} \,:\, \frac{\pi}{2} \leq \arg z \leq \pi \} \), we use the Argument Principle on a contour that bounds the region \( A \).

1. **Contour Setup**:
   - Consider a large sector of radius \( R \) with angles from \( \frac{\pi}{2} \) to \( \pi \).
   - The contour consists of three parts:
     1. The line segment from \( 0 \) to \( iR \) along the positive imaginary axis.
     2. The arc from \( iR \) to \( -R \) along the circle of radius \( R \).
     3. The line segment from \( -R \) back to \( 0 \) along the negative real axis.

2. **Behavior on the Arc**:
   - For large \( R \), \( P(z) \approx z^8 \) dominates.
   - The argument of \( P(z) \) changes by \( 8\theta \) as \( \theta \) varies from \( \frac{\pi}{2} \) to \( \pi \).
   - The total change in argument is \( 8(\pi - \frac{\pi}{2}) = 4\pi \), contributing \( \frac{4\pi}{2\pi} = 2 \) to the count.

3. **Behavior on the Positive Imaginary Axis**:
   - \( z = iy \) ( \( y \) from 0 to \( R \) ), \( P(z) = y^8 + 5iy^3 + 10 \).
   - Both real and imaginary parts are positive, leading to a negligible net change in argument.

4. **Behavior on the Negative Real Axis**:
   - \( z = x \) ( \( x \) from \( -R \) to 0 ), \( P(z) = x^8 + 5|x|^3 + 10 \).
   - \( P(z) \) is always positive real, leading to no change in argument.

5. **Total Change in Argument**:
   - The dominant contribution comes from the arc, giving a total change of \( 4\pi \).
   - By the Argument Principle, the number of zeros inside the contour is \( \frac{4\pi}{2\pi} = 2 \).

Thus, the number of zeros of \( P(z) \) in the set \( A \) is \(\boxed{2}\).