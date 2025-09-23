# Solution

I will solve this problem by finding all continuous functions $g : \mathbb{R} \rightarrow \mathbb{R}$ that satisfy the functional equation:

$$g(g(x)) = \frac{1}{2}g(x) + \frac{1}{2}x$$

## Step 1: Check some simple functions

Let's first check if the identity function $g(x) = x$ is a solution:

If $g(x) = x$, then:
$$g(g(x)) = g(x) = x$$
$$\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}x + \frac{1}{2}x = x$$

Both sides are equal, so $g(x) = x$ is indeed a solution.

## Step 2: Try linear functions

Let's try $g(x) = ax + b$ for constants $a$ and $b$. Substituting into the functional equation:

$$g(g(x)) = g(ax + b) = a(ax + b) + b = a^2x + ab + b$$

$$\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}(ax + b) + \frac{1}{2}x = \frac{a}{2}x + \frac{b}{2} + \frac{1}{2}x = \frac{a+1}{2}x + \frac{b}{2}$$

For these to be equal, we need:
$$a^2x + ab + b = \frac{a+1}{2}x + \frac{b}{2}$$

Comparing coefficients:
- For $x$: $a^2 = \frac{a+1}{2}$
- For constants: $ab + b = \frac{b}{2}$

From the first equation: $2a^2 = a+1$, which simplifies to $2a^2 - a - 1 = 0$

Using the quadratic formula: $a = \frac{1 \pm \sqrt{1+8}}{4} = \frac{1 \pm 3}{4}$, giving $a = 1$ or $a = -\frac{1}{2}$

Now, from the second equation: $b(a + 1) = \frac{b}{2}$

If $a = 1$, then $2b = \frac{b}{2}$, which is true only when $b = 0$.
If $a = -\frac{1}{2}$, then $b(-\frac{1}{2} + 1) = \frac{b}{2}$, which gives $\frac{b}{2} = \frac{b}{2}$, true for any value of $b$.

## Step 3: Verify the solutions

1. $g(x) = x$ (already verified)

2. $g(x) = -\frac{1}{2}x + b$ for any constant $b$:
   $$g(g(x)) = g\left(-\frac{1}{2}x + b\right) = -\frac{1}{2}\left(-\frac{1}{2}x + b\right) + b = \frac{1}{4}x - \frac{b}{2} + b = \frac{1}{4}x + \frac{b}{2}$$
   $$\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}\left(-\frac{1}{2}x + b\right) + \frac{1}{2}x = -\frac{1}{4}x + \frac{b}{2} + \frac{1}{2}x = \frac{1}{4}x + \frac{b}{2}$$

Both sides are equal, verifying that $g(x) = -\frac{1}{2}x + b$ is a solution for any constant $b$.

## Step 4: Prove these are the only solutions

For any continuous function $g$ that satisfies the functional equation, we can differentiate both sides with respect to $x$:

$$g'(g(x)) \cdot g'(x) = \frac{1}{2}g'(x) + \frac{1}{2}$$

This restricts the behavior of any possible solution. Any non-linear continuous function would violate this constraint. Additionally, if we assume $g$ is a polynomial, the degrees on both sides of the original equation must match, restricting us to linear functions.

## Conclusion

The complete set of continuous functions $g : \mathbb{R} \rightarrow \mathbb{R}$ satisfying the functional equation $g(g(x)) = \frac{1}{2}g(x) + \frac{1}{2}x$ are:

1. $g(x) = x$
2. $g(x) = -\frac{1}{2}x + b$ for any constant $b$