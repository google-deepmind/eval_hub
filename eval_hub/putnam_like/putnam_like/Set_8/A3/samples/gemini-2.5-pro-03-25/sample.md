Let $X$ be the set of all sequences $(x_n)_{n=0}^{\infty}$ of positive real numbers such that $\sum_{n=0}^{\infty} x_n = c$, where $c$ is a positive constant. We want to describe the set $Y = \left\{ \sum_{n=0}^{\infty} x_n^3 : (x_n) \in X \right\}$. Let $Q = \sum_{n=0}^{\infty} x_n^3$.

First, let's establish bounds for $Q$.
Since $x_n > 0$ for all $n$, we have $x_n^3 > 0$ for all $n$. Thus $Q = \sum_{n=0}^{\infty} x_n^3 > 0$. The sum must be strictly positive because if $Q=0$, then $x_n=0$ for all $n$, which contradicts $\sum x_n = c > 0$. So $0$ is a lower bound for $Y$.

Now consider the upper bound. We know that $c = \sum_{n=0}^{\infty} x_n$. Let's cube this sum:
\[
c^3 = \left(\sum_{n=0}^{\infty} x_n\right)^3 = \sum_{n=0}^{\infty} x_n^3 + 3 \sum_{i \ne j} x_i^2 x_j + 6 \sum_{i<j<k} x_i x_j x_k
\]
Let $Q = \sum_{n=0}^{\infty} x_n^3$. The remaining terms are $R = 3 \sum_{i \ne j} x_i^2 x_j + 6 \sum_{i<j<k} x_i x_j x_k$.
Since $x_n > 0$ for all $n \ge 0$, all the terms $x_i^2 x_j$ and $x_i x_j x_k$ are positive.
The condition $\sum x_n = c$ implies that there are infinitely many terms $x_n > 0$. If there were only a finite number of non-zero terms, say $x_0, \dots, x_{N-1}$, then we could not state $x_n > 0$ for all $n \ge 0$. Since $x_n > 0$ for all $n$, there exists at least two distinct indices $i, j$ such that $x_i > 0$ and $x_j > 0$. Then $x_i^2 x_j > 0$.
The sum $R$ contains positive terms. For example, $x_0^2 x_1 > 0$. Thus $R > 0$.
Since $c^3 = Q + R$ and $R > 0$, we must have $Q < c^3$.
So $c^3$ is an upper bound for $Y$.

We have established that $Y \subseteq (0, c^3)$. Now we need to determine if $Y$ is equal to this interval. We check if the bounds $0$ and $c^3$ can be approached arbitrarily closely.

Supremum: Let's show that $\sup Y = c^3$.
Consider a sequence $(x_n)$ defined as follows: Let $\epsilon$ be a small positive number ($0 < \epsilon < c$). Let $x_0 = c - \epsilon$. To satisfy $\sum x_n = c$, we need $\sum_{n=1}^{\infty} x_n = \epsilon$. Let's distribute this sum $\epsilon$ among infinitely many positive terms.
Choose $q \in (0, 1)$ and set $x_n = \epsilon (1-q) q^{n-1}$ for $n \ge 1$. All $x_n > 0$ for $n \ge 1$.
The sum is $\sum_{n=1}^{\infty} x_n = \epsilon(1-q) \sum_{n=1}^{\infty} q^{n-1} = \epsilon(1-q) \sum_{k=0}^{\infty} q^k = \epsilon(1-q) \frac{1}{1-q} = \epsilon$.
The sequence $(x_n) = (c-\epsilon, \epsilon(1-q), \epsilon(1-q)q, \dots)$ is in $X$.
Now compute $Q = \sum_{n=0}^{\infty} x_n^3$.
\[
Q = x_0^3 + \sum_{n=1}^{\infty} x_n^3 = (c-\epsilon)^3 + \sum_{n=1}^{\infty} (\epsilon(1-q)q^{n-1})^3
\]
\[
Q = (c-\epsilon)^3 + \epsilon^3 (1-q)^3 \sum_{n=1}^{\infty} (q^3)^{n-1} = (c-\epsilon)^3 + \epsilon^3 (1-q)^3 \sum_{k=0}^{\infty} (q^3)^k
\]
\[
Q = (c-\epsilon)^3 + \epsilon^3 (1-q)^3 \frac{1}{1-q^3} = (c-\epsilon)^3 + \epsilon^3 \frac{(1-q)^3}{(1-q)(1+q+q^2)}
\]
\[
Q = (c-\epsilon)^3 + \epsilon^3 \frac{(1-q)^2}{1+q+q^2}
\]
Let $f(q) = \frac{(1-q)^2}{1+q+q^2}$. As shown earlier, $f(q)$ maps $(0, 1)$ to $(0, 1)$.
Let $\delta > 0$. We want to show that we can find a sequence $(x_n) \in X$ such that $Q > c^3 - \delta$.
Choose $\epsilon > 0$ small enough such that $(c-\epsilon)^3 > c^3 - \delta$. This is possible since $\lim_{\epsilon \to 0^+} (c-\epsilon)^3 = c^3$. Specifically, we need $c^3 - (c-\epsilon)^3 < \delta$. $c^3 - (c^3 - 3c^2\epsilon + 3c\epsilon^2 - \epsilon^3) = 3c^2\epsilon - 3c\epsilon^2 + \epsilon^3 < \delta$. This inequality holds for sufficiently small $\epsilon > 0$. For example, choose $\epsilon < \frac{\delta}{4c^2}$ and $\epsilon < c$. Then $3c^2\epsilon < \frac{3\delta}{4}$. The term $3c\epsilon^2 - \epsilon^3$ is positive for $\epsilon < 3c$ and small relative to $3c^2\epsilon$.
$Q = (c-\epsilon)^3 + \epsilon^3 f(q)$. Since $\epsilon^3 f(q) > 0$, we have $Q > (c-\epsilon)^3$.
If we choose $\epsilon$ small enough such that $(c-\epsilon)^3 > c^3 - \delta$, then $Q > c^3 - \delta$.
Thus, we can make $Q$ arbitrarily close to $c^3$. So $\sup Y = c^3$. Since $Q < c^3$, the supremum is not attained.

