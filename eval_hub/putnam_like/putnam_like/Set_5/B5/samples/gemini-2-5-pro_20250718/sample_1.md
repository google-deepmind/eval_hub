Of course. Here is a detailed, step-by-step solution to the problem.

### **Method**

To find the number of zeros of the polynomial $P(z)$ in the specified sector $A$, we will use the **Argument Principle**. The Argument Principle states that for a function $f(z)$ that is analytic inside and on a simple closed contour $\Gamma$, the number of zeros $N$ of $f(z)$ inside $\Gamma$ (counted with multiplicity) is given by:
$$ N = \frac{1}{2\pi} \Delta_\Gamma \arg(f(z)) $$
where $\Delta_\Gamma \arg(f(z))$ is the total change in the argument of $f(z)$ as $z$ traverses the contour $\Gamma$ once in the counter-clockwise direction.

### **Step 1: Define the Contour**

The region $A = \{z\in\mathcal{C}\,:\, \frac \pi 2 \leq \arg z\leq \pi\}$ is an infinite sector in the second quadrant. We can't directly apply the Argument Principle to an infinite region. Instead, we define a closed contour $\Gamma_R$ that encloses a finite portion of this region and then take the limit as the contour expands to cover the entire region.

Let's define the contour $\Gamma_R$ for a large positive real number $R$. The contour consists of three parts, traversed counter-clockwise:

1.  **$C_1$**: The line segment along the positive imaginary axis from $z=0$ to $z=iR$.
2.  **$C_2$**: The circular arc of radius $R$ from $z=iR$ to $z=-R$, described by $z = Re^{i\theta}$ for $\theta$ from $\frac{\pi}{2}$ to $\pi$.
3.  **$C_3$**: The line segment along the negative real axis from $z=-R$ to $z=0$.

The contour $\Gamma_R = C_1 \cup C_2 \cup C_3$ is a closed semi-annular sector. As we let $R \to \infty$, this contour will enclose the entire region $A$. The number of zeros in $A$, let's call it $N_A$, will be:
$$ N_A = \frac{1}{2\pi} \lim_{R\to\infty} \Delta_{\Gamma_R} \arg(P(z)) $$
First, we should check if there are any zeros on the boundaries of the region $A$.
- For $z$ on the positive imaginary axis, let $z = iy$ with $y > 0$.
  $P(iy) = (iy)^8 - 5(iy)^3 + 10 = y^8 - 5(-iy^3) + 10 = (y^8+10) + i(5y^3)$.
  For $P(iy)=0$, both the real and imaginary parts must be zero. $5y^3=0$ implies $y=0$. But for $y=0$, $P(0)=10 \neq 0$. For $y>0$, the real part $y^8+10$ is always positive. Thus, there are no zeros on the positive imaginary axis.
- For $z$ on the negative real axis, let $z = x$ with $x < 0$. Let $x = -t$ for $t > 0$.
  $P(-t) = (-t)^8 - 5(-t)^3 + 10 = t^8 + 5t^3 + 10$.
  For $t>0$, every term is positive, so $P(-t) > 10$. Thus, there are no zeros on the negative real axis.

Since there are no zeros on the boundary of $A$, we can proceed with the contour integration.

### **Step 2: Analyze the Change in Argument along each part of the Contour**

We will calculate the change in argument of $P(z)$ along $C_1$, $C_2$, and $C_3$.

**Part 1: Change in argument along $C_1$**

On $C_1$, $z = iy$ where $y$ goes from $0$ to $R$.
$$ P(iy) = (y^8+10) + i(5y^3) $$
Let's analyze the argument of $P(iy)$: $\phi_1(y) = \arg(P(iy)) = \arctan\left(\frac{5y^3}{y^8+10}\right)$.

- At the start point, $y=0$:
  $P(0) = 10$. This is on the positive real axis, so $\arg(P(0)) = 0$.
- At the end point, $y=R$ (for large $R$):
  $P(iR) = (R^8+10) + i(5R^3)$.
  As $R \to \infty$, the real part $R^8+10$ grows much faster than the imaginary part $5R^3$.
  $$ \lim_{R\to\infty} \arg(P(iR)) = \lim_{R\to\infty} \arctan\left(\frac{5R^3}{R^8+10}\right) = \arctan(0) = 0 $$
As $y$ increases from $0$ to $R$, both the real part $(y^8+10)$ and the imaginary part $(5y^3)$ are positive. This means the image of $C_1$ under $P(z)$, which we can call $P(C_1)$, lies entirely in the first quadrant. The path of $P(iy)$ starts at $10$, moves into the first quadrant, and then curves back towards the positive real axis for large $y$.
The net change in argument along $C_1$ as $R \to \infty$ is:
$$ \Delta_{C_1} \arg(P(z)) = \lim_{R\to\infty} \arg(P(iR)) - \arg(P(0)) = 0 - 0 = 0 $$

**Part 2: Change in argument along $C_2$**

