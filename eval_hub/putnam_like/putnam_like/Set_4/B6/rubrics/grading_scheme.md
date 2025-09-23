Yes, such a sequence exists.

This step is worth 8 points.
We will construct a sequence $(z_n)_{n \geq 1}$ such that $B(z_n,1/n) \subset B(0,R_n)$ and $B(z_n, 1/n) \cap B(z_m, 1/m) = \emptyset$, where $(R_n)$ is a decreasing sequence such that $(\sqrt{n} R_n)$ is bounded.

Consider the family of squares $\{ Q_n \}_{n\geq 1}$ in $\mathbb{R}^2$, where $Q_n$ is defined as follows: its sides are parallel to the axis, side length equals $\frac{1}{2^{n-2}}$ and the right bottom vertex is $( 8 - \sum_{k=0}^{n-2} \frac{1}{2^{k-2}}, 0 )$. Observe that

* we can divide $Q_1$ into $4$ squares of the side length $2$ and choose $z_1, z_2, z_3$ such that the balls $B(z_1, 1)$, $B(z_2, 1/2)$, $B(z_3, 1/3)$ are pairwise disjoint and contained in $Q_1$ (each ball in one of the smaller squares); note that $1$ square will be left empty;
* we divide $Q_2$ into $16$ squares of the side length $\frac{1}{2}$ and then we choose $z_4, x_5, \ldots, z_{15}$ such that $B(z_4, 1/4)$, $B(z_5, 1/5)$, $\ldots$,  $B(z_{15}, 1/15)$ are pairwise disjoint and contained in $Q_2$ (again, each ball in one of the smaller squares); this time $4$ smaller squares are left empty;
* ...
* we divide $Q_n$ into $4^{n}$ squares, each of the side length equal to $\frac{1}{2^{n-2} \cdot 2^n} = \frac{1}{4^{n-1}}$; then we can choose $z_{4^{n-1}}, \ldots, z_{4^{n}-1}$ such that they are pairwise disjoint and contained in $Q_n$ - each ball in one of the smaller squares and $4^{n-1}$ squares are left empty.

This way we constructed a sequence $(z_n) \subset \mathbb{R}^2$ such that
$$
z_{4^{n-1}}, \ldots, z_{4^{n}-1} \in Q_n.
$$
Hence, we can write that
$$
z_{n} \in Q_{\lfloor \log_4(n) \rfloor + 1} \quad \text{ for every } n \geq 1.
$$
Note that the square $Q_n$ is contained in $B(0, r_n)$, where $r_n$ is the distance from $0$ to the right top vertex of $Q_n$. Thus
$$
\begin{aligned}
r_n &= \sqrt{ \left(8 - \sum_{k=0}^{n-2} \frac{1}{2^{k-2}}\right)^2 + \left( \frac{1}{2^{n-2}} \right)^2} = \sqrt{ \left( \frac{4}{2^{n-2}} \right)^2 + \left( \frac{1}{2^{n-2}} \right)^2 } \\
&= \sqrt{ 17 \left( \frac{1}{2^{n-2}} \right)^2 } = \frac{\sqrt{17}}{2^{n-2}} = \frac{\sqrt{17}}{4} \cdot \frac{1}{2^n}.
\end{aligned}
$$
Define 
$$
R_n := r_{\lfloor \log_4(n) \rfloor + 1}.
$$
Then clearly $B(z_n,1/n) \subset B(0, R_n)$. We need to show that $(\sqrt{n} R_n)$ is bounded. Indeed, we have that 
$$
\begin{aligned}
\sqrt{n} R_n &= \sqrt{n} r_{\lfloor \log_4(n) \rfloor + 1} =  \sqrt{n} \frac{\sqrt{17}}{4} \cdot \frac{1}{2^{\lfloor \log_4(n) \rfloor + 1}} \leq \sqrt{n} \frac{\sqrt{17}}{4} \cdot \frac{1}{2^{\log_4(n)}} \\
&= \sqrt{n} \frac{\sqrt{17}}{4} \cdot \frac{1}{\sqrt{n}} = \frac{\sqrt{17}}{4}.
\end{aligned}
$$

This step is worth 2 points.
We will show that for such a sequence
$$
\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx \to 0.
$$
Clearly, since $|B(z_n, 1/n)| = \frac{\pi}{n^2}$, $\frac{1}{n} \varphi(0) = \frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(0) \, dx \to 0$.
It is enough then to show that
$$
| \frac{n}{\pi} \int_{B(z_n, 1/n)}  \varphi(x) - \varphi(0)  \, dx | \to 0.
$$
For this purpose we recall that $B(z_n, 1/n) \subset B(0,R_n)$ and we estimate
$$
\begin{aligned}
\left| \frac{n}{\pi} \int_{B(z_n, 1/n)}  \varphi(x) - \varphi(0)  \, dx \right| &\leq  \frac{n}{\pi}  \int_{B(z_n, 1/n)} \left| \varphi(x) - \varphi(0) \right| \, dx \\
&\leq  \frac{n}{\pi}  \int_{B(0, R_n)} \left| \varphi(x) - \varphi(0) \right| \, dx = (*).
\end{aligned}
$$
Since the set $\overline{B(0,R_n)}$ is compact, $\varphi$ is uniformly continuous on $B(0,R_n)$. Moreover, $R_n\to 0^+$. Hence for every $\varepsilon > 0$ there is $n$ such that $\sup_{x \in B(0, R_n)} |\varphi(x)-\varphi(0)| < \varepsilon$. Since $R_n$ is decreasing we infer that, $\sup_{x \in B(0, R_m)} |\varphi(x)-\varphi(0)| < \varepsilon$ for all $m \geq n$. Then we can estimate
$$
(*) \leq \frac{n}{\pi}  \int_{B(0, R_n)} \varepsilon \, dx  = n R_n^2 \varepsilon
$$
and the proof is completed, because the sequence $(\sqrt{n} R_n)$ is bounded.