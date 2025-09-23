Let $P(x)$ be the assertion $g(g(x)) = \frac12 g(x) + \frac12 x$.
The function $g: \mathbb{R} \rightarrow \mathbb{R}$ is continuous.

First, let's test for linear solutions of the form $g(x) = cx+d$.
Substituting into the equation:
$c(cx+d)+d = \frac12 (cx+d) + \frac12 x$
$c^2 x + cd + d = \frac12 c x + \frac12 d + \frac12 x$
$c^2 x + (cd+d) = (\frac12 c + \frac12) x + \frac12 d$
Equating the coefficients of $x$:
$c^2 = \frac12 c + \frac12$
$2c^2 - c - 1 = 0$
$(2c+1)(c-1) = 0$
So $c=1$ or $c=-1/2$.

Equating the constant terms:
$cd + d = \frac12 d$
$cd + \frac12 d = 0$
$d(c+\frac12) = 0$

Case 1: $c=1$. The second equation becomes $d(1+\frac12) = 0$, so $\frac32 d = 0$, which implies $d=0$.
Thus $g(x) = x$ is a solution.
Check: $g(g(x)) = g(x) = x$. $\frac12 g(x) + \frac12 x = \frac12 x + \frac12 x = x$. This is a valid solution. $g(x)=x$ is continuous.

Case 2: $c=-1/2$. The second equation becomes $d(-1/2 + 1/2) = 0$, which is $d(0)=0$. This holds for any $d \in \mathbb{R}$.
Thus $g(x) = -\frac12 x + d$ is a potential solution for any $d \in \mathbb{R}$.
Check: $g(g(x)) = g(-\frac12 x + d) = -\frac12 (-\frac12 x + d) + d = \frac14 x - \frac12 d + d = \frac14 x + \frac12 d$.
$\frac12 g(x) + \frac12 x = \frac12 (-\frac12 x + d) + \frac12 x = -\frac14 x + \frac12 d + \frac12 x = \frac14 x + \frac12 d$.
LHS = RHS. So $g(x) = -\frac12 x + d$ for any $d \in \mathbb{R}$ is a family of solutions. These functions are linear and thus continuous.

Now, we need to determine if there are any other solutions.
Suppose $g(x) = g(y)$. Then applying $g$ to both sides, $g(g(x)) = g(g(y))$.
Using the given equation, $\frac12 g(x) + \frac12 x = \frac12 g(y) + \frac12 y$.
Since $g(x)=g(y)$, this simplifies to $\frac12 x = \frac12 y$, which implies $x=y$.
Therefore, $g$ must be injective.

Since $g: \mathbb{R} \rightarrow \mathbb{R}$ is continuous and injective, it must be strictly monotonic.
So $g$ is either strictly increasing or strictly decreasing.

Case A: $g$ is strictly increasing.
Suppose there exists $x_0 \in \mathbb{R}$ such that $g(x_0) \ne x_0$.
If $g(x_0) > x_0$, let $x_1 = g(x_0)$. Then $x_1 > x_0$.
The equation $P(x_0)$ is $g(g(x_0)) = \frac12 g(x_0) + \frac12 x_0$.
This can be written as $g(x_1) = \frac12 x_1 + \frac12 x_0$.
Since $x_1 > x_0$, we have $x_0 < \frac{x_1+x_0}{2} < x_1$.
So $x_0 < g(x_1) < x_1$.
Since $g$ is strictly increasing and $x_1 > x_0$, we must have $g(x_1) > g(x_0)$.
$g(x_1) > x_1$.
But we found $g(x_1) < x_1$. This is a contradiction.
So the assumption $g(x_0) > x_0$ must be false.

If $g(x_0) < x_0$, let $x_1 = g(x_0)$. Then $x_1 < x_0$.
The equation $P(x_0)$ gives $g(x_1) = \frac12 x_1 + \frac12 x_0$.
Since $x_1 < x_0$, we have $x_1 < \frac{x_1+x_0}{2} < x_0$.
So $x_1 < g(x_1) < x_0$.
Since $g$ is strictly increasing and $x_1 < x_0$, we must have $g(x_1) < g(x_0)$.
$g(x_1) < x_1$.
But we found $g(x_1) > x_1$. This is a contradiction.
So the assumption $g(x_0) < x_0$ must be false.

Combining these results, we must have $g(x_0) = x_0$ for all $x_0 \in \mathbb{R}$.
Therefore, if $g$ is strictly increasing, the only solution is $g(x) = x$.

