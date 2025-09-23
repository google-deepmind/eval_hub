Let the given equation be
\[f(b)+f(a)-2f\left(\frac{a+b}2\right)=(b-a)^2f''(\sqrt{ab}),\quad \text{for all }a,b>0. \quad (*).\]
Let $x>0$ be fixed. Choose $a=xe^{-t}$ and $b=xe^t$ for $t \in \mathbb{R}$. Since $x>0$, $a$ and $b$ are always positive.
Then $\frac{a+b}{2} = \frac{xe^{-t}+xe^t}{2} = x\cosh(t)$.
$\sqrt{ab} = \sqrt{xe^{-t}xe^t} = \sqrt{x^2} = x$ (since $x>0$).
$b-a = xe^t - xe^{-t} = 2x\sinh(t)$.
$(b-a)^2 = (2x\sinh(t))^2 = 4x^2\sinh^2(t)$.

Substituting these into the equation $(*)$, we get:
\[f(xe^t)+f(xe^{-t})-2f(x\cosh(t)) = 4x^2\sinh^2(t)f''(x).\]
This equation holds for all $x>0$ and all $t \in \mathbb{R}$. Note that $f''(x)$ is the value of the second derivative at $x$, so for a fixed $x$, $f''(x)$ is a constant with respect to $t$.

Let $g(t) = f(xe^t)+f(xe^{-t})-2f(x\cosh(t))$ for a fixed $x>0$.
Let $R(t) = 4x^2\sinh^2(t)f''(x)$.
The equation is $g(t) = R(t)$ for all $t \in \mathbb{R}$.

Let's differentiate $g(t)$ and $R(t)$ with respect to $t$.
$f$ is twice differentiable, so $f'$ is differentiable. Let $u(t)=xe^t$, $v(t)=xe^{-t}$, $w(t)=x\cosh t$. These functions are $C^\infty$ with respect to $t$, and their values are always in $(0,\infty)$ for $x>0$.
$u'(t)=xe^t$, $v'(t)=-xe^{-t}$, $w'(t)=x\sinh t$.
$g'(t) = f'(u(t))u'(t) + f'(v(t))v'(t) - 2f'(w(t))w'(t)$.
$g'(t) = f'(xe^t)xe^t - f'(xe^{-t})xe^{-t} - 2f'(x\cosh t)x\sinh t$.
Since $f'$ is differentiable, it is continuous. $g'(t)$ is differentiable for all $t$ because $f'$ is differentiable and $u,v,w$ are $C^\infty$. Thus, $g(t)$ is twice differentiable.

$u''(t)=xe^t$, $v''(t)=xe^{-t}$, $w''(t)=x\cosh t$.
$g''(t) = \frac{d}{dt}(f'(u)u') + \frac{d}{dt}(f'(v)v') - 2\frac{d}{dt}(f'(w)w')$.
$\frac{d}{dt}(f'(u)u') = f''(u)u'^2 + f'(u)u'' = f''(xe^t)(xe^t)^2 + f'(xe^t)xe^t$.
$\frac{d}{dt}(f'(v)v') = f''(v)v'^2 + f'(v)v'' = f''(xe^{-t})(-xe^{-t})^2 + f'(xe^{-t})xe^{-t} = f''(xe^{-t})(xe^{-t})^2 + f'(xe^{-t})xe^{-t}$.
$\frac{d}{dt}(f'(w)w') = f''(w)w'^2 + f'(w)w'' = f''(x\cosh t)(x\sinh t)^2 + f'(x\cosh t)x\cosh t$.

$g''(t) = x^2e^{2t}f''(xe^t) + xe^tf'(xe^t) + x^2e^{-2t}f''(xe^{-t}) + xe^{-t}f'(xe^{-t}) - 2(x^2\sinh^2(t)f''(x\cosh t) + x\cosh t f'(x\cosh t))$.
This expression for $g''(t)$ exists for all $t \in \mathbb{R}$ because $f''$ exists on $(0,\infty)$.

Now let's find the second derivative of $R(t) = 4x^2\sinh^2(t)f''(x)$.
$R'(t) = 4x^2 (2\sinh t \cosh t) f''(x) = 4x^2 \sinh(2t) f''(x)$.
$R''(t) = 4x^2 (2\cosh(2t)) f''(x) = 8x^2 \cosh(2t) f''(x)$.
Since $g(t)=R(t)$ for all $t$, their second derivatives must be equal for all $t$.
$g''(t)=R''(t)$ for all $t \in \mathbb{R}$.

Let's evaluate $g''(t)$ and $R''(t)$ at $t=0$.
At $t=0$, $u(0)=x$, $v(0)=x$, $w(0)=x$. $u'(0)=x$, $v'(0)=-x$, $w'(0)=0$. $u''(0)=x$, $v''(0)=x$, $w''(0)=x$.
$g''(0) = x^2e^0f''(x) + xe^0f'(x) + x^2e^0f''(x) + xe^0f'(x) - 2(x^2\sinh^2(0)f''(x) + x\cosh(0)f'(x))$.
$g''(0) = x^2f''(x) + xf'(x) + x^2f''(x) + xf'(x) - 2(0 \cdot f''(x) + x \cdot 1 \cdot f'(x))$.
$g''(0) = 2x^2f''(x) + 2xf'(x) - 2xf'(x) = 2x^2f''(x)$.

$R''(0) = 8x^2\cosh(2 \cdot 0)f''(x) = 8x^2\cosh(0)f''(x) = 8x^2f''(x)$.

Equating $g''(0)$ and $R''(0)$:
$2x^2f''(x) = 8x^2f''(x)$.
$6x^2f''(x) = 0$.
Since $x>0$, $x^2>0$. Thus, $f''(x)=0$.

This holds for any $x>0$. Therefore, $f''(x)=0$ for all $x>0$.
This implies that $f'(x)$ must be a constant on $(0,\infty)$. Let $f'(x)=A$ for some $A \in \mathbb{R}$.
Integrating $f'(x)=A$ with respect to $x$, we get $f(x)=Ax+B$ for some constant $B \in \mathbb{R}$.

Let's verify this solution in the original equation $(*)$.
$f(x)=Ax+B$. $f'(x)=A$. $f''(x)=0$.
LHS: $f(b)+f(a)-2f\left(\frac{a+b}{2}\right) = (Ab+B)+(Aa+B)-2\left(A\frac{a+b}{2}+B\right)$
$= Aa+Ab+2B - A(a+b) - 2B = Aa+Ab+2B - Aa-Ab-2B = 0$.
RHS: $(b-a)^2f''(\sqrt{ab}) = (b-a)^2 \cdot 0 = 0$.
LHS = RHS, so the equation is satisfied for all $a,b>0$.
The function $f(x)=Ax+B$ is twice differentiable on $(0,\infty)$ for any $A, B \in \mathbb{R}$.

The final answer is $\boxed{f(x) = Ax+B, A,B \in \mathbb{R}}$.