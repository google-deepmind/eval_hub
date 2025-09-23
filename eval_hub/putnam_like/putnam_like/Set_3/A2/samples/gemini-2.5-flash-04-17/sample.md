Let $f(x) = \frac{1}{x^k+1} = (x^k+1)^{-1}$. We are given $p(x) = (x^k+1)^{n+1}f^{(n)}(x)$, where $k, n$ are positive integers. Let $p_n(x) = (x^k+1)^{n+1}f^{(n)}(x)$.

First, let's find a recurrence relation for $p_n(x)$.
For $n=0$, $f^{(0)}(x)=f(x)$, so $p_0(x) = (x^k+1)^1 f(x) = (x^k+1) \frac{1}{x^k+1} = 1$.
For $n \ge 0$, $f^{(n)}(x) = p_n(x) (x^k+1)^{-(n+1)}$.
Differentiating with respect to $x$:
$f^{(n+1)}(x) = p_n'(x) (x^k+1)^{-(n+1)} + p_n(x) \cdot (-(n+1))(x^k+1)^{-(n+2)} \cdot (kx^{k-1})$
$f^{(n+1)}(x) = (x^k+1)^{-(n+2)} \left[ p_n'(x)(x^k+1) - k(n+1)x^{k-1}p_n(x) \right]$.
By definition, $p_{n+1}(x) = (x^k+1)^{n+2} f^{(n+1)}(x)$.
So, the recurrence relation is $p_{n+1}(x) = (x^k+1)p_n'(x) - k(n+1)x^{k-1} p_n(x)$ for $n \ge 0$.

We prove by induction that $p_n(x)$ is a polynomial with integer coefficients for all $n \ge 0$.
Base case $n=0$: $p_0(x)=1$, which is a polynomial with integer coefficients.
Assume $p_n(x)$ is a polynomial with integer coefficients for some $n \ge 0$.
If $p_n(x)$ has integer coefficients, then its derivative $p_n'(x)$ also has integer coefficients.
The product $(x^k+1)p_n'(x)$ is a polynomial with integer coefficients.
The product $k(n+1)x^{k-1} p_n(x)$ is also a polynomial with integer coefficients, since $k$ and $n$ are integers.
The difference of two polynomials with integer coefficients is a polynomial with integer coefficients.
Thus, $p_{n+1}(x) = (x^k+1)p_n'(x) - k(n+1)x^{k-1} p_n(x)$ is a polynomial with integer coefficients.
By induction, $p_n(x)$ is a polynomial with integer coefficients for all $n \ge 0$.

Since $n$ is a positive integer, $n \ge 1$. $p(x) = p_n(x)$ has integer coefficients.
$k$ is a positive integer, so $k-1$ is an integer (possibly 0 if $k=1$).
$p(k-1) = p_n(k-1)$ is an integer because $p_n(x)$ is a polynomial with integer coefficients and $k-1$ is an integer. This proves $p(k-1)\in\mathbb{Z}$.

Next, we prove that $k|p_n(k-1)$ for $n \ge 1$.
Let $p_n(x) = \sum_{i=0}^{d_n} c_{n,i} x^i$, where $d_n = n(k-1)$ is the degree of $p_n(x)$ and $c_{n,i}$ are integers.
We will show by induction that $k|c_{n,i}$ for all $i$ and for all $n \ge 1$.
Base case $n=1$:
$p_1(x) = (x^k+1)p_0'(x) - k(1)x^{k-1}p_0(x) = (x^k+1)\cdot 0 - kx^{k-1}\cdot 1 = -kx^{k-1}$.
The coefficients of $p_1(x)$ are $c_{1, k-1} = -k$ and $c_{1,i}=0$ for $i \ne k-1$.
Clearly, $k|c_{1,i}$ for all $i$. The base case holds.

Inductive step: Assume $k|c_{n,i}$ for all $i$ for some $n \ge 1$.
The recurrence relation for $p_{n+1}(x)$ in terms of coefficients is obtained by comparing coefficients of $x^j$:
$p_{n+1}(x) = (x^k+1)\sum i c_{n,i} x^{i-1} - k(n+1)x^{k-1} \sum c_{n,i} x^i$
$p_{n+1}(x) = \sum i c_{n,i} x^{i+k-1} + \sum i c_{n,i} x^{i-1} - \sum k(n+1)c_{n,i} x^{i+k-1}$
$p_{n+1}(x) = \sum (i - k(n+1)) c_{n,i} x^{i+k-1} + \sum i c_{n,i} x^{i-1}$.
Let $p_{n+1}(x) = \sum_j c_{n+1, j} x^j$. The coefficient $c_{n+1, j}$ is obtained by collecting terms $x^j$ from the right side.
A term $x^{i+k-1}$ contributes to $x^j$ if $i+k-1=j$, so $i=j-k+1$.
A term $x^{i-1}$ contributes to $x^j$ if $i-1=j$, so $i=j+1$.
The coefficients $c_{n,i}$ are zero for $i<0$ or $i>n(k-1)$.
$c_{n+1, j} = (j-k+1 - k(n+1)) c_{n, j-k+1} + (j+1) c_{n, j+1}$.
Note that $(j-k+1 - k(n+1)) = j+1-k(n+2)$.
$c_{n+1, j} = (j+1-k(n+2)) c_{n, j-k+1} + (j+1) c_{n, j+1}$.

By the induction hypothesis, $k|c_{n,i}$ for all $i$. So $c_{n, j-k+1}$ and $c_{n, j+1}$ are divisible by $k$.
Let $c_{n, j-k+1} = k \cdot d_1$ and $c_{n, j+1} = k \cdot d_2$ for some integers $d_1, d_2$.
$c_{n+1, j} = (j+1-k(n+2)) (k d_1) + (j+1) (k d_2)$
$c_{n+1, j} = k [ (j+1-k(n+2)) d_1 + (j+1) d_2 ]$.
Since $j, k, n$ are integers and $d_1, d_2$ are integers, the expression in the square bracket is an integer.
Thus, $c_{n+1, j}$ is divisible by $k$ for all $j$.
By induction, $k|c_{n,i}$ for all $i$ and for all $n \ge 1$.

Now we evaluate $p_n(k-1)$ for $n \ge 1$.
$p_n(k-1) = \sum_{i=0}^{n(k-1)} c_{n,i} (k-1)^i$.
Since $k|c_{n,i}$ for all $i$, we can write $c_{n,i} = k \cdot d_{n,i}$ for some integers $d_{n,i}$.
$p_n(k-1) = \sum_{i=0}^{n(k-1)} (k \cdot d_{n,i}) (k-1)^i = k \sum_{i=0}^{n(k-1)} d_{n,i} (k-1)^i$.
The sum $\sum_{i=0}^{n(k-1)} d_{n,i} (k-1)^i$ is an integer because $d_{n,i}$ are integers and $(k-1)^i$ are integers.
Therefore, $p_n(k-1)$ is a multiple of $k$. This proves $k|p(k-1)$.

The final answer is $\boxed{p(k-1)\in\mathbb{Z} \text{ and } k|p(k-1)}$.