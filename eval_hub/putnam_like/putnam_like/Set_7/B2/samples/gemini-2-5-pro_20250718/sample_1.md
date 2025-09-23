Here is a detailed, step-by-step solution to the problem.

### 1. Understanding the Problem

We are asked to find the supremum of the ratio of the $L^1$-norm to the $L^2$-norm of a function $f$, where $f$ belongs to a specific set of functions $\mathcal{F}$.

Let's define the norms for a function $f$ on the interval $[0,1]$:
- The $L^1$-norm is $\|f\|_1 = \int_{0}^{1} |f(x)| \, dx$.
- The $L^2$-norm is $\|f\|_2 = \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}$.

The set of functions is:
$$
\mathcal{F} = \left\{ f \in \mathcal{C}\left( [0,1]; \mathbb{R} \right) \ : \ f(0) = 0 \right\}.
$$
This is the set of all real-valued continuous functions on the interval $[0,1]$ that are zero at $x=0$. We are looking for:
$$
\sup_{f \in \mathcal{F}, f \not\equiv 0} \frac{\|f\|_1}{\|f\|_2}.
$$
We exclude the zero function $f(x) \equiv 0$ for which the ratio would be $0/0$.

The solution will proceed in two main steps:
1.  Find an upper bound for the expression.
2.  Show that this upper bound is the least upper bound (supremum) by constructing a sequence of functions in $\mathcal{F}$ whose corresponding ratio approaches this bound.

### 2. Finding an Upper Bound

We can use the Cauchy-Schwarz inequality for integrals. For any two square-integrable functions $g(x)$ and $h(x)$ on $[0,1]$, the inequality states:
$$
\left( \int_0^1 g(x) h(x) \, dx \right)^2 \le \left( \int_0^1 g(x)^2 \, dx \right) \left( \int_0^1 h(x)^2 \, dx \right).
$$

Let's apply this to our expression. For any $f \in \mathcal{F}$, the function $|f(x)|$ is continuous and hence square-integrable on $[0,1]$. Let's choose $g(x) = |f(x)|$ and $h(x) = 1$. The function $h(x)=1$ is also square-integrable on $[0,1]$.

Substituting these into the Cauchy-Schwarz inequality:
$$
\left( \int_0^1 |f(x)| \cdot 1 \, dx \right)^2 \le \left( \int_0^1 |f(x)|^2 \, dx \right) \left( \int_0^1 1^2 \, dx \right).
$$

Let's evaluate the terms:
- The left side is $(\|f\|_1)^2$.
- The first term on the right side is $(\|f\|_2)^2$.
- The second term on the right side is $\int_0^1 1 \, dx = [x]_0^1 = 1$.

So the inequality becomes:
$$
(\|f\|_1)^2 \le (\|f\|_2)^2 \cdot 1.
$$

Since norms are non-negative, we can take the square root of both sides:
$$
\|f\|_1 \le \|f\|_2.
$$

For any non-zero function $f \in \mathcal{F}$, we have $\|f\|_2 > 0$, so we can divide by $\|f\|_2$:
$$
\frac{\|f\|_1}{\|f\|_2} \le 1.
$$

This shows that 1 is an upper bound for the ratio for any function in $\mathcal{F}$. Therefore, the supremum must be less than or equal to 1:
$$
\sup_{f \in \mathcal{F}} \frac{\|f\|_1}{\|f\|_2} \le 1.
$$

Note that the condition $f(0)=0$ was not used to establish this upper bound. This bound holds for any function in $\mathcal{C}([0,1])$. The condition $f(0)=0$ will be crucial in determining whether this supremum is attained.

### 3. Constructing a Sequence to Approach the Upper Bound

Now we need to show that this upper bound of 1 is the least upper bound. We can do this by finding a sequence of functions $(f_n)_{n \in \mathbb{N}}$ in $\mathcal{F}$ such that the ratio $\frac{\|f_n\|_1}{\|f_n\|_2}$ gets arbitrarily close to 1.

Let's consider a sequence of functions $(f_n)$ that are zero at $x=0$, rise quickly to 1, and then stay at 1. A simple choice for such a function is a "ramp" function. For each integer $n \ge 2$, define $f_n: [0,1] \to \mathbb{R}$ as:
$$
f_n(x) = \begin{cases}
nx & \text{if } 0 \le x < 1/n \\
1 & \text{if } 1/n \le x \le 1
\end{cases}
$$

Let's verify that $f_n \in \mathcal{F}$:
- **Continuity:** The function is linear on $[0, 1/n)$ and constant on $[1/n, 1]$. We only need to check continuity at $x=1/n$.
  - $\lim_{x \to (1/n)^-} f_n(x) = \lim_{x \to (1/n)^-} nx = n(1/n) = 1$.
  - $f_n(1/n) = 1$.
  - Since the left-hand limit equals the function value, $f_n$ is continuous on $[0,1]$.
