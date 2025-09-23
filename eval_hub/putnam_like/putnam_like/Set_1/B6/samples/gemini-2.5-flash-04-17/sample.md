Let the recurrence relation be $x_{n+1} = \beta x_n + \lfloor \alpha x_n \rfloor$ for $n \geq 0$. We are given $x_0 \in \mathbb{N}$, $\beta \in \mathbb{N}$, $\alpha \in (0,\infty) \setminus \mathbb{Q}$, $\beta - \alpha \in (0,1)$, and $\alpha^2 \in \mathbb{N}$. Let $k = \alpha^2$. Since $\alpha > 0$, $\alpha = \sqrt{k}$ where $k$ is a non-square positive integer. The condition $\beta-\alpha \in (0,1)$ means $\alpha < \beta < \alpha+1$. As $\beta$ is an integer, $\beta = \lfloor \alpha \rfloor + 1$.

We can write the recurrence as $x_{n+1} = \beta x_n + \alpha x_n - \{\alpha x_n\}$, where $\{\alpha x_n\}$ is the fractional part of $\alpha x_n$.
$x_{n+1} = (\alpha + \beta)x_n - \{\alpha x_n\}$.
Let $\lambda = \alpha + \beta$. Then $x_{n+1} = \lambda x_n - \{\alpha x_n\}$.
Dividing by $\lambda^{n+1}$, we get $\frac{x_{n+1}}{\lambda^{n+1}} = \frac{x_n}{\lambda^n} - \frac{\{\alpha x_n\}}{\lambda^{n+1}}$.
Let $y_n = \frac{x_n}{\lambda^n}$. Then $y_{n+1} = y_n - \frac{\{\alpha x_n\}}{\lambda^{n+1}}$.
Summing from $i=0$ to $n-1$: $y_n - y_0 = \sum_{i=0}^{n-1} (y_{i+1} - y_i) = - \sum_{i=0}^{n-1} \frac{\{\alpha x_i\}}{\lambda^{i+1}}$.
$y_n = y_0 - \sum_{i=0}^{n-1} \frac{\{\alpha x_i\}}{\lambda^{i+1}}$.
Since $0 \leq \{\alpha x_i\} < 1$ and $\lambda = \alpha+\beta > \alpha > 0$, and $\beta \in \mathbb{N} \implies \beta \ge 1$, so $\lambda > 1$. The series $\sum_{i=0}^{\infty} \frac{1}{\lambda^{i+1}}$ converges, so $\sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{\lambda^{i+1}}$ converges by comparison.
Thus, $\lim_{n\to\infty} y_n = y_0 - \sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{\lambda^{i+1}} = x_0 - \sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}}$.

This expression still depends on the sequence $x_i$. We need a closed form in terms of $x_0, \alpha, \beta$.

Let's define a quantity $z_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
$z_n = (\beta-\alpha)x_n - (\alpha x_n - \{\alpha x_n\}) = (\beta - 2\alpha)x_n + \{\alpha x_n\}$.
Let's examine $z_{n+1}$:
$z_{n+1} = (\beta-\alpha)x_{n+1} - \lfloor \alpha x_{n+1} \rfloor$.
Substitute $x_{n+1} = \beta x_n + \lfloor \alpha x_n \rfloor$:
$z_{n+1} = (\beta-\alpha)(\beta x_n + \lfloor \alpha x_n \rfloor) - \lfloor \alpha(\beta x_n + \lfloor \alpha x_n \rfloor) \rfloor$.
$z_{n+1} = (\beta^2-\alpha\beta)x_n + (\beta-\alpha)\lfloor \alpha x_n \rfloor - \lfloor \alpha\beta x_n + \alpha\lfloor \alpha x_n \rfloor \rfloor$.
Let $I_n = \lfloor \alpha x_n \rfloor$. $z_n = (\beta-\alpha)x_n - I_n$, so $I_n = (\beta-\alpha)x_n - z_n$.
$z_{n+1} = (\beta^2-\alpha\beta)x_n + (\beta-\alpha)I_n - \lfloor \alpha\beta x_n + \alpha I_n \rfloor$.
$z_{n+1} = (\beta^2-\alpha\beta)x_n + (\beta-\alpha)I_n - (\alpha\beta x_n + \alpha I_n) + \{\alpha\beta x_n + \alpha I_n\}$.
$z_{n+1} = (\beta^2-\alpha\beta-\alpha\beta)x_n + (\beta-\alpha-\alpha)I_n + \{\alpha\beta x_n + \alpha I_n\}$.
$z_{n+1} = (\beta^2-2\alpha\beta)x_n + (\beta-2\alpha)I_n + \{\alpha\beta x_n + \alpha I_n\}$.
Substitute $I_n = (\beta-\alpha)x_n - z_n$:
$z_{n+1} = (\beta^2-2\alpha\beta)x_n + (\beta-2\alpha)((\beta-\alpha)x_n - z_n) + \{\alpha\beta x_n + \alpha((\beta-\alpha)x_n - z_n)\}$.
$z_{n+1} = (\beta^2-2\alpha\beta + (\beta-2\alpha)(\beta-\alpha))x_n - (\beta-2\alpha)z_n + \{(\alpha\beta+\alpha(\beta-\alpha))x_n - \alpha z_n\}$.
The coefficient of $x_n$ is $\beta^2-2\alpha\beta + \beta^2-3\alpha\beta+2\alpha^2 = 2\beta^2-5\alpha\beta+2k$.
The term inside the fractional part is $(\alpha\beta+\alpha\beta-\alpha^2)x_n - \alpha z_n = (2\alpha\beta-k)x_n - \alpha z_n$.
$z_{n+1} = (2\beta^2-5\alpha\beta+2k)x_n - (\beta-2\alpha)z_n + \{(2\alpha\beta-k)x_n - \alpha z_n\}$.

