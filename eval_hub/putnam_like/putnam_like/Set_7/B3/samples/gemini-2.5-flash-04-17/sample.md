Let $g_n(x) = \frac{f(x)}{x^n}$. The condition states that $g_n(x)$ is increasing on $(0,1)$ for all $n \geq 0$. This means that $g_n'(x) \geq 0$ for all $x \in (0,1)$.

Let's compute the derivative of $g_n(x)$:
$g_n'(x) = \frac{f'(x) \cdot x^n - f(x) \cdot n x^{n-1}}{(x^n)^2} = \frac{f'(x) x^n - n f(x) x^{n-1}}{x^{2n}} = \frac{x^{n-1} (f'(x) x - n f(x))}{x^{2n}} = \frac{f'(x) x - n f(x)}{x^{n+1}}$.

Since $x \in (0,1)$, $x^{n+1} > 0$. Thus, $g_n'(x) \geq 0$ is equivalent to:
$f'(x) x - n f(x) \geq 0$ for all $n \geq 0$ and for all $x \in (0,1)$.

Let's analyze this condition: $f'(x) x \geq n f(x)$ for all $n \geq 0$.
Fix $x \in (0,1)$. The inequality $f'(x) x \geq n f(x)$ must hold for all non-negative integers $n$.

Case 1: Suppose there exists $x_0 \in (0,1)$ such that $f(x_0) > 0$.
Then $f'(x_0) x_0 \geq n f(x_0)$ for all $n \geq 0$. Since $f(x_0) > 0$, we can divide by $f(x_0)$ while preserving the inequality direction:
$\frac{f'(x_0) x_0}{f(x_0)} \geq n$ for all $n \geq 0$.
This means that the value $\frac{f'(x_0) x_0}{f(x_0)}$ must be greater than or equal to every non-negative integer. This is impossible, as the set of non-negative integers $\{0, 1, 2, \ldots\}$ is unbounded above.
Therefore, our assumption that $f(x_0) > 0$ for some $x_0$ must be false.
This implies that $f(x) \leq 0$ for all $x \in (0,1)$.

Now, let's consider the statement we are asked to verify: $f^{(n)}(x) \geq 0$ for every $n \geq 0$ and all $x \in (0,1)$.
For $n=0$, the statement is $f^{(0)}(x) \geq 0$, which is $f(x) \geq 0$.

We have concluded that $f(x) \leq 0$ for all $x \in (0,1)$.
For $f(x)$ to satisfy both $f(x) \leq 0$ and $f(x) \geq 0$ for all $x \in (0,1)$, it must be the case that $f(x) = 0$ for all $x \in (0,1)$.
If $f(x) = 0$ for all $x \in (0,1)$, then $f^{(n)}(x) = 0$ for all $n \geq 0$ and all $x \in (0,1)$. In this case, $f^{(n)}(x) \geq 0$ is true.

However, the question is whether the statement is true for *any* function $f$ satisfying the given conditions. To show that the statement is not true in general, we need to find just one function that satisfies the given conditions but does not satisfy $f^{(n)}(x) \geq 0$ for all $n \geq 0$ and $x \in (0,1)$.

Let's consider the function $f(x) = -1$ for all $x \in (0,1)$.
This function is $\mathcal{C}^\infty$ on $(0,1)$.
Let's check the condition $\frac{f(x)}{x^n}$ is increasing for all $n \geq 0$.
$g_n(x) = \frac{-1}{x^n} = -x^{-n}$.
$g_n'(x) = -(-n)x^{-n-1} = n x^{-n-1} = \frac{n}{x^{n+1}}$.
For $x \in (0,1)$, $x^{n+1} > 0$.
For $n=0$, $g_0'(x) = 0$, which is $\geq 0$. $g_0(x)=-1$ is constant, hence increasing.
For $n \geq 1$, $n > 0$, so $g_n'(x) = \frac{n}{x^{n+1}} > 0$. $g_n(x)$ is strictly increasing.
So, $f(x)=-1$ satisfies the given condition for all $n \geq 0$.

Now let's check the statement $f^{(n)}(x) \geq 0$ for all $n \geq 0$ and $x \in (0,1)$ for $f(x)=-1$.
For $n=0$: $f^{(0)}(x) = f(x) = -1$.
Is $f^{(0)}(x) \geq 0$? No, $-1 < 0$.
The statement fails for $n=0$.

For $n \geq 1$: $f'(x) = \frac{d}{dx}(-1) = 0$, $f''(x) = 0$, and so on. $f^{(n)}(x) = 0$ for all $n \geq 1$.
For $n \geq 1$, $f^{(n)}(x) = 0 \geq 0$, which is true.
However, the statement must hold for *every* $n \geq 0$. Since it fails for $n=0$, the statement is false.

We have found a function $f(x)=-1$ that satisfies the condition that $\frac{f(x)}{x^n}$ is increasing on $(0,1)$ for all $n \geq 0$, but for which $f^{(0)}(x) \geq 0$ is false.
Therefore, the statement " $f^{(n)} (x) \geq 0$ for every $n \geq 0$ and all $x \in (0,1)$" is not true.

The final answer is $\boxed{No}$.