- **Condition at 0:** $f_n(0) = n \cdot 0 = 0$.
So, $f_n \in \mathcal{F}$ for every $n \ge 2$. Also, since $f_n(x) \ge 0$ for all $x \in [0,1]$, we have $|f_n(x)| = f_n(x)$.

Now, let's calculate the norms for $f_n$:

**Numerator: $\|f_n\|_1$**
$$
\begin{aligned}
\|f_n\|_1 &= \int_0^1 f_n(x) \, dx = \int_0^{1/n} nx \, dx + \int_{1/n}^1 1 \, dx \\
&= n \left[ \frac{x^2}{2} \right]_0^{1/n} + [x]_{1/n}^1 \\
&= n \left( \frac{(1/n)^2}{2} - 0 \right) + \left( 1 - \frac{1}{n} \right) \\
&= n \frac{1}{2n^2} + 1 - \frac{1}{n} \\
&= \frac{1}{2n} + 1 - \frac{1}{n} \\
&= 1 - \frac{1}{2n}.
\end{aligned}
$$

**Denominator: $(\|f_n\|_2)^2$**
$$
\begin{aligned}
\|f_n\|_2^2 &= \int_0^1 (f_n(x))^2 \, dx = \int_0^{1/n} (nx)^2 \, dx + \int_{1/n}^1 1^2 \, dx \\
&= \int_0^{1/n} n^2x^2 \, dx + \int_{1/n}^1 1 \, dx \\
&= n^2 \left[ \frac{x^3}{3} \right]_0^{1/n} + [x]_{1/n}^1 \\
&= n^2 \left( \frac{(1/n)^3}{3} - 0 \right) + \left( 1 - \frac{1}{n} \right) \\
&= n^2 \frac{1}{3n^3} + 1 - \frac{1}{n} \\
&= \frac{1}{3n} + 1 - \frac{1}{n} \\
&= 1 - \frac{2}{3n}.
\end{aligned}
$$
So, $\|f_n\|_2 = \sqrt{1 - \frac{2}{3n}}$.

**The Ratio**
Now we compute the ratio for $f_n$:
$$
\frac{\|f_n\|_1}{\|f_n\|_2} = \frac{1 - \frac{1}{2n}}{\sqrt{1 - \frac{2}{3n}}}.
$$

Finally, we take the limit as $n \to \infty$:
$$
\lim_{n \to \infty} \frac{\|f_n\|_1}{\|f_n\|_2} = \lim_{n \to \infty} \frac{1 - \frac{1}{2n}}{\sqrt{1 - \frac{2}{3n}}} = \frac{1 - 0}{\sqrt{1 - 0}} = 1.
$$

We have constructed a sequence of functions $(f_n)$ in $\mathcal{F}$ such that the value of the ratio approaches 1. This implies that the supremum must be at least 1:
$$
\sup_{f \in \mathcal{F}} \frac{\|f\|_1}{\|f\|_2} \ge 1.
$$

### 4. Conclusion

From our two findings:
1.  $\sup_{f \in \mathcal{F}} \frac{\|f\|_1}{\|f\|_2} \le 1$
2.  $\sup_{f \in \mathcal{F}} \frac{\|f\|_1}{\|f\|_2} \ge 1$

We can conclude that the supremum is exactly 1.
$$
\sup_{f \in \mathcal{F}} \frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}} = 1.
$$

### Addendum: Is the Supremum a Maximum?

A supremum is a maximum if it is attained by some element in the set. Let's check if there exists a function $f \in \mathcal{F}$ for which the ratio is exactly 1.
Equality in the Cauchy-Schwarz inequality $\left( \int_0^1 g(x) h(x) \, dx \right)^2 \le \left( \int_0^1 g(x)^2 \, dx \right) \left( \int_0^1 h(x)^2 \, dx \right)$ holds if and only if $g(x)$ is proportional to $h(x)$, i.e., $g(x) = c \cdot h(x)$ for some constant $c$.

In our case, $g(x) = |f(x)|$ and $h(x)=1$. Thus, for the ratio to be 1, we must have:
$$|f(x)| = c \cdot 1 = c$$
for some non-negative constant $c$. For the ratio to be defined and non-zero, we need $f$ not to be the zero function, so $c>0$.

The condition $|f(x)| = c > 0$ for a continuous function $f$ implies that either $f(x)=c$ for all $x \in [0,1]$ or $f(x)=-c$ for all $x \in [0,1]$.
However, for $f$ to be in $\mathcal{F}$, it must satisfy $f(0)=0$.
If $f(x)=c$ or $f(x)=-c$ (for $c>0$), then $f(0) \neq 0$. This contradicts the condition for being in $\mathcal{F}$.
Therefore, there is no function $f \in \mathcal{F}$ (other than the zero function) for which the ratio is exactly 1.
This means the supremum is 1, but it is not a maximum.