This is a fascinating functional equation problem. We will solve it by analyzing the properties of the function $g$ imposed by the equation and its continuity.

The given functional equation is:
$$g(g(x)) = \frac{1}{2} g(x) + \frac{1}{2} x \quad (*)$$
where $g: \mathbb{R} \rightarrow \mathbb{R}$ is a continuous function.

### Step 1: Analyze the properties of $g$

**1. Injectivity**

Let's check if $g$ is an injective (one-to-one) function. Assume that $g(x_1) = g(x_2)$ for some $x_1, x_2 \in \mathbb{R}$.
Applying $g$ to both sides, we get $g(g(x_1)) = g(g(x_2))$.
Using the given equation $(*)$, we can substitute for $g(g(x))$:
$$ \frac{1}{2} g(x_1) + \frac{1}{2} x_1 = \frac{1}{2} g(x_2) + \frac{1}{2} x_2 $$
Since we assumed $g(x_1) = g(x_2)$, the terms involving $g$ cancel out:
$$ \frac{1}{2} x_1 = \frac{1}{2} x_2 $$
This implies $x_1 = x_2$.
Therefore, $g$ is an injective function.

**2. Monotonicity**

A continuous injective function on $\mathbb{R}$ must be strictly monotone. This means $g$ is either strictly increasing or strictly decreasing. We will analyze these two cases separately.

**3. Surjectivity**

Let's determine if $g$ is surjective (onto).
From the equation $(*)$, we can express $x$ in terms of $g(x)$ and $g(g(x))$:
$$ x = 2g(g(x)) - g(x) $$
Let's consider the range of $g$, denoted as $\text{Im}(g)$. Let $y \in \text{Im}(g)$. Then there exists some $z \in \mathbb{R}$ such that $y = g(z)$. Then $g(y) = g(g(z))$ is also in the range of $g$. The expression $2g(y) - y$ must be in the domain of $g$, which is $\mathbb{R}$.

A more rigorous argument for surjectivity: Since $g$ is continuous and strictly monotone on $\mathbb{R}$, its image must be an open interval $(a, b)$ where $a, b \in \mathbb{R} \cup \{-\infty, \infty\}$.
Suppose $\text{Im}(g)$ is a proper subset of $\mathbb{R}$. For instance, suppose $\text{Im}(g)$ is bounded above, i.e., $g(x) \le M$ for all $x$. Then $g(g(x)) \le M$ as well.
From $x = 2g(g(x)) - g(x)$, we have:
$$ |x| = |2g(g(x)) - g(x)| \le 2|g(g(x))| + |g(x)| \le 2M + M = 3M $$
This implies that the domain of $g$ must be bounded, which contradicts that $g$ is defined on all of $\mathbb{R}$. A similar argument holds if $\text{Im}(g)$ is bounded below.
Therefore, $g$ is not bounded. A continuous, strictly monotone, and unbounded function on $\mathbb{R}$ must be surjective. Its range is $\mathbb{R}$.

So, $g$ is a continuous, strictly monotone bijection from $\mathbb{R}$ to $\mathbb{R}$.

### Step 2: Case Analysis based on Monotonicity

**Case 1: $g$ is strictly increasing.**

Let's analyze the fixed points of $g$. A fixed point is a value $c$ such that $g(c)=c$.
If $g(x) > x$ for some $x$, then since $g$ is strictly increasing, we have $g(g(x)) > g(x)$.
However, from the equation $(*)$:
$$ g(g(x)) - g(x) = -\frac{1}{2}g(x) + \frac{1}{2}x = -\frac{1}{2}(g(x)-x) $$
If $g(x) > x$, then $g(x)-x > 0$, so $-\frac{1}{2}(g(x)-x) < 0$.
This implies $g(g(x)) - g(x) < 0$, or $g(g(x)) < g(x)$.
This contradicts the conclusion from monotonicity that $g(g(x)) > g(x)$. The only way to avoid this contradiction is if the premise $g(x) > x$ is false.

Similarly, if we assume $g(x) < x$ for some $x$, then $g(x)-x < 0$.
The equation gives $g(g(x)) - g(x) = -\frac{1}{2}(g(x)-x) > 0$, so $g(g(x)) > g(x)$.
However, since $g$ is strictly increasing, $g(x) < x \implies g(g(x)) < g(x)$, which is again a contradiction.

The only remaining possibility is that $g(x) = x$ for all $x \in \mathbb{R}$.
Let's check if $g(x)=x$ is a solution:
LHS: $g(g(x)) = g(x) = x$.
RHS: $\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}x + \frac{1}{2}x = x$.
LHS = RHS, so $g(x)=x$ is a valid solution.

**Case 2: $g$ is strictly decreasing.**

A strictly decreasing continuous function $f: \mathbb{R} \to \mathbb{R}$ must have exactly one fixed point. To see this, consider the function $h(x) = g(x)-x$. $h(x)$ is strictly decreasing since $g(x)$ is decreasing and $-x$ is decreasing. Also, since $g$ is surjective, it is unbounded above and below.
$\lim_{x \to -\infty} g(x) = +\infty \implies \lim_{x \to -\infty} h(x) = +\infty$.
$\lim_{x \to +\infty} g(x) = -\infty \implies \lim_{x \to +\infty} h(x) = -\infty$.
Since $h$ is continuous and goes from $+\infty$ to $-\infty$, by the Intermediate Value Theorem, there must be a unique point $c$ such that $h(c)=0$, which means $g(c)=c$.

