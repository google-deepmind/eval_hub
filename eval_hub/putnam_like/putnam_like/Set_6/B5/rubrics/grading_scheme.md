Solution step (1 point):
Observe that if $a \leq 0$, then it suffices to put $c=a$ and $d=\min(0,b)$. Therefore it suffices to consider $0 \leq a < b$.

Let $S_n$ be a set of all sums of $n$ terms of the sequence $(r_n)$. We show by induction that for any natural $n$, $S_n \cap (c,d) = \emptyset$ for some $(c,d) \subset (a,b)$.

Solution step (2 points):
Let $n=1$. If for all $n$, $r_n \notin (a,b)$, then we put $c=a$ and $d=b$. If $r_n \in (a,b)$ for some $n$, then we put $c=r_n$ and $d=\min\{r_m: r_m > r_n\} \cup \{b\}$.

Solution step (3 points):
Assume the result for $n-1$ and fix $(a,b)$. Take $(c', d_0) \subset (a,b)$ such that $(c', d_0) \cap S_{n-1} = \emptyset$. Set $h = \frac{d_0 - c'}{2}$ and $c_0 = \frac{c'+d_0}{2}$. There exists $N$ such that $r_n < h$ for $n > N$.

Take $s \in S_n$. Then $s = s' + r_m$ for some $s' \in S_{n-1}$ and $m \in \mathbb{N}$. If $s \in (c_0, d_0)$, then $m \leq N$, since $|s' - c_0| \geq h$. So it suffices to find a subinterval of $(c_0, d_0)$ which excludes also sums $s = s' + r_m$ for $s' \in S_{n-1}$ and $m \leq N$.

Solution step (3 points):
Consider $(c - r_1, d - r_1)$. We can find a subinterval $(e,f)$ of this which does not intersect $S_{n-1}$. Then $(c_1, d_1) = (e+r_1, f+r_1)$ excludes sums $s' + r_1$ and $s' + r_m$ for $s' \in S_{n-1}$ and $m > N$.

Repeating this reasoning for $r_k = r_2, r_3, \ldots, r_N$ we construct intervals $(c_k, d_k) \subset (a,b)$ that exclude sums $s' + r_m$ for $m=1,2,\ldots, k, N+1, N+2, \ldots$ and $s' \in S_{n-1}$. Hence $(c,d) = (c_N, d_N)$ is a subinterval of $(a,b)$ which is distinct with $S_n$.

Solution step (1 point):
By the mathematical induction we see, that the desired result holds for $n=2025$.