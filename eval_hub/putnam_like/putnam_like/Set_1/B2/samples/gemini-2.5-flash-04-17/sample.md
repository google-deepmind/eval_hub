Let the given differential equation be $(u')^2 (1+u^2) = 1 - u'' u$. We are given that $u \in \mathcal{C}^1(\mathbb{R})$ and $u(0)=0$. We want to show $|u(x)| < \sqrt{2x}$ for all $x > 0$.

The differential equation can be rearranged as $u'' u + (u')^2 (1+u^2) - 1 = 0$, or $u'' u + (u')^2 + (u')^2 u^2 = 1$.
Note that $u'' u + (u')^2 = \frac{d}{dx}(u u')$. So the equation is $\frac{d}{dx}(u u') + (u')^2 u^2 = 1$.

Let's evaluate the equation at $x=0$. Since $u \in \mathcal{C}^1(\mathbb{R})$, $u'(0)$ is finite.
Substituting $u(0)=0$ into the equation, we get $(u'(0))^2 (1+0^2) = 1 - u''(0) \cdot 0$.
$(u'(0))^2 = 1$, which implies $u'(0) = 1$ or $u'(0) = -1$.

Let's define the function $H(x) = u(x)^2 - 2x$ for $x \in \mathbb{R}$. We want to show $H(x) < 0$ for all $x > 0$.
First, evaluate $H(0)$: $H(0) = u(0)^2 - 2(0) = 0^2 - 0 = 0$.
Next, evaluate the derivative of $H(x)$: $H'(x) = \frac{d}{dx}(u(x)^2) - \frac{d}{dx}(2x) = 2u(x)u'(x) - 2$.
Evaluate $H'(0)$: $H'(0) = 2u(0)u'(0) - 2$. Since $u(0)=0$, $H'(0) = 2(0)u'(0) - 2 = -2$.

Since $H(0)=0$ and $H'(0)=-2$, for small $x>0$, $H(x) \approx H(0) + H'(0)x = 0 - 2x = -2x$.
This implies that $H(x) < 0$ for all small $x>0$.
Thus, $u(x)^2 - 2x < 0$, or $u(x)^2 < 2x$, for small $x>0$. This is consistent with the statement we want to prove.

Suppose, for the sake of contradiction, that there exists $x_1 > 0$ such that $H(x_1) \ge 0$.
Since $H(0)=0$ and $H(x)<0$ for small $x>0$, there must be a smallest value $x_0 > 0$ such that $H(x_0) = 0$.
So $H(x_0)=0$ and $H(x) < 0$ for all $x \in (0, x_0)$.
At $x_0$, we have $u(x_0)^2 - 2x_0 = 0$, so $u(x_0)^2 = 2x_0$. Since $x_0>0$, $u(x_0)^2>0$, so $u(x_0) \ne 0$.
The condition $H(x_0)=0$ and $H(x)<0$ for $x \in (0, x_0)$ implies that $H$ is non-decreasing at $x_0$ for $x \le x_0$.
Thus, $H'(x_0) = \lim_{h \to 0^-} \frac{H(x_0)-H(x_0+h)}{-h} \ge 0$. (Since $x_0+h < x_0$ for $h<0$).
So $H'(x_0) = 2u(x_0)u'(x_0) - 2 \ge 0$, which implies $u(x_0)u'(x_0) \ge 1$.

Let's compute the second derivative of $H(x)$:
$H''(x) = \frac{d}{dx}(2uu'-2) = 2(u'u' + uu'') = 2(u')^2 + 2uu''$.
From the ODE, $uu'' = 1 - (u')^2(1+u^2)$.
Substitute this into the expression for $H''(x)$:
$H''(x) = 2(u')^2 + 2(1 - (u')^2(1+u^2)) = 2(u')^2 + 2 - 2(u')^2 - 2(u')^2 u^2 = 2 - 2(u')^2 u^2$.
$H''(x) = 2 - 2(u u')^2$.

At $x_0$, $H'(x_0) \ge 0$, so $u(x_0)u'(x_0) \ge 1$.
$H''(x_0) = 2 - 2(u(x_0)u'(x_0))^2$.
If $u(x_0)u'(x_0) > 1$, then $(u(x_0)u'(x_0))^2 > 1$, so $H''(x_0) = 2 - 2(>1) < 0$.
If $H(x_0)=0$, $H'(x_0)>0$, and $H''(x_0)<0$, then $H(x)$ increases from 0 at $x_0$ but is concave down, meaning it must become negative for $x>x_0$ near $x_0$. This contradicts the definition of $x_0$ as the smallest $x>0$ with $H(x) \ge 0$.
Therefore, we must have $H'(x_0) = 0$.

So, at $x_0$, we have $H(x_0)=0$ and $H'(x_0)=0$.
$H(x_0)=0 \implies u(x_0)^2 - 2x_0 = 0 \implies u(x_0)^2 = 2x_0$.
$H'(x_0)=0 \implies 2u(x_0)u'(x_0) - 2 = 0 \implies u(x_0)u'(x_0) = 1$.

From $u(x_0)^2 = 2x_0$ and $(u(x_0)u'(x_0))^2 = 1^2 = 1$, we get $u(x_0)^2 (u'(x_0))^2 = 1$.
$(2x_0) (u'(x_0))^2 = 1$, so $(u'(x_0))^2 = \frac{1}{2x_0}$.
This means $u'(x_0) = \pm \frac{1}{\sqrt{2x_0}}$.
Since $u(x_0)u'(x_0)=1$, $u(x_0)$ and $u'(x_0)$ must have the same sign.
As $u(x_0)^2=2x_0$, $u(x_0) = \pm \sqrt{2x_0}$.
This leaves two possibilities for the values $(u(x_0), u'(x_0))$:
1) $(u(x_0), u'(x_0)) = (\sqrt{2x_0}, 1/\sqrt{2x_0})$
2) $(u(x_0), u'(x_0)) = (-\sqrt{2x_0}, -1/\sqrt{2x_0})$

Consider case 1: $u(x_0) = \sqrt{2x_0}$ and $u'(x_0) = 1/\sqrt{2x_0}$ for some $x_0>0$.
Let $y(x) = \sqrt{2x}$ for $x>0$. This function satisfies $y(0)=0$ (in the limit) and $y'(x) = 1/\sqrt{2x}$ for $x>0$.
We verified earlier that $y(x)=\sqrt{2x}$ is a solution to the ODE for $x>0$:
$(y')^2(1+y^2) = (1/\sqrt{2x})^2(1+(\sqrt{2x})^2) = \frac{1}{2x}(1+2x) = \frac{1}{2x}+1$.
$y''(x) = \frac{d}{dx}((2x)^{-1/2}) = -\frac{1}{2}(2x)^{-3/2}(2) = -(2x)^{-3/2}$.
$1 - y''y = 1 - (-(2x)^{-3/2})(\sqrt{2x}) = 1 + (2x)^{-3/2}(2x)^{1/2} = 1 + (2x)^{-1} = 1 + \frac{1}{2x}$.
So $y(x)=\sqrt{2x}$ satisfies the ODE for $x>0$.

At $x_0>0$, the function $u(x)$ and the function $y(x)=\sqrt{2x}$ have the same value $u(x_0)=y(x_0)=\sqrt{2x_0}$ and the same derivative $u'(x_0)=y'(x_0)=1/\sqrt{2x_0}$.
Since $u(x_0) \ne 0$, the right-hand side of the ODE system $y_1'=y_2, y_2'=(1-y_2^2(1+y_1^2))/y_1$ is Lipschitz in a neighborhood of $(u(x_0), u'(x_0))$. By the uniqueness theorem for ODEs, the solution $u(x)$ must be identical to $y(x)$ in a neighborhood of $x_0$. Because the ODE is satisfied by $y(x)=\sqrt{2x}$ for all $x>0$, $u(x)$ must be $\sqrt{2x}$ for all $x>0$.

Similarly, case 2 leads to $u(x)=-\sqrt{2x}$ for all $x>0$.

However, the problem states that $u \in \mathcal{C}^1(\mathbb{R})$ and $u(0)=0$.
If $u(x)=\sqrt{2x}$ for $x>0$, then $u'(x) = 1/\sqrt{2x}$ for $x>0$.
$\lim_{x \to 0^+} u'(x) = \lim_{x \to 0^+} 1/\sqrt{2x} = +\infty$.
For $u$ to be $\mathcal{C}^1(\mathbb{R})$, $u'(x)$ must be continuous at $x=0$, and $u'(0)$ must be finite. We know $u'(0)=\pm 1$.
Since $\lim_{x \to 0^+} u'(x)$ is infinite, $u(x)$ cannot be $\sqrt{2x}$ for $x>0$ if $u \in \mathcal{C}^1(\mathbb{R})$.
The function $u(x)=\sqrt{2x}$ for $x>0$ cannot be extended to $x=0$ in a $\mathcal{C}^1$ manner with $u(0)=0$.

Similarly, if $u(x)=-\sqrt{2x}$ for $x>0$, then $u'(x)=-1/\sqrt{2x}$ for $x>0$.
$\lim_{x \to 0^+} u'(x) = \lim_{x \to 0^+} -1/\sqrt{2x} = -\infty$.
This also contradicts the requirement that $u \in \mathcal{C}^1(\mathbb{R})$ and $u'(0)=\pm 1$.

The assumption that there exists $x_1>0$ such that $H(x_1) \ge 0$ leads to a contradiction.
Therefore, $H(x) < 0$ for all $x>0$.
$u(x)^2 - 2x < 0$ for all $x>0$.
$u(x)^2 < 2x$ for all $x>0$.
$|u(x)| < \sqrt{2x}$ for all $x>0$.

We need to make sure $u'(x)$ is never zero for $x>0$. If $u'(c)=0$ for some $c>0$, the ODE gives $0=1-u''(c)u(c)$, so $u''(c)u(c)=1$. This requires $u(c) \ne 0$ and $u''(c)=1/u(c)$. If $u(c)>0$, $u''(c)>0$. If $u(c)<0$, $u''(c)<0$. $u'(c)=0$ means $c$ is a critical point. If $u(c)>0$, $u''(c)>0$ means $c$ is a local minimum, but $u(c)>0$ should be a local maximum. If $u(c)<0$, $u''(c)<0$ means $c$ is a local maximum, but $u(c)<0$ should be a local minimum. This is a contradiction. Thus $u'(x)$ is never zero for $x>0$. Since $u'(0)=\pm 1$, $u'(x)$ must have the same sign as $u'(0)$ for all $x>0$. This implies $u(x)$ is strictly monotone for $x>0$. Since $u(0)=0$, $u(x) \ne 0$ for $x>0$. This ensures $u(x_0) \ne 0$.

The final answer is $\boxed{|u(x)| < \sqrt{2x} \text{ for all } x > 0}$.