Infimum: Let's show that $\inf Y = 0$.
Consider a sequence $(x_n)$ constructed as follows: Let $N \ge 1$ be an integer. Let $\epsilon$ be a small positive number ($0 < \epsilon < c$).
Let $x_n = \frac{c-\epsilon}{N}$ for $n = 0, 1, \dots, N-1$.
Let $x_n = \epsilon (1-q) q^{n-N}$ for $n \ge N$, where $q \in (0, 1)$.
The sum is $\sum_{n=0}^{N-1} x_n + \sum_{n=N}^{\infty} x_n = N \left(\frac{c-\epsilon}{N}\right) + \epsilon (1-q) \sum_{k=0}^{\infty} q^k = (c-\epsilon) + \epsilon = c$.
All $x_n > 0$. So this sequence is in $X$.
Now compute $Q = \sum_{n=0}^{\infty} x_n^3$.
\[
Q = \sum_{n=0}^{N-1} \left(\frac{c-\epsilon}{N}\right)^3 + \sum_{n=N}^{\infty} (\epsilon (1-q) q^{n-N})^3
\]
\[
Q = N \frac{(c-\epsilon)^3}{N^3} + \epsilon^3 (1-q)^3 \sum_{k=0}^{\infty} (q^3)^k
\]
\[
Q = \frac{(c-\epsilon)^3}{N^2} + \epsilon^3 \frac{(1-q)^2}{1+q+q^2} = \frac{(c-\epsilon)^3}{N^2} + \epsilon^3 f(q)
\]
Let $\delta > 0$. We want to show we can find a sequence $(x_n) \in X$ such that $Q < \delta$.
Let's fix $\epsilon = c/2$. Then $c-\epsilon = c/2$.
$Q = \frac{(c/2)^3}{N^2} + (c/2)^3 f(q)$.
We can make $f(q)$ arbitrarily small by choosing $q$ close to 1. Choose $q \in (0, 1)$ such that $f(q) < \frac{\delta}{2(c/2)^3} = \frac{4\delta}{c^3}$.
Then $(c/2)^3 f(q) < \delta/2$.
We can make $\frac{(c/2)^3}{N^2}$ arbitrarily small by choosing $N$ large. Choose $N$ large enough such that $\frac{(c/2)^3}{N^2} < \delta/2$. Specifically, $N^2 > \frac{(c/2)^3}{\delta/2} = \frac{c^3}{4\delta}$, so $N > \frac{c^{3/2}}{2\sqrt{\delta}}$.
With these choices of $q$ and $N$, we have $Q < \delta/2 + \delta/2 = \delta$.
Thus, we can make $Q$ arbitrarily close to 0. So $\inf Y = 0$. Since $Q > 0$, the infimum is not attained.

Continuity: To show that $Y$ is the entire interval $(0, c^3)$, we can show that $Y$ is an interval. Let $Q_1, Q_2 \in Y$. Then there exist sequences $(a_n), (b_n) \in X$ such that $\sum a_n^3 = Q_1$ and $\sum b_n^3 = Q_2$.
Consider the family of sequences $(x_n(t))$ defined by $x_n(t) = (1-t)a_n + t b_n$ for $t \in [0, 1]$.
Then $\sum_{n=0}^{\infty} x_n(t) = \sum ((1-t)a_n + t b_n) = (1-t)\sum a_n + t \sum b_n = (1-t)c + tc = c$.
Since $a_n, b_n > 0$ and $t \in [0, 1]$, we have $x_n(t) > 0$ (unless $t=0$ and $a_n=0$ or $t=1$ and $b_n=0$, but $a_n, b_n > 0$). So $(x_n(t)) \in X$ for all $t \in [0, 1]$.
Let $Q(t) = \sum_{n=0}^{\infty} x_n(t)^3 = \sum_{n=0}^{\infty} ((1-t)a_n + t b_n)^3$.
$Q(0) = \sum a_n^3 = Q_1$ and $Q(1) = \sum b_n^3 = Q_2$.
The function $x_n(t)^3$ is continuous in $t$. The series $\sum x_n(t)^3$ converges uniformly for $t \in [0, 1]$ by the Weierstrass M-test, since $x_n(t) \le \max(a_n, b_n)$ implies $x_n(t)^3 \le \max(a_n^3, b_n^3) \le a_n^3 + b_n^3$, and $\sum (a_n^3 + b_n^3) = Q_1 + Q_2$ converges.
Therefore, $Q(t)$ is a continuous function on $[0, 1]$. By the Intermediate Value Theorem, $Q(t)$ takes all values between $Q_1$ and $Q_2$.
This shows that $Y$ is an interval.

Conclusion: We have shown that $Y$ is an interval, $\inf Y = 0$ and $\sup Y = c^3$. Since the infimum and supremum are not attained, the set $Y$ is the open interval $(0, c^3)$.

Final Answer: The final answer is $\boxed{(0, c^3)}$