Case B: $g$ is strictly decreasing.
Since $g$ is continuous and strictly decreasing, it must have a unique fixed point $x_0$. Let $h(x) = g(x)-x$. $h$ is continuous. As $x \to \infty$, $g(x) \to -\infty$ (otherwise if $g(x) \to L$, $g(g(x)) \to g(L)$ while $\frac12 g(x)+\frac12 x \to \infty$), so $h(x) \to -\infty$. As $x \to -\infty$, $g(x) \to \infty$ (similarly), so $h(x) \to \infty$. By IVT, there exists $x_0$ such that $h(x_0)=0$, i.e. $g(x_0)=x_0$. Since $h'(x) = g'(x)-1 < 0$, $h(x)$ is strictly decreasing, so the root $x_0$ is unique.

Let $x \in \mathbb{R}$. Define the sequence $a_n$ by $a_0 = x$ and $a_{n+1} = g(a_n)$ for $n \ge 0$.
So $a_1 = g(x)$, $a_2 = g(g(x))$, etc. $a_n = g^n(x)$.
The given equation is $a_2 = \frac12 a_1 + \frac12 a_0$.
Applying $g$ to this equation, $g(a_2) = g(\frac12 a_1 + \frac12 a_0)$.
Replacing $x$ with $a_n$ in the assertion $P(x)$, we get $g(g(a_n)) = \frac12 g(a_n) + \frac12 a_n$.
This means $a_{n+2} = \frac12 a_{n+1} + \frac12 a_n$ for all $n \ge 0$.
This is a linear homogeneous recurrence relation. The characteristic equation is $r^2 - \frac12 r - \frac12 = 0$, which is $2r^2 - r - 1 = 0$, or $(2r+1)(r-1)=0$.
The roots are $r_1 = 1$ and $r_2 = -1/2$.
The general solution is $a_n = C_1 (1)^n + C_2 (-1/2)^n = C_1 + C_2 (-1/2)^n$.

As $n \to \infty$, $(-1/2)^n \to 0$. So $\lim_{n\to\infty} a_n = C_1$.
Since $g$ is continuous, $\lim_{n\to\infty} a_{n+1} = g(\lim_{n\to\infty} a_n)$.
So $C_1 = g(C_1)$. This means $C_1$ is a fixed point of $g$.
Since $g$ is strictly decreasing, it has a unique fixed point $x_0$.
Therefore, $C_1 = x_0$.
The sequence $a_n$ must converge to $x_0$ for any starting point $x$.
So $a_n = x_0 + C_2 (-1/2)^n$.
To find $C_2$, we use the initial condition $a_0 = x$.
$x = a_0 = x_0 + C_2 (-1/2)^0 = x_0 + C_2$.
So $C_2 = x - x_0$.
The sequence is given by $a_n = x_0 + (x - x_0) (-1/2)^n$.

Now we use $a_1 = g(x)$.
$g(x) = a_1 = x_0 + (x - x_0) (-1/2)^1 = x_0 - \frac12 (x - x_0) = x_0 - \frac12 x + \frac12 x_0$.
$g(x) = \frac32 x_0 - \frac12 x$.
This is of the form $g(x) = -\frac12 x + d$, where $d = \frac32 x_0$.
For any $d \in \mathbb{R}$, the function $g(x) = -\frac12 x + d$ has a unique fixed point $x_0 = \frac23 d$.
Then $\frac32 x_0 = \frac32 (\frac23 d) = d$.
So any function of the form $g(x) = -\frac12 x + d$ is a possible solution, and we have already verified that they are indeed solutions.
These functions are strictly decreasing since their slope is $-1/2$.

Combining Case A and Case B, the solutions are $g(x)=x$ and $g(x) = -\frac12 x + d$ for any constant $d \in \mathbb{R}$.

Final verification:
1. $g(x)=x$: $g(g(x))=x$. $\frac12 g(x) + \frac12 x = \frac12 x + \frac12 x = x$. Matches. $g$ is continuous.
2. $g(x) = -\frac12 x + d$: $g(g(x)) = -\frac12(-\frac12 x + d) + d = \frac14 x - \frac12 d + d = \frac14 x + \frac12 d$. $\frac12 g(x) + \frac12 x = \frac12(-\frac12 x + d) + \frac12 x = -\frac14 x + \frac12 d + \frac12 x = \frac14 x + \frac12 d$. Matches. $g$ is continuous.

The solutions are $g(x)=x$ and $g(x) = -\frac12 x + d$ for any $d \in \mathbb{R}$.

The set of solutions is $\{g(x) = x\} \cup \{g(x) = -\frac12 x + d \mid d \in \mathbb{R}\}$.

Final Answer: The final answer is $\boxed{g(x)=x \text{ and } g(x)=-\frac12 x + d, d \in \mathbb{R}}$