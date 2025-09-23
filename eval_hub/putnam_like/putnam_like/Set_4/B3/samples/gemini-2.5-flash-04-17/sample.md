Let $f(a_1, \dots, a_n) = \sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p$. We want to minimize this function subject to the constraints $a_i > 0$ for $i=1, \ldots, n$ and $\sum_{i=1}^n a_i = 1$.

Let $g(x) = (x+1/x)^p$ for $x>0$. The sum is $\sum_{i=1}^n g(a_i)$. The constraint is $\sum_{i=1}^n a_i = 1$.

Case 1: $p \geq 1$.
Let's examine the convexity of $g(x)$.
$g'(x) = p(x+1/x)^{p-1}(1-1/x^2)$.
$g''(x) = p(p-1)(x+1/x)^{p-2}(1-1/x^2)^2 + p(x+1/x)^{p-1}(2/x^3)$.
For $x>0$ and $p \geq 1$:
The first term $p(p-1)(x+1/x)^{p-2}(1-1/x^2)^2$ is non-negative, since $p \ge 1 \implies p-1 \ge 0$, $(x+1/x)^{p-2} > 0$, and $(1-1/x^2)^2 \ge 0$.
The second term $p(x+1/x)^{p-1}(2/x^3)$ is positive, since $p > 0$, $(x+1/x)^{p-1} > 0$, and $2/x^3 > 0$.
Thus, $g''(x) \geq 0$ for $x>0$ when $p \geq 1$. $g(x)$ is convex for $p \geq 1$. (If $p=1$, $g''(x)=2/x^3>0$, strictly convex. If $p>1$, $g''(x)>0$ except possibly at $x=1$, where $1-1/x^2=0$. At $x=1$, $g''(1) = p(p-1) \cdot 2^{p-2} \cdot 0 + p \cdot 2^{p-1} \cdot 2 = p \cdot 2^p > 0$. So $g(x)$ is strictly convex for $p>1$.)

By Jensen's inequality for convex functions, for positive values $a_i$ and weights $w_i=1$:
$\frac{1}{n} \sum_{i=1}^n g(a_i) \geq g\left(\frac{\sum_{i=1}^n a_i}{n}\right)$.
Given $\sum_{i=1}^n a_i = 1$:
$\frac{1}{n} \sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p \geq \left( \frac{1/n} + \frac{1}{1/n} \right)^p = \left( \frac{1}{n} + n \right)^p$.
Multiplying by $n$:
$\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p \geq n \left( \frac{1+n^2}{n} \right)^p = n \frac{(1+n^2)^p}{n^p} = \frac{(1+n^2)^p}{n^{p-1}}$.
This proves the inequality for $p \geq 1$.

Case 2: $0 < p < 1$.
In this case, $g''(x)$ is not always non-negative, so $g(x)$ is not convex over its entire domain. We use the method of Lagrange multipliers to find the minimum value.
We want to minimize $F(a_1, \ldots, a_n) = \sum_{i=1}^n (a_i + 1/a_i)^p$ subject to $G(a_1, \ldots, a_n) = \sum_{i=1}^n a_i - 1 = 0$, with $a_i > 0$.
The Lagrangian is $L(a_1, \ldots, a_n, \lambda) = \sum_{i=1}^n (a_i + 1/a_i)^p - \lambda(\sum_{i=1}^n a_i - 1)$.
Setting the partial derivatives with respect to $a_i$ to zero:
$\frac{\partial L}{\partial a_i} = p(a_i+1/a_i)^{p-1}(1-1/a_i^2) - \lambda = 0$.
This must hold for all $i=1, \ldots, n$. So, $p(a_i+1/a_i)^{p-1}(1-1/a_i^2)$ must be constant for all $i$. Let this constant be $\lambda$.
Let $h(x) = (x+1/x)^{p-1}(1-1/x^2)$. We need $h(a_i) = \lambda/p$ for all $i$.

Let's analyze $h(x)$ for $x>0$. $h(1) = (1+1)^p(1-1) = 0$.
$h(x) = (x+1/x)^{p-1}\frac{x^2-1}{x^2}$. For $x \in (0,1)$, $x^2-1 < 0$, so $h(x) < 0$. For $x \in (1, \infty)$, $x^2-1 > 0$, so $h(x) > 0$.
$h'(x) = \frac{1}{p}(x+1/x)^{p-2} g''(x)$, as shown in the thought process. For $0<p<1$, $g''(x)$ changes sign. $g''(x) = p(x+1/x)^{p-2} \left[ p-1 + (4-2p)/x^2 + (p+1)/x^4 \right]$. The term in brackets is negative for small $1/x^2$ (large $x$) and positive for large $1/x^2$ (small $x$).
$h'(x)$ has the same sign as $g''(x)/(p(x+1/x)^{p-2})$. Since $p>0$ and $(x+1/x)^{p-2}>0$, $h'(x)$ has the same sign as $g''(x)$.
$g''(x)$ is negative for $x^2 > 1/u_1$ and positive for $x^2 < 1/u_1$, where $u_1 = \frac{p-2 + \sqrt{5-4p}}{p+1} \in (0,1)$.
So $h(x)$ increases for $x \in (0, \sqrt{1/u_1})$ and decreases for $x \in (\sqrt{1/u_1}, \infty)$. Let $x_0 = \sqrt{1/u_1}$. Since $u_1<1$, $x_0>1$.
$h(x)$ starts at $-\infty$ as $x \to 0^+$, increases to $h(x_0)>0$, then decreases towards 0 as $x \to \infty$. $h(1)=0$.
For $x \in (0,1)$, $h(x)$ increases from $-\infty$ to $h(1)=0$. For $x \in (1, \infty)$, $h(x)$ increases from $h(1)=0$ to $h(x_0)$, then decreases to 0.

