Let the given equation be
$$6^{x^2} + 5^{x^2} - 10^{x^2} = 1.$$
Let $y = x^2$. Since $x \in \mathbb{R}$, $x^2 \ge 0$, so $y \ge 0$. The equation becomes
$$6^y + 5^y - 10^y = 1.$$
We are looking for non-negative solutions $y$ to this equation.

Let's test some simple values for $y \ge 0$.
If $y=0$, the equation becomes $6^0 + 5^0 - 10^0 = 1 + 1 - 1 = 1$, which is true. So $y=0$ is a solution.
If $y=1$, the equation becomes $6^1 + 5^1 - 10^1 = 6 + 5 - 10 = 11 - 10 = 1$, which is true. So $y=1$ is a solution.

Since $y=x^2$, $y=0$ corresponds to $x^2=0$, which gives $x=0$.
$y=1$ corresponds to $x^2=1$, which gives $x=1$ or $x=-1$.
Thus, $x=0, 1, -1$ are solutions to the original equation.

To determine if there are any other solutions for $y \ge 0$, let's define a function $f(y) = 6^y + 5^y - 10^y - 1$ for $y \ge 0$. We want to find all $y \ge 0$ such that $f(y)=0$. We already found $y=0$ and $y=1$.

Let's analyze the behavior of $f(y)$ for $y \ge 0$. We can use calculus.
The first derivative is $f'(y) = 6^y \ln 6 + 5^y \ln 5 - 10^y \ln 10$.
Let's evaluate the derivative at $y=0$ and $y=1$.
$f'(0) = 6^0 \ln 6 + 5^0 \ln 5 - 10^0 \ln 10 = \ln 6 + \ln 5 - \ln 10 = \ln(6 \times 5) - \ln 10 = \ln 30 - \ln 10 = \ln(30/10) = \ln 3$.
Since $\ln 3 > 0$, $f'(0) > 0$. This means $f(y)$ is increasing at $y=0$.

$f'(1) = 6^1 \ln 6 + 5^1 \ln 5 - 10^1 \ln 10 = 6 \ln 6 + 5 \ln 5 - 10 \ln 10$.
$f'(1) = \ln(6^6) + \ln(5^5) - \ln(10^{10}) = \ln\left(\frac{6^6 5^5}{10^{10}}\right) = \ln\left(\frac{(2 \times 3)^6 \times 5^5}{(2 \times 5)^{10}}\right) = \ln\left(\frac{2^6 \times 3^6 \times 5^5}{2^{10} \times 5^{10}}\right) = \ln\left(\frac{3^6}{2^4 \times 5^5}\right)$.
$\frac{3^6}{2^4 \times 5^5} = \frac{729}{16 \times 3125} = \frac{729}{50000}$.
Since $729/50000 < 1$, $\ln(729/50000) < 0$. So $f'(1) < 0$. This means $f(y)$ is decreasing at $y=1$.

Since $f(y)$ is continuous for $y \ge 0$, and $f'(0) > 0$ and $f'(1) < 0$, by the Intermediate Value Theorem for derivatives, there must be at least one value $y_0 \in (0, 1)$ such that $f'(y_0) = 0$.

Let's examine the second derivative $f''(y) = 6^y (\ln 6)^2 + 5^y (\ln 5)^2 - 10^y (\ln 10)^2$.
$f''(y) = 10^y \left[ \left(\frac{6}{10}\right)^y (\ln 6)^2 + \left(\frac{5}{10}\right)^y (\ln 5)^2 - (\ln 10)^2 \right]$.
Let $m(y) = (0.6)^y (\ln 6)^2 + (0.5)^y (\ln 5)^2 - (\ln 10)^2$. The sign of $f''(y)$ is determined by $m(y)$.
$m(0) = (\ln 6)^2 + (\ln 5)^2 - (\ln 10)^2 \approx (1.79)^2 + (1.61)^2 - (2.30)^2 \approx 3.20 + 2.59 - 5.29 = 0.5 > 0$.
$m(1) = 0.6 (\ln 6)^2 + 0.5 (\ln 5)^2 - (\ln 10)^2 \approx 0.6(3.20) + 0.5(2.59) - 5.29 \approx 1.92 + 1.30 - 5.29 = 3.22 - 5.29 = -2.07 < 0$.
$m'(y) = (0.6)^y (\ln 0.6)(\ln 6)^2 + (0.5)^y (\ln 0.5)(\ln 5)^2$. Since $\ln 0.6 < 0$ and $\ln 0.5 < 0$, $m'(y) < 0$ for all $y$.
So $m(y)$ is a strictly decreasing function. Since $m(0)>0$ and $m(1)<0$, there is a unique $y_1 \in (0,1)$ such that $m(y_1)=0$.
$f''(y) > 0$ for $0 \le y < y_1$ and $f''(y) < 0$ for $y > y_1$.
This means $f'(y)$ is increasing for $0 \le y < y_1$ and decreasing for $y > y_1$.

We know $f'(0) = \ln 3 > 0$. $f'(y)$ increases from $f'(0)$ to a maximum at $y_1$, then decreases. Since $f'(1) < 0$, the unique root $y_0$ of $f'(y)=0$ must be in $(y_1, 1)$.
$f'(y) > 0$ for $0 \le y < y_0$ and $f'(y) < 0$ for $y > y_0$.
This implies that $f(y)$ is strictly increasing for $0 \le y \le y_0$ and strictly decreasing for $y \ge y_0$.
$f(0) = 0$. $f(y)$ increases from $0$ to a maximum at $y_0$. Since $y_0 > 0$, $f(y_0) > f(0) = 0$.
For $y > y_0$, $f(y)$ decreases. Since $y_0 < 1$, $f(y)$ decreases from $f(y_0)$ to $f(1)$. We know $f(1)=0$.
As $f(y)$ is strictly decreasing for $y \ge y_0$, and $f(1)=0$, for any $y > 1$, $f(y) < f(1) = 0$.
Also, since $f(y)$ is strictly increasing for $0 \le y \le y_0$ and $f(0)=0$, for any $y \in (0, y_0]$, $f(y) > 0$ (unless $y=0$).
For $y \in (y_0, 1)$, $f(y)$ is decreasing from $f(y_0)>0$ to $f(1)=0$. So $f(y) > 0$ for $y \in (y_0, 1)$.

Thus, $f(y)=0$ has only two non-negative solutions: $y=0$ and $y=1$.

These solutions are for $y = x^2$.
$x^2 = 0 \implies x = 0$.
$x^2 = 1 \implies x = 1$ or $x = -1$.

The set of all real numbers $x$ satisfying the equation is $\{-1, 0, 1\}$.

The final answer is $\boxed{\{-1, 0, 1\}}$.