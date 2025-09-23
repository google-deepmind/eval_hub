This step is worth 2 points.
The double sum looks like Riemann sum for double integral. However, the double Riemann sum are defined on rectangular domains. Therefore we introduce indicator function to the sum:
$$
\frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}=
\frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^n e^{l/k}\mathbf{1}_{\{l\leq k\}}.
$$

This step is worth 5 points.
Since the function $\mathbf{1}_{\{y\leq x\}}$ is discontinuous on the line $\{y=x\}$ , and this is a zero-measure set, the function $e^{y/x}\mathbf{1}_{\{y\leq x\}}$ is Riemann-integrable. Therefore our sum is a Riemann sum for this function over the square $[0,1]\times[0,1]$ partitioned onto $\frac 1n\times\frac 1n$ rectangles. Hence
$$
\lim_{n\to\infty} \frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^n e^{l/k}\mathbf{1}_{\{l\leq k\}} = \int_0^1 \int_0^1 e^{y/x}\mathbf{1}_{\{y\leq x\}}\,dy\,dx=\int_0^1 \int_0^x e^{y/x}\,dy\,dx.
$$

This step is worth 3 points.
Now it is a standard computation to get
$$
\int_0^1 \int_0^x e^{y/x} dy\,dx=\int_0^1 \left[xe^{y/x}\right]_{y=0}^{y=x}\, dx=\int_0^1 x(e-1)\,dx=(e-1)\left[\frac{x^2}2\right]_{x=0}^{x=1}=\frac{e-1}2.
$$