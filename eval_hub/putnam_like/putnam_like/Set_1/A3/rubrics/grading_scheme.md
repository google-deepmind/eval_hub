This step is worth 1 point.
Suppose that $f(\frac{1}{2^n}) \in \mathbb{Q}$. Then
$$
\sum_{i=0}^\infty a_i 2^{-ni} \in \mathbb{Q}.
$$
Note that the left hand side is a binary representation of some fraction of the form
$$
0,a_0 \underbrace{0..0}_{\times (n-1)} a_1 \underbrace{0..0}_{\times (n-1)} a_2 \underbrace{0..0}_{\times (n-1)} a_3 \ldots_{(2)}.
$$
Hence, this representation is finite or periodic.

This step is worth 2 points.
If it is finite, then $a_i = 0$ for $i > m$ for some $m \in \mathbb{N}$. Then we can easily write that
$$
f\left(\frac{2}{q}\right) = \sum_{i=0}^m a_i \frac{2^i}{q^i} = \frac{\sum_{i=0}^m a_i 2^i q^{m-i}}{q^m}
$$
and $q^m$ is odd. Hence, after the reduction of the fraction, the denominator will stay odd.

This step is worth 7 points.
Consider the second case, namely - the binary representation of $f(\frac{1}{2^n})$ is infinite and periodic starting from some digit. It means that the sequence defined as
$$
d_i := \begin{cases}
a_{i/n} & \text{ for } i \text{ divisible by } n, \\
0 & \text{ otherwise}
\end{cases}
$$
is periodic for $i > k$. Let $m$ denote the period of $(d_i)$. Then, we can rewrite $f$ as
$$
f(x) = \sum_{i=0}^\infty d_{ni} x^i.
$$
Note that $(d_{ni})$ is $m$-periodic as well for $i > \frac{k}{n}$. Put $\ell := [\frac{k}{n}]$. Then, we have
$$
\begin{aligned}
f(x) &= \sum_{i=0}^\infty d_{ni} x^i = \sum_{i=0}^\ell d_{ni} x^i + \sum_{i=0}^{m-1} d_{n(\ell+1+i)} x^i (x^{\ell+1} + x^{\ell+1+m} + x^{\ell+1+2m} + \ldots)\\
&= \sum_{i=0}^\ell d_{ni} x^i + \frac{x^{\ell+1}}{1-x^m} \sum_{i=0}^{m-1} d_{n(\ell+1+i)} x^i.
\end{aligned}
$$
Hence
$$
f\left(\frac{2}{q}\right) = \sum_{i=0}^\ell d_{ni} \frac{2^i}{q^i} + \frac{2^{\ell+1}}{q^{\ell+1}} \cdot \frac{q^m}{q^m - 2^m} \sum_{i=0}^{m-1} d_{n(\ell+1+i)} \frac{2^i}{q^i}.
$$
Note that the right hand side is a sum of rationals and therefore $f(\frac{2}{q}) \in \mathbb{Q}$. Moreover, all the fractions on the right hand side have odd denominators and therefore, after summing and reduction, the resulting fraction has an odd denominator.