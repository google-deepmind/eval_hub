Solution:
Let the given limit be
$$ L = \lim_{x\to\infty} \left( f(x) + \frac{f'(x)}{g'(x)} \right) = 0 $$
We are given that $f, g : (0,\infty) \rightarrow \mathbb{R}$ are differentiable functions and $g(x) \to \infty$ as $x \to \infty$. We want to show that $\lim_{x\to\infty} f(x) = 0$.

Let $h(x) = f(x) + \frac{f'(x)}{g'(x)}$. We are given $\lim_{x\to\infty} h(x) = 0$.
The existence of this limit implies that $h(x)$ must be defined for sufficiently large $x$, say for $x > M$ for some constant $M$. This requires that $g'(x) \neq 0$ for $x > M$.

Since $g$ is differentiable, its derivative $g'$ satisfies the Intermediate Value Property (Darboux's Theorem). As $g'(x) \neq 0$ for $x > M$, $g'(x)$ must have a constant sign on $(M, \infty)$. If $g'(x)$ were negative for $x > M$, then $g(x)$ would be decreasing for $x > M$. This contradicts the given condition $g(x) \to \infty$ as $x \to \infty$. Therefore, $g'(x)$ must be positive for $x > M$.

We want to determine the limit of $f(x)$ as $x \to \infty$. Consider the function $f(x)$ written as:
$$ f(x) = \frac{f(x)e^{g(x)}}{e^{g(x)}} $$
Let $F(x) = f(x)e^{g(x)}$ and $G(x) = e^{g(x)}$. Since $f$ and $g$ are differentiable, $F(x)$ and $G(x)$ are differentiable for $x > 0$.

We check the conditions for applying L'Hopital's Rule to the limit $\lim_{x\to\infty} \frac{F(x)}{G(x)}$.
1. $F(x)$ and $G(x)$ are differentiable on $(M, \infty)$.
2. $G(x) = e^{g(x)}$. Since $g(x) \to \infty$ as $x \to \infty$, we have $\lim_{x\to\infty} G(x) = \infty$.
3. $G'(x) = e^{g(x)}g'(x)$. Since $g'(x) > 0$ for $x > M$ and $e^{g(x)} > 0$, we have $G'(x) > 0$ for $x > M$. In particular, $G'(x) \neq 0$ for $x > M$.

Now we compute the limit of the ratio of the derivatives $\frac{F'(x)}{G'(x)}$:
$$ F'(x) = \frac{d}{dx} (f(x)e^{g(x)}) = f'(x)e^{g(x)} + f(x)e^{g(x)}g'(x) = e^{g(x)} (f'(x) + f(x)g'(x)) $$
$$ G'(x) = \frac{d}{dx} (e^{g(x)}) = e^{g(x)}g'(x) $$
The ratio is:
$$ \frac{F'(x)}{G'(x)} = \frac{e^{g(x)} (f'(x) + f(x)g'(x))}{e^{g(x)}g'(x)} = \frac{f'(x) + f(x)g'(x)}{g'(x)} = \frac{f'(x)}{g'(x)} + f(x) $$
This is precisely the expression $h(x)$ that we were given.
So, we have:
$$ \lim_{x\to\infty} \frac{F'(x)}{G'(x)} = \lim_{x\to\infty} h(x) = 0 $$

Since the conditions for L'Hopital's Rule (for the case $\frac{?}{\infty}$) are satisfied and the limit of the ratio of derivatives exists and is equal to 0, we can conclude that:
$$ \lim_{x\to\infty} \frac{F(x)}{G(x)} = \lim_{x\to\infty} \frac{F'(x)}{G'(x)} = 0 $$
Substituting back $f(x) = \frac{F(x)}{G(x)}$, we get:
$$ \lim_{x\to\infty} f(x) = 0 $$

Alternative approach using integration:
The condition $f(x) + \frac{f'(x)}{g'(x)} = h(x)$ can be rewritten as a linear first-order differential equation for $f(x)$:
$$ f'(x) + g'(x)f(x) = g'(x)h(x) $$
Multiply by the integrating factor $e^{\int g'(x)dx} = e^{g(x)}$ (we choose the constant of integration to be 0):
$$ e^{g(x)}f'(x) + g'(x)e^{g(x)}f(x) = g'(x)e^{g(x)}h(x) $$
The left side is the derivative of $f(x)e^{g(x)}$ with respect to $x$:
$$ \frac{d}{dx} \left( f(x)e^{g(x)} \right) = g'(x)e^{g(x)}h(x) $$
Integrate both sides from some large $M$ (where $g'(x)>0$) to $x$:
$$ f(x)e^{g(x)} - f(M)e^{g(M)} = \int_M^x g'(t)e^{g(t)}h(t) dt $$
$$ f(x)e^{g(x)} = f(M)e^{g(M)} + \int_M^x g'(t)e^{g(t)}h(t) dt $$
$$ f(x) = f(M)e^{g(M)-g(x)} + e^{-g(x)} \int_M^x g'(t)e^{g(t)}h(t) dt $$
We want to find the limit of $f(x)$ as $x \to \infty$.
For the first term, since $g(x) \to \infty$, $g(M)-g(x) \to -\infty$. Thus, $e^{g(M)-g(x)} \to 0$.
So, $\lim_{x\to\infty} f(M)e^{g(M)-g(x)} = 0$.
For the second term, we need to evaluate $\lim_{x\to\infty} \frac{\int_M^x g'(t)e^{g(t)}h(t) dt}{e^{g(x)}}$.
This limit has the indeterminate form $\frac{?}{\infty}$ since $e^{g(x)} \to \infty$. We can use L'Hopital's Rule.
Let $N(x) = \int_M^x g'(t)e^{g(t)}h(t) dt$ and $D(x) = e^{g(x)}$.
Then $N'(x) = g'(x)e^{g(x)}h(x)$ by the Fundamental Theorem of Calculus.
And $D'(x) = g'(x)e^{g(x)}$.
We need to evaluate $\lim_{x\to\infty} \frac{N'(x)}{D'(x)}$:
$$ \lim_{x\to\infty} \frac{g'(x)e^{g(x)}h(x)}{g'(x)e^{g(x)}} = \lim_{x\to\infty} h(x) = 0 $$
Since $D(x) \to \infty$, $D'(x) \neq 0$ for $x>M$, and the limit of the ratio of derivatives is 0, L'Hopital's Rule applies and gives:
$$ \lim_{x\to\infty} \frac{N(x)}{D(x)} = 0 $$
Therefore, the second term also tends to 0.
Combining the limits of both terms, we get:
$$ \lim_{x\to\infty} f(x) = 0 + 0 = 0 $$

Final Answer: The final answer is $\boxed{\lim_{x\to\infty} f(x) = 0}$