Let's analyze the behavior of iterates of $g$. For a fixed $x_0 \in \mathbb{R}$, define a sequence $(x_n)_{n \ge 0}$ by $x_{n+1} = g(x_n)$, with $x_1=g(x_0)$.
The functional equation gives a recurrence relation for this sequence:
$$ x_{n+2} = g(x_{n+1}) = g(g(x_n)) = \frac{1}{2}g(x_n) + \frac{1}{2}x_n = \frac{1}{2}x_{n+1} + \frac{1}{2}x_n $$
This is a homogeneous linear recurrence relation with constant coefficients. The characteristic equation is:
$$ r^2 - \frac{1}{2}r - \frac{1}{2} = 0 $$
$$ 2r^2 - r - 1 = 0 $$
$$ (2r+1)(r-1) = 0 $$
The roots are $r_1 = 1$ and $r_2 = -1/2$.
The general solution for the sequence is of the form:
$$ x_n = A \cdot (1)^n + B \cdot \left(-\frac{1}{2}\right)^n = A + B\left(-\frac{1}{2}\right)^n $$
where $A$ and $B$ are constants that depend on the initial values $x_0 = x$ and $x_1 = g(x)$.
For $n=0$: $x_0 = x = A+B$.
For $n=1$: $x_1 = g(x) = A - \frac{1}{2}B$.

As $n \to \infty$, the term $(-\frac{1}{2})^n \to 0$. So, the sequence $x_n = g^{(n)}(x)$ converges to a limit:
$$ L(x) = \lim_{n \to \infty} x_n = A $$
Since $g$ is continuous, if $x_n \to L(x)$, then $g(x_n) \to g(L(x))$.
But $g(x_n) = x_{n+1}$, and $\lim_{n \to \infty} x_{n+1} = L(x)$ as well.
Therefore, $g(L(x)) = L(x)$. This means the limit $L(x)$ must be a fixed point of $g$.
As we established, a strictly decreasing continuous function $g$ has a unique fixed point, say $c$.
Thus, for any starting value $x$, the sequence of iterates $g^{(n)}(x)$ must converge to this unique fixed point $c$.
So, $L(x) = A = c$ for all $x \in \mathbb{R}$.

Now we can determine the form of $g(x)$. We have the system of equations for $A$ and $B$:
1) $x = A+B$
2) $g(x) = A - \frac{1}{2}B$

Since $A=c$ for all $x$, we have:
1) $x = c+B \implies B = x-c$.
2) $g(x) = c - \frac{1}{2}B$.
Substitute the expression for $B$ from (1) into (2):
$$ g(x) = c - \frac{1}{2}(x-c) = c - \frac{1}{2}x + \frac{1}{2}c = \frac{3}{2}c - \frac{1}{2}x $$
This suggests that any solution in this case must be a linear function of the form $g(x) = -\frac{1}{2}x + b$, where $b = \frac{3}{2}c$ is some constant.
Since the fixed point $c$ can be any real number, $b$ can also be any real number.

Let's check if $g(x) = -\frac{1}{2}x + b$ for any constant $b \in \mathbb{R}$ is a solution.
This function is continuous and strictly decreasing (slope is $-1/2$).
LHS: $g(g(x)) = g(-\frac{1}{2}x+b) = -\frac{1}{2}(-\frac{1}{2}x+b) + b = \frac{1}{4}x - \frac{1}{2}b + b = \frac{1}{4}x + \frac{1}{2}b$.
RHS: $\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}(-\frac{1}{2}x+b) + \frac{1}{2}x = -\frac{1}{4}x + \frac{1}{2}b + \frac{1}{2}x = \frac{1}{4}x + \frac{1}{2}b$.
LHS = RHS, so $g(x) = -\frac{1}{2}x + b$ is a solution for any $b \in \mathbb{R}$.

### Summary of Solutions

We have exhausted all possibilities by splitting the problem based on the monotonicity of $g$. The solutions we found are:

1.  From the strictly increasing case:
    $$ g(x) = x $$
2.  From the strictly decreasing case:
    $$ g(x) = -\frac{1}{2}x + b, \quad \text{for any constant } b \in \mathbb{R} $$

These are all the continuous functions satisfying the given equation.

Final verification:
-   If $g(x)=x$, $g(g(x)) = x$ and $\frac{1}{2}g(x)+\frac{1}{2}x = \frac{1}{2}x+\frac{1}{2}x = x$. This is correct.
-   If $g(x)=-\frac{1}{2}x+b$, $g(g(x)) = -\frac{1}{2}(-\frac{1}{2}x+b)+b = \frac{1}{4}x+\frac{1}{2}b$.
    $\frac{1}{2}g(x)+\frac{1}{2}x = \frac{1}{2}(-\frac{1}{2}x+b)+\frac{1}{2}x = -\frac{1}{4}x+\frac{1}{2}b+\frac{1}{2}x = \frac{1}{4}x+\frac{1}{2}b$. This is also correct.