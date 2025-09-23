# Solution

I need to find all twice differentiable functions $f:(0,+\infty)\to\mathbb{R}$ satisfying:
\[
f(b)+f(a)-2f\left(\frac{a+b}2\right)=(b-a)^2f''(\sqrt{ab}),\quad \text{for all }a,b>0.
\]

## Step 1: Fix $a$ and analyze the equation with respect to $b$

Let's fix $a > 0$ and define:
\[
F(b) = f(b)+f(a)-2f\left(\frac{a+b}2\right)-(b-a)^2f''(\sqrt{ab})
\]

If $f$ satisfies the functional equation, then $F(b) = 0$ for all $b > 0$. 

## Step 2: Compute the second derivative and evaluate at $b = a$

The first derivative $F'(b)$ evaluated at $b = a$ equals zero regardless of the function $f$. Let's compute the second derivative:

\[
F''(b) = f''(b) - \frac{1}{2}f''\left(\frac{a+b}{2}\right) - 2f''(\sqrt{ab}) - \text{(other terms with $(b-a)$ factor)}
\]

When we evaluate at $b = a$, the terms with $(b-a)$ factors vanish, giving:
\[
F''(a) = f''(a) - \frac{1}{2}f''(a) - 2f''(a) = -\frac{3}{2}f''(a)
\]

Since $F''(a) = 0$ for a solution, we must have $f''(a) = 0$. 

## Step 3: General solution

Since $a$ was arbitrary and $f''(a) = 0$ for all $a > 0$, we conclude that $f''(x) = 0$ for all $x > 0$.

Integrating twice, we get:
\[
f(x) = Ax + B
\]
where $A$ and $B$ are arbitrary constants.

## Step 4: Verification

Let's verify our solution by substituting back into the original equation:
\[
A b + B + A a + B - 2\left(A\frac{a+b}{2} + B\right) = (b-a)^2 \cdot 0
\]

Simplifying:
\[
A(a+b) + 2B - A(a+b) - 2B = 0
\]

This is valid for all $a, b > 0$, confirming our solution.

## Answer

The general solution is $f(x) = Ax + B$, where $A$ and $B$ are arbitrary constants.