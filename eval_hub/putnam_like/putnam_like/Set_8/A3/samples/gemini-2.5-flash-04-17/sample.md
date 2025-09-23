Let $X$ be the set of sequences $(x_n)$ of positive real numbers such that $\sum_{n=0}^{\infty} x_n = c$ for a positive constant $c$. We want to find the set $Y = \left\{\sum_{n=0}^{\infty} x_n^3 : (x_n) \in X\right\}$.

Let $S = \sum_{n=0}^{\infty} x_n^3$. Since $x_n > 0$ for all $n$, $x_n^3 > 0$ for all $n$, and thus $S > 0$. So the infimum of $Y$ is non-negative.

Let's find the supremum of $Y$. For any $(x_n) \in X$, $x_n > 0$ and $\sum_{n=0}^{\infty} x_n = c$. This implies that $x_n < c$ for all $n$.
Since $x_n > 0$, we can write $x_n^3 = x_n \cdot x_n \cdot x_n$. Since $x_n < c$, we have $x_n^2 < c x_n$, so $x_n^3 < c x_n^2$. This is not helpful.
However, $x_n < c$ implies $x_n^3 = x_n \cdot x_n^2 < c^2 x_n$.
Summing over $n$:
$S = \sum_{n=0}^{\infty} x_n^3 < \sum_{n=0}^{\infty} c^2 x_n = c^2 \sum_{n=0}^{\infty} x_n = c^2 \cdot c = c^3$.
So, $S < c^3$ for all $(x_n) \in X$. The supremum of $Y$ is at most $c^3$.

Can $S$ be arbitrarily close to $c^3$?
Let $\delta \in (0, c)$. Consider sequences where $x_0 = c-\delta$ and $\sum_{n=1}^{\infty} x_n = \delta$. For $x_n$ to be positive for all $n$, we must have $c-\delta > 0$ (so $\delta < c$) and $x_n>0$ for $n \ge 1$ (so $\delta > 0$).
Let's choose $x_0 = c-\delta$ and $x_n = \delta \frac{1}{2^n}$ for $n \ge 1$.
Then $\sum_{n=0}^{\infty} x_n = (c-\delta) + \sum_{n=1}^{\infty} \delta \frac{1}{2^n} = c-\delta + \delta \frac{1/2}{1-1/2} = c-\delta+\delta = c$.
All $x_n > 0$ for $0 < \delta < c$. So these sequences are in $X$.
For these sequences, the sum of cubes is $S(\delta) = (c-\delta)^3 + \sum_{n=1}^{\infty} (\delta \frac{1}{2^n})^3 = (c-\delta)^3 + \delta^3 \sum_{n=1}^{\infty} (1/8)^n$.
The geometric series $\sum_{n=1}^{\infty} (1/8)^n = \frac{1/8}{1-1/8} = \frac{1/8}{7/8} = 1/7$.
So $S(\delta) = (c-\delta)^3 + \delta^3/7$ for $\delta \in (0, c)$.
As $\delta \to 0^+$, $S(\delta) \to (c-0)^3 + 0^3/7 = c^3$.
Since $S(\delta) < c^3$ for all $\delta \in (0,c)$, $c^3$ is not attained. But $S(\delta)$ can be arbitrarily close to $c^3$. So $\sup Y = c^3$.

Now let's find the infimum of $Y$. We know $S>0$. Can $S$ be arbitrarily close to 0?
Let $r \in (0,1)$. Consider the sequence $x_n = c(1-r)r^n$ for $n \ge 0$.
$\sum_{n=0}^{\infty} x_n = c(1-r) \sum_{n=0}^{\infty} r^n = c(1-r) \frac{1}{1-r} = c$.
Since $c>0$ and $r \in (0,1)$, $1-r>0$ and $r^n>0$, so $x_n>0$ for all $n$. These sequences are in $X$.
The sum of cubes is $S(r) = \sum_{n=0}^{\infty} (c(1-r)r^n)^3 = c^3(1-r)^3 \sum_{n=0}^{\infty} (r^3)^n = c^3(1-r)^3 \frac{1}{1-r^3}$.
$S(r) = c^3 \frac{(1-r)^3}{(1-r)(1+r+r^2)} = c^3 \frac{(1-r)^2}{1+r+r^2}$ for $r \in (0,1)$.
As $r \to 1^-$, $S(r) \to c^3 \frac{(1-1)^2}{1+1+1} = c^3 \frac{0}{3} = 0$.
Since $S(r) > 0$ for $r \in (0,1)$, 0 is not attained. But $S(r)$ can be arbitrarily close to 0. So $\inf Y = 0$.

The set $Y$ is a subset of $(0, c^3)$. We have shown that $0$ is the infimum and $c^3$ is the supremum, and these values are not included in $Y$. It remains to show that $Y$ is the entire interval $(0, c^3)$.

