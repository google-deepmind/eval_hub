# Solution

I need to find all $x \in \mathbb{R}$ satisfying $6^{x^2} + 5^{x^2} - 10^{x^2} = 1$.

Let me substitute $y = x^2$ to simplify, so I'm looking for all $y \geq 0$ such that:

$$6^y + 5^y - 10^y = 1$$

## Step 1: Finding specific solutions
Let's check some simple values:

For $y = 0$:
$$6^0 + 5^0 - 10^0 = 1 + 1 - 1 = 1$$
So $y = 0$ is a solution.

For $y = 1$:
$$6^1 + 5^1 - 10^1 = 6 + 5 - 10 = 1$$
So $y = 1$ is also a solution.

## Step 2: Proving these are the only solutions
Let's define $f(y) = 6^y + 5^y - 10^y - 1$, so we're looking for $y$ where $f(y) = 0$.

### For $y \in (0,1)$:
I'll use the strict convexity of exponential functions. For any strictly convex function $g(y)$ and $y \in (0,1)$:
- $g(y) < (1-y)g(0) + yg(1)$ if $g$ is strictly concave
- $g(y) > (1-y)g(0) + yg(1)$ if $g$ is strictly convex

Since $6^y$ and $5^y$ are strictly convex, we have:
$$6^y > (1-y)6^0 + y6^1 = 1-y+6y = 1+5y$$
$$5^y > (1-y)5^0 + y5^1 = 1-y+5y = 1+4y$$

Similarly, since $10^y$ is strictly convex:
$$10^y < (1-y)10^0 + y10^1 = 1-y+10y = 1+9y$$

Therefore:
$$f(y) = 6^y + 5^y - 10^y - 1 > (1+5y) + (1+4y) - (1+9y) - 1 = 0$$

This proves $f(y) > 0$ for all $y \in (0,1)$.

### For $y > 1$:
We can show that $f(y) < 0$ for all $y > 1$.

First, let's calculate $f(2)$:
$$f(2) = 6^2 + 5^2 - 10^2 - 1 = 36 + 25 - 100 - 1 = -40 < 0$$

Also, $f'(y) = 6^y\ln 6 + 5^y\ln 5 - 10^y\ln 10$. At $y = 1$:
$$f'(1) = 6\ln 6 + 5\ln 5 - 10\ln 10 \approx 10.75 + 8.05 - 23.03 < 0$$

Since $f(1) = 0$, $f'(1) < 0$, and $f(2) < 0$, we know that $f(y) < 0$ for all $y > 1$.

## Step 3: Finding all values of $x$
Since $y = x^2$, the solutions are:
- $y = 0$ gives $x = 0$
- $y = 1$ gives $x = 1$ or $x = -1$

Therefore, the solutions to the original equation are $x \in \{-1, 0, 1\}$.