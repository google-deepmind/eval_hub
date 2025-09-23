

To find the supremum of the ratio between the \( L^1 \) norm and the \( L^2 \) norm for functions in the class \( \mathcal{F} \), we start by noting that the Cauchy-Schwarz inequality provides an upper bound. For any \( f \in \mathcal{F} \),

\[
\|f\|_1 \leq \|f\|_2 \|1\|_2 = \|f\|_2,
\]

which implies that the ratio \( \frac{\|f\|_1}{\|f\|_2} \leq 1 \). Therefore, the supremum is at most 1.

To show that this bound can be approached arbitrarily closely, consider a family of functions \( f_\epsilon \) parameterized by \( \epsilon \) (where \( \epsilon \) is small). Define \( f_\epsilon \) as follows:

- \( f_\epsilon(x) = \frac{M}{\epsilon} x \) for \( x \in [0, \epsilon] \),
- \( f_\epsilon(x) = M \) for \( x \in [\epsilon, 1] \).

Here, \( M \) is a constant. For continuity, we set \( M = 1 \). Calculating the norms:

1. \( L^1 \) norm:
\[
\|f_\epsilon\|_1 = \int_0^\epsilon \frac{x}{\epsilon} \, dx + \int_\epsilon^1 1 \, dx = \frac{\epsilon}{2} + (1 - \epsilon) = 1 - \frac{\epsilon}{2}.
\]

2. \( L^2 \) norm:
\[
\|f_\epsilon\|_2 = \left( \int_0^\epsilon \left( \frac{x}{\epsilon} \right)^2 \, dx + \int_\epsilon^1 1^2 \, dx \right)^{1/2} = \left( \frac{\epsilon}{3} + (1 - \epsilon) \right)^{1/2} = \sqrt{1 - \frac{2\epsilon}{3}}.
\]

The ratio becomes:
\[
\frac{\|f_\epsilon\|_1}{\|f_\epsilon\|_2} = \frac{1 - \frac{\epsilon}{2}}{\sqrt{1 - \frac{2\epsilon}{3}}}.
\]

As \( \epsilon \to 0 \), both the numerator and the denominator approach 1. Using a Taylor expansion for small \( \epsilon \), we find:
\[
\frac{1 - \frac{\epsilon}{2}}{\sqrt{1 - \frac{2\epsilon}{3}}} \approx \frac{1 - \frac{\epsilon}{2}}{1 - \frac{\epsilon}{3}} \approx 1 - \frac{\epsilon}{6} + O(\epsilon^2),
\]

which approaches 1. Thus, the supremum is indeed 1.

Therefore, the supremum is \(\boxed{1}\).