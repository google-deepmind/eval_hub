Solution:
Let $I_1 = \int_{1-\frac{1}{n}}^1 f(x)dx$, $I_2 = \int_0^1 x^{n-1}f(x)dx$, and $I_3 = \int_0^{\frac{1}{n}}f(x)dx$. We want to show that $I_1 \leq I_2 \leq I_3$ for all $n\in \mathbb{N}$.
The function $f: [0,1]\to \mathbb{R}$ is continuous and decreasing.

Case $n=1$:
$I_1 = \int_{1-1}^1 f(x)dx = \int_0^1 f(x)dx$.
$I_2 = \int_0^1 x^{1-1}f(x)dx = \int_0^1 f(x)dx$.
$I_3 = \int_0^{1/1} f(x)dx = \int_0^1 f(x)dx$.
In this case, $I_1 = I_2 = I_3$, so the inequalities hold.

Assume $n \geq 2$.

**Part 1: Show $I_2 \leq I_3$.**
We perform a change of variable in $I_2$. Let $x = t^{1/n}$. This means $t = x^n$. Then $dt = nx^{n-1}dx$. When $x=0$, $t=0$. When $x=1$, $t=1$.
\[
I_2 = \int_0^1 x^{n-1}f(x)dx = \int_0^1 f(t^{1/n}) \frac{dt}{n} = \frac{1}{n} \int_0^1 f(t^{1/n}) dt.
\]
Now we compare $t^{1/n}$ and $t/n$ for $t \in [0,1]$. Let $g(t) = t^{1/n} - t/n$.
$g(0) = 0 - 0 = 0$.
The derivative is $g'(t) = \frac{1}{n} t^{1/n - 1} - \frac{1}{n} = \frac{1}{n} (t^{(1-n)/n} - 1)$.
Since $n \geq 2$, we have $(1-n)/n < 0$. For $t \in (0,1)$, we have $t^{(1-n)/n} > 1$.
Therefore, $g'(t) > 0$ for $t \in (0,1)$.
Since $g(0)=0$ and $g$ is increasing on $[0,1]$, we have $g(t) \geq 0$ for all $t \in [0,1]$.
So, $t^{1/n} \geq t/n$ for all $t \in [0,1]$.
Since $f$ is a decreasing function, this implies $f(t^{1/n}) \leq f(t/n)$ for all $t \in [0,1]$.
Integrating both sides from $t=0$ to $t=1$:
\[
\int_0^1 f(t^{1/n}) dt \leq \int_0^1 f(t/n) dt.
\]
Multiplying by $1/n$ (which is positive):
\[
\frac{1}{n} \int_0^1 f(t^{1/n}) dt \leq \frac{1}{n} \int_0^1 f(t/n) dt.
\]
The left side is $I_2$. Let's evaluate the right side.
Let $u = t/n$. Then $du = dt/n$. When $t=0$, $u=0$. When $t=1$, $u=1/n$.
\[
\frac{1}{n} \int_0^1 f(t/n) dt = \int_0^{1/n} f(u) du.
\]
This is exactly $I_3$.
Thus, we have shown $I_2 \leq I_3$.

**Part 2: Show $I_1 \leq I_2$.**
We perform a change of variable in $I_1$. Let $x = 1-t/n$. Then $t = n(1-x)$. $dx = -dt/n$. When $x=1-1/n$, $t=1$. When $x=1$, $t=0$.
\[
I_1 = \int_{1-1/n}^1 f(x)dx = \int_1^0 f(1-t/n) \left(-\frac{dt}{n}\right) = \frac{1}{n} \int_0^1 f(1-t/n) dt.
\]
Now we perform a different change of variable in $I_2$. Let $x = (1-t)^{1/n}$. Then $x^n = 1-t$, so $t=1-x^n$. $nx^{n-1}dx = -dt$. When $x=0$, $t=1$. When $x=1$, $t=0$.
\[
I_2 = \int_0^1 x^{n-1} f(x) dx = \int_1^0 f((1-t)^{1/n}) \left(-\frac{dt}{n}\right) = \frac{1}{n} \int_0^1 f((1-t)^{1/n}) dt.
\]
We want to show $I_1 \leq I_2$, which is equivalent to:
\[
\frac{1}{n} \int_0^1 f(1-t/n) dt \leq \frac{1}{n} \int_0^1 f((1-t)^{1/n}) dt.
\]
Multiplying by $n$, we need to show:
\[
\int_0^1 f(1-t/n) dt \leq \int_0^1 f((1-t)^{1/n}) dt.
\]
Since $f$ is decreasing, this inequality holds if $1-t/n \geq (1-t)^{1/n}$ for all $t \in [0,1]$.
Let $k(t) = (1-t/n) - (1-t)^{1/n}$ for $t \in [0,1]$.
$k(0) = (1-0) - (1-0)^{1/n} = 1-1 = 0$.
The derivative is $k'(t) = -\frac{1}{n} - \frac{1}{n}(1-t)^{1/n-1}(-1) = -\frac{1}{n} + \frac{1}{n}(1-t)^{(1-n)/n} = \frac{1}{n} ((1-t)^{(1-n)/n} - 1)$.
Since $n \geq 2$, $(1-n)/n < 0$. For $t \in (0,1)$, $1-t \in (0,1)$, so $(1-t)^{(1-n)/n} > 1$.
Therefore, $k'(t) > 0$ for $t \in (0,1)$.
Since $k(0)=0$ and $k$ is increasing on $[0,1]$, we have $k(t) \geq 0$ for all $t \in [0,1]$.
So, $1-t/n \geq (1-t)^{1/n}$ for all $t \in [0,1]$.
Since $f$ is decreasing, this implies $f(1-t/n) \leq f((1-t)^{1/n})$ for all $t \in [0,1]$.
Integrating both sides from $t=0$ to $t=1$:
\[
\int_0^1 f(1-t/n) dt \leq \int_0^1 f((1-t)^{1/n}) dt.
\]
Multiplying by $1/n$:
\[
\frac{1}{n} \int_0^1 f(1-t/n) dt \leq \frac{1}{n} \int_0^1 f((1-t)^{1/n}) dt.
\]
The left side is $I_1$ and the right side is $I_2$.
Thus, we have shown $I_1 \leq I_2$.

Combining both parts, we have shown that $I_1 \leq I_2 \leq I_3$ for all $n \in \mathbb{N}$.

Final Result: The final result is $\boxed{\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx}$