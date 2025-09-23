Let the given functional equation be
$$g(g(x)) = \frac{1}{2} g(x) + \frac{1}{2} x \quad (*)$$
for all $x \in \mathbb{R}$. The function $g: \mathbb{R} \rightarrow \mathbb{R}$ is continuous.

First, let's check for linear solutions $g(x) = ax+b$.
Substituting into $(*)$:
$a(ax+b)+b = \frac{1}{2}(ax+b) + \frac{1}{2}x$
$a^2x + ab + b = \frac{a}{2}x + \frac{b}{2} + \frac{1}{2}x$
$a^2x + ab + b = \left(\frac{a+1}{2}\right)x + \frac{b}{2}$
Comparing coefficients for $x$: $a^2 = \frac{a+1}{2} \implies 2a^2 - a - 1 = 0$. This quadratic equation factors as $(2a+1)(a-1)=0$, giving roots $a=1$ or $a=-\frac{1}{2}$.
Comparing constant terms: $ab+b = \frac{b}{2} \implies ab + \frac{b}{2} = 0 \implies b(a+\frac{1}{2})=0$.

Case 1: $a=1$. The second equation gives $b(1+\frac{1}{2})=0 \implies \frac{3}{2}b=0 \implies b=0$.
This gives the solution $g(x)=x$. Let's verify: $g(g(x))=g(x)=x$. $\frac12 g(x) + \frac12 x = \frac12 x + \frac12 x = x$. So $g(x)=x$ is a solution. It is continuous.

Case 2: $a=-\frac{1}{2}$. The second equation gives $b(-\frac{1}{2}+\frac{1}{2})=0 \implies b(0)=0$. This is true for any $b \in \mathbb{R}$.
This gives a family of solutions $g(x)=-\frac{1}{2}x+b$ for any $b \in \mathbb{R}$. Let's verify:
$g(g(x)) = g(-\frac{1}{2}x+b) = -\frac{1}{2}(-\frac{1}{2}x+b) + b = \frac{1}{4}x - \frac{b}{2} + b = \frac{1}{4}x + \frac{b}{2}$.
$\frac12 g(x) + \frac12 x = \frac12(-\frac{1}{2}x+b) + \frac12 x = -\frac{1}{4}x + \frac{b}{2} + \frac12 x = \frac{1}{4}x + \frac{b}{2}$.
Both sides are equal. So $g(x)=-\frac{1}{2}x+b$ for any $b \in \mathbb{R}$ is a solution. These functions are continuous.

Now we need to show that these are the only continuous solutions.
First, we show $g$ must be injective. Suppose $g(x_1)=g(x_2)$ for some $x_1, x_2$.
Then $g(g(x_1))=g(g(x_2))$. Using $(*)$, $\frac12 g(x_1)+\frac12 x_1 = \frac12 g(x_2)+\frac12 x_2$.
Since $g(x_1)=g(x_2)$, let $y=g(x_1)=g(x_2)$. $\frac12 y + \frac12 x_1 = \frac12 y + \frac12 x_2 \implies \frac12 x_1 = \frac12 x_2 \implies x_1=x_2$.
Thus, $g$ is injective. Since $g$ is continuous and injective on $\mathbb{R}$, it must be strictly monotone (either strictly increasing or strictly decreasing).

Case A: $g$ is strictly increasing.
If $g(x)=x$ for all $x$, it is strictly increasing and is a solution.
Suppose there exists $x_0$ such that $g(x_0) \ne x_0$.
If $g(x_0)>x_0$: Since $g$ is strictly increasing, $g(g(x_0)) > g(x_0)$.
From $(*)$, $g(g(x_0)) = \frac12 g(x_0) + \frac12 x_0$.
So $\frac12 g(x_0) + \frac12 x_0 > g(x_0) \implies \frac12 x_0 > \frac12 g(x_0) \implies x_0 > g(x_0)$. This contradicts $g(x_0)>x_0$.
If $g(x_0)<x_0$: Since $g$ is strictly increasing, $g(g(x_0)) < g(x_0)$.
From $(*)$, $\frac12 g(x_0) + \frac12 x_0 < g(x_0) \implies \frac12 x_0 < \frac12 g(x_0) \implies x_0 < g(x_0)$. This contradicts $g(x_0)<x_0$.
Both assumptions $g(x_0)>x_0$ and $g(x_0)<x_0$ lead to contradictions. Thus, if $g$ is strictly increasing, it must be $g(x)=x$ for all $x$.

