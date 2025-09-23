Solution step (1 point):
No. Consider a function $f : \mathbb{R}^2 \rightarrow \mathbb{R}$ of the form $f(x) = \sin (\lambda x_1)$ for some $\lambda > 0$, where $x = (x_1, x_2)$. We will show that there exists $\lambda > 0$ such that 
$$
\int_{B(x_0, r)} \sin (\lambda x_1) \, dx = 0
$$
for any $x_0 \in \mathbb{R}^2$.

Solution step (1 point):
Let $x_0 = (a,b)$. Then
$$
\begin{aligned}
\int_{B(x_0,r)} \sin(\lambda x_1) \, dx &= \int_{B(0,r)} \sin \left( \lambda(x_1 + a) \right) \, dx \\
&= \int_{B(0,r)} \sin (\lambda a) \cos(\lambda x_1) + \cos(\lambda a) \sin (\lambda x_1) \, dx \\
&= \sin (\lambda a) \int_{B(0,r)}  \cos(\lambda x_1) \, dx + \cos(\lambda a) \int_{B(0,r)} \sin (\lambda x_1) \, dx.
\end{aligned}
$$
First note that
$$
\int_{B(0,r)} \sin (\lambda x_1) \, dx = \int_{-r}^r \int_{-\sqrt{r^2 - x_1^2}}^{\sqrt{r^2 - x_1^2}} \sin (\lambda x_1) \, dx_2 \, dx_1 = \int_{-r}^r 2 \sqrt{r^2 - x_1^2} \sin (\lambda x_1)  \, dx_1 = 0,
$$
since the map $x_1 \mapsto 2 \sqrt{r^2 - x_1^2} \sin (\lambda x_1)$ is odd. Hence
$$
\int_{B(x_0,r)} \sin(\lambda x_1) \, dx = \sin (\lambda a) \int_{B(0,r)}  \cos(\lambda x_1) \, dx.
$$

Solution step (7 points):
Let $g : \mathbb{R} \rightarrow \mathbb{R}$ be a function given by
$$
g(\lambda) := \int_{B(0,r)}  \cos(\lambda x_1) \, dx.
$$
It is enough to show that there is $\lambda > 0$ for which $g(\lambda) = 0$. Note that $g$ is continuous and $g(0) = \int_{B(0,r)} \, dx = \pi r^2 > 0$. Then we compute
$$
\begin{aligned}
g \left( \frac{2\pi}{r} \right) &= \int_{B(0,r)}  \cos\left( \frac{2\pi x_1}{r} \right) \, dx = \int_{-r}^r \int_{-\sqrt{r^2 - x_1^2}}^{\sqrt{r^2 - x_1^2}} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_2 \, dx_1 \\
&= \int_{-r}^r 2  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1 = \int_{0}^r 4  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1,
\end{aligned}
$$
where the last equality holds because the function $x_1 \mapsto 2  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right)$ is even. Observe that $\sqrt{r^2 - x_1^2} > 0$ for $x_1 \in (-r, r)$ and that $\cos\left( \frac{2\pi x_1}{r} \right)$ changes its sign at $\frac{r}{4}$ and $\frac{3r}{4}$. We will split this integral into two and make a change of variables in a way that the function that we integrate is positive in the first half of the interval and negative in the second part of the interval. For this purpose note that $\cos\left( \frac{2\pi x_1}{r} \right)$ is symmetric with respect to the line $x_1 = \frac{r}{2}$. Hence

$$
\begin{aligned}
&\quad \int_{0}^r 4  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1 \\
&= \int_{0}^{r/2} 4  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1 + \int_{r/2}^r 4  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1 \\
&= \int_{0}^{r/2} 4  \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1 + \int_{0}^{r/2} 4  \sqrt{r^2 - (1-x_1)^2} \cos\left( \frac{2\pi (1-x_1)}{r} \right) \, dx_1 \\
&= 4 \int_{0}^{r/2} \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) + \sqrt{r^2 - (r-x_1)^2} \cos\left( \frac{2\pi (r-x_1)}{r} \right) \, dx_1 \\
&= 4 \int_{0}^{r/2} \sqrt{r^2 - x_1^2} \cos\left( \frac{2\pi x_1}{r} \right) + \sqrt{r^2 - (r-x_1)^2} \cos\left( 2 \pi - \frac{2\pi x_1}{r} \right) \, dx_1 \\
&= 4 \int_{0}^{r/2} \left( \sqrt{r^2 - x_1^2} + \sqrt{r^2 - (r-x_1)^2} \right)  \cos\left( \frac{2\pi x_1}{r} \right) \, dx_1.
\end{aligned}
$$
Let $h : [0, r/2] \rightarrow \mathbb{R}$ be a function given by
$$
h(y) := \left( \sqrt{r^2 - y^2} + \sqrt{r^2 - (r-y)^2} \right)  \cos\left( \frac{2\pi y}{r} \right).
$$

