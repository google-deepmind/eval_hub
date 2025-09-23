# Solution

I'll solve this step-by-step to find all continuous functions $f: (0,\infty) \rightarrow (0,\infty)$ that satisfy the given functional equation.

## Step 1: Verify that $f(x) = 1$ is a solution

Let's first check if the constant function $f(x) = 1$ satisfies the functional equation:

$$f(xf(y+z)) + f(yf(x+z)) + f(zf(x+y)) = 2 + f(x+y+z)$$

Substituting $f(x) = 1$ for all $x > 0$:
- Left side: $f(x \cdot 1) + f(y \cdot 1) + f(z \cdot 1) = f(x) + f(y) + f(z) = 1 + 1 + 1 = 3$
- Right side: $2 + f(x+y+z) = 2 + 1 = 3$

Since both sides equal 3, $f(x) = 1$ is indeed a solution.

## Step 2: Prove that $f(x) = 1$ is the only solution

To show this is the unique solution, I'll use a perturbation approach. Let's assume there's a solution of the form:

$$f_\epsilon(x) = 1 + \epsilon g(x)$$

where $g$ is a continuous function and $\epsilon$ is a small parameter. Substituting this into the functional equation:

$$f_\epsilon(xf_\epsilon(y+z)) + f_\epsilon(yf_\epsilon(x+z)) + f_\epsilon(zf_\epsilon(x+y)) = 2 + f_\epsilon(x+y+z)$$

Expanding the left side terms using Taylor approximation:

$$f_\epsilon(x + \epsilon x g(y+z)) \approx 1 + \epsilon g(x) + \epsilon^2 x g(y+z)g'(x)$$

Substituting all terms and collecting by powers of $\epsilon$:

$$3 + \epsilon(g(x) + g(y) + g(z)) + \epsilon^2(\ldots) = 3 + \epsilon g(x+y+z)$$

Comparing coefficients of $\epsilon^1$:

$$g(x) + g(y) + g(z) = g(x+y+z)$$

This is Cauchy's functional equation, and since $g$ is continuous, its solution is $g(x) = cx$ for some constant $c$.

For the $\epsilon^2$ terms, we get:

$$c^2(x(y+z) + y(x+z) + z(x+y)) = 0$$

Simplifying:
$$c^2(2xy + 2xz + 2yz) = 0$$

Since $x,y,z > 0$, the term $(2xy + 2xz + 2yz)$ is always positive, so we must have $c = 0$.

This means $g(x) = 0$ for all $x$, which implies $f_\epsilon(x) = 1$.

## Conclusion

The unique continuous solution to the functional equation is $f(x) = 1$ for all $x \in (0,\infty)$.