Solution:
Let $S_n(x) = \sum_{k=0}^n f^{(k)}(x)$. The given condition is
\[
\frac{S_n(b_n)}{S_n(a_n)} = \frac{e^{b_n}}{e^{a_n}}.
\]
This condition implies that $S_n(a_n)$ cannot be zero. If $S_n(a_n)=0$, then the left side is undefined. However, if we rewrite the condition as
\[
e^{-b_n} S_n(b_n) = e^{-a_n} S_n(a_n),
\]
this form is well-defined even if $S_n(a_n)=0$. If $S_n(a_n)=0$, then $e^{-a_n} S_n(a_n) = 0$, which implies $e^{-b_n} S_n(b_n) = 0$. Since $e^{-b_n} \ne 0$, this means $S_n(b_n) = 0$. So if $S_n(a_n)=0$, then $S_n(b_n)=0$, and the original equation should be interpreted as $0/0$, which is consistent with $e^{b_n}/e^{a_n}$ only if this ratio is indeterminate or if we interpret the cross-product equation $e^{a_n} S_n(b_n) = e^{b_n} S_n(a_n)$ which gives $0=0$. Let's proceed with the form $e^{-b_n} S_n(b_n) = e^{-a_n} S_n(a_n)$.

Let $h_n(x) = e^{-x} S_n(x) = e^{-x} \sum_{k=0}^n f^{(k)}(x)$. Since $f \in C^\infty((-1,1), \mathbb{R})$, each $f^{(k)}$ is infinitely differentiable. Thus, $S_n(x)$ is infinitely differentiable, and so is $h_n(x)$.
The condition $e^{-b_n} S_n(b_n) = e^{-a_n} S_n(a_n)$ can be written as $h_n(b_n) = h_n(a_n)$.

Since $h_n(x)$ is continuous on $[a_n, b_n]$ (or $[b_n, a_n]$ if $b_n < a_n$, but the problem states $a_n < b_n$) and differentiable on $(a_n, b_n)$, by Rolle's Theorem, there exists a point $x_n \in (a_n, b_n)$ such that $h_n'(x_n) = 0$.

