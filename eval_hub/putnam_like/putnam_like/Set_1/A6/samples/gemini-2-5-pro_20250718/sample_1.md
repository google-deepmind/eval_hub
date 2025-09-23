This is a fascinating problem that delves into the relationship between a function and its integrals over specific regions. The statement is **false**. It does not imply that $f \equiv 0$.

We will construct a non-zero continuous function $f$ that satisfies the given condition. The key idea is to use Fourier analysis.

### Step 1: Reformulating the Problem as a Convolution

Let $g(x)$ be the indicator function of the disk of radius $r$ centered at the origin:
$$
g(x) = \mathbf{1}_{B(0, r)}(x) = \begin{cases} 1 & \text{if } |x| \le r \\ 0 & \text{if } |x| > r \end{cases}
$$
The integral of $f$ over a ball $B(x_0, r)$ can be written as:
$$
\int_{B(x_0, r)} f(y) \, dy
$$
Let's make a change of variables $y = x_0 + z$. Then $dy = dz$ and the region of integration becomes $|(x_0+z) - x_0| \le r$, which is $|z| \le r$, or $z \in B(0, r)$. The integral is:
$$
\int_{B(0, r)} f(x_0 + z) \, dz
$$
Now, let's define another change of variables $x = -z$. Then $dz = dx$ and the region of integration remains $B(0, r)$ since it's symmetric about the origin.
$$
\int_{B(0, r)} f(x_0 - x) \, dx
$$
This expression is precisely the definition of the convolution of functions $f$ and $g$, evaluated at $x_0$.
$$
(f * g)(x_0) = \int_{\mathbb{R}^2} f(x_0 - x) g(x) \, dx = \int_{B(0, r)} f(x_0 - x) \cdot 1 \, dx
$$
The problem statement says that this integral is zero for all $x_0 \in \mathbb{R}^2$. Therefore, the condition is equivalent to:
$$
(f * g)(x) \equiv 0 \quad \text{for all } x \in \mathbb{R}^2
$$

### Step 2: Applying the Convolution Theorem

The Convolution Theorem states that the Fourier transform of a convolution of two functions is the product of their individual Fourier transforms. Let $\hat{f}$ denote the Fourier transform of $f$.
$$
\widehat{f*g}(\xi) = \hat{f}(\xi) \hat{g}(\xi)
$$
Since $f*g$ is the zero function, its Fourier transform is also the zero function. Thus, we have:
$$
\hat{f}(\xi) \hat{g}(\xi) = 0 \quad \text{for all } \xi \in \mathbb{R}^2
$$
This equation is the key to constructing a counter-example. If we can find a non-zero function $f$ such that its Fourier transform $\hat{f}(\xi)$ is non-zero only where $\hat{g}(\xi)$ is zero, then the condition will be satisfied.

### Step 3: Calculating the Fourier Transform of the Indicator Function of a Disk

Our function $g(x)$ is the indicator function of the disk $B(0, r)$. We need to find its Fourier transform $\hat{g}(\xi)$. The 2D Fourier transform is defined as:
$$
\hat{g}(\xi) = \int_{\mathbb{R}^2} g(x) e^{-2\pi i x \cdot \xi} \, dx = \int_{B(0, r)} e^{-2\pi i x \cdot \xi} \, dx
$$
This integral is radially symmetric. Its value depends only on the magnitude $\rho = |\xi|$. We can align the coordinate system such that $\xi = (\rho, 0)$. Then $x \cdot \xi = x_1 \rho$. Using polar coordinates for $x = (s \cos\theta, s \sin\theta)$, we have $x_1 = s \cos\theta$ and $dx = s \, ds \, d\theta$.
$$
\hat{g}(\rho) = \int_0^r \int_0^{2\pi} e^{-2\pi i s \rho \cos\theta} s \, d\theta \, ds
$$
The inner integral is related to the Bessel function of the first kind of order zero, $J_0(z)$, which has the integral representation:
$$
J_0(z) = \frac{1}{2\pi} \int_0^{2\pi} e^{iz \cos\theta} \, d\theta
$$
So, $\int_0^{2\pi} e^{-2\pi i s \rho \cos\theta} \, d\theta = 2\pi J_0(2\pi s \rho)$.
Substituting this back, we get:
$$
\hat{g}(\rho) = 2\pi \int_0^r s J_0(2\pi s \rho) \, ds
$$
Using the identity $\frac{d}{dz}(z J_1(z)) = z J_0(z)$, where $J_1(z)$ is the Bessel function of the first kind of order one, we can evaluate the integral. Let $u = 2\pi s \rho$, then $s = u/(2\pi\rho)$ and $ds = du/(2\pi\rho)$.
\begin{align*}
\hat{g}(\rho) &= 2\pi \int_0^{2\pi r \rho} \frac{u}{2\pi\rho} J_0(u) \frac{du}{2\pi\rho} \\
&= \frac{1}{2\pi\rho^2} \int_0^{2\pi r \rho} u J_0(u) \, du \\
&= \frac{1}{2\pi\rho^2} [u J_1(u)]_0^{2\pi r \rho} \\
&= \frac{1}{2\pi\rho^2} (2\pi r \rho) J_1(2\pi r \rho) \\
&= \frac{r}{\rho} J_1(2\pi r \rho)
\end{align*}
So, the Fourier transform of the indicator function of a disk of radius $r$ is (up to a constant depending on FT conventions):
$$
\hat{g}(\xi) = C \frac{r}{|\xi|} J_1(2\pi r |\xi|)
$$