Case B: $g$ is strictly decreasing.
A continuous strictly decreasing function $g: \mathbb{R} \to \mathbb{R}$ must have a unique fixed point $x_f$, i.e., $g(x_f)=x_f$. This is because $g(x)-x$ is continuous and strictly decreasing, so it must cross zero exactly once.
Let $x_f$ be the unique fixed point: $g(x_f)=x_f$.
The equation $(*)$ can be written as $g(g(x)) - g(x) = \frac12(x-g(x))$.
Let $x_0$ be any point in $\mathbb{R}$, and define the sequence $x_{n+1}=g(x_n)$ for $n \ge 0$.
For $n \ge 1$, $x_{n+1}=g(x_n)=g(g(x_{n-1})) = \frac12 g(x_{n-1}) + \frac12 x_{n-1} = \frac12 x_n + \frac12 x_{n-1}$.
This is a linear recurrence relation $x_{n+1} - \frac12 x_n - \frac12 x_{n-1} = 0$ for $n \ge 1$.
The characteristic equation is $r^2 - \frac12 r - \frac12 = 0$, which is $2r^2-r-1=0$, with roots $r_1=1$ and $r_2=-\frac12$.
The general solution is $x_n = c_1 (1)^n + c_2 (-\frac12)^n = c_1 + c_2 (-\frac12)^n$ for some constants $c_1, c_2$ determined by $x_0$ and $x_1=g(x_0)$.
$x_0 = c_1+c_2$
$x_1 = c_1 - \frac12 c_2 = g(x_0)$.
As $n \to \infty$, $x_n = c_1 + c_2 (-\frac12)^n \to c_1$.
Since $g$ is continuous, $g(\lim_{n\to\infty} x_n) = \lim_{n\to\infty} g(x_n) = \lim_{n\to\infty} x_{n+1}$.
$g(c_1)=c_1$. This means $c_1$ is a fixed point of $g$. Since $x_f$ is the unique fixed point, $c_1=x_f$.
So $x_n = x_f + c_2 (-\frac12)^n$.
Substitute this into the equations for $x_0$ and $x_1$:
$x_0 = x_f + c_2$
$x_1 = x_f - \frac12 c_2 = g(x_0)$.
From the first equation, $c_2 = x_0-x_f$.
So $g(x_0) = x_f - \frac12 (x_0-x_f) = x_f - \frac12 x_0 + \frac12 x_f = -\frac12 x_0 + \frac32 x_f$.
This holds for any $x_0 \in \mathbb{R}$. Let $x_0=x$. Then $g(x) = -\frac12 x + \frac32 x_f$.
This is a function of the form $g(x)=-\frac12 x + b$ with $b=\frac32 x_f$. For any $b \in \mathbb{R}$, $x_f=\frac23 b$ is a fixed point. So this is consistent.
The function $g(x) = -\frac12 x + \frac32 x_f$ is indeed strictly decreasing, which is consistent with this case.

The continuous function $g$ must be strictly monotone. If strictly increasing, $g(x)=x$. If strictly decreasing, $g(x)=-\frac12 x + \frac32 x_f$ where $x_f$ is its unique fixed point.

Let $b = \frac32 x_f$. Then $x_f=\frac23 b$. $g(x)=-\frac12 x+b$.
The set of solutions is $g(x)=x$ and $g(x)=-\frac12 x+b$ for any $b \in \mathbb{R}$.

Final check:
1. $g(x)=x$. Continuous. $g(g(x))=x$. $\frac12 g(x)+\frac12 x = \frac12 x + \frac12 x = x$. Yes.
2. $g(x)=-\frac12 x+b$. Continuous. $g(g(x)) = -\frac12(-\frac12 x+b)+b = \frac14 x-\frac b2+b = \frac14 x+\frac b2$. $\frac12 g(x)+\frac12 x = \frac12(-\frac12 x+b)+\frac12 x = -\frac14 x+\frac b2+\frac12 x = \frac14 x+\frac b2$. Yes.

Conclusion: The continuous functions satisfying the equation are $g(x)=x$ and $g(x)=-\frac12 x+b$ for any $b \in \mathbb{R}$.

The final answer is $\boxed{g(x) = x \text{ and } g(x) = -\frac12 x + b \text{ for any } b \in \mathbb{R}}$.