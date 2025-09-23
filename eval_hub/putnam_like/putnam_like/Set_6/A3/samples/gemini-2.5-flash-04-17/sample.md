Let $S_n(x) = \sum_{k=0}^{n} f^{(k)}(x)$. The given condition is
$$ \frac{S_n(b_n)}{S_n(a_n)} = \frac{e^{b_n}}{e^{a_n}} $$
This can be rewritten as $e^{a_n} S_n(b_n) = e^{b_n} S_n(a_n)$, which is equivalent to $e^{-b_n} S_n(b_n) = e^{-a_n} S_n(a_n)$.

Let $H_n(x) = e^{-x} S_n(x) = e^{-x} \sum_{k=0}^{n} f^{(k)}(x)$.
The given condition states that $H_n(a_n) = H_n(b_n)$.
Since $f \in C^\infty((-1,1), \mathbb{R})$, $f^{(k)}(x)$ exists for all $k \ge 0$. The function $H_n(x)$ is differentiable on $(-1,1)$ for each $n$.
By Rolle's Theorem, as $a_n < b_n$ and $H_n(a_n) = H_n(b_n)$, there exists $c_n \in (a_n, b_n)$ such that $H_n'(c_n) = 0$.

Let's compute the derivative of $H_n(x)$:
$$ H_n'(x) = \frac{d}{dx} \left( e^{-x} \sum_{k=0}^{n} f^{(k)}(x) \right) = -e^{-x} \sum_{k=0}^{n} f^{(k)}(x) + e^{-x} \sum_{k=0}^{n} f^{(k+1)}(x) $$
$$ H_n'(x) = e^{-x} \left( \sum_{k=1}^{n+1} f^{(k)}(x) - \sum_{k=0}^{n} f^{(k)}(x) \right) $$
$$ H_n'(x) = e^{-x} \left( (f^{(n+1)}(x) + \sum_{k=1}^{n} f^{(k)}(x)) - (f(x) + \sum_{k=1}^{n} f^{(k)}(x)) \right) $$
$$ H_n'(x) = e^{-x} (f^{(n+1)}(x) - f(x)) $$
Since $H_n'(c_n) = 0$ and $e^{-c_n} \neq 0$, we must have $f^{(n+1)}(c_n) - f(c_n) = 0$.
Thus, $f^{(n+1)}(c_n) = f(c_n)$ for some $c_n \in (a_n, b_n)$.

We are given that $\lim_{n \to \infty} a_n = c$ and $\lim_{n \to \infty} b_n = c$, where $c \in (-1,1)$.
Since $a_n < c_n < b_n$, by the Squeeze Theorem, we have $\lim_{n \to \infty} c_n = c$.

As $f \in C^\infty((-1,1), \mathbb{R})$, $f$ is continuous on $(-1,1)$. Since $c_n \to c$ and $c_n, c \in (-1,1)$ for sufficiently large $n$, we have $\lim_{n \to \infty} f(c_n) = f(c)$.
From the equality $f^{(n+1)}(c_n) = f(c_n)$, taking the limit as $n \to \infty$, we get:
$$ \lim_{n \to \infty} f^{(n+1)}(c_n) = \lim_{n \to \infty} f(c_n) = f(c) $$

The problem states that all derivatives of $f$ are uniformly bounded. This means there exists a constant $M > 0$ such that $|f^{(k)}(x)| \le M$ for all integers $k \ge 0$ and all $x \in (-1,1)$.

We want to relate $\lim_{n \to \infty} f^{(n+1)}(c_n)$ to $\lim_{n \to \infty} f^{(n)}(c)$.
Let's consider the difference $f^{(n+1)}(c_n) - f^{(n+1)}(c)$.
By the Mean Value Theorem applied to $f^{(n+1)}$ on the interval between $c_n$ and $c$, there exists a point $\xi_n$ between $c_n$ and $c$ such that:
$$ f^{(n+1)}(c_n) - f^{(n+1)}(c) = f^{(n+2)}(\xi_n) (c_n - c) $$
Since $c_n \to c$, for $n$ large enough, $c_n$ is arbitrarily close to $c$. As $c \in (-1,1)$, there exists a $\delta > 0$ such that $(c-\delta, c+\delta) \subset (-1,1)$. For $n$ large enough, $c_n \in (c-\delta, c+\delta)$, and the interval between $c_n$ and $c$ is also contained in $(c-\delta, c+\delta)$, which is a subset of $(-1,1)$.
By the uniform boundedness condition, $|f^{(n+2)}(x)| \le M$ for all $x \in (-1,1)$. Thus, $|f^{(n+2)}(\xi_n)| \le M$ for $n$ large enough.
So, we have:
$$ |f^{(n+1)}(c_n) - f^{(n+1)}(c)| = |f^{(n+2)}(\xi_n)| |c_n - c| \le M |c_n - c| $$
Since $\lim_{n \to \infty} c_n = c$, we have $\lim_{n \to \infty} |c_n - c| = 0$.
Therefore, $\lim_{n \to \infty} (f^{(n+1)}(c_n) - f^{(n+1)}(c)) = 0$.
This implies $\lim_{n \to \infty} f^{(n+1)}(c_n) = \lim_{n \to \infty} f^{(n+1)}(c)$.

Combining this result with $\lim_{n \to \infty} f^{(n+1)}(c_n) = f(c)$, we get:
$$ \lim_{n \to \infty} f^{(n+1)}(c) = f(c) $$
Let $m = n+1$. As $n \to \infty$, $m \to \infty$. The equation becomes:
$$ \lim_{m \to \infty} f^{(m)}(c) = f(c) $$
This is the desired result.

The final answer is $\boxed{\lim_{n \to \infty} f^{(n)}(c) = f(c)}$.