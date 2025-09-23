Let the given equation be
$$ 6^{x^2} + 5^{x^2} - 10^{x^2} = 1 $$
We are looking for solutions $x \in \mathbb{R}$.
Let $y = x^2$. Since $x \in \mathbb{R}$, we must have $y \ge 0$.
Substituting $y = x^2$ into the equation gives
$$ 6^y + 5^y - 10^y = 1 $$
We need to find all non-negative real numbers $y$ that satisfy this equation.

Let's test some small non-negative integer values for $y$.
If $y = 0$, we have $6^0 + 5^0 - 10^0 = 1 + 1 - 1 = 1$. So $y=0$ is a solution.
If $y = 1$, we have $6^1 + 5^1 - 10^1 = 6 + 5 - 10 = 11 - 10 = 1$. So $y=1$ is a solution.
If $y = 2$, we have $6^2 + 5^2 - 10^2 = 36 + 25 - 100 = 61 - 100 = -39 \ne 1$.
If $y = 3$, we have $6^3 + 5^3 - 10^3 = 216 + 125 - 1000 = 341 - 1000 = -659 \ne 1$.

To determine if there are other solutions, let's analyze the function $f(y) = 6^y + 5^y - 10^y$ for $y \ge 0$. We are looking for the roots of $f(y) = 1$.

Consider the derivative of $f(y)$:
$$ f'(y) = \frac{d}{dy}(6^y + 5^y - 10^y) = (\ln 6) 6^y + (\ln 5) 5^y - (\ln 10) 10^y $$
Let's evaluate the derivative at $y=0$ and $y=1$.
$f'(0) = (\ln 6) 6^0 + (\ln 5) 5^0 - (\ln 10) 10^0 = \ln 6 + \ln 5 - \ln 10 = \ln(6 \cdot 5) - \ln 10 = \ln 30 - \ln 10 = \ln(30/10) = \ln 3$.
Since $\ln 3 > 0$, the function $f(y)$ is increasing at $y=0$.
$f'(1) = (\ln 6) 6^1 + (\ln 5) 5^1 - (\ln 10) 10^1 = 6 \ln 6 + 5 \ln 5 - 10 \ln 10$.
$f'(1) = \ln(6^6) + \ln(5^5) - \ln(10^{10}) = \ln\left(\frac{6^6 \cdot 5^5}{10^{10}}\right)$.
$6^6 \cdot 5^5 = (2 \cdot 3)^6 \cdot 5^5 = 2^6 \cdot 3^6 \cdot 5^5$.
$10^{10} = (2 \cdot 5)^{10} = 2^{10} \cdot 5^{10}$.
$\frac{6^6 \cdot 5^5}{10^{10}} = \frac{2^6 \cdot 3^6 \cdot 5^5}{2^{10} \cdot 5^{10}} = \frac{3^6}{2^4 \cdot 5^5} = \frac{729}{16 \cdot 3125} = \frac{729}{50000}$.
$f'(1) = \ln\left(\frac{729}{50000}\right)$. Since $\frac{729}{50000} < 1$, $f'(1) < 0$. The function $f(y)$ is decreasing at $y=1$.

