# Solution

I'm going to determine which is greater: $a^b$ or $b^a$, where $a=\sqrt[3]{n}$ and $b=\sqrt[3]{n+1}$ for $n\geq 21$.

To compare these expressions, I'll take the natural logarithm of both sides, which is a strictly increasing function. This preserves the inequality:

$a^b > b^a \iff \ln(a^b) > \ln(b^a)$

Using properties of logarithms:
$\ln(a^b) = b\ln(a)$ and $\ln(b^a) = a\ln(b)$

So I need to determine whether $b\ln(a) > a\ln(b)$.

Substituting the given values:
$b\ln(a) = \sqrt[3]{n+1} \cdot \ln(\sqrt[3]{n}) = \sqrt[3]{n+1} \cdot \frac{1}{3}\ln(n)$
$a\ln(b) = \sqrt[3]{n} \cdot \ln(\sqrt[3]{n+1}) = \sqrt[3]{n} \cdot \frac{1}{3}\ln(n+1)$

After removing the common factor of $\frac{1}{3}$, I'm comparing:
$\sqrt[3]{n+1} \cdot \ln(n)$ vs $\sqrt[3]{n} \cdot \ln(n+1)$

Rearranging to compare the values:
$\frac{\ln(n)}{n^{1/3}} > \frac{\ln(n+1)}{(n+1)^{1/3}}$

Let me define $f(x) = \frac{\ln(x)}{x^{1/3}}$. I need to determine if $f(n) > f(n+1)$.

To do this, I'll compute the derivative of $f(x)$:
$$f'(x) = \frac{d}{dx}\left(\frac{\ln(x)}{x^{1/3}}\right)$$

Using the quotient rule:
$$f'(x) = \frac{\frac{1}{x} \cdot x^{1/3} - \ln(x) \cdot \frac{1}{3}x^{-2/3}}{(x^{1/3})^2}$$

Simplifying the numerator:
$$\frac{1}{x} \cdot x^{1/3} - \ln(x) \cdot \frac{1}{3}x^{-2/3} = x^{-2/3}\left(1 - \frac{1}{3}\ln(x)\right)$$

Therefore:
$$f'(x) = \frac{x^{-2/3}\left(1 - \frac{1}{3}\ln(x)\right)}{x^{2/3}} = \frac{1 - \frac{1}{3}\ln(x)}{x^{4/3}}$$

For $n \geq 21$, we have $\ln(n) \geq \ln(21) \approx 3.04 > 3$. This means $1 - \frac{1}{3}\ln(n) < 0$, and since $x^{4/3} > 0$ for all $x > 0$, we have $f'(n) < 0$.

Since $f'(n) < 0$ for $n \geq 21$, the function $f(x)$ is strictly decreasing at $x = n$. Therefore, $f(n) > f(n+1)$, which implies:
$$\sqrt[3]{n+1} \cdot \ln(n) > \sqrt[3]{n} \cdot \ln(n+1)$$

This means $b\ln(a) > a\ln(b)$, and thus $a^b > b^a$.

Therefore, for $n \geq 21$, $a^b$ is greater than $b^a$.