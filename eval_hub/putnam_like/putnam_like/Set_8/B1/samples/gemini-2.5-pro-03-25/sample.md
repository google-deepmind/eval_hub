Solution:
Let $a=\sqrt[3]{n}$ and $b=\sqrt[3]{n+1}$ for $n\in\mathbb{N}$, $n\geq 21$. We want to compare $a^b$ and $b^a$.

We can compare the logarithms of the two expressions. Since the natural logarithm function $\ln(x)$ is strictly increasing for $x>0$, comparing $a^b$ and $b^a$ (which are both positive) is equivalent to comparing $\ln(a^b)$ and $\ln(b^a)$.
Using the property of logarithms $\ln(x^y) = y \ln x$, we compare $b \ln a$ and $a \ln b$.

Dividing both expressions by $ab$ (which is positive since $n\geq 21$, thus $a=\sqrt[3]{n}>0$ and $b=\sqrt[3]{n+1}>0$), we see that comparing $b \ln a$ and $a \ln b$ is equivalent to comparing $\frac{\ln a}{a}$ and $\frac{\ln b}{b}$.

Let's consider the function $f(t) = \frac{\ln t}{t}$ for $t>0$. We want to compare $f(a)$ and $f(b)$.
To understand the behavior of $f(t)$, we compute its derivative:
$$ f'(t) = \frac{d}{dt}\left(\frac{\ln t}{t}\right) = \frac{(1/t) \cdot t - (\ln t) \cdot 1}{t^2} = \frac{1 - \ln t}{t^2} $$
The derivative $f'(t)$ is zero when $1 - \ln t = 0$, which means $\ln t = 1$, so $t = e$.
The sign of $f'(t)$ depends on the sign of $1 - \ln t$.
- If $0 < t < e$, then $\ln t < \ln e = 1$, so $1 - \ln t > 0$. Thus $f'(t) > 0$, which means $f(t)$ is strictly increasing on $(0, e)$.
- If $t > e$, then $\ln t > \ln e = 1$, so $1 - \ln t < 0$. Thus $f'(t) < 0$, which means $f(t)$ is strictly decreasing on $(e, \infty)$.

Now we need to determine where $a$ and $b$ lie relative to $e$.
We are given $n \geq 21$.
$a = \sqrt[3]{n} \geq \sqrt[3]{21}$.
$b = \sqrt[3]{n+1} > \sqrt[3]{n} = a$.
We need to compare $a$ with $e$. Let's compare $\sqrt[3]{21}$ with $e$. This is equivalent to comparing $21$ with $e^3$.
The value of $e$ is approximately $2.71828$.
$e^2 \approx (2.71828)^2 \approx 7.389056$.
$e^3 \approx 7.389056 \times 2.71828 \approx 20.085537$.
Since $21 > 20.085537$, we have $21 > e^3$.
Taking the cube root of both sides (which is a strictly increasing function), we get $\sqrt[3]{21} > \sqrt[3]{e^3} = e$.
So, for $n \geq 21$, we have $a = \sqrt[3]{n} \geq \sqrt[3]{21} > e$.
Since $b = \sqrt[3]{n+1} > \sqrt[3]{n} = a$, we have $b > a > e$.

Since $f(t)$ is strictly decreasing for $t > e$, and we have $b > a > e$, it follows that $f(b) < f(a)$.
$$ \frac{\ln b}{b} < \frac{\ln a}{a} $$
Multiplying both sides by the positive number $ab$:
$$ a \ln b < b \ln a $$
Using the logarithm property $y \ln x = \ln(x^y)$:
$$ \ln(b^a) < \ln(a^b) $$
Since the natural logarithm function $\ln(x)$ is strictly increasing, this inequality implies:
$$ b^a < a^b $$

Therefore, $a^b$ is greater than $b^a$.

Final Answer: The final answer is $\boxed{a^b}$