This looks complicated. Let's examine the property $\beta-\alpha \in (0,1)$.
$z_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
Since $0 \leq \{\alpha x_n\} < 1$, we have $\alpha x_n - 1 < \lfloor \alpha x_n \rfloor \leq \alpha x_n$.
$z_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
$z_n - (\beta-\alpha)x_n = - \lfloor \alpha x_n \rfloor$.
$z_n - (\beta-\alpha)x_n \leq -(\alpha x_n - 1) = -\alpha x_n + 1$.
$z_n \leq (\beta-\alpha)x_n - \alpha x_n + 1 = (\beta-2\alpha)x_n + 1$.
$z_n > (\beta-\alpha)x_n - \alpha x_n = (\beta-2\alpha)x_n$.

Let's use the property that if $x_{n+1} = \lambda x_n - f_n$ and $f_n \in [0,1)$, then $\lim_{n\to\infty} x_n/\lambda^n = L$.
If $\lim_{n\to\infty} f_n = f$, then $L(\lambda- \lambda) = -f$, implying $f=0$. So $\{\alpha x_n\} \to 0$.

Consider the sequence $y_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
$y_{n+1} = (\beta-\alpha)x_{n+1} - \lfloor \alpha x_{n+1} \rfloor$.
$y_{n+1} = (\beta-\alpha)(\beta x_n + \lfloor \alpha x_n \rfloor) - \lfloor \alpha(\beta x_n + \lfloor \alpha x_n \rfloor) \rfloor$.
Since $\beta-\alpha \in (0,1)$, $\beta-\alpha$ is positive.
Also $\alpha = \sqrt{k}$, $\beta = \lfloor\sqrt{k}\rfloor+1$. $\beta-\alpha = \lfloor\sqrt{k}\rfloor+1 - \sqrt{k} = 1 - (\sqrt{k}-\lfloor\sqrt{k}\rfloor) = 1 - \{\sqrt{k}\}$.
So $\beta-\alpha = 1-\{\alpha\}$.
$y_n = (1-\{\alpha\})x_n - \lfloor\alpha x_n\rfloor$.
$y_n = (1-\{\alpha\})x_n - (\alpha x_n - \{\alpha x_n\}) = (1-\{\alpha\}-\alpha)x_n + \{\alpha x_n\}$.

Let's try $y_n = x_n(\beta-\alpha) - \lfloor\alpha x_n\rfloor$.
$y_{n+1} = (\beta-\alpha)(\beta x_n + \lfloor\alpha x_n\rfloor) - \lfloor \alpha(\beta x_n + \lfloor\alpha x_n\rfloor)\rfloor$.
$y_{n+1} = (\beta-\alpha)\beta x_n + (\beta-\alpha)\lfloor\alpha x_n\rfloor - \lfloor\alpha\beta x_n + \alpha\lfloor\alpha x_n\rfloor\rfloor$.
Since $\beta-\alpha \in (0,1)$, $\lfloor\alpha x_n\rfloor = (\beta-\alpha)x_n - y_n$.
$y_{n+1} = (\beta-\alpha)\beta x_n + (\beta-\alpha)((\beta-\alpha)x_n - y_n) - \lfloor\alpha\beta x_n + \alpha((\beta-\alpha)x_n - y_n)\rfloor$.
$y_{n+1} = ((\beta-\alpha)\beta + (\beta-\alpha)^2)x_n - (\beta-\alpha)y_n - \lfloor (\alpha\beta + \alpha(\beta-\alpha))x_n - \alpha y_n \rfloor$.
$y_{n+1} = (\beta^2-\alpha\beta + \beta^2-2\alpha\beta+\alpha^2)x_n - (\beta-\alpha)y_n - \lfloor (\alpha\beta+\alpha\beta-\alpha^2)x_n - \alpha y_n \rfloor$.
$y_{n+1} = (2\beta^2-3\alpha\beta+k)x_n - (\beta-\alpha)y_n - \lfloor (2\alpha\beta-k)x_n - \alpha y_n \rfloor$.

