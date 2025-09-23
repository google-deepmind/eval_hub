Solution:
Let $B_n = B(z_n, 1/n)$ denote the open ball centered at $z_n \in \mathbb{R}^2$ with radius $r_n = 1/n$. The problem asks if there exists a sequence $(z_n) \subset \mathbb{R}^2$ such that:
1. The balls $B_n$ are pairwise disjoint, i.e., $B_n \cap B_m = \emptyset$ for $n \neq m$.
2. For every continuous function $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$, the sequence $L_n(\varphi)$ converges to 0, where
$$
L_n(\varphi) = \frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx.
$$

Let's analyze the expression $L_n(\varphi)$. The area of the ball $B_n$ is $A_n = \pi r_n^2 = \pi (1/n)^2 = \pi/n^2$.
By the Mean Value Theorem for integrals, for a continuous function $\varphi$, there exists a point $c_n \in B_n$ such that
$$
\int_{B_n} \varphi(x) \, dx = A_n \varphi(c_n) = \frac{\pi}{n^2} \varphi(c_n).
$$
Substituting this into the expression for $L_n(\varphi)$, we get
$$
L_n(\varphi) = \frac{n}{\pi} \left( \frac{\pi}{n^2} \varphi(c_n) \right) = \frac{\varphi(c_n)}{n}.
$$
So the condition 2 is equivalent to $\frac{\varphi(c_n)}{n} \to 0$ for every continuous function $\varphi$, where $c_n$ is some point in $B_n$ (the specific point $c_n$ may depend on $\varphi$).

We investigate the properties of the sequence $(z_n)$.

Case 1: Assume the sequence $(z_n)$ is bounded.
If $(z_n)$ is bounded, there exists $R > 0$ such that $\|z_n\| \le R$ for all $n$.
Since $c_n \in B(z_n, 1/n)$, we have $\|c_n\| \le \|z_n\| + 1/n \le R + 1/n$. For $n \ge 1$, $\|c_n\| \le R+1$.
Thus, the sequence $(c_n)$ is contained in the closed ball $\bar{B}(0, R+1)$. Let $K = \bar{B}(0, R+1)$. $K$ is a compact set in $\mathbb{R}^2$.
Let $\varphi: \mathbb{R}^2 \to \mathbb{R}$ be any continuous function. Since $\varphi$ is continuous on $\mathbb{R}^2$, it is continuous on the compact set $K$. Therefore, $\varphi$ is bounded on $K$. Let $M_\varphi = \sup_{x \in K} |\varphi(x)|$. Then $M_\varphi < \infty$.
Since $c_n \in K$ for all $n \ge 1$, we have $|\varphi(c_n)| \le M_\varphi$.
Then, for $n \ge 1$,
$$
|L_n(\varphi)| = \left| \frac{\varphi(c_n)}{n} \right| \le \frac{M_\varphi}{n}.
$$
As $n \to \infty$, $M_\varphi/n \to 0$. Thus, by the Squeeze Theorem, $L_n(\varphi) \to 0$.
Since this holds for any continuous function $\varphi$, condition 2 is satisfied if $(z_n)$ is bounded and satisfies condition 1.

