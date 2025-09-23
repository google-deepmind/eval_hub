Yes, such a sequence exists.

To prove this, we will follow a two-step argument:
1.  First, we will show that if we can find a **bounded** sequence $(z_n) \subset \mathbb{R}^2$ such that the balls $B(z_n, 1/n)$ are mutually disjoint, then this sequence satisfies the limit condition for every continuous function $\varphi$.
2.  Second, we will show that such a bounded sequence with disjoint balls does indeed exist.

---
### Step 1: A Bounded Sequence with Disjoint Balls Satisfies the Limit Condition

Let's assume we have a sequence of points $(z_n)$ in $\mathbb{R}^2$ that is **bounded**. This means there exists a real number $R > 0$ such that $\|z_n\| < R$ for all $n \in \mathbb{N}$.
Let this sequence also satisfy the condition that the open balls $B_n = B(z_n, 1/n)$ are mutually disjoint, i.e., $B_n \cap B_m = \emptyset$ for $n \neq m$.

We need to show that for any arbitrary continuous function $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$, the following limit holds:
$$
\lim_{n \to \infty} \frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx = 0
$$

Let's analyze the location of the balls $B_n$. For any point $x \in B_n$, its norm can be bounded using the triangle inequality:
$$
\|x\| = \|x - z_n + z_n\| \le \|x - z_n\| + \|z_n\|
$$
Since $x \in B(z_n, 1/n)$, we have $\|x - z_n\| < 1/n$. Since the sequence $(z_n)$ is bounded, $\|z_n\| < R$. Also, since $n \ge 1$, we have $1/n \le 1$.
Therefore, for any $x$ in any of the balls $B_n$,
$$
\|x\| < \frac{1}{n} + R \le 1 + R
$$
This shows that the union of all balls $\bigcup_{n=1}^\infty B_n$ is contained within the open ball $B(0, R+1)$. Let $K$ be the closure of this ball, $K = \overline{B(0, R+1)}$. The set $K$ is a closed and bounded subset of $\mathbb{R}^2$, so it is compact.

Now, let $\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}$ be any continuous function. The restriction of $\varphi$ to the compact set $K$ is continuous. A well-known theorem from analysis states that a continuous function on a compact set is bounded. Therefore, there exists a finite constant $M > 0$ such that $|\varphi(x)| \le M$ for all $x \in K$.

Since each ball $B_n$ is contained in $K$, we have $|\varphi(x)| \le M$ for all $x \in B_n$ and for all $n$.

Let's consider the expression from the problem statement:
$$
I_n = \frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx
$$
We can bound its absolute value:
$$
|I_n| = \left| \frac{n}{\pi} \int_{B_n} \varphi(x) \, dx \right| \le \frac{n}{\pi} \int_{B_n} |\varphi(x)| \, dx
$$
Using the bound $|\varphi(x)| \le M$ for $x \in B_n$, we get:
$$
|I_n| \le \frac{n}{\pi} \int_{B_n} M \, dx
$$
The integral of the constant $M$ over the ball $B_n$ is $M$ times the area of the ball. The area of $B_n = B(z_n, 1/n)$ is $\pi (1/n)^2 = \pi/n^2$.
$$
|I_n| \le \frac{n}{\pi} \cdot M \cdot \left(\pi \left(\frac{1}{n}\right)^2\right) = \frac{n}{\pi} M \frac{\pi}{n^2} = \frac{M}{n}
$$
So, we have established the inequality $0 \le |I_n| \le \frac{M}{n}$ for all $n \ge 1$.
As $n \to \infty$, we have $\frac{M}{n} \to 0$. By the Squeeze Theorem, it follows that:
$$
\lim_{n \to \infty} |I_n| = 0 \implies \lim_{n \to \infty} I_n = 0
$$
This proves that if a bounded sequence $(z_n)$ with the disjoint ball property exists, it satisfies the required limit condition for any continuous function $\varphi$.

---
### Step 2: Existence of a Bounded Sequence with Disjoint Balls

Now we need to show that such a sequence actually exists. We need to find a bounded sequence of points $(z_n)$ such that the balls $B_n = B(z_n, 1/n)$ are mutually disjoint.

Consider the areas of these balls. The area of $B_n$ is $A_n = \pi(1/n)^2 = \pi/n^2$.
Let's find the sum of the areas of all such balls:
$$
\sum_{n=1}^\infty A_n = \sum_{n=1}^\infty \frac{\pi}{n^2} = \pi \sum_{n=1}^\infty \frac{1}{n^2}
$$
This is a p-series with $p=2 > 1$, so it converges. We know its value is the Basel problem result:
$$
\sum_{n=1}^\infty A_n = \pi \cdot \frac{\pi^2}{6} = \frac{\pi^3}{6}
$$
The total area of all the balls is finite. This suggests that they can all be packed into a bounded region of the plane without overlapping.

A known result from packing theory confirms this: a collection of disks with radii $r_n$ can be packed into a bounded region of the plane if the sum of their areas, $\sum \pi r_n^2$, is finite. In our case, $r_n = 1/n$, and we have just shown that $\sum \pi (1/n)^2$ is finite.

Therefore, there exists a packing of the balls $\{B_n\}_{n=1}^\infty$ into a bounded subset of $\mathbb{R}^2$. This means we can find a sequence of centers $(z_n)$ such that:
1.  The balls $B(z_n, 1/n)$ are mutually disjoint.
2.  The set of centers $\{z_n\}$ is bounded (since all balls lie in a bounded region).

This completes the proof. We have shown that a suitable bounded sequence exists, and that any such sequence fulfills the required limit condition.

---
### Conclusion

Yes, such a sequence $(z_n)$ exists. We can construct one by taking a packing of the disjoint balls $B(z_n, 1/n)$ into a bounded region, which is possible because the sum of their areas is finite. For any such sequence, because it is bounded, the sequence of balls $\{B(z_n, 1/n)\}_n$ is contained in a larger, fixed compact set. This allows us to bound any continuous function $\varphi$ on all the balls simultaneously, which in turn leads to the conclusion that the given limit is zero.

It is worth noting that if the sequence $(z_n)$ were unbounded (e.g., $\|z_n\| \to \infty$), we could construct a continuous function $\varphi$ for which the limit condition fails. For instance, by defining $\varphi$ to have a tall, narrow peak on each ball $B_n$ with height proportional to $n^2$, we could make the integral grow with $n$. The boundedness of the sequence is therefore essential.