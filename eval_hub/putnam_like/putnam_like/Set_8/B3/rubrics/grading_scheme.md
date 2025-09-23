This step is worth 5 points.
We will prove the inequality:
$$
\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx.
$$
We have
$$
\begin{aligned}
&\int_0^1 f(x)x^{n-1}dx - \int_{1-\frac{1}{n}}^1 f(x)dx\\
&=\int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx+ \int_{1-\frac{1}{n}}^1 f(x)x^{n-1}dx - \int_{1-\frac{1}{n}}^1 f(x)dx\\
&= \int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx + \int_{1-\frac{1}{n}}^1 f(x)\big(x^{n-1} - 1\big)dx \\
&\geq \int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx +  \left( \int_{1-\frac{1}{n}}^1 f\left(1-\frac{1}{n}\right)(x^{n-1}-1)dx\right) \\
&=\int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx + f\left(1-\frac{1}{n}\right) \left( \int_{1-\frac{1}{n}}^1 (x^{n-1}-1)dx\right) \\
&= \int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx + f\left(1-\frac{1}{n}\right) \left( \int_{1-\frac{1}{n}}^1 x^{n-1}dx - \int_{1-\frac{1}{n}}^11dx\right) \\
&= \int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx + f\left(1-\frac{1}{n}\right) \left( \int_{1-\frac{1}{n}}^1 x^{n-1}dx - \frac{1}{n} \right) \\
&= \int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx + f\left(1-\frac{1}{n}\right) \left( \int_{1-\frac{1}{n}}^1 x^{n-1}dx - \int_0^1 x^{n-1}dx \right) \\
&= \int_0^{1-\frac{1}{n}} f(x)x^{n-1}dx - f\left(1-\frac{1}{n}\right) \int_0^{1-\frac{1}{n}}x^{n-1}dx \\
&= \int_0^{1-\frac{1}{n}}x^{n-1}\left(f(x) - f\left(1-\frac{1}{n}\right)\right)dx \geq 0,
\end{aligned}
$$
where the last inequality holds because $ f(x) $ is decreasing, and thus
$$
f(x) \geq f\left(1-\frac{1}{n}\right) \quad \text{for all } x \in \left[0, 1-\frac{1}{n}\right].
$$
This concludes the proof of the desired inequality.

This step is worth 5 points.
Now we prove the inequality:
$$
\int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx.
$$
We have
$$
\begin{aligned}
&\int_0^1 f(x)x^{n-1}dx - \int_0^{\frac{1}{n}} f(x)dx\\
&=\int_0^{\frac{1}{n}} f(x)x^{n-1}dx+ \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx - \int_0^{\frac{1}{n}} f(x)dx\\
&= \int_0^{\frac{1}{n}} f(x)(x^{n-1}-1)dx + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&\leq \int_0^{\frac{1}{n}} f\left(\frac{1}{n}\right)(x^{n-1}-1)dx + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&= f\left(\frac{1}{n}\right)\left(\int_0^{\frac{1}{n}} (x^{n-1}-1)dx\right) + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&= f\left(\frac{1}{n}\right)\left(\int_0^{\frac{1}{n}} x^{n-1}dx-\int_0^{\frac{1}{n}}1dx\right) + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&= f\left(\frac{1}{n}\right)\left(\int_0^{\frac{1}{n}} x^{n-1}dx-\frac{1}{n}\right) + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&= f\left(\frac{1}{n}\right)\left(\int_0^{\frac{1}{n}} x^{n-1}dx-\int_0^1x^{n-1}dx\right) + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&= f\left(\frac{1}{n}\right)\left(\int_{\frac{1}{n}}^1 -x^{n-1}dx\right) + \int_{\frac{1}{n}}^1 f(x)x^{n-1}dx \\
&= \int_{\frac{1}{n}}^1 \left(f(x)-f\left(\frac{1}{n}\right)\right)x^{n-1}dx\leq 0,
\end{aligned}
$$
where the last inequality holds because $f(x)$ is decreasing, and thus
$$
f(x) \leq f\left(\frac{1}{n}\right) \quad \text{for all } x \in \left[ \frac{1}{n},1\right].
$$
This concludes the proof of the desired inequality.