### Step 4: Finding the Zeros of $\hat{g}(\xi)$

The function $\hat{g}(\xi)$ is zero if and only if $J_1(2\pi r |\xi|) = 0$ (for $|\xi| \neq 0$). The Bessel function $J_1(z)$ is an oscillating function with infinitely many positive zeros. Let these zeros be denoted by $j_{1,k}$ for $k=1, 2, 3, \ldots$. The first zero is $j_{1,1} \approx 3.8317$.

So, $\hat{g}(\xi)$ is zero on a set of circles in the frequency domain, with radii $\rho_k$ satisfying:
$$
2\pi r \rho_k = j_{1,k} \implies \rho_k = \frac{j_{1,k}}{2\pi r}
$$

### Step 5: Constructing a Counter-Example

We can now construct a non-zero continuous function $f$ whose Fourier transform $\hat{f}(\xi)$ is supported only on one of these circles of zeros. Let's pick the first circle, where $|\xi| = \rho_1 = \frac{j_{1,1}}{2\pi r}$.

A function whose Fourier transform is concentrated on a circle of radius $\rho_1$ is the Bessel function $J_0(2\pi \rho_1 |x|)$. The Fourier transform of $J_0(2\pi \rho_1 |x|)$ is a distribution (specifically, a delta function) supported on the circle $|\xi|=\rho_1$.

Let's define our counter-example function $f$ as:
$$
f(x) = J_0(2\pi \rho_1 |x|) = J_0\left(\frac{j_{1,1}}{r}|x|\right)
$$
Let's verify this function:
1.  **Is $f$ continuous?** Yes, $J_0(z)$ is a continuous (in fact, analytic) function for all $z \in \mathbb{C}$. Since $|x|$ is continuous, their composition $f(x)$ is continuous on $\mathbb{R}^2$.
2.  **Is $f$ identically zero?** No. For example, $f(0) = J_0(0) = 1$. The function oscillates and decays like $1/\sqrt{|x|}$ as $|x| \to \infty$, but it is not the zero function.
3.  **Does $f$ satisfy the condition?** The Fourier transform $\hat{f}(\xi)$ is non-zero only for $|\xi| = \rho_1 = \frac{j_{1,1}}{2\pi r}$. But we have shown that for any $\xi$ on this circle, $\hat{g}(\xi) = 0$. Therefore, the product $\hat{f}(\xi)\hat{g}(\xi) = 0$ for all $\xi \in \mathbb{R}^2$.
    By the Convolution Theorem, this implies that the Fourier transform of their convolution is zero: $\widehat{f*g}(\xi) = 0$.
    By the injectivity of the Fourier transform, this means the convolution itself is zero: $(f*g)(x) = 0$ for all $x \in \mathbb{R}^2$.
    As shown in Step 1, this is equivalent to the condition $\int_{B(x_0, r)} f(x) \, dx = 0$ for all $x_0 \in \mathbb{R}^2$.

### Conclusion

We have constructed a function
$$
f(x) = J_0\left(\frac{j_{1,1}}{r}|x|\right)
$$
where $r>0$ is the fixed radius from the problem and $j_{1,1} \approx 3.8317$ is the first positive zero of the Bessel function $J_1$. This function $f$ is continuous on $\mathbb{R}^2$, is not identically zero, yet its integral over any disk of radius $r$ is zero.

Therefore, the statement that $\int_{B(x_0, r)} f(x) \, dx = 0$ for any $x_0 \in \mathbb{R}^2$ implies $f \equiv 0$ is **false**.