Let $S \in (0, c^3)$. We want to find $(x_n) \in X$ such that $\sum x_n^3 = S$.
Let $x_0 = a$ for some $a \in (0,c)$. Then $\sum_{n=1}^{\infty} x_n = c-a$. For $(x_n)_{n\ge 1}$ to be a sequence of positive numbers summing to $c-a$, $\sum_{n=1}^\infty x_n^3$ can take any value in $(0, (c-a)^3)$. This is the range for sum $c-a$. Let this value be $S'$.
Then $\sum_{n=0}^{\infty} x_n^3 = x_0^3 + \sum_{n=1}^{\infty} x_n^3 = a^3 + S'$.
So for a fixed $a \in (0,c)$, the possible values of $S$ are in the interval $(a^3, a^3+(c-a)^3)$.
The set $Y$ is the union of these intervals for $a \in (0,c)$:
$Y = \bigcup_{a \in (0,c)} (a^3, a^3+(c-a)^3)$.

Let $f(a) = a^3$ and $k(a) = a^3+(c-a)^3$. $a \in (0,c)$.
$f(a)$ ranges from $0$ to $c^3$. $k(a)$ ranges from $c^3$ down to $c^3/4$ (minimum at $a=c/2$) and back up to $c^3$. The range of $k(a)$ for $a \in (0,c)$ is $[c^3/4, c^3)$.

Let $S \in (0, c^3)$. We want to show that there exists $a \in (0,c)$ such that $a^3 < S < a^3+(c-a)^3$.
This is equivalent to $a < S^{1/3}$ and $S < k(a)$.

If $S \in (0, c^3/4]$. Let $a \in (0, c)$ be such that $a < S^{1/3}$. Such $a$ exists, e.g., $a = S^{1/3}/2$. Since $S \le c^3/4$, $S^{1/3} \le c/2^{1/3}$. $a \le c/2^{4/3} < c/2$. So $a \in (0, c/2) \subset (0,c)$.
For such $a$, $a^3 < S$. Also $k(a) \ge c^3/4$. Since $S \le c^3/4$, $S \le k(a)$.
If $S < c^3/4$, then $S < k(a)$ for all $a \in (0,c)$, since $k(a)$ minimum is $c^3/4$.
If $S = c^3/4$, we need $S < k(a)$, so $c^3/4 < a^3+(c-a)^3$. This holds for all $a \ne c/2$.
So for $S \in (0, c^3/4]$, we can choose $a \in (0, S^{1/3})$. Then $a^3 < S$. And $S \le c^3/4 \le k(a)$. So $a^3 < S \le k(a)$.
If $S < k(a)$, $S \in (a^3, k(a))$. If $S = k(a)$, $S$ is not in $(a^3, k(a))$.
$S=k(a)$ only occurs for $S \ge c^3/4$.
If $S=c^3/4$, $k(a)=c^3/4$ for $a=c/2$. We would need $a^3 < c^3/4$, so $(c/2)^3 < c^3/4$, $c^3/8 < c^3/4$, which is true.
So for $S=c^3/4$, we need $a< (c^3/4)^{1/3} = c/2^{1/3}$ and $c^3/4 \le k(a)$.
Choose $a=c/2$. $a^3=c^3/8$. $k(a)=c^3/4$. We need $c^3/8 < c^3/4 \le c^3/4$. The interval is $(c^3/8, c^3/4)$. $c^3/4$ is the endpoint.

Let $S \in (0, c^3)$. Consider the function $g(a) = a^3$. $g^{-1}(S) = S^{1/3}$.
Consider $h(a) = a^3+(c-a)^3$.
For any $S \in (0, c^3)$, we need to find $a \in (0,c)$ such that $a^3 < S < a^3+(c-a)^3$.
The left endpoints $a^3$ vary from $0$ to $c^3$. The right endpoints $a^3+(c-a)^3$ vary in $[c^3/4, c^3)$.
The union is $(0, c^3)$.
To be more rigorous: For any $S \in (0, c^3)$, we seek $a \in (0, c)$ such that $S \in (a^3, a^3+(c-a)^3)$.
This is $a < S^{1/3}$ and $S < a^3+(c-a)^3$.
Let $\delta_S = S^{1/3}$. We require $a \in (0, \delta_S)$ and $a^3+(c-a)^3 > S$.
If $S \in (0, c^3/4]$, $\delta_S \le c/2^{1/3}$. $k(a) \ge c^3/4 \ge S$. So any $a \in (0, \delta_S)$ works. This range for $a$ is non-empty.
If $S \in (c^3/4, c^3)$, $\delta_S > c/2^{1/3}$. We need $a \in (0, \delta_S)$ and $k(a)>S$.
$k(a)=S$ has two solutions $a_1, a_2$ with $0<a_1<c/2<a_2<c$. $k(a)>S$ for $a \in (0, a_1) \cup (a_2, c)$.
We need $a \in (0, \delta_S) \cap ((0, a_1) \cup (a_2, c))$.
$a_1<c/2 < c/2^{1/3} < \delta_S$. So $(0, a_1) \subset (0, \delta_S)$. $a \in (0, a_1)$ satisfies $a<\delta_S$ and $k(a)>S$.
So any $S \in (0, c^3/4]$ or $S \in (c^3/4, c^3)$ is in $Y$.

Thus, the set $Y$ is the interval $(0, c^3)$.

The final answer is $\boxed{(0, c^3)}$.