Let's compute the derivative of $h_n(x)$:
\begin{align*} h_n'(x) &= \frac{d}{dx} \left( e^{-x} \sum_{k=0}^n f^{(k)}(x) \right) \\ &= -e^{-x} \sum_{k=0}^n f^{(k)}(x) + e^{-x} \sum_{k=0}^n f^{(k+1)}(x) \\ &= e^{-x} \left( \sum_{k=0}^n f^{(k+1)}(x) - \sum_{k=0}^n f^{(k)}(x) \right) \\ &= e^{-x} \left( (f'(x) + f''(x) + \cdots + f^{(n+1)}(x)) - (f(x) + f'(x) + \cdots + f^{(n)}(x)) \right) \\ &= e^{-x} (f^{(n+1)}(x) - f(x)). \end{align*}
The condition $h_n'(x_n) = 0$ implies $e^{-x_n} (f^{(n+1)}(x_n) - f(x_n)) = 0$.
Since $e^{-x_n} \ne 0$, we must have $f^{(n+1)}(x_n) = f(x_n)$.

This holds for every $n \in \mathbb{N}$. So for each $n \in \mathbb{N}$, there exists $x_n \in (a_n, b_n)$ such that $f^{(n+1)}(x_n) = f(x_n)$.

We are given that $\lim_{n \to \infty} a_n = c$ and $\lim_{n \to \infty} b_n = c$, where $c \in (-1,1)$.
Since $a_n < x_n < b_n$, by the Squeeze Theorem, we have $\lim_{n \to \infty} x_n = c$.

We want to show that $\lim_{n \to \infty} f^{(n)}(c) = f(c)$. Let's analyze the relation $f^{(n+1)}(x_n) = f(x_n)$.
We can write
\[ f^{(n+1)}(c) - f(c) = (f^{(n+1)}(c) - f^{(n+1)}(x_n)) + (f^{(n+1)}(x_n) - f(c)) \]
Using $f^{(n+1)}(x_n) = f(x_n)$, we get
\[ f^{(n+1)}(c) - f(c) = (f^{(n+1)}(c) - f^{(n+1)}(x_n)) + (f(x_n) - f(c)). \]
Let $y_n = f^{(n+1)}(x_n) - f^{(n+1)}(c)$ and $z_n = f(x_n) - f(c)$. Then
\[ f^{(n+1)}(c) - f(c) = -y_n + z_n. \]
We need to show that $y_n \to 0$ and $z_n \to 0$ as $n \to \infty$.

Since $f \in C^\infty$, the function $f$ is continuous. As $x_n \to c$, we have $f(x_n) \to f(c)$, so $z_n = f(x_n) - f(c) \to 0$ as $n \to \infty$.

For $y_n$, we use the Mean Value Theorem (MVT). Since $f \in C^\infty$, $f^{(n+1)}$ is differentiable. By MVT, there exists $\xi_n$ between $x_n$ and $c$ such that
\[ f^{(n+1)}(x_n) - f^{(n+1)}(c) = f^{(n+2)}(\xi_n) (x_n - c). \]
So $y_n = f^{(n+2)}(\xi_n) (x_n - c)$.

We are given that all derivatives of $f$ are uniformly bounded. This means there exists a constant $M > 0$ such that $|f^{(k)}(x)| \le M$ for all $k \ge 0$ and all $x \in (-1,1)$.
Since $x_n \in (a_n, b_n)$ and $a_n, b_n \to c$, $x_n \to c$. Since $c \in (-1,1)$, for sufficiently large $n$, $x_n$ is in $(-1,1)$. Also $\xi_n$ is between $x_n$ and $c$, so $\xi_n$ is also in $(-1,1)$ for sufficiently large $n$.
Therefore, $|f^{(n+2)}(\xi_n)| \le M$.

Now we can bound $|y_n|$:
\[ |y_n| = |f^{(n+2)}(\xi_n) (x_n - c)| = |f^{(n+2)}(\xi_n)| |x_n - c| \le M |x_n - c|. \]
Since $x_n \to c$, we have $|x_n - c| \to 0$ as $n \to \infty$.
Thus, $\lim_{n \to \infty} |y_n| = 0$, which implies $\lim_{n \to \infty} y_n = 0$.

Now we can conclude for the limit of $f^{(n+1)}(c) - f(c)$:
\[ \lim_{n \to \infty} (f^{(n+1)}(c) - f(c)) = \lim_{n \to \infty} (-y_n + z_n) = - \lim_{n \to \infty} y_n + \lim_{n \to \infty} z_n = -0 + 0 = 0. \]
This means $\lim_{n \to \infty} f^{(n+1)}(c) = f(c)$.

Let $k = n+1$. As $n \to \infty$, $k \to \infty$. The index $n$ runs over $\mathbb{N}$. If $\mathbb{N}=\{1, 2, 3, \dots\}$, then $k$ runs over $\{2, 3, 4, \dots\}$. If $\mathbb{N}=\{0, 1, 2, \dots\}$, then $k$ runs over $\{1, 2, 3, \dots\}$. In either case, this shows that the sequence $(f^{(k)}(c))_{k \ge 1 \text{ or } 2}$ converges to $f(c)$.
The statement $\lim_{n \to \infty} f^{(n)}(c) = f(c)$ means that for any $\epsilon > 0$, there exists $N$ such that for all $n > N$, $|f^{(n)}(c) - f(c)| < \epsilon$. Our result $\lim_{k \to \infty} f^{(k)}(c) = f(c)$ implies this statement.

Thus, we have shown that $\lim_{n \to \infty} f^{(n)}(c) = f(c)$.

Final check of the argument steps:
1. Define $h_n(x) = e^{-x} S_n(x)$. Condition $h_n(b_n) = h_n(a_n)$.
2. Rolle's Theorem implies existence of $x_n \in (a_n, b_n)$ with $h_n'(x_n)=0$.
3. $h_n'(x) = e^{-x} (f^{(n+1)}(x) - f(x))$. So $f^{(n+1)}(x_n) = f(x_n)$.
4. $a_n, b_n \to c$ implies $x_n \to c$.
5. $f^{(n+1)}(c) - f(c) = (f^{(n+1)}(c) - f^{(n+1)}(x_n)) + (f(x_n) - f(c))$.
6. Show $f(x_n) - f(c) \to 0$ using continuity of $f$.
7. Show $f^{(n+1)}(x_n) - f^{(n+1)}(c) \to 0$ using MVT and uniform boundedness of derivatives. $f^{(n+1)}(x_n) - f^{(n+1)}(c) = f^{(n+2)}(\xi_n)(x_n-c)$. $|f^{(n+2)}(\xi_n)| \le M$. Term goes to 0 as $x_n \to c$.
8. Conclude $\lim_{n \to \infty} (f^{(n+1)}(c) - f(c)) = 0$. This is equivalent to $\lim_{n \to \infty} f^{(n)}(c) = f(c)$.
All steps are verified.

Final Answer: The final answer is $\boxed{\lim_{n \to \infty} f^{(n)}(c) = f(c)}$