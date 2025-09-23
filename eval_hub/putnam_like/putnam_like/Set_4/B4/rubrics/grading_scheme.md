This step is worth 2 points.
Observe that, by the invariance of $B(0,1)$ with respect to rotations around $0$, we have
$$
\int_{B(0,1)} |x_1|^{2k} \, dx = \int_{B(0,1)} |x_i|^{2k} \, dx
$$
for every $1 \leq i \leq n$. Then
$$
\int_{B(0,1)} |x_1|^{2k} \, dx = \frac{1}{n} \sum_{i=1}^n \int_{B(0,1)} |x_i|^{2k} \, dx = \frac{1}{n}  \int_{B(0,1)} \sum_{i=1}^n \left( |x_i|^{2} \right)^k \, dx = (*).
$$

This step is worth 8 points.
Since the function $f : [0, \infty) \rightarrow [0,\infty)$, given by $f(y) = y^k$, is convex, Jensen's inequality provides
$$
\left( |x_1|^2 + \ldots + |x_n|^2 \right)^k \leq n^{k-1} \left( (|x_1|^2)^k + \ldots + (|x_n|^2)^k \right).
$$
Hence
$$
\begin{aligned}
(*) &\geq \frac{1}{n} \int_{B(0,1)} \frac{1}{n^{k-1}} \left( |x_1|^2 + \ldots + |x_n|^2 \right)^k \, dx = \frac{1}{n} \int_{B(0,1)} \frac{1}{n^{k-1}} |x|^{2k} \, dx\\
& = \frac{1}{n^k} \int_{B(0,1)} |x|^{2k} \, dx 
= \frac{1}{n^k} \omega_n \int_0^1 r^{2k} r^{n-1} \, dr = \frac{\omega_n}{n^k} \frac{1}{2k+n} = \frac{\omega_n}{n^{k} (2k+n)},
\end{aligned}
$$
where we used the coarea formula and the change of variables $r=|x|$. Hence the proof is completed.