

To determine whether \(a^b\) or \(b^a\) is greater for \(a = \sqrt[3]{n}\) and \(b = \sqrt[3]{n+1}\) with \(n \geq 21\), we analyze the natural logarithms of both expressions:

\[
\ln(a^b) = b \ln(a) \quad \text{and} \quad \ln(b^a) = a \ln(b).
\]

We compare \(b \ln(a)\) and \(a \ln(b)\). Let \(f(x) = \frac{\ln(x)}{x}\). The derivative \(f'(x) = \frac{1 - \ln(x)}{x^2}\) shows that \(f(x)\) is decreasing for \(x > e\). Since \(n \geq 21\), we have \(a = \sqrt[3]{n} \geq \sqrt[3]{21} \approx 2.758 > e \approx 2.718\), and \(b > a\). Thus, \(f(x)\) is decreasing, and \(f(a) > f(b)\) because \(a < b\). This implies:

\[
\frac{\ln(a)}{a} > \frac{\ln(b)}{b} \implies b \ln(a) > a \ln(b).
\]

Exponentiating both sides, we conclude \(a^b > b^a\).

**Conclusion**: \(a^b\) is greater than \(b^a\) for \(n \geq 21\).

\boxed{a^b}