This step is worth 3 points.
Denote
$$
C := \sup_{f \in \mathcal{F}} \frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}}.
$$
First, observe that thanks to the Hölder inequality we can write
$$
\int_{0}^{1} |f(x)| \, dx = \int_{0}^{1} 1 \cdot |f(x)| \, dx \leq \left( \int_0^1 1^2 \, dx \right)^{1/2} \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}
$$
and therefore $C \leq 1$.

This step is worth 7 points.
Consider the sequence of functions $f_n \in \mathcal{F}$ given by $f_n(x) = x^{1/n}$. Then
$$
\int_{0}^{1} |f_n(x)| \, dx = \int_0^1 x^{1/n} \, dx = \frac{n}{n+1} \to 1 \quad \text{as } n \to \infty
$$
and
$$
\left( \int_{0}^{1} |f_n(x)|^2 \, dx\right)^{1/2} = \left( \int_0^1 x^{2/n} \, dx \right)^{1/2} = \left( \frac{n}{n+2} \right)^{1/2} \to 1 \quad \text{as } n \to \infty.
$$
Then
$$
\frac{\int_{0}^{1} |f_n(x)| \, dx}{\left( \int_0^1 |f_n(x)|^2 \, dx \right)^{1/2}} \to 1
$$
and $C = 1$.