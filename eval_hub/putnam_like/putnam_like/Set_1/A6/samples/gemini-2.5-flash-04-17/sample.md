Let $B(x_0, r)$ denote the open disk centered at $x_0$ with radius $r$. The given condition is $\int_{B(x_0, r)} f(x) \, dx = 0$ for all $x_0 \in \mathbb{R}^2$. The function $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ is continuous.

Let $g(x)$ be the characteristic function of the open disk $B(0, r)$, i.e., $g(x) = \mathbf{1}_{B(0, r)}(x) = \begin{cases} 1 & \text{if } \|x\| < r \\ 0 & \text{if } \|x\| \ge r \end{cases}$.
The integral condition can be written as $\int_{\mathbb{R}^2} f(x) \mathbf{1}_{B(x_0, r)}(x) \, dx = 0$.
Let $y = x - x_0$. Then $x = y + x_0$ and the integral becomes $\int_{\mathbb{R}^2} f(y+x_0) \mathbf{1}_{B(0, r)}(y) \, dy = 0$.
Let $\tilde{g}(y) = \mathbf{1}_{B(0, r)}(-y)$. Since $B(0, r)$ is symmetric about the origin, $\tilde{g}(y) = \mathbf{1}_{B(0, r)}(y) = g(y)$.
The condition is $\int_{\mathbb{R}^2} f(y+x_0) g(y) \, dy = 0$.
Let $y' = -y$. $\int_{\mathbb{R}^2} f(x_0-y') g(-y') \, dy' = \int_{\mathbb{R}^2} f(x_0-y') g(y') \, dy' = (f * g)(x_0) = 0$ for all $x_0 \in \mathbb{R}^2$.

We are given that $f$ is continuous. A continuous function on $\mathbb{R}^2$ is a tempered distribution. The characteristic function $g$ is an $L^1$ function (compactly supported). The convolution of a tempered distribution and an $L^1$ function is a tempered distribution. The Fourier transform of a tempered distribution $T$ is denoted by $\hat{T}$. The convolution theorem for tempered distributions states that $\widehat{T*S} = \hat{T}\hat{S}$ for $T \in \mathcal{S}'$ and $S \in \mathcal{O}_M$ or if one is $\mathcal{S}'$ and the other is $\mathcal{S}$ or $C_c^\infty$. Here $f \in \mathcal{S}'$ and $g \in L^1 \subset \mathcal{S}'$. $g$ is $C_c^\infty$ except at boundary, but its Fourier transform $\hat{g}$ is a smooth function rapidly decreasing. This case is covered by the convolution theorem.

Taking the Fourier transform of $(f*g)(x_0) = 0$, we get $\hat{f}(\xi)\hat{g}(\xi) = 0$ in the sense of tempered distributions.

We need to compute the Fourier transform of $g(x) = \mathbf{1}_{B(0, r)}(x)$. We use the convention $\hat{h}(\xi) = \int_{\mathbb{R}^2} h(x) e^{-i x \cdot \xi} \, dx$.
Using polar coordinates for $x=(x_1, x_2)$ and $\xi=(\xi_1, \xi_2)$, let $x = (\rho \cos\theta, \rho \sin\theta)$ and $\xi = (\lambda \cos\alpha, \lambda \sin\alpha)$, where $\rho=\|x\| \ge 0$, $\lambda=\|\xi\| \ge 0$. $x \cdot \xi = \rho\lambda \cos(\theta-\alpha)$.
$\hat{g}(\xi) = \int_0^r \int_0^{2\pi} e^{-i \rho\lambda \cos(\theta-\alpha)} \rho \, d\theta \, d\rho$.
The inner integral $\int_0^{2\pi} e^{-i z \cos\phi} \, d\phi = 2\pi J_0(z)$, where $J_0$ is the Bessel function of the first kind of order 0.
So $\hat{g}(\xi) = \int_0^r \rho (2\pi J_0(\rho\lambda)) \, d\rho = 2\pi \int_0^r \rho J_0(\rho\lambda) \, d\rho$.
Using the identity $\int z J_0(z) \, dz = z J_1(z)$, let $z=\rho\lambda$.
$\int_0^r \rho J_0(\rho\lambda) \, d\rho = \frac{1}{\lambda^2} \int_0^{r\lambda} (\rho\lambda) J_0(\rho\lambda) \lambda \, d\rho = \frac{1}{\lambda^2} \int_0^{r\lambda} z J_0(z) \, dz = \frac{1}{\lambda^2} [z J_1(z)]_0^{r\lambda} = \frac{1}{\lambda^2} r\lambda J_1(r\lambda) = \frac{r}{\lambda} J_1(r\lambda)$ for $\lambda \ne 0$.
For $\lambda = 0$, $\hat{g}(0) = \int_{B(0,r)} 1 \, dx = \pi r^2$.
The expression $\frac{J_1(z)}{z}$ approaches $1/2$ as $z \to 0$, so $2\pi r \frac{J_1(r\lambda)}{\lambda} = 2\pi r^2 \frac{J_1(r\lambda)}{r\lambda} \to 2\pi r^2 (1/2) = \pi r^2$ as $\lambda \to 0$.
Thus, $\hat{g}(\xi) = 2\pi r^2 \frac{J_1(r\|\xi\|)}{r\|\xi\|}$ for $\|\xi\| \ne 0$ and $\hat{g}(0) = \pi r^2$.

The equation $\hat{f}(\xi)\hat{g}(\xi) = 0$ means that $\hat{f}$ must be supported on the set of zeros of $\hat{g}$.
The positive zeros of $J_1(z)$ are denoted by $z_k$ for $k=1, 2, \ldots$.
$\hat{g}(\xi) = 0$ if $r\|\xi\| = z_k$ for $k=1, 2, \ldots$. This is because $J_1(z)/z$ is non-zero at $z=0$.
So the set of zeros of $\hat{g}$ is $Z = \{\xi \in \mathbb{R}^2 : \|\xi\| = z_k/r, \text{ for } k=1, 2, \ldots\}$. This is a countable union of circles centered at the origin.

$\hat{f}$ must be supported on $Z$. This means that for any test function $\phi$ with support disjoint from $Z$, $\langle \hat{f}, \phi \rangle = 0$.
For a general continuous function $f$, this does not imply $f \equiv 0$. For example, if $f(x) = \cos(a \cdot x)$, its Fourier transform is $\hat{f}(\xi) = \pi (\delta(\xi-a) + \delta(\xi+a))$ using the $e^{-ix\cdot\xi}$ convention. The support of $\hat{f}$ is $\{a, -a\}$. If this set is contained in $Z$, then $\hat{f}\hat{g}=0$ is satisfied.

Let's choose $a = (a_1, a_2)$ such that $\|a\| = z_k/r$ for some $k \ge 1$. For instance, take $a=(z_k/r, 0)$.
Consider the function $f(x_1, x_2) = \cos( (z_k/r) x_1 )$ for $k \ge 1$. This function is continuous and not identically zero. Let $a = z_k/r$.
We check if $\int_{B(x_0, r)} \cos(ax_1) \, dx = 0$ for all $x_0 \in \mathbb{R}^2$.
Let $x_0 = (x_{01}, x_{02})$. The integral is $\int_{B(0,r)} \cos(a(y_1+x_{01})) \, dy$, where $y=x-x_0$.
$\int_{B(0,r)} \cos(ay_1)\cos(ax_{01}) - \sin(ay_1)\sin(ax_{01}) \, dy$.
Using polar coordinates $y=(\rho\cos\theta, \rho\sin\theta)$:
$\int_{B(0,r)} \cos(ay_1) \, dy = \int_0^r \int_0^{2\pi} \cos(a\rho\cos\theta) \rho \, d\theta \, d\rho = \int_0^r \rho (2\pi J_0(a\rho)) \, d\rho = 2\pi \frac{r}{a} J_1(ar)$.
$\int_{B(0,r)} \sin(ay_1) \, dy = \int_0^r \int_0^{2\pi} \sin(a\rho\cos\theta) \rho \, d\theta \, d\rho = \int_0^r \rho (0) \, d\rho = 0$.
So the integral is $\cos(ax_{01}) \left( 2\pi \frac{r}{a} J_1(ar) \right) - \sin(ax_{01}) (0) = 2\pi \frac{r}{a} J_1(ar) \cos(ax_{01})$.
For this to be zero for all $x_{01} \in \mathbb{R}$, we must have $J_1(ar) = 0$.
This is true if $ar = z_k$ for some $k=1, 2, \ldots$.
Since $a=z_k/r$, $ar = (z_k/r)r = z_k$. So $J_1(ar) = J_1(z_k) = 0$.

Thus, $f(x_1, x_2) = \cos(z_k x_1/r)$ for any $k \ge 1$ is a continuous, non-zero function such that its integral over any disk of radius $r$ is zero.

The answer to the question is no.

The final answer is $\boxed{No}$.