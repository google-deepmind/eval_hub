This step is worth 2 points.
Recalling that $\Gamma(\ell+1) = \ell!$ for $\ell \in \mathbb{N}$, we can rewrite the desired inequality as
$$
\begin{aligned}
&\quad x \cdot \Gamma(2n+1) + y \cdot \Gamma(2m + 1) + z \cdot \Gamma(2k + 1) \\
&\geq (x-y+z) \cdot \Gamma(n+k+1) + (-x+y+z) \cdot \Gamma(m+k+1) + (x+y-z) \cdot \Gamma(n+m+1).
\end{aligned}
$$

This step is worth 6 points.
Move all the summands to the left hand side and observe that
$$
\begin{aligned}
&\quad x \Gamma(2n+1) + y \Gamma(2m+1) + z \Gamma(2k+1) \\
&\quad + (-x+y-z) \Gamma(n+k+1) + (x-y-z) \Gamma(k+m+1) + (-x-y+z) \Gamma(n+m+1) \\
&= \int_0^\infty e^{-t} \left( xt^{2n} + y t^{2m} + z t^{2k} +   \right) \, dt \\
&\quad+ \int_0^\infty e^{-t} \left(t^{n+k} (-x+y-z)  + t^{m+k} (x-y-z) + t^{n+m} (-x-y+z) \right) \, dt \\
&= \int_0^\infty e^{-t} \left( x (t^n-t^m)(t^n-t^k) + y (t^m-t^n)(t^m-t^k) + z(t^k-t^n)(t^k-t^m) \right) \, dt.
\end{aligned}
$$
Hence, it is enough to show that
$$
x (t^n-t^m)(t^n-t^k) + y (t^m-t^n)(t^m-t^k) + z(t^k-t^n)(t^k-t^m) \geq 0
$$
for $t > 0$.

This step is worth 2 points.
Indeed, assuming without a loss of generality that $t^n \leq t^m \leq t^k$, using the inequalities $1 \leq x,y,z \leq 4$, we get
$$
x (t^n-t^m)(t^n-t^k) + y (t^m-t^n)(t^m-t^k) + z(t^k-t^n)(t^k-t^m)
$$
$$
= x (t^m - t^n) ( (t^m-t^n) + (t^k-t^m) ) - y (t^m-t^n)(t^k-t^m) + z( (t^m-t^n) + (t^k-t^m) ) (t^k-t^m)
$$
$$
\geq (t^m - t^n) ( (t^m-t^n) + (t^k-t^m) ) - 4 (t^m-t^n)(t^k-t^m) + ( (t^m-t^n) + (t^k-t^m) ) (t^k-t^m)
$$
$$
= (t^m - t^n)^2  - 2 (t^m-t^n)(t^k-t^m) +  (t^k-t^m)^2
$$
$$
= ( (t^m-t^n) - (t^k-t^m) )^2 \geq 0.
$$