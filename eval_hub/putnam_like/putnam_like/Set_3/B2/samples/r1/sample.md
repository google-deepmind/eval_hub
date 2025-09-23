

To compute the limit
\[
\lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n\sum\limits_{l=1}^k e^{l/k},
\]
we start by analyzing the inner sum. For large \( k \), the sum \( \sum_{l=1}^k e^{l/k} \) can be approximated by a Riemann sum. Let \( x = \frac{l}{k} \), then \( x \) ranges from \( \frac{1}{k} \) to \( 1 \) in increments of \( \frac{1}{k} \). This sum approximates the integral of \( e^x \) over the interval \([0, 1]\):

\[
\sum_{l=1}^k e^{l/k} \approx k \int_0^1 e^x \, dx = k(e - 1).
\]

The error in this approximation is \( O(1) \) for each \( k \). Substituting this into the outer sum, we get:

\[
\sum_{k=1}^n \sum_{l=1}^k e^{l/k} \approx \sum_{k=1}^n \left[ k(e - 1) + O(1) \right].
\]

The dominant term in the sum is \( (e - 1) \sum_{k=1}^n k \). Using the formula for the sum of the first \( n \) integers:

\[
\sum_{k=1}^n k = \frac{n(n+1)}{2} \approx \frac{n^2}{2}.
\]

The error term \( \sum_{k=1}^n O(1) \) is \( O(n) \), which becomes negligible when divided by \( n^2 \). Thus, the original expression becomes:

\[
\frac{1}{n^2} \left( (e - 1) \frac{n^2}{2} + O(n) \right) \approx \frac{e - 1}{2} + O\left(\frac{1}{n}\right).
\]

Taking the limit as \( n \to \infty \), the error term vanishes, leading to:

\[
\boxed{\dfrac{e - 1}{2}}.
\]