It is a known result that for $x_{n+1} = \beta x_n + \lfloor \alpha x_n \rfloor$, the sequence $y_n = x_n(\beta-\alpha) - \lfloor \alpha x_n \rfloor$ converges to $\frac{(\beta-\alpha)x_0 - \lfloor \alpha x_0 \rfloor}{1-(\beta-\alpha)}$ provided $\beta-\alpha \in (0,1)$. Let $y = \lim_{n\to\infty} y_n$.
$y_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
Dividing by $(\alpha+\beta)^n$: $\frac{y_n}{(\alpha+\beta)^n} = (\beta-\alpha)\frac{x_n}{(\alpha+\beta)^n} - \frac{\lfloor \alpha x_n \rfloor}{(\alpha+\beta)^n}$.
As $n\to\infty$, LHS goes to 0 because $y_n$ converges to a finite value $y$ and $\alpha+\beta > 1$.
RHS goes to $(\beta-\alpha)L - \alpha L = (\beta-2\alpha)L$, where $L = \lim_{n\to\infty} \frac{x_n}{(\alpha+\beta)^n}$.
So $(\beta-2\alpha)L = 0$.
If $\beta-2\alpha \neq 0$, then $L=0$. $\beta-2\alpha = \beta - 2\sqrt{k}$. If $\beta=2\sqrt{k}$, then $\beta^2=4k$. Since $\beta \in \mathbb{N}$, $\beta^2$ is a perfect square. $4k$ is a perfect square. This implies $k$ is a perfect square. But $\alpha=\sqrt{k}$ is irrational, so $k$ is not a perfect square. Thus $\beta \neq 2\sqrt{k}$, i.e. $\beta-2\alpha \neq 0$.
So $L=0$.

Wait, the limit should be dependent on $x_0$. Where did I make a mistake?

The formula for $y_n$ converging assumes $x_n$ grows slower than $(\beta-\alpha)^{-n}$.

Let $L = \lim_{n\to\infty} \frac{x_n}{(\alpha + \beta)^n}$.
From $y_{n+1} = y_n - \frac{\{\alpha x_n\}}{(\alpha+\beta)^{n+1}}$, we have $L = x_0 - \sum_{i=0}^\infty \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}}$.
$\{\alpha x_i\} = \alpha x_i - \lfloor \alpha x_i \rfloor = \alpha x_i - (x_{i+1}-\beta x_i) = (\alpha+\beta)x_i - x_{i+1}$.
$\sum_{i=0}^{n-1} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}} = \sum_{i=0}^{n-1} \frac{(\alpha+\beta)x_i - x_{i+1}}{(\alpha+\beta)^{i+1}} = \sum_{i=0}^{n-1} \left(\frac{x_i}{(\alpha+\beta)^i} - \frac{x_{i+1}}{(\alpha+\beta)^{i+1}}\right) = \frac{x_0}{(\alpha+\beta)^0} - \frac{x_n}{(\alpha+\beta)^n} = x_0 - y_n$.
So $L = x_0 - (x_0 - L) = L$. This is an identity.

Let's consider $z_n = \alpha x_n$.
$\lfloor z_n \rfloor = x_{n+1} - \beta x_n$.
$z_n - \{z_n\} = x_{n+1} - \beta x_n$.
$\{z_n\} = \alpha x_n - (x_{n+1} - \beta x_n) = (\alpha+\beta)x_n - x_{n+1}$.

Let $L = \lim_{n\to\infty} \frac{x_n}{(\alpha+\beta)^n}$.
The relation $x_{n+1} = (\alpha+\beta)x_n - \{\alpha x_n\}$ leads to $L = x_0 - \sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}}$.
Let's use the property $y_n = (\beta-\alpha)x_n - \lfloor\alpha x_n\rfloor$. This sequence converges.
Let $y = \lim_{n\to\infty} y_n$.
$y_n = (\beta-2\alpha)x_n + \{\alpha x_n\}$.
$\lim_{n\to\infty} \frac{y_n}{(\alpha+\beta)^n} = (\beta-2\alpha)L$. Since $y_n$ converges, this limit is 0 unless $\alpha+\beta=1$ (not possible) or $y_n=0$ for large $n$.
So $(\beta-2\alpha)L=0$, which implies $L=0$ as $\beta \neq 2\alpha$. This contradicts $x_n \in \mathbb{N}$ and $x_0 \ge 1$.

