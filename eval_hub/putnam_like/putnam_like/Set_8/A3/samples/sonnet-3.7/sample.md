# Solution

I need to determine the set $Y = \left\{\sum_{n=0}^{\infty}x_n^3\;:\; (x_n)\in X\right\}$, where $X$ is the set of all sequences of positive real numbers $(x_n)$ such that $\sum_{n=0}^{\infty}x_n=c$.

## Finding the maximum value in $Y$

First, I'll determine the maximum possible value in $Y$. Consider a sequence where all the "mass" $c$ is concentrated at a single index, for example: $x_0 = c$ and $x_n = 0$ for all $n > 0$.

For this sequence, $\sum_{n=0}^{\infty}x_n^3 = c^3$.

This is the maximum possible value because by the convexity of $f(x) = x^3$ for $x > 0$ and using Jensen's inequality, we have:
$$\sum_{n=0}^{\infty}x_n^3 \leq c^3$$
with equality when all mass is concentrated at a single point.

## Finding the infimum of $Y$

Since all $x_n > 0$, we have $x_n^3 > 0$ for all $n$, so $\sum_{n=0}^{\infty}x_n^3 > 0$. Therefore, $0$ is a lower bound for $Y$.

To show that $\inf Y = 0$, consider a geometric distribution:
$$x_n = c(1-p)p^n \text{ for } n \geq 0$$
where $p \in (0,1)$.

This gives $\sum_{n=0}^{\infty}x_n = c(1-p)\sum_{n=0}^{\infty}p^n = c(1-p) \cdot \frac{1}{1-p} = c$, satisfying our constraint.

The sum of cubes is:
$$\sum_{n=0}^{\infty}x_n^3 = \sum_{n=0}^{\infty}(c(1-p)p^n)^3 = c^3(1-p)^3\sum_{n=0}^{\infty}p^{3n} = c^3(1-p)^3 \cdot \frac{1}{1-p^3}$$

As $p \rightarrow 1$, this sum approaches $0$. Therefore, $\inf Y = 0$, but $0 \notin Y$ since every sequence in $X$ has positive terms.

## Showing that $Y = (0,c^3]$

I've established that $\sup Y = c^3$ (and this is achieved) and $\inf Y = 0$ (but not achieved).

To show that every value in $(0,c^3]$ is in $Y$, I'll construct a specific family of sequences.

For any $t \in [0,1]$ and $p \in (0,1)$, define:
$$z_n(t) = t \cdot \begin{cases} c, & n=0 \\ 0, & n>0 \end{cases} + (1-t) \cdot c(1-p)p^n$$

This is a convex combination of the sequence that achieves $c^3$ and the geometric sequence that can make the sum of cubes arbitrarily small.

We can verify that $\sum_{n=0}^{\infty}z_n(t) = c$, and the sum of cubes is:
$$\sum_{n=0}^{\infty}z_n(t)^3 = c^3[t+(1-t)(1-p)]^3 + (1-t)^3c^3(1-p)^3\frac{p^3}{1-p^3}$$

When $t=1$, this sum equals $c^3$. When $t=0$, this sum equals $c^3(1-p)^3\frac{1}{1-p^3}$, which can be made arbitrarily close to $0$ as $p \rightarrow 1$.

By the intermediate value theorem, for any fixed $p$ close to $1$, as $t$ varies from $0$ to $1$, the sum of cubes takes all values in some interval $(\delta, c^3]$ where $\delta$ depends on $p$. As $p \rightarrow 1$, $\delta$ can be made arbitrarily close to $0$.

Therefore, $Y = (0,c^3]$.