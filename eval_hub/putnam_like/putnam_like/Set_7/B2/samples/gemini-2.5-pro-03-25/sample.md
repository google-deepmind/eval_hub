Let $S$ be the value we want to find:
$$
S = \sup_{f \in \mathcal{F}} \frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}},
$$
where $\mathcal{F} = \{ f \in \mathcal{C}([0,1]; \mathbb{R}) \ : \ f(0) = 0 \}$.
Let $\|f\|_1 = \int_0^1 |f(x)| dx$ and $\|f\|_2 = \left( \int_0^1 |f(x)|^2 dx \right)^{1/2}$ denote the $L^1$ and $L^2$ norms of $f$ on $[0,1]$, respectively.
We are looking for $S = \sup_{f \in \mathcal{F}, f \ne 0} \frac{\|f\|_1}{\|f\|_2}$. The condition $f \ne 0$ ensures that $\|f\|_2 > 0$, since $f$ is continuous.

By the Cauchy-Schwarz inequality, for any $f \in \mathcal{F}$:
$$
\|f\|_1 = \int_0^1 |f(x)| \cdot 1 \, dx \le \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2} \left( \int_0^1 1^2 \, dx \right)^{1/2} = \|f\|_2 \cdot \sqrt{1} = \|f\|_2.
$$
Therefore, for any $f \in \mathcal{F}$ with $f \neq 0$, we have
$$
\frac{\|f\|_1}{\|f\|_2} \le 1.
$$
This implies that the supremum $S$ must satisfy $S \le 1$.

Now we need to check if the value 1 can be approached by functions in $\mathcal{F}$.
The equality in the Cauchy-Schwarz inequality holds if and only if $|f(x)| = c \cdot 1$ for some constant $c \ge 0$, for almost every $x \in [0,1]$. Since $f$ is continuous, this must hold for all $x \in [0,1]$. So $|f(x)| = c$ for all $x \in [0,1]$.
If $c=0$, then $f(x)=0$ for all $x$. This function is in $\mathcal{F}$, but the ratio $\frac{\|f\|_1}{\|f\|_2}$ is $0/0$, which is undefined (or considered 0). The supremum must be at least 0, but we expect a positive value.
If $c>0$, then $|f(x)|=c$. Since $f$ is continuous, this means either $f(x)=c$ for all $x$ or $f(x)=-c$ for all $x$.
If $f(x)=c$ for all $x$, then $f(0)=c$. Since $f \in \mathcal{F}$, we must have $f(0)=0$, so $c=0$. This implies $f(x)=0$.
If $f(x)=-c$ for all $x$, then $f(0)=-c$. Since $f \in \mathcal{F}$, we must have $f(0)=0$, so $c=0$. This implies $f(x)=0$.
Thus, the only function in $\mathcal{F}$ for which the ratio $\frac{\|f\|_1}{\|f\|_2}$ is equal to 1 is the zero function $f=0$. For any non-zero function $f \in \mathcal{F}$, the ratio is strictly less than 1.
This means that the supremum $S$ is not attained by any function in $\mathcal{F}$. However, the supremum can still be 1.

We need to construct a sequence of functions $(f_n)$ in $\mathcal{F}$ such that $\lim_{n \to \infty} \frac{\|f_n\|_1}{\|f_n\|_2} = 1$.

Consider the sequence of functions $f_a(x) = x^a$ for $a > 0$.
For any $a>0$, $f_a$ is continuous on $[0,1]$. Also $f_a(0)=0^a=0$. So $f_a \in \mathcal{F}$.
$f_a(x) = x^a \ge 0$ for $x \in [0,1]$.
The $L^1$ norm is:
$$
\|f_a\|_1 = \int_0^1 x^a \, dx = \left[ \frac{x^{a+1}}{a+1} \right]_0^1 = \frac{1}{a+1}.
$$
The $L^2$ norm squared is:
$$
\|f_a\|_2^2 = \int_0^1 (x^a)^2 \, dx = \int_0^1 x^{2a} \, dx = \left[ \frac{x^{2a+1}}{2a+1} \right]_0^1 = \frac{1}{2a+1}.
$$
So the $L^2$ norm is $\|f_a\|_2 = \frac{1}{\sqrt{2a+1}}$.
The ratio is:
$$
\frac{\|f_a\|_1}{\|f_a\|_2} = \frac{1/(a+1)}{1/\sqrt{2a+1}} = \frac{\sqrt{2a+1}}{a+1}.
$$
We want to see if this ratio can approach 1. Let's consider the limit as $a \to 0^+$:
$$
\lim_{a \to 0^+} \frac{\sqrt{2a+1}}{a+1} = \frac{\sqrt{2(0)+1}}{0+1} = \frac{\sqrt{1}}{1} = 1.
$$
We can define a sequence by setting $a_n = 1/n$ for $n=1, 2, \dots$. Let $f_n(x) = x^{1/n}$. Then $f_n \in \mathcal{F}$ for all $n$. The ratio for $f_n$ is $\frac{\sqrt{2/n+1}}{1/n+1}$.
$$
\lim_{n \to \infty} \frac{\|f_n\|_1}{\|f_n\|_2} = \lim_{n \to \infty} \frac{\sqrt{2/n+1}}{1/n+1} = \frac{\sqrt{1}}{1} = 1.
$$
Since we have found a sequence of functions $(f_n)$ in $\mathcal{F}$ such that the ratio $\frac{\|f_n\|_1}{\|f_n\|_2}$ approaches 1, and we know that the ratio is always bounded above by 1, the supremum must be 1.

Alternative sequence: Consider $f_\epsilon(x) = \min(x/\epsilon, 1)$ for $\epsilon > 0$.
$f_\epsilon$ is continuous, $f_\epsilon(0) = \min(0/\epsilon, 1) = 0$. So $f_\epsilon \in \mathcal{F}$.
$$
\|f_\epsilon\|_1 = \int_0^1 f_\epsilon(x) dx = \int_0^\epsilon \frac{x}{\epsilon} dx + \int_\epsilon^1 1 dx = \frac{1}{\epsilon} \left[\frac{x^2}{2}\right]_0^\epsilon + [x]_\epsilon^1 = \frac{\epsilon^2}{2\epsilon} + (1-\epsilon) = \frac{\epsilon}{2} + 1 - \epsilon = 1 - \frac{\epsilon}{2}.
$$
$$
\|f_\epsilon\|_2^2 = \int_0^1 (f_\epsilon(x))^2 dx = \int_0^\epsilon \left(\frac{x}{\epsilon}\right)^2 dx + \int_\epsilon^1 1^2 dx = \frac{1}{\epsilon^2} \left[\frac{x^3}{3}\right]_0^\epsilon + [x]_\epsilon^1 = \frac{\epsilon^3}{3\epsilon^2} + (1-\epsilon) = \frac{\epsilon}{3} + 1 - \epsilon = 1 - \frac{2\epsilon}{3}.
$$
$$
\|f_\epsilon\|_2 = \sqrt{1 - \frac{2\epsilon}{3}}.
$$
The ratio is:
$$
\frac{\|f_\epsilon\|_1}{\|f_\epsilon\|_2} = \frac{1 - \epsilon/2}{\sqrt{1 - 2\epsilon/3}}.
$$
As $\epsilon \to 0^+$, the ratio approaches $\frac{1-0}{\sqrt{1-0}} = 1$.
This confirms that the supremum is 1.

Conclusion: The supremum value is 1.

Final Answer: The final answer is $\boxed{1}$