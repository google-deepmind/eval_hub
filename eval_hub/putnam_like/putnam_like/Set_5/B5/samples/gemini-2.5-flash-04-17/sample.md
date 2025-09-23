Let $P(z) = z^8 - 5z^3 + 10$. We want to find the number of zeros of $P(z)$ in the set $A = \{z \in \mathbb{C} : \frac{\pi}{2} \leq \arg z \leq \pi\}$. This set is a sector in the complex plane. We can use the Argument Principle by integrating around a contour that encloses the sector. Let's consider the region $A_R = \{z \in \mathbb{C} : \frac{\pi}{2} \leq \arg z \leq \pi, |z| \leq R\}$ for a sufficiently large $R$. The number of zeros in $A$ is the limit of the number of zeros in $A_R$ as $R \to \infty$.

The boundary of $A_R$, traversed in the positive (counterclockwise) direction, consists of three parts:
1. The line segment $L_1$ along the positive imaginary axis from $z=iR$ to $z=i\epsilon$ for a small $\epsilon > 0$.
2. The circular arc $C_\epsilon$ of radius $\epsilon$ from $z=i\epsilon$ to $z=-\epsilon$.
3. The line segment $L_2$ along the negative real axis from $z=-\epsilon$ to $z=-R$.
4. The circular arc $C_R$ of radius $R$ from $z=-R$ to $z=iR$.

Wait, the region is $A_R = \{z : \pi/2 \leq \arg z \leq \pi, |z| \leq R\}$. The boundary should be oriented counterclockwise.
The boundary consists of:
1. $L_1$: segment on the positive imaginary axis from $z=i\epsilon$ to $z=iR$. ($z=iy$, $y \in [\epsilon, R]$)
2. $C_R$: circular arc $|z|=R$ from $z=iR$ to $z=-R$. ($z=Re^{i\theta}$, $\theta \in [\pi/2, \pi]$)
3. $L_2$: segment on the negative real axis from $z=-R$ to $z=-\epsilon$. ($z=x$, $x \in [-R, -\epsilon]$)
4. $C_\epsilon$: circular arc $|z|=\epsilon$ from $z=-\epsilon$ to $z=i\epsilon$. ($z=\epsilon e^{i\theta}$, $\theta \in [\pi, \pi/2]$)

The number of zeros inside this contour is given by $N_{R,\epsilon} = \frac{1}{2\pi} \Delta_{\partial A_R} \arg P(z)$, where $\Delta_{\partial A_R} \arg P(z)$ is the total change in the argument of $P(z)$ as $z$ traverses the boundary of $A_R$ once counterclockwise.

Let's analyze the change in argument along each part of the contour as $R \to \infty$ and $\epsilon \to 0$.

1. Along $L_1$: $z = iy$ for $y \in [\epsilon, R]$.
$P(iy) = (iy)^8 - 5(iy)^3 + 10 = i^8 y^8 - 5i^3 y^3 + 10 = y^8 + 5iy^3 + 10 = (y^8+10) + i(5y^3)$.
The real part is $u(y) = y^8+10$ and the imaginary part is $v(y) = 5y^3$. For $y > 0$, both $u(y)$ and $v(y)$ are positive. So $P(iy)$ lies in the first quadrant for $y > 0$.
The argument is $\arg P(iy) = \arctan\left(\frac{5y^3}{y^8+10}\right)$.
As $y \to \infty$, $\frac{5y^3}{y^8+10} \sim \frac{5}{y^5} \to 0$. So $\arg P(iR) \to \arctan(0) = 0$.
As $y \to 0^+$, $\frac{5y^3}{\epsilon^8+10} \to 0$. So $\arg P(i\epsilon) \to \arctan(0) = 0$.
The change in argument along $L_1$ as $y$ goes from $\epsilon$ to $R$ is $\arg P(iR) - \arg P(i\epsilon)$. In the limit $R \to \infty, \epsilon \to 0$, this change is $0 - 0 = 0$.
$\lim_{R \to \infty, \epsilon \to 0} \Delta_{L_1} \arg P(z) = 0$.