Since $f'(0) > 0$ and $f'(1) < 0$, there must be a critical point $y_c \in (0, 1)$ where $f'(y_c)=0$. Let's examine the second derivative:
$$ f''(y) = \frac{d}{dy}(f'(y)) = (\ln 6)^2 6^y + (\ln 5)^2 5^y - (\ln 10)^2 10^y $$
Consider the sign of $f''(y)$. Let $k(y) = f''(y) / 10^y = (\ln 6)^2 (6/10)^y + (\ln 5)^2 (5/10)^y - (\ln 10)^2$.
$k(y) = (\ln 6)^2 (3/5)^y + (\ln 5)^2 (1/2)^y - (\ln 10)^2$.
The derivative of $k(y)$ is $k'(y) = (\ln 6)^2 \ln(3/5) (3/5)^y + (\ln 5)^2 \ln(1/2) (1/2)^y$.
Since $3/5 < 1$ and $1/2 < 1$, $\ln(3/5) < 0$ and $\ln(1/2) < 0$. Also $(\ln 6)^2 > 0$ and $(\ln 5)^2 > 0$.
Thus, $k'(y) < 0$ for all $y$. This means $k(y)$ is a strictly decreasing function.
A strictly decreasing function can cross zero at most once. So $f''(y)$ has at most one root.
$f''(0) = (\ln 6)^2 + (\ln 5)^2 - (\ln 10)^2 = (\ln 6)^2 + (\ln 5)^2 - (\ln 2 + \ln 5)^2 = (\ln 6)^2 - (\ln 2)^2 - 2 \ln 2 \ln 5 = (\ln(2\cdot 3))^2 - (\ln 2)^2 - 2 \ln 2 \ln 5 = (\ln 2 + \ln 3)^2 - (\ln 2)^2 - 2 \ln 2 \ln 5 = (\ln 2)^2 + 2 \ln 2 \ln 3 + (\ln 3)^2 - (\ln 2)^2 - 2 \ln 2 \ln 5 = 2 \ln 2 \ln 3 + (\ln 3)^2 - 2 \ln 2 \ln 5 = \ln 3 (2 \ln 2 + \ln 3) - 2 \ln 2 \ln 5 = \ln 3 \ln 12 - \ln 4 \ln 5$. Approximately, $f''(0) \approx (1.1)(2.5) - (1.4)(1.6) = 2.75 - 2.24 = 0.51 > 0$.
$f''(1) = (\ln 6)^2 6 + (\ln 5)^2 5 - (\ln 10)^2 10$. Approximately, $f''(1) \approx (1.79)^2 6 + (1.61)^2 5 - (2.30)^2 10 \approx (3.2) 6 + (2.6) 5 - (5.3) 10 = 19.2 + 13 - 53 = 32.2 - 53 = -20.8 < 0$.
Since $f''(0) > 0$ and $f''(1) < 0$, the unique root $y_0$ of $f''(y)$ lies in the interval $(0, 1)$.
$f(y)$ is convex on $[0, y_0)$ and concave on $(y_0, \infty)$.
$f'(y)$ increases on $[0, y_0)$ and decreases on $(y_0, \infty)$.
Since $f'(0) = \ln 3 > 0$ and $f'(1) < 0$, the unique root $y_c$ of $f'(y)$ must be in $(0, 1)$. In fact $y_c \in (y_0, 1)$.
$f(y)$ increases on $[0, y_c)$ and decreases on $(y_c, \infty)$.
$f(0)=1$. $f(y)$ increases to a maximum value $f(y_c) > 1$. Then $f(y)$ decreases. We know $f(1)=1$.
For $y > 1$, $f(y)$ continues to decrease.
As $y \to \infty$, $f(y) = 10^y((6/10)^y + (5/10)^y - 1) = 10^y((3/5)^y + (1/2)^y - 1)$.
Since $(3/5)^y \to 0$ and $(1/2)^y \to 0$ as $y \to \infty$, $f(y) \approx 10^y(0 + 0 - 1) = -10^y$.
So $f(y) \to -\infty$ as $y \to \infty$.
The function $f(y)$ starts at $f(0)=1$, increases to a maximum $f(y_c)>1$ for some $y_c \in (0,1)$, then decreases passing through $f(1)=1$, and tends to $-\infty$.
Therefore, the equation $f(y)=1$ has exactly two solutions for $y \ge 0$: $y=0$ and $y=1$.

We need to find $x$ such that $y = x^2$.
Case 1: $y=0$.
$x^2 = 0 \implies x=0$.
Case 2: $y=1$.
$x^2 = 1 \implies x = \pm 1$.

The real solutions for $x$ are $x=-1$, $x=0$, and $x=1$.

Alternative approach using Mean Value Theorem:
Rewrite the equation $6^y + 5^y - 10^y = 1$ as $10^y - 6^y = 5^y - 1$.
Check $y=0$: $10^0 - 6^0 = 1 - 1 = 0$. $5^0 - 1 = 1 - 1 = 0$. So $y=0$ is a solution.
Check $y=1$: $10^1 - 6^1 = 10 - 6 = 4$. $5^1 - 1 = 5 - 1 = 4$. So $y=1$ is a solution.
Assume $y > 0$ and $y \ne 1$.
Let $f(t) = t^y$. For $t>0$, $f$ is differentiable and $f'(t) = y t^{y-1}$.
By the Mean Value Theorem on the interval $[6, 10]$, there exists $\xi_1 \in (6, 10)$ such that
$$ \frac{f(10) - f(6)}{10 - 6} = f'(\xi_1) $$
$$ \frac{10^y - 6^y}{4} = y \xi_1^{y-1} \implies 10^y - 6^y = 4y \xi_1^{y-1} $$
By the Mean Value Theorem on the interval $[1, 5]$, there exists $\xi_2 \in (1, 5)$ such that
$$ \frac{f(5) - f(1)}{5 - 1} = f'(\xi_2) $$
$$ \frac{5^y - 1^y}{4} = y \xi_2^{y-1} \implies 5^y - 1 = 4y \xi_2^{y-1} $$
Substituting these into the equation $10^y - 6^y = 5^y - 1$:
$$ 4y \xi_1^{y-1} = 4y \xi_2^{y-1} $$
Since $y > 0$, we can divide by $4y$:
$$ \xi_1^{y-1} = \xi_2^{y-1} $$
Since $y \ne 1$, $y-1 \ne 0$. The function $t \mapsto t^{y-1}$ is strictly monotonic for $t > 0$.
Therefore, $\xi_1^{y-1} = \xi_2^{y-1}$ implies $\xi_1 = \xi_2$.
However, we have $\xi_1 \in (6, 10)$ and $\xi_2 \in (1, 5)$. These intervals are disjoint.
So it must be $\xi_1 > 6$ and $\xi_2 < 5$, which means $\xi_1 \ne \xi_2$.
This contradiction shows that there are no solutions for $y > 0$ and $y \ne 1$.
Thus, the only non-negative solutions for $y$ are $y=0$ and $y=1$.

Finally, we find the values of $x$ corresponding to these values of $y=x^2$.
If $y=0$, then $x^2=0$, which gives $x=0$.
If $y=1$, then $x^2=1$, which gives $x=1$ or $x=-1$.
The set of solutions for $x \in \mathbb{R}$ is $\{-1, 0, 1\}$.

Final Answer: The final answer is $\boxed{x \in \{-1, 0, 1\}}$