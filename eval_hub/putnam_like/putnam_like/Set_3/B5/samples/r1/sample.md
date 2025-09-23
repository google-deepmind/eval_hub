

To solve the given problem, we start by finding the polynomial whose roots are \( y_i = x_i^2 \), where \( x_i \) are the roots of \( x^4 - 2x - 1 = 0 \). Substituting \( y = x^2 \) into the original polynomial, we derive the polynomial for \( y \):

\[
y^4 - 2y^2 - 4y + 1 = 0
\]

Next, we need to compute the sum:

\[
\sum_{i=1}^4 \frac{2y_i + 1}{(y_i - 1)^2}
\]

Rewriting each term in the sum:

\[
\frac{2y_i + 1}{(y_i - 1)^2} = \frac{2(y_i - 1) + 3}{(y_i - 1)^2} = \frac{2}{y_i - 1} + \frac{3}{(y_i - 1)^2}
\]

Thus, the sum becomes:

\[
2\sum_{i=1}^4 \frac{1}{y_i - 1} + 3\sum_{i=1}^4 \frac{1}{(y_i - 1)^2}
\]

Let \( z_i = y_i - 1 \). The polynomial for \( z_i \) is found by substituting \( z = y - 1 \):

\[
z^4 + 4z^3 + 4z^2 - 4z - 4 = 0
\]

Using Vieta's formulas:
- The sum of reciprocals of roots \( \sum \frac{1}{z_i} = -\frac{\text{coefficient of } z}{\text{constant term}} = -\frac{-4}{-4} = -1 \)
- The sum \( \sum \frac{1}{z_i^2} \) can be computed using \( (\sum \frac{1}{z_i})^2 - 2\sum \frac{1}{z_i z_j} \). Here, \( \sum \frac{1}{z_i z_j} = -1 \), leading to \( \sum \frac{1}{z_i^2} = (-1)^2 - 2(-1) = 3 \).

Substituting these values back:

\[
2(-1) + 3(3) = -2 + 9 = 7
\]

**Answer:**

The sum is \boxed{7}.