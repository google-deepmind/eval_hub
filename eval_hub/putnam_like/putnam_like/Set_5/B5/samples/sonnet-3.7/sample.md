# Solution

I need to find the number of zeros of $P(z)=z^8-5z^3+10$ in the set $A=\{z\in\mathcal{C}\,:\, \frac{\pi}{2} \leq \arg z\leq \pi\}$.

I'll use the argument principle to solve this problem. According to this principle, the number of zeros inside a simple closed contour equals $\frac{1}{2\pi}$ times the change in argument of the function as we traverse the contour counterclockwise.

Let's construct a contour that encloses the region $A_R = A \cap \{z : |z| \leq R\}$ for some large $R$:
1. The positive imaginary axis from $0$ to $iR$
2. An arc of the circle $|z| = R$ from $\arg z = \frac{\pi}{2}$ to $\arg z = \pi$
3. The negative real axis from $-R$ to $0$

First, I need to verify that $P(z)$ has no zeros on this contour:

- On the positive imaginary axis ($z = iy$, $y > 0$):
  $P(iy) = (iy)^8 - 5(iy)^3 + 10 = y^8 + 5iy^3 + 10$
  For this to equal zero, both real and imaginary parts must be zero:
  $y^8 + 10 = 0$ and $5y^3 = 0$
  Since $y^8 + 10 > 0$ for all $y > 0$, there are no zeros on this segment.

- On the negative real axis ($z = -x$, $x > 0$):
  $P(-x) = (-x)^8 - 5(-x)^3 + 10 = x^8 + 5x^3 + 10 > 0$ for all $x > 0$
  So there are no zeros on this segment either.

- On the large arc, for sufficiently large $R$, the term $z^8$ dominates, so there are no zeros.

Now I'll compute the change in argument of $P(z)$ around this contour:

1. On the positive imaginary axis:
   For $z = iy$ with $y$ from $0$ to $R$, the argument of $P(iy) = y^8 + 5iy^3 + 10$ starts at $0$ (when $y = 0$), increases to a maximum, then decreases back to approximately $0$ (for large $y$). The net change in argument is approximately $0$.

2. On the large circular arc:
   For $z = Re^{i\theta}$ with $\theta$ from $\frac{\pi}{2}$ to $\pi$, and large $R$:
   $P(z) \approx z^8 = R^8e^{8i\theta}$
   As $\theta$ increases from $\frac{\pi}{2}$ to $\pi$, the argument of $P(z)$ increases by $8(\pi - \frac{\pi}{2}) = 4\pi$.

3. On the negative real axis:
   For $z = -x$ with $x$ from $R$ to $0$, the value $P(-x) = x^8 + 5x^3 + 10$ remains positive real, so the argument stays at $0$. The change in argument is $0$.

The total change in argument around the contour is $0 + 4\pi + 0 = 4\pi$.

By the argument principle, the number of zeros inside the contour is:
$$Z = \frac{1}{2\pi} \cdot 4\pi = 2$$

Therefore, the polynomial $P(z)=z^8-5z^3+10$ has exactly 2 zeros in the set $A$.