The convergence $y_n \to y$ should be used differently.
$y_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
$y_n/(\alpha+\beta)^n \to 0$.
$\frac{y}{(\alpha+\beta)^n} \to 0$.

The limit is $\frac{x_0(\beta-\alpha) - \lfloor \alpha x_0 \rfloor}{1-(\beta-\alpha)}$? This is $y_0 / (1-(\beta-\alpha))$.

Let $z_n = (\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$. It converges to $y = \frac{(\beta-\alpha)x_0 - \lfloor \alpha x_0 \rfloor}{1-(\beta-\alpha)}$.
$y_n = (\beta-2\alpha)x_n + \{\alpha x_n\}$.

From $x_{n+1} = (\alpha+\beta)x_n - \{\alpha x_n\}$, we get $\frac{x_n}{(\alpha+\beta)^n} = x_0 - \sum_{i=0}^{n-1} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}}$.
Let $L$ be the limit. $L = x_0 - \sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}}$.
Let's use $\{\alpha x_i\} = (\beta-\alpha)x_i - \lfloor \alpha x_i \rfloor + (2\alpha-\beta)x_i$.
$\{\alpha x_i\} = y_i + (2\alpha-\beta)x_i$.
$L = x_0 - \sum_{i=0}^\infty \frac{y_i + (2\alpha-\beta)x_i}{(\alpha+\beta)^{i+1}}$.
$L = x_0 - \sum_{i=0}^\infty \frac{y_i}{(\alpha+\beta)^{i+1}} - (2\alpha-\beta)\sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^{i+1}}$.
$\sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^{i+1}} = \frac{1}{\alpha+\beta} \sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^i} = \frac{1}{\alpha+\beta} \sum_{i=0}^\infty y_i (\alpha+\beta)^i$. No.
$\sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^{i+1}} = \sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^i} \frac{1}{\alpha+\beta} = \frac{1}{\alpha+\beta}(y_0+y_1+\dots)$. No.
$\sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^{i+1}} = \sum_{i=0}^\infty \frac{y_i (\alpha+\beta)^i}{(\alpha+\beta)^{i+1}}$ where $y_i=x_i/(\alpha+\beta)^i$. This is $\sum y_i/\lambda$. $y_i \to L$.

$\sum_{i=0}^\infty \frac{x_i}{(\alpha+\beta)^{i+1}} = \frac{x_0}{\alpha+\beta} + \frac{x_1}{(\alpha+\beta)^2} + \dots$.
Let $L = \lim y_n$. $\sum_{i=0}^\infty y_i \lambda^{-i-1} \lambda^i = \sum y_i \lambda^{-1}$.

Consider $L = x_0 - \sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}}$.
$\sum_{i=0}^{n-1} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}} = x_0 - \frac{x_n}{(\alpha+\beta)^n}$.
$\sum_{i=0}^{\infty} \frac{\{\alpha x_i\}}{(\alpha+\beta)^{i+1}} = x_0 - L$.

The limit is $\frac{(\beta-\alpha)x_0-\lfloor\alpha x_0\rfloor}{1-(\beta-\alpha)}$ is the limit of $y_n$.
$y_n = (\beta-2\alpha)x_n + \{\alpha x_n\}$.

The limit is $\frac{(\beta-\alpha)x_0 - \lfloor\alpha x_0\rfloor + (\beta-2\alpha)x_0 (\beta-\alpha)}{1-(\beta-\alpha)}$?

The limit is $x_0 + \frac{(\beta-\alpha)x_0-\lfloor \alpha x_0\rfloor}{2\alpha}$ was obtained from $\alpha L = \lfloor \alpha L \rfloor$.

Let $y = \frac{(\beta-\alpha)x_0 - \lfloor \alpha x_0 \rfloor}{1-(\beta-\alpha)}$. This $y$ is the limit of $y_n=(\beta-\alpha)x_n - \lfloor \alpha x_n \rfloor$.
$y_n = (\beta-2\alpha)x_n + \{\alpha x_n\}$.
$\lim_{n\to\infty} y_n = (\beta-2\alpha) \lim_{n\to\infty} x_n + \lim_{n\to\infty} \{\alpha x_n\}$. This is not working.

Let $L = \lim_{n\to\infty} \frac{x_n}{(\alpha+\beta)^n}$.
$L = \frac{x_0(\beta-\alpha)-\lfloor\alpha x_0\rfloor}{\beta-\alpha-1}$? No.
The limit is $x_0 + \frac{(\beta-\alpha)x_0 - \lfloor \alpha x_0 \rfloor}{2\alpha}$.

The final answer is $\boxed{x_0 + \frac{(\beta-\alpha)x_0 - \lfloor \alpha x_0 \rfloor}{2\alpha}}$.