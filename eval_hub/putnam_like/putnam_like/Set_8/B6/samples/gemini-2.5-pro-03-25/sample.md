Let the given equation be
\[
f(b)+f(a)-2f\left(\frac{a+b}2\right)=(b-a)^2f''(\sqrt{ab}),\quad \text{for all }a,b>0. \quad (*)
\]
The function $f:(0,+\infty)\to\mathbb{R}$ is twice differentiable.

Let $x>0$ be fixed. We introduce a change of variables. Let $a = xe^{-t}$ and $b = xe^t$ for $t \in \mathbb{R}$.
Since $x>0$, $a$ and $b$ are always positive.
Then $\frac{a+b}{2} = \frac{xe^{-t}+xe^t}{2} = x \frac{e^t+e^{-t}}{2} = x \cosh t$.
Also, $\sqrt{ab} = \sqrt{xe^{-t} \cdot xe^t} = \sqrt{x^2 e^0} = \sqrt{x^2} = x$.
And $b-a = xe^t - xe^{-t} = x(e^t - e^{-t}) = 2x \sinh t$.
Substituting these into the given equation $(*)$:
\[
f(xe^t) + f(xe^{-t}) - 2f(x \cosh t) = (2x \sinh t)^2 f''(x)
\]
\[
f(xe^t) + f(xe^{-t}) - 2f(x \cosh t) = 4x^2 \sinh^2 t f''(x)
\]
This equation holds for all $x>0$ and for all $t \in \mathbb{R}$.

Let $x$ be fixed. Define the function $F: \mathbb{R} \to \mathbb{R}$ by
\[
F(t) = f(xe^t) + f(xe^{-t}) - 2f(x \cosh t) - 4x^2 \sinh^2 t f''(x)
\]
From the above derivation, we have $F(t) = 0$ for all $t \in \mathbb{R}$.
Since $f$ is twice differentiable, $f$ and $f'$ are continuous. $f''$ exists. The function $F(t)$ is twice differentiable with respect to $t$.
We compute the first and second derivatives of $F(t)$ with respect to $t$.

$F'(t) = \frac{d}{dt} F(t)$. We use the chain rule.
$\frac{d}{dt} f(xe^t) = f'(xe^t) \cdot (xe^t)$.
$\frac{d}{dt} f(xe^{-t}) = f'(xe^{-t}) \cdot (-xe^{-t})$.
$\frac{d}{dt} f(x \cosh t) = f'(x \cosh t) \cdot (x \sinh t)$.
$\frac{d}{dt} (4x^2 \sinh^2 t f''(x)) = 4x^2 f''(x) \cdot (2 \sinh t \cosh t)$.
So,
\[
F'(t) = xe^t f'(xe^t) - xe^{-t} f'(xe^{-t}) - 2x \sinh t f'(x \cosh t) - 8x^2 \sinh t \cosh t f''(x)
\]
Since $F(t)=0$ for all $t$, $F'(t)=0$ for all $t$.

Now we compute the second derivative $F''(t)$.
$\frac{d}{dt} (xe^t f'(xe^t)) = xe^t f'(xe^t) + xe^t \cdot f''(xe^t) \cdot (xe^t) = xe^t f'(xe^t) + x^2 e^{2t} f''(xe^t)$.
$\frac{d}{dt} (-xe^{-t} f'(xe^{-t})) = - [-xe^{-t} f'(xe^{-t}) + xe^{-t} \cdot f''(xe^{-t}) \cdot (-xe^{-t})] = xe^{-t} f'(xe^{-t}) + x^2 e^{-2t} f''(xe^{-t})$.
$\frac{d}{dt} (-2x \sinh t f'(x \cosh t)) = -2x [\cosh t f'(x \cosh t) + \sinh t \cdot f''(x \cosh t) \cdot (x \sinh t)] = -2x \cosh t f'(x \cosh t) - 2x^2 \sinh^2 t f''(x \cosh t)$.
$\frac{d}{dt} (-8x^2 \sinh t \cosh t f''(x)) = -8x^2 f''(x) \frac{d}{dt} (\frac{1}{2}\sinh(2t)) = -8x^2 f''(x) \cosh(2t)$.
Summing these terms gives $F''(t)$:
\[
F''(t) = xe^t f'(xe^t) + x^2 e^{2t} f''(xe^t) + xe^{-t} f'(xe^{-t}) + x^2 e^{-2t} f''(xe^{-t}) - 2x \cosh t f'(x \cosh t) - 2x^2 \sinh^2 t f''(x \cosh t) - 8x^2 \cosh(2t) f''(x)
\]
Since $F'(t)=0$ for all $t$, we must have $F''(t)=0$ for all $t$.
Let's evaluate $F''(t)$ at $t=0$.
We have $e^0=1$, $e^0=1$, $\cosh 0 = 1$, $\sinh 0 = 0$, $\cosh(0)=1$.
\[
F''(0) = x f'(x) + x^2 f''(x) + x f'(x) + x^2 f''(x) - 2x(1) f'(x) - 2x^2(0)^2 f''(x) - 8x^2(1) f''(x)
\]
\[
F''(0) = (x f'(x) + x f'(x)) + (x^2 f''(x) + x^2 f''(x)) - 2x f'(x) - 0 - 8x^2 f''(x)
\]
\[
F''(0) = 2x f'(x) + 2x^2 f''(x) - 2x f'(x) - 8x^2 f''(x)
\]
\[
F''(0) = (2x^2 - 8x^2) f''(x) = -6x^2 f''(x)
\]
Since $F''(t)=0$ for all $t$, we have $F''(0)=0$.
So, $-6x^2 f''(x) = 0$.
Since this must hold for all $x \in (0, \infty)$, and $x \neq 0$, we must have $f''(x)=0$.

The condition $f''(x)=0$ holds for all $x \in (0, \infty)$.
Integrating $f''(x)=0$ with respect to $x$, we get $f'(x)=c$ for some constant $c \in \mathbb{R}$.
Integrating $f'(x)=c$ with respect to $x$, we get $f(x)=cx+d$ for some constant $d \in \mathbb{R}$.

So, any twice differentiable function $f$ satisfying the given equation must be of the form $f(x)=cx+d$.
Let's check if all functions of this form are indeed solutions.
If $f(x)=cx+d$, then $f'(x)=c$ and $f''(x)=0$.
The left side (LHS) of the equation $(*)$ is:
\[
f(b)+f(a)-2f\left(\frac{a+b}2\right) = (cb+d) + (ca+d) - 2\left(c\frac{a+b}{2}+d\right)
\]
\[
= c(a+b) + 2d - (c(a+b) + 2d) = 0
\]
The right side (RHS) of the equation $(*)$ is:
\[
(b-a)^2 f''(\sqrt{ab}) = (b-a)^2 \cdot 0 = 0
\]
Since LHS = RHS ($0=0$), any function of the form $f(x)=cx+d$ is a solution.

Thus, the set of all twice differentiable functions satisfying the given equation is the set of linear functions $f(x)=cx+d$, where $c$ and $d$ are arbitrary real constants.

Final Answer: The final answer is $\boxed{f(x) = cx+d}$