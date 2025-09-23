Solution:
Let $n$ be an odd integer and let $e_1, e_2, \ldots, e_n$ be the $n$-th roots of unity. These are the roots of the polynomial $Q(z) = z^n - 1$. We are given $e_1=1$. The roots can be explicitly written as $e_k = \exp(2\pi i (k-1)/n)$ for $k=1, \ldots, n$.
We want to prove that $P = \prod_{1 \le i < j \le n} (e_i + e_j)^2 = 1$.

Let's consider the product $\prod_{i \ne j} (e_i+e_j)$, where the product is taken over all ordered pairs $(i,j)$ such that $i,j \in \{1, \ldots, n\}$ and $i \ne j$. This product has $n(n-1)$ terms.
We can group the terms in pairs $(i,j)$ and $(j,i)$. Since $e_i+e_j = e_j+e_i$, we have:
$$ \prod_{i \ne j} (e_i+e_j) = \prod_{1 \le i < j \le n} (e_i+e_j) \prod_{1 \le j < i \le n} (e_i+e_j) $$
By swapping the indices $i$ and $j$ in the second product, we get:
$$ \prod_{1 \le j < i \le n} (e_i+e_j) = \prod_{1 \le i < j \le n} (e_j+e_i) $$
So,
$$ \prod_{i \ne j} (e_i+e_j) = \prod_{1 \le i < j \le n} (e_i+e_j) \prod_{1 \le i < j \le n} (e_j+e_i) = \prod_{1 \le i < j \le n} (e_i+e_j)^2 = P $$
Thus, the quantity we want to compute is $P = \prod_{i \ne j} (e_i+e_j)$.

We can compute this product by grouping the terms by the first index $j$:
$$ P = \prod_{j=1}^n \left( \prod_{k=1, k \ne j}^n (e_j+e_k) \right) $$

To evaluate the inner product $\prod_{k \ne j} (e_j+e_k)$, let's consider the polynomial $Q(z) = z^n - 1$. We know $Q(z) = \prod_{k=1}^n (z-e_k)$.
Let's evaluate $Q(-z)$. Since $n$ is an odd integer, $(-z)^n = -z^n$.
So $Q(-z) = (-z)^n - 1 = -z^n - 1$.
Also, $Q(-z) = \prod_{k=1}^n (-z - e_k) = \prod_{k=1}^n -(z+e_k) = (-1)^n \prod_{k=1}^n (z+e_k)$.
Since $n$ is odd, $(-1)^n = -1$.
Therefore, $Q(-z) = - \prod_{k=1}^n (z+e_k)$.
Equating the two expressions for $Q(-z)$:
$$ -z^n - 1 = - \prod_{k=1}^n (z+e_k) $$
Multiplying by $-1$, we get:
$$ z^n + 1 = \prod_{k=1}^n (z+e_k) $$
Now, let's substitute $z = e_j$ into this identity for a fixed $j \in \{1, \ldots, n\}$.
$$ e_j^n + 1 = \prod_{k=1}^n (e_j+e_k) $$
Since $e_j$ is an $n$-th root of unity, $e_j^n = 1$.
So, $1 + 1 = 2$.
$$ 2 = \prod_{k=1}^n (e_j+e_k) $$
The product on the right side includes the term where $k=j$. We can separate this term:
$$ 2 = (e_j+e_j) \prod_{k=1, k \ne j}^n (e_j+e_k) = 2e_j \prod_{k \ne j} (e_j+e_k) $$
Since $e_j$ is a root of unity, $e_j \ne 0$. We can divide by $2e_j$:
$$ \prod_{k \ne j} (e_j+e_k) = \frac{2}{2e_j} = \frac{1}{e_j} $$
Now substitute this result back into the expression for $P$:
$$ P = \prod_{j=1}^n \left( \prod_{k \ne j} (e_j+e_k) \right) = \prod_{j=1}^n \frac{1}{e_j} $$
$$ P = \frac{1}{\prod_{j=1}^n e_j} $$
Let $E = \prod_{j=1}^n e_j$ be the product of the $n$-th roots of unity.
The roots $e_1, \ldots, e_n$ are the roots of $z^n-1=0$.
From Vieta's formulas, the product of the roots is related to the constant term of the polynomial $z^n-1$.
$z^n - 1 = \prod_{j=1}^n (z-e_j)$.
Expanding the product, the constant term is $\prod_{j=1}^n (-e_j) = (-1)^n \prod_{j=1}^n e_j = (-1)^n E$.
The constant term of $z^n-1$ is $-1$.
So, $-1 = (-1)^n E$.
Since $n$ is odd, $(-1)^n = -1$.
So, $-1 = -E$, which implies $E = 1$.
Alternatively, we can compute the product directly:
$$ E = \prod_{k=1}^n e_k = \prod_{k=1}^n \exp\left(\frac{2\pi i (k-1)}{n}\right) = \exp\left(\sum_{k=1}^n \frac{2\pi i (k-1)}{n}\right) $$
$$ \sum_{k=1}^n (k-1) = \sum_{m=0}^{n-1} m = \frac{(n-1)n}{2} $$
$$ E = \exp\left(\frac{2\pi i}{n} \frac{n(n-1)}{2}\right) = \exp(\pi i (n-1)) $$
Since $n$ is odd, $n-1$ is an even integer. Let $n-1 = 2m$ for some integer $m$.
$$ E = \exp(\pi i (2m)) = \exp(2m\pi i) = (\exp(2\pi i))^m = 1^m = 1 $$
Finally, substituting $E=1$ into the expression for $P$:
$$ P = \frac{1}{E} = \frac{1}{1} = 1 $$
Thus, we have proven that $\prod_{1 \le i < j \le n} (e_i + e_j)^2 = 1$.

Final Answer: The final answer is $\boxed{1}$