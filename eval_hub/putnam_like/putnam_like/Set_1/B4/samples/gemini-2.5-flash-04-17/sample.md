Let the given integral be $I_n$:
$$I_n = \int_0^1 \frac{(1-\ln(1-x))^n}{n!} \, dx.$$

We perform a substitution to simplify the term $1-\ln(1-x)$. Let $y = 1-\ln(1-x)$.
When $x=0$, $y = 1-\ln(1) = 1-0 = 1$.
When $x \to 1^-$, $1-x \to 0^+$, $\ln(1-x) \to -\infty$, so $y \to 1-(-\infty) = +\infty$.
The range of integration for $y$ is $[1, \infty)$.

Now we express $x$ in terms of $y$:
$y-1 = -\ln(1-x)$
$\ln(1-x) = 1-y$
$1-x = e^{1-y}$
$x = 1 - e^{1-y}$.

Next, we find the differential $dx$ in terms of $dy$:
$dx = \frac{d}{dy}(1 - e^{1-y}) \, dy = -e^{1-y}(-1) \, dy = e^{1-y} \, dy$.

Substitute these into the integral $I_n$:
$$I_n = \int_1^\infty \frac{y^n}{n!} e^{1-y} \, dy.$$
We can factor out the constant $e$:
$$I_n = \frac{e}{n!} \int_1^\infty y^n e^{-y} \, dy.$$

The integral $\int_0^\infty y^n e^{-y} dy$ is the Gamma function $\Gamma(n+1)$, which for integer $n$ is equal to $n!$.
We can split the integral from $1$ to $\infty$ into the difference between the integral from $0$ to $\infty$ and the integral from $0$ to $1$:
$$ \int_1^\infty y^n e^{-y} \, dy = \int_0^\infty y^n e^{-y} \, dy - \int_0^1 y^n e^{-y} \, dy = n! - \int_0^1 y^n e^{-y} \, dy. $$
Substitute this back into the expression for $I_n$:
$$ I_n = \frac{e}{n!} \left( n! - \int_0^1 y^n e^{-y} \, dy \right) = e \left( 1 - \frac{1}{n!} \int_0^1 y^n e^{-y} \, dy \right). $$

Let $J_n = \int_0^1 y^n e^{-y} \, dy$. We need to find the limit of $I_n$ as $n \to \infty$, which requires finding the limit of $\frac{J_n}{n!}$ as $n \to \infty$.

For $y \in [0, 1]$, the exponential term $e^{-y}$ satisfies $e^{-1} \le e^{-y} \le e^0 = 1$.
Therefore, for $y \in [0, 1]$, we have $0 \le y^n e^{-y} \le y^n \cdot 1 = y^n$.
Integrating this inequality from 0 to 1:
$$ \int_0^1 0 \, dy \le \int_0^1 y^n e^{-y} \, dy \le \int_0^1 y^n \, dy. $$
$$ 0 \le J_n \le \left[ \frac{y^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}. $$
So, we have $0 \le J_n \le \frac{1}{n+1}$.

Now consider the term $\frac{J_n}{n!}$:
$$ 0 \le \frac{J_n}{n!} \le \frac{1}{(n+1)n!}. $$
As $n \to \infty$, the upper bound $\frac{1}{(n+1)n!} \to 0$.
By the Squeeze Theorem, $\lim_{n\to\infty} \frac{J_n}{n!} = 0$.

Now we can find the limit of $I_n$:
$$ \lim_{n\to\infty} I_n = \lim_{n\to\infty} e \left( 1 - \frac{J_n}{n!} \right). $$
Using the limit we found for $\frac{J_n}{n!}$:
$$ \lim_{n\to\infty} I_n = e (1 - 0) = e. $$

The final answer is $\boxed{e}$.