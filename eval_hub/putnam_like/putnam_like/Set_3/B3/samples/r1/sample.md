

To investigate the convergence of the integral \(\int_0^\infty \cos(x) \cos(x^2) \, dx\), we start by using the product-to-sum trigonometric identity:

\[
\cos(x) \cos(x^2) = \frac{1}{2} \left[ \cos(x^2 + x) + \cos(x^2 - x) \right]
\]

This transforms the integral into:

\[
\frac{1}{2} \left( \int_0^\infty \cos(x^2 + x) \, dx + \int_0^\infty \cos(x^2 - x) \, dx \right)
\]

We analyze each integral separately.

### Integral \(\int_0^\infty \cos(x^2 + x) \, dx\)

For large \(x\), \(x^2 + x \approx x^2\). The integral \(\int_0^\infty \cos(x^2) \, dx\) is known to converge (Fresnel integral). Using integration by parts with \(u = \frac{1}{2x + 1}\) and \(dv = (2x + 1) \cos(x^2 + x) \, dx\), we show that the integral converges. The boundary terms vanish, and the remaining integral involves \(\sin(x^2 + x)\) divided by \((2x + 1)^2\), which converges absolutely due to the \(O(1/x^2)\) decay.

### Integral \(\int_0^\infty \cos(x^2 - x) \, dx\)

For large \(x\), \(x^2 - x \approx x^2\). Using a similar integration by parts approach with \(u = \frac{1}{2x - 1}\) and \(dv = (2x - 1) \cos(x^2 - x) \, dx\), we show convergence. The boundary terms vanish, and the remaining integral involves \(\sin(x^2 - x)\) divided by \((2x - 1)^2\), which also converges absolutely due to the \(O(1/x^2)\) decay. The critical point at \(x = 1/2\) does not affect convergence as the integrand remains continuous.

### Conclusion

Both integrals \(\int_0^\infty \cos(x^2 + x) \, dx\) and \(\int_0^\infty \cos(x^2 - x) \, dx\) converge. Therefore, the original integral \(\int_0^\infty \cos(x) \cos(x^2) \, dx\) converges.

\[
\boxed{\text{The integral is convergent.}}
\]