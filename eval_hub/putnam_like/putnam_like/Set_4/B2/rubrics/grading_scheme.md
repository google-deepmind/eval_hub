This step is worth 8 points:

Suppose that $(x_1, x_2, \ldots, x_n)$ solves the system. Taking the sum of both sides we arrive at
$$
\sum_{k=1}^n x_k^2 + \sum_{k=1}^n (1-x_k \ln x_k)^2 = 2\sum_{k=1}^n x_k - 2\sum_{k=1}^n x_k^2 \ln x_k = \sum_{k=1}^n 2 x_k (1-x_k \ln x_k).
$$
Thus
$$
\sum_{k=1}^n x_k^2 - \sum_{k=1}^n 2 x_k (1-x_k \ln x_k) + \sum_{k=1}^n (1-x_k \ln x_k)^2 = 0
$$
or equivalently
$$
\sum_{k=1}^n \left( x_k - (1 - x_k \ln x_k) \right)^2 = 0.
$$

This step is worth 2 points:

Hence $x_k - (1 - x_k \ln x_k) = 0$ for every $k \in \{1,2,\ldots,n\}$. Rewrite this equation as 
$$
\frac{1}{x_k} = 1 + \ln x_k.
$$
Since $y \mapsto \frac{1}{y}$ is decreasing on $(0,\infty)$, and $y \mapsto 1 + \ln y$ is increasing on $(0,\infty)$, there is at most one $x_k > 0$ such that $\frac{1}{x_k} = 1 + \ln x_k$. One can easily check that $x_k = 1$ satisfies the equation. Hence $(1,1,\ldots,1)$ is the unique solution to the system.