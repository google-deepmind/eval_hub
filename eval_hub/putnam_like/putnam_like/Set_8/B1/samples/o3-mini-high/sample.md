```markdown
We are given
\[
a=\sqrt[3]{n}\quad\text{and}\quad b=\sqrt[3]{n+1},
\]
and we wish to compare
\[
a^b\quad \text{vs.}\quad b^a.
\]

A natural way to compare these numbers is to take logarithms. Notice that
\[
a^b = \exp(b\ln a) \quad \text{and} \quad b^a = \exp(a\ln b).
\]
Thus, comparing \(a^b\) and \(b^a\) amounts to comparing the exponents \(b\ln a\) and \(a\ln b\). In particular, we have:
\[
a^b > b^a \quad \Longleftrightarrow \quad b\ln a > a\ln b.
\]

Dividing both sides by \(ab\) (which is positive), the inequality becomes
\[
\frac{\ln a}{a} > \frac{\ln b}{b}.
\]
Define the function
\[
f(x)=\frac{\ln x}{x}.
\]
Its derivative is
\[
f'(x)=\frac{1-\ln x}{x^2}.
\]
We see that:
- \(f'(x) > 0\) when \(1-\ln x > 0\), i.e. when \(x < e\),
- \(f'(x) < 0\) when \(x > e\).

For \(n\ge21\), we have
\[
a=\sqrt[3]{n} \quad \text{and} \quad b=\sqrt[3]{n+1}.
\]
A quick check shows that even for \(n=21\), 
\[
a \approx \sqrt[3]{21} \approx 2.76 \quad \text{and} \quad b \approx \sqrt[3]{22} \approx 2.80.
\]
Since \(e\approx 2.718\), we have \(a>e\) and \(b>e\). Therefore, on the interval where \(x>e\), the function \(f(x)\) is decreasing. Since \(a<b\), it follows that
\[
f(a) > f(b),
\]
which is equivalent to
\[
\frac{\ln a}{a} > \frac{\ln b}{b}.
\]
Multiplying back by the positive quantity \(ab\), we obtain
\[
b\ln a > a\ln b.
\]
This inequality tells us that
\[
a^b > b^a.
\]

Thus, for all natural numbers \(n\ge21\),
\[
\boxed{\sqrt[3]{n}^{\,\sqrt[3]{n+1}} > \sqrt[3]{n+1}^{\,\sqrt[3]{n}}.}
\]
```