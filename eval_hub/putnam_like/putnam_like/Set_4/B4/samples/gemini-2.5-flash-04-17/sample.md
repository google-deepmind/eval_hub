Let $I$ be the integral we want to evaluate:
$$ I = \int_{B(0,1)} |x_1|^{2k} \, dx $$
where $B(0,1) = \{x \in \mathbb{R}^n : |x| \leq 1\}$. Since the integrand $|x_1|^{2k} = x_1^{2k}$ is an even function of $x_1$ and the domain $B(0,1)$ is symmetric with respect to the hyperplane $x_1=0$, we can write $I = \int_{B(0,1)} x_1^{2k} \, dx$.

We use spherical coordinates $x = r \xi$, where $r = |x| \in [0,1]$ and $\xi \in S^{n-1}$ (the unit sphere in $\mathbb{R}^n$). The Jacobian of this transformation is $r^{n-1}$. The integral becomes:
$$ I = \int_0^1 \int_{S^{n-1}} (r\xi_1)^{2k} r^{n-1} \, d\sigma(\xi) dr = \int_0^1 r^{2k+n-1} \, dr \int_{S^{n-1}} \xi_1^{2k} \, d\sigma(\xi) $$
Let $J_m = \int_{S^{n-1}} \xi_1^m \, d\sigma(\xi)$. The radial integral is $\int_0^1 r^{2k+n-1} \, dr = \left[\frac{r^{2k+n}}{2k+n}\right]_0^1 = \frac{1}{2k+n}$ for $2k+n > 0$, which is true since $k \ge 1$ and $n \ge 1$.
So, $I = \frac{1}{2k+n} J_{2k}$.

To evaluate $J_{2k}$, we can use the divergence theorem. Let $F(x) = (x_1^{m+1}, 0, \dots, 0)$. The divergence of $F$ is $\nabla \cdot F = \frac{\partial}{\partial x_1}(x_1^{m+1}) = (m+1)x_1^m$. For $m=2k$, this is $(2k+1)x_1^{2k}$.
For $k \ge 1$, $m=2k \ge 2$, so $m+1 \ge 3$. The function $x_1^{m+1}$ is $C^2$, so the divergence theorem is applicable on the ball $B(0,1)$.
The divergence theorem states $\int_{B(0,1)} \nabla \cdot F \, dx = \int_{\partial B(0,1)} F \cdot \nu \, d\sigma$, where $\nu$ is the outward normal to the boundary $\partial B(0,1)$. The boundary of $B(0,1)$ is the unit sphere $S^{n-1}$, and the outward normal at a point $x \in S^{n-1}$ is $\nu = x$.
$$ \int_{B(0,1)} (2k+1)x_1^{2k} \, dx = \int_{S^{n-1}} (x_1^{2k+1}, 0, \dots, 0) \cdot (x_1, x_2, \dots, x_n) \, d\sigma(x) $$
$$ (2k+1) \int_{B(0,1)} x_1^{2k} \, dx = \int_{S^{n-1}} x_1^{2k+2} \, d\sigma(x) $$
The integral on the left is $(2k+1)I$. The integral on the right is $J_{2k+2}$ (using $x$ for the integration variable on $S^{n-1}$, which is the same as $\xi$).
So we have the relation $(2k+1)I = J_{2k+2}$.
Substituting $I = \frac{1}{2k+n} J_{2k}$, we get $(2k+1) \frac{1}{2k+n} J_{2k} = J_{2k+2}$.
This gives a recursive formula for $J_m$ for even $m$:
$$ J_{m+2} = \frac{m+1}{m+n} J_m $$
Let $m=2k$.
$J_{2k} = \frac{2k-1}{2k-2+n} J_{2k-2} = \frac{2k-1}{2k+n-2} \frac{2k-3}{2k+n-4} J_{2k-4} = \dots$
We can apply this repeatedly until we reach $J_0$:
$$ J_{2k} = \frac{2k-1}{2k+n-2} \frac{2k-3}{2k+n-4} \dots \frac{1}{n} J_0 $$
$J_0 = \int_{S^{n-1}} \xi_1^0 \, d\sigma(\xi) = \int_{S^{n-1}} 1 \, d\sigma(\xi) = \omega_n$, the surface area of $S^{n-1}$.
So, $J_{2k} = \omega_n \prod_{j=1}^k \frac{2j-1}{2j+n-2}$.

Now substitute this back into the expression for $I$:
$$ I = \frac{1}{2k+n} J_{2k} = \frac{\omega_n}{2k+n} \prod_{j=1}^k \frac{2j-1}{2j+n-2} $$
We want to show that $I \geq \frac{\omega_n}{n^{k} (2k+n)}$.
This is equivalent to showing:
$$ \frac{\omega_n}{2k+n} \prod_{j=1}^k \frac{2j-1}{2j+n-2} \geq \frac{\omega_n}{n^k (2k+n)} $$
Since $\omega_n > 0$ and $2k+n > 0$, we can multiply by $\frac{2k+n}{\omega_n}$:
$$ \prod_{j=1}^k \frac{2j-1}{2j+n-2} \geq \frac{1}{n^k} $$
Multiply both sides by $n^k$:
$$ n^k \prod_{j=1}^k \frac{2j-1}{2j+n-2} \geq 1 $$
$$ \prod_{j=1}^k \frac{n(2j-1)}{2j+n-2} \geq 1 $$
This inequality holds if each term in the product is greater than or equal to 1:
$$ \frac{n(2j-1)}{2j+n-2} \geq 1 \quad \text{for each } j \in \{1, 2, \dots, k\} $$
Let's check this inequality:
$$ n(2j-1) \geq 2j+n-2 $$
$$ 2jn - n \geq 2j + n - 2 $$
$$ 2jn - 2j - 2n + 2 \geq 0 $$
$$ 2j(n-1) - 2(n-1) \geq 0 $$
$$ 2(j-1)(n-1) \geq 0 $$
This inequality holds for all integers $j \geq 1$ and $n \geq 1$.
Since $k \geq 1$, the index $j$ runs from 1 to $k$.
For $j=1$, the term is $2(1-1)(n-1) = 0 \geq 0$.
For $j \geq 2$, $j-1 > 0$. If $n=1$, $(j-1)(0)=0$. If $n > 1$, $n-1 > 0$, so $2(j-1)(n-1) > 0$.
Thus, for all $j \in \{1, 2, \dots, k\}$ and $n \ge 1$, the inequality $\frac{n(2j-1)}{2j+n-2} \geq 1$ is true.

Therefore, the product $\prod_{j=1}^k \frac{n(2j-1)}{2j+n-2} \geq \prod_{j=1}^k 1 = 1$.
This proves the desired inequality:
$$ \int_{B(0,1)} |x_1|^{2k} \, dx \geq \frac{\omega_n}{n^{k} (2k+n)} $$

The final answer is $\boxed{\int_{B(0,1)} |x_1|^{2k} \, dx \geq \frac{\omega_n}{n^{k} (2k+n)}}$.