Does such a bounded sequence $(z_n)$ exist? Condition 1 requires the balls $B_n = B(z_n, 1/n)$ to be disjoint. The total area of these balls is
$$
\sum_{n=1}^\infty \text{Area}(B_n) = \sum_{n=1}^\infty \frac{\pi}{n^2} = \pi \sum_{n=1}^\infty \frac{1}{n^2} = \pi \frac{\pi^2}{6} = \frac{\pi^3}{6}.
$$
Since the total area is finite, it is known from packing theory that such a sequence of disjoint balls can be placed within a bounded region of $\mathbb{R}^2$. For example, theorems by Kershner (1939) or related results imply that if the sum of the areas of disks is finite, they can be packed into a sufficiently large bounded set (e.g., a larger disk or square). Therefore, there exists a sequence $(z_n)$ such that all $z_n$ are contained in some large ball $B(0, R')$, and the balls $B(z_n, 1/n)$ are disjoint. Thus, a bounded sequence $(z_n)$ satisfying condition 1 exists.

Case 2: Assume the sequence $(z_n)$ is unbounded.
If $(z_n)$ is unbounded, then $\|z_n\| \to \infty$ (perhaps for a subsequence, but let's assume for the whole sequence for simplicity; if only for a subsequence, the argument still shows failure). Since the balls $B_n$ are disjoint, the points $z_n$ must be distinct. As $\|z_n\| \to \infty$, the set $\{z_n\}_{n=1}^\infty$ is a discrete set in $\mathbb{R}^2$ (it has no limit points).
We construct a specific continuous function $\varphi$ for which condition 2 fails.
Let $\delta_n = 1/(2n)$. Since $1/n+1/m > 1/(2n)+1/(2m)$ for $n \neq m$, the balls $B(z_n, \delta_n)$ are also disjoint. Note that $B(z_n, \delta_n) \subset B(z_n, 1/n) = B_n$.
Define $\varphi_n: \mathbb{R}^2 \to \mathbb{R}$ by
$$
\varphi_n(x) = \max\left(0, n \left(1 - \frac{\|x-z_n\|}{\delta_n}\right)\right) = \max(0, n(1 - 2n\|x-z_n\|)).
$$
$\varphi_n$ is continuous, non-negative, $\varphi_n(z_n)=n$, and the support of $\varphi_n$ is the closed ball $\bar{B}(z_n, \delta_n)$.
Since the balls $\bar{B}(z_n, \delta_n)$ are disjoint and the set of centers $\{z_n\}$ is discrete (as $\|z_n\| \to \infty$), the function $\varphi(x) = \sum_{k=1}^\infty \varphi_k(x)$ is well-defined and continuous. For any $x$, at most one term in the sum is non-zero. Continuity at any point $x \notin \bigcup_k \text{supp}(\varphi_k)$ is clear ($\varphi=0$ in a neighborhood). Continuity at $x \in \text{supp}(\varphi_k)$ follows from continuity of $\varphi_k$. Continuity at limit points of the union of supports needs checking. However, since $\|z_n\| \to \infty$, the set $S = \bigcup_k \text{supp}(\varphi_k)$ is closed, and $\varphi$ is continuous.

Now we compute $L_n(\varphi)$ for this function $\varphi$. Since the supports are disjoint, when integrating over $B_n = B(z_n, 1/n)$, only $\varphi_n(x)$ contributes to the integral.
$$
L_n(\varphi) = \frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx = \frac{n}{\pi} \int_{B(z_n, \delta_n)} n(1 - 2n\|x-z_n\|) \, dx.
$$
Let $y = x - z_n$. The integral becomes
$$
L_n(\varphi) = \frac{n^2}{\pi} \int_{B(0, \delta_n)} (1 - 2n\|y\|) \, dy.
$$
Using polar coordinates $y = (r \cos \theta, r \sin \theta)$, $dy = r dr d\theta$, and $\delta_n = 1/(2n)$:
$$
L_n(\varphi) = \frac{n^2}{\pi} \int_0^{2\pi} \int_0^{1/(2n)} (1 - 2n r) r \, dr \, d\theta = \frac{n^2}{\pi} (2\pi) \int_0^{1/(2n)} (r - 2n r^2) \, dr
$$
$$
L_n(\varphi) = 2n^2 \left[ \frac{r^2}{2} - \frac{2n r^3}{3} \right]_0^{1/(2n)} = 2n^2 \left( \frac{(1/(2n))^2}{2} - \frac{2n (1/(2n))^3}{3} \right)
$$
$$
L_n(\varphi) = 2n^2 \left( \frac{1}{2(4n^2)} - \frac{2n}{3(8n^3)} \right) = 2n^2 \left( \frac{1}{8n^2} - \frac{1}{12n^2} \right)
$$
$$
L_n(\varphi) = 2n^2 \left( \frac{3 - 2}{24n^2} \right) = 2n^2 \left( \frac{1}{24n^2} \right) = \frac{2}{24} = \frac{1}{12}.
$$
So, for this continuous function $\varphi$, $L_n(\varphi) = 1/12$ for all $n$. This sequence does not converge to 0.
Therefore, if the sequence $(z_n)$ is unbounded, condition 2 cannot hold for all continuous functions.

Conclusion:
A sequence $(z_n)$ satisfying the conditions exists if and only if there exists a bounded sequence $(z_n)$ satisfying condition 1. We have argued, based on packing theory, that such a bounded sequence exists because the total area of the balls is finite. For any such bounded sequence, we showed that condition 2 is satisfied for all continuous functions $\varphi$.

Final Answer: Yes, such a sequence exists.

```markdown
Let $B_n = B(z_n, 1/n)$ denote the open ball in $\mathbb{R}^2$ centered at $z_n$ with radius $r_n = 1/n$. The problem asks for the existence of a sequence $(z_n) \subset \mathbb{R}^2$ satisfying two conditions:
1. The balls $B_n$ are pairwise disjoint: $B_n \cap B_m = \emptyset$ for $n \neq m$.
2. For every continuous function $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$, $L_n(\varphi) \to 0$ as $n \to \infty$, where
$$ L_n(\varphi) = \frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx. $$

The area of the ball $B_n$ is $A_n = \pi r_n^2 = \pi (1/n)^2 = \pi/n^2$.
By the Mean Value Theorem for integrals, for any continuous function $\varphi$, there exists a point $c_n \in B_n$ such that
$$ \int_{B_n} \varphi(x) \, dx = A_n \varphi(c_n) = \frac{\pi}{n^2} \varphi(c_n). $$
Substituting this into the expression for $L_n(\varphi)$, we obtain
$$ L_n(\varphi) = \frac{n}{\pi} \left( \frac{\pi}{n^2} \varphi(c_n) \right) = \frac{\varphi(c_n)}{n}. $$
Note that the point $c_n$ generally depends on $\varphi$. The condition 2 is thus equivalent to $\frac{\varphi(c_n)}{n} \to 0$ for every continuous function $\varphi$, for some $c_n \in B_n$.

We analyze the consequences of the sequence $(z_n)$ being bounded or unbounded.

Case 1: $(z_n)$ is bounded.
Suppose there exists $R > 0$ such that $\|z_n\| \le R$ for all $n$. Since $c_n \in B(z_n, 1/n)$, we have $\|c_n\| \le \|z_n\| + 1/n \le R + 1/n$. For $n \ge 1$, $\|c_n\| \le R+1$. Thus, the sequence $(c_n)$ is contained in the closed ball $K = \bar{B}(0, R+1)$, which is a compact set.
Let $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$ be any continuous function. Since $K$ is compact, $\varphi$ is bounded on $K$. Let $M_\varphi = \sup_{x \in K} |\varphi(x)| < \infty$.
Since $c_n \in K$ (for any choice of $c_n \in B_n$), we have $|\varphi(c_n)| \le M_\varphi$.
Therefore, $|L_n(\varphi)| = \left| \frac{\varphi(c_n)}{n} \right| \le \frac{M_\varphi}{n}$.
As $n \to \infty$, $M_\varphi/n \to 0$. By the Squeeze Theorem, $L_n(\varphi) \to 0$.
This holds for *every* continuous function $\varphi$.
So, if a bounded sequence $(z_n)$ satisfying condition 1 exists, then condition 2 is also satisfied.

The existence of such a bounded sequence $(z_n)$ is a result from packing theory. The sum of the areas of the balls $B_n$ is $\sum_{n=1}^\infty A_n = \sum_{n=1}^\infty \frac{\pi}{n^2} = \frac{\pi^3}{6}$, which is finite. It is known that any sequence of disks with finite total area can be packed into a bounded region in $\mathbb{R}^2$. Thus, there exists a bounded sequence $(z_n)$ satisfying condition 1.

Case 2: $(z_n)$ is unbounded.
If $(z_n)$ is unbounded, then $\|z_n\| \to \infty$ (at least for a subsequence). We show that condition 2 fails for such sequences. Assume $\|z_n\| \to \infty$. This implies the set $\{z_n\}$ is discrete.
Let $\delta_n = 1/(2n)$. The balls $B(z_n, \delta_n)$ are disjoint and $B(z_n, \delta_n) \subset B_n$. Define a function $\varphi$ as follows: Let $\varphi_n(x) = \max(0, n(1 - \|x-z_n\|/\delta_n))$. Let $\varphi(x) = \sum_{n=1}^\infty \varphi_n(x)$. Since the supports $\text{supp}(\varphi_n) = \bar{B}(z_n, \delta_n)$ are disjoint and form a closed set (because $\|z_n\| \to \infty$), the function $\varphi$ is continuous. Also $\varphi(x) \ge 0$ for all $x$.
Let's compute $L_n(\varphi)$.
$$ L_n(\varphi) = \frac{n}{\pi} \int_{B_n} \varphi(x) \, dx = \frac{n}{\pi} \int_{B(z_n, \delta_n)} n(1 - 2n\|x-z_n\|) \, dx. $$
Using the calculation from the thought process (polar coordinates substitution):
$$ L_n(\varphi) = \frac{1}{12}. $$
Since $L_n(\varphi) = 1/12$ for all $n$, the sequence $L_n(\varphi)$ does not converge to 0.
Thus, if $(z_n)$ is unbounded, condition 2 fails for this specific continuous function $\varphi$.

Combining the cases:
A sequence $(z_n)$ satisfying both conditions can only exist if it is bounded. The existence of a bounded sequence satisfying condition 1 is guaranteed by packing results for disks with finite total area. For any such bounded sequence, condition 2 is satisfied for all continuous functions.

Therefore, such a sequence $(z_n)$ exists.

Final Answer: The final answer is $\boxed{Yes}$
```