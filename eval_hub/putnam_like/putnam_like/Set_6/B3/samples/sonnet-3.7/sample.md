# Solution

To prove that $f$ is constant, I'll show that $f(x) = f(0)$ for all $x \in \mathbb{R}$.

## Step 1: Define an auxiliary function

Let $g(x) = f(x) - f(0)$. Then:
- $g'(x) = f'(x)$ (since $f(0)$ is a constant)
- $g(0) = 0$
- $|g'(x)| \leq |g(x)|$ for all $x \in \mathbb{R}$ (from the given condition)

## Step 2: Introduce a strategic function

Define $h(x) = |g(x)|e^{-|x|}$. Note that:
- $h(0) = |g(0)|e^0 = 0$
- $h(x) \geq 0$ for all $x \in \mathbb{R}$ (by definition)

## Step 3: Analyze the behavior of $h(x)$ for $x > 0$

For $x > 0$, we need to compute $h'(x)$ and determine its sign.

Case 1: If $g(x) > 0$, then:
$h(x) = g(x)e^{-x}$ and $h'(x) = (g'(x) - g(x))e^{-x}$

From $|g'(x)| \leq |g(x)|$ and $g(x) > 0$, we get $-g(x) \leq g'(x) \leq g(x)$, which implies $g'(x) - g(x) \leq 0$. Therefore, $h'(x) \leq 0$.

Case 2: If $g(x) < 0$, then:
$h(x) = -g(x)e^{-x}$ and $h'(x) = (g(x) - g'(x))e^{-x}$

From $|g'(x)| \leq |g(x)|$ and $g(x) < 0$, we get $g(x) \leq g'(x) \leq -g(x)$, which implies $g(x) - g'(x) \leq 0$. Therefore, $h'(x) \leq 0$.

Case 3: If $g(x) = 0$, then from $|g'(x)| \leq |g(x)| = 0$, we get $g'(x) = 0$, which means $h'(x) = 0$.

Thus, for all $x > 0$, we have $h'(x) \leq 0$, making $h$ non-increasing on $[0,\infty)$.

## Step 4: Analyze the behavior of $h(x)$ for $x < 0$

Similarly, for $x < 0$:

Case 1: If $g(x) > 0$, then:
$h(x) = g(x)e^{x}$ (since $|x| = -x$ for $x < 0$) and $h'(x) = (g'(x) + g(x))e^{x}$

From $|g'(x)| \leq |g(x)|$ and $g(x) > 0$, we get $-g(x) \leq g'(x) \leq g(x)$, which implies $g'(x) + g(x) \geq 0$. Therefore, $h'(x) \geq 0$.

Case 2: If $g(x) < 0$, then:
$h(x) = -g(x)e^{x}$ and $h'(x) = (-g'(x) - g(x))e^{x}$

From $|g'(x)| \leq |g(x)|$ and $g(x) < 0$, we get $g(x) \leq g'(x) \leq -g(x)$, which implies $-g'(x) - g(x) \geq 0$. Therefore, $h'(x) \geq 0$.

Case 3: If $g(x) = 0$, then $g'(x) = 0$ as before, so $h'(x) = 0$.

Thus, for all $x < 0$, we have $h'(x) \geq 0$, making $h$ non-decreasing on $(-\infty,0]$.

## Step 5: Conclude that $f$ is constant

Since $h(0) = 0$ and:
- $h$ is non-increasing on $[0,\infty)$
- $h$ is non-decreasing on $(-\infty,0]$
- $h(x) \geq 0$ for all $x \in \mathbb{R}$

The only possibility is that $h(x) = 0$ for all $x \in \mathbb{R}$.

Since $h(x) = |g(x)|e^{-|x|} = 0$ and $e^{-|x|} > 0$ for all $x$, we must have $|g(x)| = 0$ for all $x \in \mathbb{R}$, which means $g(x) = 0$ for all $x \in \mathbb{R}$.

Therefore, $f(x) = f(0)$ for all $x \in \mathbb{R}$, proving that $f$ is constant.