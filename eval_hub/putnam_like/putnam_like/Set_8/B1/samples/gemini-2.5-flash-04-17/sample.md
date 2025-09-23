Let $a = \sqrt[3]{n}$ and $b = \sqrt[3]{n+1}$ for some $n \in \mathbb{N}$, $n \geq 21$. We want to compare $a^b$ and $b^a$.

To compare $a^b$ and $b^a$, we can compare their natural logarithms.
$\ln(a^b) = b \ln a$
$\ln(b^a) = a \ln b$

Since $a = n^{1/3}$ and $b = (n+1)^{1/3}$, and $n \geq 21$, both $a$ and $b$ are positive. We can divide by $ab$ and compare $\frac{\ln a}{a}$ and $\frac{\ln b}{b}$.

Let's consider the function $f(x) = \frac{\ln x}{x}$ for $x > 0$. We want to compare $f(a)$ and $f(b)$.
To determine whether $f(a)$ is greater than or less than $f(b)$, we analyze the derivative of $f(x)$:
$f'(x) = \frac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}$.

The sign of $f'(x)$ depends on the sign of the numerator $1 - \ln x$.
$f'(x) > 0$ if $1 - \ln x > 0 \implies \ln x < 1 \implies x < e$.
$f'(x) < 0$ if $1 - \ln x < 0 \implies \ln x > 1 \implies x > e$.
$f'(x) = 0$ if $1 - \ln x = 0 \implies \ln x = 1 \implies x = e$.

Thus, the function $f(x)$ is strictly increasing for $x \in (0, e)$ and strictly decreasing for $x \in (e, \infty)$.

Now, let's determine the values of $a$ and $b$ relative to $e \approx 2.718$.
We are given $n \geq 21$.
$a = n^{1/3}$. Since $n \geq 21$, $a = n^{1/3} \geq 21^{1/3}$.
We need to compare $21^{1/3}$ with $e$.
$e^3 \approx (2.718)^3 \approx 20.0855$.
Since $n \geq 21$, $n > e^3$.
Taking the cube root of both sides (the cube root function is increasing), we get $n^{1/3} > (e^3)^{1/3}$, which means $a > e$.

Since $n \geq 21$, we have $n+1 > n \geq 21$.
$b = (n+1)^{1/3} > n^{1/3} = a$.
So $b > a$.
Since $a > e$, and $b > a$, it follows that $b > e$ as well.
Both $a$ and $b$ are in the interval $(e, \infty)$.

In the interval $(e, \infty)$, the function $f(x) = \frac{\ln x}{x}$ is strictly decreasing.
Since $e < a < b$, and $f(x)$ is decreasing on $(e, \infty)$, we have $f(a) > f(b)$.
Substituting the expressions for $f(a)$ and $f(b)$:
$\frac{\ln a}{a} > \frac{\ln b}{b}$.

Now, we convert this inequality back to the comparison of $a^b$ and $b^a$. Multiply both sides of the inequality by $ab$ (which is positive):
$ab \cdot \frac{\ln a}{a} > ab \cdot \frac{\ln b}{b}$
$b \ln a > a \ln b$
Using the logarithm property $k \ln x = \ln x^k$:
$\ln(a^b) > \ln(b^a)$

Since the natural logarithm function $\ln x$ is strictly increasing, this inequality implies:
$a^b > b^a$.

Thus, $a^b$ is greater than $b^a$.

The final answer is $\boxed{a^b}$.