Solution step (1 point):
$e_1,\ldots, e_n$ are the roots of $0=x^n-1=(x-1)(x^{n-1}+\ldots +x+1)$, so $e_2,\ldots, e_n$ are the roots of $x^{n-1}+\ldots +x+1=0$. Note, that $\prod_{i=1}^n e_i=(-1)^{n}\cdot (-1)=1$, by Vieta's formulas.

Solution step (2 points):
By translation, the numbers $1+e_2,\ldots,1+e_n$ are the roots of
$$(x-1)^{n-1}+\ldots +(x-1)+1.$$
Since $n$ is odd, the coefficient of $x^0$ is equal to $1$, hence applying Vieta's formulas we get
$$\prod_{i=2}^n (1+e_i)=1.$$

Solution step (7 points):
Fix $j$ and multiply the above equation by $e_j$. Since multiplication by $e_j$ is a one-to-one map of the set $\{e_i\,:\, i\neq 1\}$ to $\{e_i\,:\, i\neq j\}$ we get
$$e_j=\prod_{i=2}^n (e_j+e_ie_j)=\prod_{i\neq j} (e_j+e_i).$$
Multiplying all of these equations for $1\leq j\leq n$ we finish at
$$1=\prod_{j=1}^n e_j=\prod_{j=1}^n \prod_{i\neq j} (e_j+e_i)=\prod_{i<j} (e_i+e_j)^2,$$
since each pair of indices $(i,j)$, $i\neq j$ appears in the product exactly two times.