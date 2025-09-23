Let $e_1, e_2, \ldots, e_n$ be the $n$-th roots of unity. Since $n$ is an odd number, $e_1=1$ is one of the roots. The set $\{e_1, \ldots, e_n\}$ is the set of all $n$-th roots of unity. These are the roots of the polynomial $P(x) = x^n - 1$.

We can write $P(x)$ in terms of its roots as $P(x) = \prod_{k=1}^n (x-e_k)$.

Consider the polynomial $P(-x)$:
$P(-x) = (-x)^n - 1$.
Since $n$ is an odd number, $(-x)^n = -x^n$.
So, $P(-x) = -x^n - 1 = -(x^n+1)$.

The roots of $P(-x)$ are the values of $x$ for which $P(-x)=0$. Let $y=-x$, then $P(y)=0$, so $y$ must be one of the roots $e_k$. Thus, $-x=e_k$, which implies $x=-e_k$. The roots of $P(-x)$ are $-e_1, -e_2, \ldots, -e_n$.
Therefore, we can also write $P(-x)$ in terms of its roots:
$P(-x) = \prod_{k=1}^n (x - (-e_k)) = \prod_{k=1}^n (x+e_k)$.

Equating the two expressions for $P(-x)$:
$-(x^n+1) = \prod_{k=1}^n (x+e_k)$.
Multiplying both sides by $-1$:
$x^n+1 = -\prod_{k=1}^n (x+e_k)$. This is incorrect. The relation is $P(-x) = (-1)^n \prod (x+e_k)$.
$P(-x) = -x^n - 1$. Also $P(-x) = (-1)^n \prod_{k=1}^n (x - (-e_k)) = (-1)^n \prod_{k=1}^n (x+e_k)$.
Since $n$ is odd, $(-1)^n = -1$.
So, $-x^n - 1 = - \prod_{k=1}^n (x+e_k)$.
Multiplying by $-1$, we get $x^n+1 = \prod_{k=1}^n (x+e_k)$.
Let $R(x) = \prod_{k=1}^n (x+e_k)$. So $R(x) = x^n+1$.

Now, let's evaluate $R(x)$ at each root $e_j$ for $j=1, \ldots, n$.
$R(e_j) = e_j^n + 1$.
Since $e_j$ is an $n$-th root of unity, $e_j^n = 1$ for all $j=1, \ldots, n$.
So, $R(e_j) = 1+1=2$ for all $j=1, \ldots, n$.

Consider the product of $R(e_j)$ for $j=1, \ldots, n$:
$\prod_{j=1}^n R(e_j) = \prod_{j=1}^n 2 = 2^n$.

On the other hand, $R(e_j) = \prod_{k=1}^n (e_j+e_k)$.
So, $\prod_{j=1}^n R(e_j) = \prod_{j=1}^n \left(\prod_{k=1}^n (e_j+e_k)\right)$.
This is the product of the term $(e_j+e_k)$ over all $n^2$ ordered pairs of indices $(j,k)$ where $1 \le j,k \le n$.

We can split this product into two parts: the terms where $j=k$ and the terms where $j \ne k$.
$\prod_{j=1}^n \prod_{k=1}^n (e_j+e_k) = \left(\prod_{\substack{1 \le j,k \le n \\ j \ne k}} (e_j+e_k)\right) \left(\prod_{j=1}^n (e_j+e_j)\right)$.

The second part is $\prod_{j=1}^n (e_j+e_j) = \prod_{j=1}^n (2e_j) = 2^n \prod_{j=1}^n e_j$.
The $n$-th roots of unity are $e^{2\pi i m/n}$ for $m=0, 1, \ldots, n-1$. The set $\{e_1, \dots, e_n\}$ is this set of roots. The product of the $n$-th roots of unity is:
$\prod_{m=0}^{n-1} e^{2\pi i m/n} = e^{\sum_{m=0}^{n-1} \frac{2\pi i m}{n}}$.
The sum of the indices is $\sum_{m=0}^{n-1} m = \frac{(n-1)n}{2}$.
So, $\prod_{j=1}^n e_j = e^{\frac{2\pi i}{n} \frac{n(n-1)}{2}} = e^{\pi i (n-1)}$.
Since $n$ is an odd number, $n-1$ is an even number. Thus $e^{\pi i (n-1)} = (e^{\pi i})^{n-1} = (-1)^{n-1}=1$.
So, $\prod_{j=1}^n e_j = 1$.
Therefore, $\prod_{j=k} (e_j+e_j) = 2^n \cdot 1 = 2^n$.

The first part is $\prod_{j \ne k} (e_j+e_k)$. This product is over all ordered pairs $(j,k)$ with $1 \le j, k \le n$ and $j \ne k$. There are $n(n-1)$ such pairs.
This product can be written as the product over pairs $(j,k)$ with $j<k$ times the product over pairs $(j,k)$ with $j>k$.
$\prod_{\substack{1 \le j,k \le n \\ j \ne k}} (e_j+e_k) = \left(\prod_{1 \le j < k \le n} (e_j+e_k)\right) \left(\prod_{1 \le k < j \le n} (e_j+e_k)\right)$.
In the second part, $\prod_{1 \le k < j \le n} (e_j+e_k)$, we swap the indices $j$ and $k$. The set of pairs $(k,j)$ with $1 \le k < j \le n$ is the same as the set of pairs $(j,k)$ with $1 \le j < k \le n$.
So, $\prod_{1 \le k < j \le n} (e_j+e_k) = \prod_{1 \le j < k \le n} (e_k+e_j)$.
Since $e_j+e_k = e_k+e_j$, we have:
$\prod_{j \ne k} (e_j+e_k) = \left(\prod_{1 \le j < k \le n} (e_j+e_k)\right) \left(\prod_{1 \le j < k \le n} (e_j+e_k)\right) = \left(\prod_{1 \le j < k \le n} (e_j+e_k)\right)^2$.

Now, combining the parts of $\prod_{j=1}^n R(e_j)$:
$\prod_{j=1}^n R(e_j) = \left(\prod_{1 \le j < k \le n} (e_j+e_k)\right)^2 \times 2^n$.
We also know that $\prod_{j=1}^n R(e_j) = 2^n$.
So, $\left(\prod_{1 \le j < k \le n} (e_j+e_k)\right)^2 \times 2^n = 2^n$.
Since $n$ is a positive integer, $2^n \ne 0$. We can divide both sides by $2^n$:
$\left(\prod_{1 \le j < k \le n} (e_j+e_k)\right)^2 = 1$.

The expression we want to prove is $\prod_{i<j} (e_i+e_j)^2$.
The set of indices $i<j$ for $1 \le i,j \le n$ is the same as $j<k$ for $1 \le j,k \le n$.
$\prod_{i<j} (e_i+e_j)^2 = \left(\prod_{i<j} (e_i+e_j)\right)^2$.
We have shown that $\left(\prod_{1 \le i < j \le n} (e_i+e_j)\right)^2 = 1$.

Thus, $\prod_{i<j} (e_i+e_j)^2=1$.

The final answer is $\boxed{\prod_{i<j} (e_i+e_j)^2=1}$.