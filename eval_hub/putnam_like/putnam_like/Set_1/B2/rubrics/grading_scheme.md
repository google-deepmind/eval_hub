This step is worth 1 point.
Consider the equation
$$
(u')^2 (1+u^2) = 1 - u'' u
$$
and rewrite it in the following way
$$
u'' u + (u')^2 = 1 - (u u')^2
$$
$$
(uu')' = 1 - (u u')^2
$$

This step is worth 8 points.
Hence $w := uu'$ satisfies the equation
$$
\begin{cases}
w' = h(w) := 1-w^2, \\
w(0) = 0.
\end{cases}
$$
Since $h(-1) = 0$ and $h(1) = 0$, from the uniqueness of solutions to ODEs, we obtain that $-1 < w(x) < 1$ for all $x \in \mathbb{R}$. Indeed, suppose there exists a point $x_0\in \mathbb{R}$ such that $w(x_0) = 1$ or $w(x_0) = -1$. Without loss of generality, assume $w(x_0) = 1$. Then, starting from the point $x_0$, we would have two trajectories: the trajectory $w(x)$ and another constant trajectory $w_2(x) \equiv 1$. This contradicts the uniqueness of solutions. Thus, 
$$-1 < u(x) u'(x) < 1$$ 
and hence
$$
-1 < \left( \frac{1}{2} u^2 \right)' < 1
$$
or equivalently
$$
-2 < (u^2)' < 2
$$

This step is worth 1 point.
Fix any $x > 0$ and integrate the above inequality on the interval $[0,x]$. Using that $u(0) = 0$ we get
$$
-2x < \int_0^x (u^2)' (t) \, dt < 2x
$$
or equivalently
$$
-2x < u^2(x) < 2x
$$
which implies $|u(x)| < \sqrt{2x}$.