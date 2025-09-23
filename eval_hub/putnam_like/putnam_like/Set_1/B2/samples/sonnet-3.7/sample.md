# Solution

I'll solve this problem by introducing an auxiliary function and showing it satisfies a more tractable differential equation.

## Step 1: Define an auxiliary function
Let's define $q(x) = u(x) \cdot u'(x)$. We'll find a differential equation for $q(x)$.

First, let's compute $q'(x)$:
$$q'(x) = (u'(x))^2 + u(x) \cdot u''(x)$$

From the given differential equation, we can rearrange to isolate $u(x) \cdot u''(x)$:
$$(u')^2(1+u^2) = 1 - u''u$$
$$\Rightarrow u''u = 1 - (u')^2(1+u^2)$$
$$\Rightarrow u''u = 1 - (u')^2 - (u')^2u^2$$

Substituting this into our expression for $q'(x)$:
$$q'(x) = (u')^2 + 1 - (u')^2 - (u')^2u^2 = 1 - (u')^2u^2 = 1 - (u \cdot u')^2 = 1 - q(x)^2$$

## Step 2: Finding the solution for $q(x)$
We've shown that $q(x)$ satisfies the differential equation:
$$q'(x) = 1 - q(x)^2$$

From the original conditions, $u(0) = 0$, and evaluating the original differential equation at $x = 0$:
$$(u'(0))^2(1+0^2) = 1 - u''(0) \cdot 0$$
$$\Rightarrow (u'(0))^2 = 1$$

So $u'(0) = \pm 1$. Therefore:
$$q(0) = u(0) \cdot u'(0) = 0 \cdot u'(0) = 0$$

The unique solution to $q'(x) = 1 - q(x)^2$ with $q(0) = 0$ is $q(x) = \tanh(x)$.

## Step 3: Proving the inequality
Let's define $g(x) = u(x)^2 - 2x$. We have:
$$g'(x) = 2u(x)u'(x) - 2 = 2q(x) - 2 = 2\tanh(x) - 2$$

Since $\tanh(x) < 1$ for all $x > 0$, we have $g'(x) < 0$ for all $x > 0$.

Also, $g(0) = u(0)^2 - 2 \cdot 0 = 0$.

Since $g(0) = 0$ and $g'(x) < 0$ for all $x > 0$, it follows that $g(x) < 0$ for all $x > 0$.

Therefore, $u(x)^2 < 2x$ for all $x > 0$, which implies $|u(x)| < \sqrt{2x}$ for all $x > 0$.