2. Along $C_R$: $z = Re^{i\theta}$ for $\theta \in [\pi/2, \pi]$.
For large $|z|=R$, $P(z) = z^8 - 5z^3 + 10$ is dominated by the $z^8$ term. By Rouché's theorem, for sufficiently large $R$, $P(z)$ has the same number of zeros as $z^8$ inside $|z|=R$, which is 8.
Also, for large $R$, $|z^8| = R^8$ and $|-5z^3+10| \leq 5R^3+10$. For $R^8 > 5R^3+10$ (e.g., $R=2$), $|z^8| > |-5z^3+10|$.
On the arc $C_R$, $P(z) \approx z^8$. The argument of $P(z)$ is approximately the argument of $z^8$.
$\arg P(z) \approx \arg(z^8) = 8\arg(z) = 8\theta$.
As $\theta$ goes from $\pi/2$ to $\pi$, $8\theta$ goes from $8(\pi/2) = 4\pi$ to $8\pi$.
The change in argument of $P(z)$ along $C_R$ is approximately $8\pi - 4\pi = 4\pi$.
More precisely, since $|z^8| > |-5z^3+10|$ on $C_R$, the change in argument of $P(z)=z^8+(-5z^3+10)$ is equal to the change in argument of $z^8$ along $C_R$.
$\lim_{R \to \infty} \Delta_{C_R} \arg P(z) = 4\pi$.

3. Along $L_2$: $z = x$ for $x \in [-R, -\epsilon]$. This is the negative real axis.
$P(x) = x^8 - 5x^3 + 10$. For $x < 0$, $x^8 > 0$, $x^3 < 0$ so $-5x^3 > 0$. Thus, $P(x) = (\text{positive}) + (\text{positive}) + 10 > 0$ for $x < 0$.
$P(x)$ is real and positive for $x \in [-R, -\epsilon]$. The argument is always 0.
The change in argument along $L_2$ is $\arg P(-\epsilon) - \arg P(-R)$. Since $P(x) > 0$ for $x < 0$, both arguments are 0.
$\lim_{R \to \infty, \epsilon \to 0} \Delta_{L_2} \arg P(z) = 0 - 0 = 0$.

4. Along $C_\epsilon$: $z = \epsilon e^{i\theta}$ for $\theta \in [\pi, \pi/2]$.
As $\epsilon \to 0$, $P(z) = z^8 - 5z^3 + 10 \to P(0) = 10$.
The path $P(z)$ for $z \in C_\epsilon$ is a small curve close to $P(0)=10$.
The starting point is $z=-\epsilon$. $P(-\epsilon) = \epsilon^8 + 5\epsilon^3 + 10 \approx 10$.
The ending point is $z=i\epsilon$. $P(i\epsilon) = \epsilon^8 + 10 + i5\epsilon^3 \approx 10$.
Since $P(0)=10 \neq 0$, for small enough $\epsilon$, $P(z)$ is non-zero on $C_\epsilon$ and the curve $P(C_\epsilon)$ does not enclose the origin.
The change in argument $\Delta_{C_\epsilon} \arg P(z)$ tends to 0 as $\epsilon \to 0$.
$\lim_{\epsilon \to 0} \Delta_{C_\epsilon} \arg P(z) = 0$.

The total change in argument around the contour is the sum of changes along the four parts:
$\Delta_{\partial A_R} \arg P(z) = \Delta_{L_1} + \Delta_{C_R} + \Delta_{L_2} + \Delta_{C_\epsilon}$.
In the limit $R \to \infty, \epsilon \to 0$:
$\Delta \arg P(z) = 0 + 4\pi + 0 + 0 = 4\pi$.

The number of zeros in the limiting region $\{z : \pi/2 < \arg z < \pi, |z| > 0\}$ is $N = \frac{1}{2\pi} (4\pi) = 2$.

We need to check if there are any zeros on the boundary of the sector $A = \{z : \pi/2 \leq \arg z \leq \pi\}$. The boundary consists of the positive imaginary axis $\{iy : y \geq 0\}$ and the negative real axis $\{x : x \leq 0\}$.
- On the negative real axis ($z=x \leq 0$): $P(x) = x^8 - 5x^3 + 10$. As shown above, for $x \leq 0$, $P(x) > 0$. So there are no zeros on the negative real axis.
- On the positive imaginary axis ($z=iy$, $y \geq 0$): $P(iy) = (y^8+10) + i(5y^3)$. For $P(iy)=0$, both the real and imaginary parts must be zero. $y^8+10 = 0$ has no real solution for $y$. $5y^3=0$ implies $y=0$. If $y=0$, $z=0$, and $P(0)=10 \neq 0$. So there are no zeros on the positive imaginary axis.

Since there are no zeros on the boundary of the sector $A$, the number of zeros in the closed sector $A$ is equal to the number of zeros in the open sector $\{z : \pi/2 < \arg z < \pi\}$.
Our calculation using the Argument Principle on the contour excluding the origin (by $C_\epsilon$) gives the number of zeros in the open sector $\{z : \pi/2 < \arg z < \pi\}$.
Since $P(0) \neq 0$, there are no zeros at the origin.

Thus, the number of zeros of $P(z)$ in the set $A = \{z \in \mathbb{C} : \frac{\pi}{2} \leq \arg z \leq \pi\}$ is 2.

The final answer is $\boxed{2}$.