On $C_2$, $z = Re^{i\theta}$ where $\theta$ goes from $\frac{\pi}{2}$ to $\pi$. We are interested in the limit as $R \to \infty$.
For very large $|z|=R$, the term $z^8$ dominates the polynomial $P(z)$. We can write:
$$ P(z) = z^8 - 5z^3 + 10 = z^8 \left(1 - \frac{5}{z^5} + \frac{10}{z^8}\right) $$
Let $w = 1 - \frac{5}{z^5} + \frac{10}{z^8}$. On $C_2$, $|z|=R$, so:
$$ |w - 1| = \left|-\frac{5}{z^5} + \frac{10}{z^8}\right| \leq \frac{5}{|z|^5} + \frac{10}{|z|^8} = \frac{5}{R^5} + \frac{10}{R^8} $$
As $R \to \infty$, $|w-1| \to 0$. This means for a sufficiently large $R$, the value of $w$ remains in a small disk around $1$ and never encircles the origin. Therefore, the change in argument of $w$ along $C_2$ approaches 0 as $R \to \infty$.
$$ \lim_{R\to\infty} \Delta_{C_2} \arg(w) = 0 $$
So, the change in argument of $P(z)$ is dominated by the change in argument of $z^8$:
$$ \Delta_{C_2} \arg(P(z)) = \Delta_{C_2} \arg(z^8) + \Delta_{C_2} \arg(w) \approx \Delta_{C_2} \arg(z^8) $$
The argument of $z^8$ is $\arg((Re^{i\theta})^8) = \arg(R^8 e^{i8\theta}) = 8\theta$.
As $z$ traverses $C_2$, $\theta$ changes from $\frac{\pi}{2}$ to $\pi$.
The change in the argument of $z^8$ is:
$$ \Delta_{C_2} \arg(z^8) = 8(\pi) - 8\left(\frac{\pi}{2}\right) = 8\pi - 4\pi = 4\pi $$
Thus, in the limit as $R \to \infty$:
$$ \Delta_{C_2} \arg(P(z)) = 4\pi $$

**Part 3: Change in argument along $C_3$**

On $C_3$, $z$ is on the negative real axis, going from $-R$ to $0$. Let $z=x$ where $x$ goes from $-R$ to $0$. Let's set $x = -t$, so $t$ goes from $R$ down to $0$.
$$ P(z) = P(-t) = (-t)^8 - 5(-t)^3 + 10 = t^8 + 5t^3 + 10 $$
For any $t \ge 0$, $P(-t)$ is a real and strictly positive number.
- At the start point of $C_3$, $z=-R$ (i.e., $t=R$):
  $P(-R) = R^8 + 5R^3 + 10$. For large $R$, this is a very large positive real number. Its argument is $0$.
- At the end point of $C_3$, $z=0$ (i.e., $t=0$):
  $P(0) = 10$. This is also a positive real number. Its argument is $0$.
Since $P(z)$ on $C_3$ is always real and positive, its argument is constantly $0$. The path $P(C_3)$ lies entirely on the positive real axis, moving from $R^8+5R^3+10$ to $10$.
Therefore, the change in argument along $C_3$ is:
$$ \Delta_{C_3} \arg(P(z)) = 0 - 0 = 0 $$

### **Step 3: Calculate the Total Change in Argument and the Number of Zeros**

Now, we sum the changes in argument from all three parts of the contour $\Gamma_R$ in the limit as $R \to \infty$.
$$ \lim_{R\to\infty} \Delta_{\Gamma_R} \arg(P(z)) = \Delta_{C_1} \arg(P(z)) + \Delta_{C_2} \arg(P(z)) + \Delta_{C_3} \arg(P(z)) $$
$$ \lim_{R\to\infty} \Delta_{\Gamma_R} \arg(P(z)) = 0 + 4\pi + 0 = 4\pi $$
Finally, we apply the Argument Principle to find the number of zeros $N_A$ in the sector $A$:
$$ N_A = \frac{1}{2\pi} \lim_{R\to\infty} \Delta_{\Gamma_R} \arg(P(z)) = \frac{1}{2\pi} (4\pi) = 2 $$

### **Conclusion**

The polynomial $P(z)=z^8-5z^3+10$ has **2** zeros in the set $A=\{z\in\mathcal{C}\,:\, \frac \pi 2 \leq \arg z\leq \pi\}$.

---
**Summary of the argument changes:**
- **On $C_1$ (positive imaginary axis):** $P(z)$ starts at $10$ (argument 0), moves into the first quadrant, and returns to the positive real axis direction as $|z| \to \infty$. The net change in argument is 0.
- **On $C_2$ (large circular arc):** $P(z)$ behaves like $z^8$. As the argument of $z$ changes by $\pi - \pi/2 = \pi/2$, the argument of $z^8$ changes by $8 \times (\pi/2) = 4\pi$.
- **On $C_3$ (negative real axis):** $P(z)$ is always real and positive. The path of $P(z)$ stays on the positive real axis, so the change in argument is 0.

Total change in argument: $0 + 4\pi + 0 = 4\pi$.
Number of zeros: $\frac{4\pi}{2\pi} = 2$.