Observe that now $h(y) \geq 0$ for $y \in [0, r/4]$ and $h(y) \leq 0$ for $y \in [r/4, r/2]$. To show that $\int_0^{r/2} h(y) \, dx \leq 0$ it is enough to show that
$$\tag{1}
h\left( \frac{r}{4} - z \right) \leq - h \left( \frac{r}{4} + z \right)
$$
for $z \in [0, r/4]$. For this purpose we note the following identities
$$
\begin{aligned}
\cos\left( \frac{2\pi \left( \frac{r}{4} - z \right)}{r} \right) &= \cos \left( \frac{\pi}{2} - \frac{2\pi z}{r} \right) = \sin \left( \frac{2\pi z}{r} \right), \\
\cos\left( \frac{2\pi \left( \frac{r}{4} + z \right)}{r} \right) &= \cos \left( \frac{\pi}{2} + \frac{2\pi z}{r} \right) = - \sin \left( \frac{2\pi z}{r} \right),
\end{aligned}
$$
hence (1) may be rewritten as
$$
\begin{aligned}
&\quad \left( \sqrt{r^2 - \left( \frac{r}{4} - z \right)^2} + \sqrt{r^2 - \left(r-\left( \frac{r}{4} - z \right) \right)^2} \right) \sin \left( \frac{2\pi z}{r} \right) \\
&\leq \left( \sqrt{r^2 - \left( \frac{r}{4} + z \right)^2} + \sqrt{r^2 - \left(r-\left( \frac{r}{4} + z \right)\right)^2} \right) \sin \left( \frac{2\pi z}{r} \right).
\end{aligned}
$$
Since $\sin \left( \frac{2\pi z}{r} \right) \geq 0$ for $z \in [0, r/4]$, it is enough to verify that
$$
\begin{aligned}
 \sqrt{r^2 - \left( \frac{r}{4} - z \right)^2} + \sqrt{r^2 - \left(r-\left( \frac{r}{4} - z \right) \right)^2}  \leq  \sqrt{r^2 - \left( \frac{r}{4} + z \right)^2} + \sqrt{r^2 - \left(r-\left( \frac{r}{4} + z \right)\right)^2}
\end{aligned}
$$
or equivalently
$$
\sqrt{(5 r - 4 z) (3 r + 4 z)} + \sqrt{(r - 4 z) (7 r + 4 z)} \leq \sqrt{(7 r - 4 z) (r + 4 z)} + \sqrt{(3 r - 4 z) (5 r + 4 z)}.
$$
Taking square of both sides we get
$$
\begin{aligned}
&\quad (5 r - 4 z) (3 r + 4 z) + 2 \sqrt{(5 r - 4 z) (3 r + 4 z)} \sqrt{(r - 4 z) (7 r + 4 z)} + (r - 4 z) (7 r + 4 z) \\
&\leq (7 r - 4 z) (r + 4 z) + 2 \sqrt{(7 r - 4 z) (r + 4 z)} \sqrt{(3 r - 4 z) (5 r + 4 z)} + (3 r - 4 z) (5 r + 4 z)
\end{aligned}
$$
and
$$
\begin{aligned}
 \sqrt{(5 r - 4 z) (3 r + 4 z)} \sqrt{(r - 4 z) (7 r + 4 z)} \leq \sqrt{(7 r - 4 z) (r + 4 z)} \sqrt{(3 r - 4 z) (5 r + 4 z)} + 16 r z.
\end{aligned}
$$
Taking squares of both sides again  we arrive at
$$
\begin{aligned}
&\quad (5 r - 4 z) (3 r + 4 z) (r - 4 z) (7 r + 4 z) \\
 &\leq (7 r - 4 z) (r + 4 z) (3 r - 4 z) (5 r + 4 z) + 32 \sqrt{(7 r - 4 z) (r + 4 z)} \sqrt{(3 r - 4 z) (5 r + 4 z)} rz + 256 r^2 z^2
\end{aligned}
$$
and
$$
\begin{aligned}
 - 608 r^2   + 512  z^2 - 256 r z  \leq 32 \sqrt{(7 r - 4 z) (r + 4 z)} \sqrt{(3 r - 4 z) (5 r + 4 z)} .
\end{aligned}
$$
Observe that the left hand side is nonpositive for $z \in \left[ \frac{r}{4} \left(1 - 2 \sqrt{5} \right), \frac{r}{4} \left( 1 + 2 \sqrt{5} \right) \right]$, in particular for $z \in [0, r/4]$. Thus the desired inequality holds (note that in this interval, anytime we took the square of both sides, they were nonnegative). 


Solution step (1 point):
To summarize, we obtained that
$$
g(0) = \pi r^2 > 0 \quad \text{and} \quad g \left( \frac{2\pi}{r} \right) \leq 0.
$$
Hence, there exists $\lambda \in \left( 0, \frac{2\pi}{r} \right]$ such that $g(\lambda) = 0$, which completes the proof.