If $h(a_i) = C$ for all $i$:
If $C > 0$, then all $a_i$ must be in $(1, \infty)$. For a given $C \in (0, h(x_0))$, there are two solutions to $h(x)=C$ in $(1, \infty)$. If $a_i$ take two distinct values $x_A, x_B > 1$, say $k$ values are $x_A$ and $n-k$ values are $x_B$. $\sum a_i = k x_A + (n-k) x_B = 1$. Since $x_A > 1, x_B > 1$, $k x_A + (n-k) x_B > k + n - k = n$. So $1 > n$. This is only possible if $n<1$, which contradicts $n \ge 1$. If $C \ge h(x_0)$, there is at most one solution $x_0$ in $(1, \infty)$, so $a_i=x_0$. $\sum a_i = n x_0 = 1$. $x_0 = 1/n$. Since $x_0 > 1$, $1/n > 1$, $n < 1$, again impossible for $n \ge 1$.
So for $n \ge 1$, $C>0$ does not yield a solution with $a_i>0$ unless $n=0$.

If $C = 0$, then $h(a_i)=0$, which implies $a_i=1$. $\sum a_i = n \cdot 1 = n$. For this to satisfy the constraint $\sum a_i = 1$, we must have $n=1$. If $n=1$, $a_1=1$, which satisfies the constraint. $\sum (a_i+1/a_i)^p = (1+1)^p=2^p$. The RHS is $\frac{(1^2+1)^p}{1^{p-1}} = 2^p$. The inequality is an equality.

If $C < 0$, then all $a_i$ must be in $(0, 1)$. For a given $C < 0$, there is a unique solution to $h(x)=C$ in $(0,1)$. This implies all $a_i$ must be equal to this value. Let $a_i=a$. Then $\sum a_i = na = 1$, so $a=1/n$. For $a=1/n$ to be in $(0,1)$, we need $n>1$. For $n=1$, $a=1$, which is the $C=0$ case.
If $n>1$, $a=1/n \in (0,1)$. Let's check the value of $h(1/n)$: $h(1/n) = (1/n+n)^{p-1}(1-n^2)$. Since $n>1$, $1-n^2 < 0$, so $h(1/n) < 0$. This is a valid critical point with $C = h(1/n) < 0$.

Thus, for $n=1$, $a_1=1$ is the only critical point. For $n>1$, $a_i=1/n$ for all $i$ is the only critical point in the domain $a_i>0, \sum a_i=1$.

We need to determine if this critical point is a minimum. The domain $D = \{(a_1, \dots, a_n) \mid a_i > 0, \sum a_i = 1\}$ is not compact. However, consider sequences of $a_i$ approaching the boundary, i.e., where one or more $a_i \to 0$. If $a_k \to 0$ for some $k$, then $a_k+1/a_k \to \infty$. Since $p>0$, $(a_k+1/a_k)^p \to \infty$. Thus $\sum (a_i+1/a_i)^p \to \infty$ as any $a_i \to 0$.
This means the minimum value cannot occur on the boundary of the region $a_i \ge 0, \sum a_i = 1$. The minimum must be attained in the interior where $a_i>0$ for all $i$. The interior minimum must be a critical point. Since $a_i=1/n$ is the unique critical point in the interior for $n \ge 1$, it must be the global minimum for $a_i>0$.

The value of the sum at $a_i=1/n$ is:
$\sum_{i=1}^n \left( \frac{1}{n} + \frac{1}{1/n} \right)^p = \sum_{i=1}^n \left( \frac{1}{n} + n \right)^p = n \left( \frac{1+n^2}{n} \right)^p = n \frac{(1+n^2)^p}{n^p} = \frac{(1+n^2)^p}{n^{p-1}}$.

Therefore, for all $p>0$ and $n \ge 1$,
$$
\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p \geq \frac{(n^2+1)^p}{n^{p-1}}.
$$

The final answer is $\boxed{\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p \geq \frac{(n^2+1)^p}{n^{p-1}}}$.