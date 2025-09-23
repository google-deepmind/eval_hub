Let $h(x) = f(x) + \frac{f'(x)}{g'(x)}$. We are given that $\lim_{x\to\infty} h(x) = 0$. We want to show that $\lim_{x\to\infty} f(x) = 0$.

Since $\lim_{x\to\infty} h(x) = 0$, there must exist $X_0 > 0$ such that $h(x)$ is defined for all $x > X_0$. The expression for $h(x)$ involves $f'(x)/g'(x)$, so $g'(x)$ must be non-zero for all $x > X_0$.
We are given that $g(x) \to \infty$ as $x \to \infty$. A function that tends to $\infty$ must be eventually monotonic. If $g(x)$ is eventually decreasing, it would tend to $-\infty$ or a finite limit. Thus, $g(x)$ must be eventually increasing. This implies that there exists $X_1$ such that $g'(x) \ge 0$ for all $x > X_1$. Since $g'(x)$ cannot be zero for $x > \max(X_0, X_1)$, we must have $g'(x) > 0$ for $x$ sufficiently large, say for $x > a$.

Consider the function $F(x) = f(x)e^{g(x)}$. Since $f$ and $g$ are differentiable, $F(x)$ is differentiable for $x \in (0, \infty)$.
The derivative of $F(x)$ is $F'(x) = f'(x)e^{g(x)} + f(x)g'(x)e^{g(x)}$.
For $x > a$, where $g'(x) > 0$, we can rewrite $F'(x)$ as:
$F'(x) = e^{g(x)} \left( f'(x) + f(x)g'(x) \right) = e^{g(x)} g'(x) \left( \frac{f'(x)}{g'(x)} + f(x) \right)$.
Using the definition of $h(x)$, we have $F'(x) = e^{g(x)} g'(x) h(x)$.

We want to evaluate $\lim_{x\to\infty} f(x)$. We can write $f(x) = \frac{f(x)e^{g(x)}}{e^{g(x)}} = \frac{F(x)}{e^{g(x)}}$.
Let $u(x) = F(x)$ and $v(x) = e^{g(x)}$. We want to find $\lim_{x\to\infty} \frac{u(x)}{v(x)}$.
We can apply L'Hopital's rule if the conditions are met.
1. $u(x)$ and $v(x)$ are differentiable for $x > a$. This is true since $f, g$ are differentiable for $x > 0$, and we chose $a > X_0, X_1$.
2. $v(x) = e^{g(x)} \to \infty$ as $x \to \infty$ because $g(x) \to \infty$.
3. $v'(x) = g'(x)e^{g(x)}$. As shown, $g'(x) > 0$ for $x > a$, so $v'(x) \ne 0$ for $x > a$.
4. We need to evaluate the limit of the ratio of the derivatives, $\lim_{x\to\infty} \frac{u'(x)}{v'(x)}$.
$\frac{u'(x)}{v'(x)} = \frac{F'(x)}{(e^{g(x)})'} = \frac{h(x)g'(x)e^{g(x)}}{g'(x)e^{g(x)}}$.
For $x > a$, $g'(x)e^{g(x)} \ne 0$, so we can cancel the term $g'(x)e^{g(x)}$:
$\frac{u'(x)}{v'(x)} = h(x)$ for $x > a$.

We are given that $\lim_{x\to\infty} h(x) = 0$.
So, $\lim_{x\to\infty} \frac{u'(x)}{v'(x)} = \lim_{x\to\infty} h(x) = 0$.

Since $\lim_{x\to\infty} \frac{u'(x)}{v'(x)}$ exists and is equal to 0, and $v(x) \to \infty$ as $x \to \infty$, L'Hopital's rule states that $\lim_{x\to\infty} \frac{u(x)}{v(x)}$ exists and is equal to this limit.
$\lim_{x\to\infty} \frac{F(x)}{e^{g(x)}} = 0$.
Substituting back $F(x) = f(x)e^{g(x)}$:
$\lim_{x\to\infty} \frac{f(x)e^{g(x)}}{e^{g(x)}} = \lim_{x\to\infty} f(x) = 0$.

Thus, we have shown that if $\lim_{x\to\infty} (f(x) + f'(x)/g'(x)) = 0$ and $g(x) \to \infty$, then $\lim_{x\to\infty} f(x) = 0$.

The final answer is $\boxed{\lim_{x\to\infty} f(x) = 0}$.