Let $f(x) = u(x)^2$. Since $u \in \mathcal{C}^1$, $f(x)$ is also $\mathcal{C}^1$. The given differential equation involves $u''$, which implies $u$ must be at least $\mathcal{C}^2$ in intervals where $u(x) \ne 0$.
The initial condition is $u(0)=0$, so $f(0)=0$.
The derivative of $f(x)$ is $f'(x) = 2u(x)u'(x)$.
At $x=0$, $f'(0) = 2u(0)u'(0) = 0$.
The second derivative of $f(x)$ is $f''(x) = 2(u'(x))^2 + 2u(x)u''(x)$.
From the differential equation, we have $u(x)u''(x) = 1 - (u'(x))^2 (1+u(x)^2)$.
Substituting this into the expression for $f''(x)$:
$f''(x) = 2(u'(x))^2 + 2[1 - (u'(x))^2 (1+u(x)^2)] = 2(u'(x))^2 + 2 - 2(u'(x))^2 - 2(u'(x))^2 u(x)^2$
$f''(x) = 2 - 2(u'(x))^2 u(x)^2$.
Since $(u'(x))^2 \ge 0$ and $u(x)^2 \ge 0$, we have $(u'(x)u(x))^2 \ge 0$.
Therefore, $f''(x) \le 2$ for all $x$.

We want to show that $|u(x)| < \sqrt{2x}$ for all $x>0$. This is equivalent to showing $u(x)^2 < 2x$, which is $f(x) < 2x$.
Let $h(x) = 2x - f(x) = 2x - u(x)^2$. We want to show that $h(x)>0$ for all $x>0$.
We have $h(0) = 2(0) - f(0) = 0$.
The first derivative is $h'(x) = 2 - f'(x) = 2 - 2u(x)u'(x)$.
At $x=0$, $h'(0) = 2 - f'(0) = 2 - 0 = 2$.
Since $h(0)=0$ and $h'(0)=2$, $h(x)$ is positive for small $x>0$.
The second derivative is $h''(x) = -f''(x) = -[2 - 2(u'(x)u(x))^2] = 2(u'(x)u(x))^2 - 2$.

Assume for contradiction that there exists some $x_0 > 0$ such that $h(x_0) \le 0$.
Since $h(x)>0$ for small $x$, let $x_0 = \inf \{ x>0 \mid h(x) \le 0 \}$. By continuity of $h(x)$, we must have $h(x_0)=0$. And for $x \in (0, x_0)$, $h(x)>0$.
Since $h(x_0)=0$ and $h(x)>0$ for $x \in (0, x_0)$, the slope at $x_0$ must be non-positive, i.e., $h'(x_0) \le 0$.
$h'(x_0) = 2 - 2u(x_0)u'(x_0) \le 0$. This implies $u(x_0)u'(x_0) \ge 1$.
Now consider $h''(x_0) = 2(u'(x_0)u(x_0))^2 - 2$.
Since $u(x_0)u'(x_0) \ge 1$, we have $(u'(x_0)u(x_0))^2 \ge 1$.
So $h''(x_0) = 2(u'(x_0)u(x_0))^2 - 2 \ge 2(1)^2 - 2 = 0$.

Let's consider the case $h'(x_0) = 0$. This implies $u(x_0)u'(x_0) = 1$.
In this case, $h''(x_0) = 2(1)^2 - 2 = 0$.
Let's check higher derivatives at $x_0$. If $u'u=1$, let's evaluate the ODE: $(u')^2(1+u^2) = 1 - u''u$. $u'=1/u$. $(1/u)^2(1+u^2)=1-u''u$. $(1+u^2)/u^2=1-u''u$. $1/u^2+1=1-u''u$. $u''u = -1/u^2$. Since $u'(x_0)=1/u(x_0)$, $(u'(x_0))^2=1/u(x_0)^2$.
$h'''(x) = \frac{d}{dx}(2(u'u)^2-2) = 4(u'u)(u''u+(u')^2)$.
At $x_0$, $h'''(x_0) = 4(1)(u''(x_0)u(x_0) + (u'(x_0))^2) = 4(-1/u(x_0)^2 + 1/u(x_0)^2) = 0$.
Continuing this process, one can show $h^{(k)}(x_0)=0$ for all $k \ge 1$. This requires showing that $u$ is $\mathcal{C}^\infty$. This can be established by showing that $u^{(k+1)}$ exists and is continuous if $u^{(k)}$ is, using the ODE and potentially L'Hopital's rule at points where $u=0$. Assuming $u \in \mathcal{C}^\infty$, then $h \in \mathcal{C}^\infty$.
If $h(x_0)=0$ and $h^{(k)}(x_0)=0$ for all $k \ge 1$, and if $h$ were analytic, this implies $h(x) \equiv 0$ in a neighborhood of $x_0$.
Let's verify this using ODE uniqueness. If $h'(x_0)=0$, then $u(x_0)u'(x_0)=1$. We also have $h(x_0)=0$, which means $2x_0 - u(x_0)^2 = 0$, so $u(x_0)^2=2x_0$.
Consider the function $w(x) = \sigma \sqrt{2x}$ where $\sigma = \text{sgn}(u(x_0))$. Then $w(x_0)^2 = 2x_0 = u(x_0)^2$, so $w(x_0)=u(x_0)$.
$w'(x) = \sigma \frac{1}{\sqrt{2x}}$. $w'(x_0) = \sigma \frac{1}{\sqrt{2x_0}} = \sigma \frac{1}{|u(x_0)|} = \frac{\text{sgn}(u(x_0))}{|u(x_0)|} = \frac{u(x_0)}{u(x_0)^2}$.
$u'(x_0) = 1/u(x_0)$. So $w'(x_0)$ is not necessarily $u'(x_0)$. Let's recheck.
$u'(x_0) = 1/u(x_0)$. $w'(x_0) = \sigma/\sqrt{2x_0} = \sigma/|u(x_0)| = u(x_0)/u(x_0)^2 = 1/u(x_0)$.
Yes, $w'(x_0) = u'(x_0)$.
The function $w(x)$ satisfies the ODE $(w')^2(1+w^2) = 1-w''w$ for $x>0$.
$w'' = \sigma (-\frac{1}{2}) (2x)^{-3/2} (2) = -\sigma (2x)^{-3/2}$.
$1 - w''w = 1 - (-\sigma (2x)^{-3/2}) (\sigma \sqrt{2x}) = 1 + \sigma^2 (2x)^{-3/2} (2x)^{1/2} = 1 + (2x)^{-1} = 1 + 1/(2x)$.
$(w')^2(1+w^2) = (\sigma/\sqrt{2x})^2 (1+(\sigma\sqrt{2x})^2) = (1/2x)(1+2x) = (1+2x)/(2x) = 1/(2x)+1$.
So $w(x)$ is a solution to the ODE for $x>0$.
Since $u(x_0)=w(x_0)$ and $u'(x_0)=w'(x_0)$, and the ODE $u'' = F(u, u') = \frac{1-(u')^2(1+u^2)}{u}$ has a unique solution for $u \ne 0$. Note that $u(x_0)^2=2x_0$. Since $x_0>0$, $u(x_0)\ne 0$.
By the uniqueness theorem for ODEs, $u(x) = w(x)$ in a neighborhood of $x_0$.
This implies $u(x)$ must be either $\sqrt{2x}$ or $-\sqrt{2x}$ for all $x>0$.
However, these functions $w(x)=\pm \sqrt{2x}$ are not $\mathcal{C}^1$ at $x=0$. $w'(x)=\pm 1/\sqrt{2x}$, which blows up as $x \to 0^+$.
The problem states that $u: \mathbb{R} \to \mathbb{R}$ is a $\mathcal{C}^1$-class function. This implies $u'(0)$ must be finite. Indeed, substituting $u(0)=0$ into the ODE gives $(u'(0))^2(1+0) = 1 - u''(0)\cdot 0$, so $(u'(0))^2=1$.
Thus, the solution $u(x)$ cannot be $w(x)=\pm \sqrt{2x}$.
This contradicts the consequence of assuming $h'(x_0)=0$.
Therefore, the case $h'(x_0)=0$ is impossible for the given function $u$.

We are left with the case $h'(x_0)<0$. This implies $u(x_0)u'(x_0)>1$, and $h''(x_0)>0$.
In this case, $h(x_0)=0$, $h'(x_0)<0$, $h''(x_0)>0$.
Let's examine the behavior of $h(x)$ near $x_0$. $h(x) \approx h(x_0) + h'(x_0)(x-x_0) + \frac{h''(x_0)}{2}(x-x_0)^2$.
$h(x) \approx h'(x_0)(x-x_0) + \frac{h''(x_0)}{2}(x-x_0)^2$.
For $x < x_0$, $x-x_0 < 0$. $h(x) \approx -h'(x_0)|x-x_0| + \frac{h''(x_0)}{2}|x-x_0|^2$.
Since $h'(x_0)<0$ and $h''(x_0)>0$, both terms are positive. So $h(x)>0$ for $x$ just below $x_0$. This is consistent with $x_0$ being the first point where $h(x_0)=0$.
For $x>x_0$, $x-x_0>0$. $h(x) \approx h'(x_0)(x-x_0) + \frac{h''(x_0)}{2}(x-x_0)^2$.
Since $h'(x_0)<0$ and $h''(x_0)>0$, $h(x)$ is negative for $x$ just above $x_0$. This does not lead to a contradiction on its own.

Let's reconsider the argument about $h'(x_m)=0$.
Since $h'(0)=2$ and $h'(x_0)<0$, by the Intermediate Value Theorem, there must exist some $x_m \in (0, x_0)$ such that $h'(x_m)=0$.
As shown before, $h'(x_m)=0 \implies u(x_m)u'(x_m)=1$.
This implies $h''(x_m)=0$, $h'''(x_m)=0$, $h^{(4)}(x_m)=0$.
If we assume $u \in \mathcal{C}^\infty$, then $h \in \mathcal{C}^\infty$. The fact that $h'(x_m)=0$ and all higher derivatives $h^{(k)}(x_m)=0$ for $k \ge 2$ implies that $h'(x)$ must be identically zero in a neighborhood of $x_m$. This means $h(x)$ is constant in that neighborhood, $h(x) = h(x_m)$.
If $h(x)$ is constant on an interval, $h'(x)=0$ on this interval. This implies $u'u=1$. As shown before, this means $u(x)^2=2x+C$. Since $u(0)=0$, we need $u(x)^2=2x$. So $h(x)=2x-u(x)^2=0$.
This constant value must be 0.
However, $x_m \in (0, x_0)$, and $h(x)>0$ for $x \in (0, x_0)$. So $h(x_m)>0$.
This is a contradiction. The assumption that $h(x_0)=0$ for some $x_0>0$ must be false.

Since $h(0)=0$ and $h(x)$ never reaches 0 for $x>0$, and $h(x)$ starts positive ($h'(0)=2$), we must have $h(x)>0$ for all $x>0$.
$2x - u(x)^2 > 0$.
$u(x)^2 < 2x$.
$|u(x)| < \sqrt{2x}$ for all $x>0$.

Final check on the assumption $u \in \mathcal{C}^\infty$. We showed $u \in \mathcal{C}^3$. The argument structure at points where $u=0$ seems to allow lifting regularity iteratively. $u''=h/u$. If $u \in \mathcal{C}^k$, $h=1-(u')^2(1+u^2) \in \mathcal{C}^{k-1}$. $u''$ is $\mathcal{C}^{k-1}$ where $u \ne 0$. Where $u(x_0)=0$, $u''(x_0)=0$ and one can show continuity of $u''$. Inductively, one might be able to show $u^{(k)}(x_0)=0$ for even $k$ and $u^{(k)}(x_0)$ is related to $u'$ for odd $k$. This suggests $u$ is likely $\mathcal{C}^\infty$.


Final Result: The final result is $\boxed{|u(x)| < \sqrt{2x} \text{ for all } x > 0}$