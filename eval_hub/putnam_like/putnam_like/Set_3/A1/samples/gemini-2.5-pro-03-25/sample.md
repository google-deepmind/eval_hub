Solution:
Let the sequence be $(a_n)$ defined by
\[ a_n=\frac{\left(1+\frac 1n\right)^{3n+2}}{\left(1+\frac 1n\right)^n+\left(1+\frac 1n\right)^{n+1}+\left(1+\frac 1n\right)^{n+2}} \]
We want to prove that $a_n$ is strictly increasing, i.e., $a_{n+1} > a_n$ for all $n \ge 1$.
Let $x_n = 1+\frac{1}{n}$. Since $n \ge 1$, we have $x_n > 1$. The expression for $a_n$ can be rewritten as:
\[ a_n = \frac{x_n^{3n+2}}{x_n^n + x_n^{n+1} + x_n^{n+2}} \]
Factor out $x_n^n$ from the denominator:
\[ a_n = \frac{x_n^{3n+2}}{x_n^n (1 + x_n + x_n^2)} = \frac{x_n^{2n+2}}{1 + x_n + x_n^2} \]
Substitute $x_n = 1+\frac{1}{n}$:
\[ a_n = \frac{\left(1+\frac 1n\right)^{2n+2}}{1 + \left(1+\frac 1n\right) + \left(1+\frac 1n\right)^2} \]
The denominator is $1 + (1+\frac{1}{n}) + (1+\frac{2}{n}+\frac{1}{n^2}) = 3 + \frac{3}{n} + \frac{1}{n^2}$.
So,
\[ a_n = \frac{\left(1+\frac 1n\right)^{2n+2}}{3 + \frac{3}{n} + \frac{1}{n^2}} \]
To show that $(a_n)$ is strictly increasing, we consider the function $g(y)$ obtained by replacing $n$ with a real variable $y \ge 1$:
\[ g(y) = \frac{\left(1+\frac 1y\right)^{2y+2}}{3 + \frac{3}{y} + \frac{1}{y^2}} \]
We have $a_n = g(n)$. We will show that $g(y)$ is strictly increasing for $y \ge 1$. This will imply $a_{n+1} = g(n+1) > g(n) = a_n$ for all integers $n \ge 1$.

Let's simplify the expression for $g(y)$:
\[ g(y) = \frac{\left(\frac{y+1}{y}\right)^{2y+2}}{\frac{3y^2+3y+1}{y^2}} = \frac{(y+1)^{2y+2}}{y^{2y+2}} \frac{y^2}{3y^2+3y+1} = \frac{(y+1)^{2y+2}}{y^{2y}(3y^2+3y+1)} \]
To show $g(y)$ is increasing, we analyze the sign of its derivative $g'(y)$. It is generally easier to analyze the derivative of $\ln g(y)$.
\[ \ln g(y) = \ln \left( \frac{(y+1)^{2y+2}}{y^{2y}(3y^2+3y+1)} \right) \]
\[ \ln g(y) = (2y+2) \ln(y+1) - 2y \ln y - \ln(3y^2+3y+1) \]
Now we differentiate $\ln g(y)$ with respect to $y$:
\begin{align*} (\ln g(y))' &= \frac{d}{dy} [(2y+2) \ln(y+1) - 2y \ln y - \ln(3y^2+3y+1)] \\ &= \left[ 2 \ln(y+1) + (2y+2) \frac{1}{y+1} \right] - \left[ 2 \ln y + 2y \frac{1}{y} \right] - \frac{6y+3}{3y^2+3y+1} \\ &= 2 \ln(y+1) + 2 - 2 \ln y - 2 - \frac{6y+3}{3y^2+3y+1} \\ &= 2 (\ln(y+1) - \ln y) - \frac{3(2y+1)}{3y^2+3y+1} \\ &= 2 \ln\left(\frac{y+1}{y}\right) - \frac{3(2y+1)}{3y^2+3y+1} \\ &= 2 \ln\left(1+\frac{1}{y}\right) - \frac{6y+3}{3y^2+3y+1} \end{align*}
Let $h(y) = (\ln g(y))'$. We want to show $h(y)>0$ for $y \ge 1$.
Let's compute the derivative of $h(y)$:
\begin{align*} h'(y) &= \frac{d}{dy} \left[ 2 \ln\left(1+\frac{1}{y}\right) - \frac{6y+3}{3y^2+3y+1} \right] \\ &= 2 \frac{1}{1+\frac{1}{y}} \left(-\frac{1}{y^2}\right) - \frac{6(3y^2+3y+1) - (6y+3)(6y+3)}{(3y^2+3y+1)^2} \\ &= 2 \frac{y}{y+1} \left(-\frac{1}{y^2}\right) - \frac{18y^2+18y+6 - (36y^2+36y+9)}{(3y^2+3y+1)^2} \\ &= -\frac{2}{y(y+1)} - \frac{-18y^2-18y-3}{(3y^2+3y+1)^2} \\ &= -\frac{2}{y(y+1)} + \frac{3(6y^2+6y+1)}{(3y^2+3y+1)^2} \end{align*}
To combine these terms, we use the common denominator $y(y+1)(3y^2+3y+1)^2$:
\[ h'(y) = \frac{-2(3y^2+3y+1)^2 + 3y(y+1)(6y^2+6y+1)}{y(y+1)(3y^2+3y+1)^2} \]
Let's analyze the numerator $N(y)$:
\[ N(y) = -2(3y^2+3y+1)^2 + 3(y^2+y)(6y^2+6y+1) \]
Let $z = y^2+y = y(y+1)$. Then $3y^2+3y+1 = 3z+1$ and $6y^2+6y+1 = 6z+1$.
\[ N(y) = -2(3z+1)^2 + 3z(6z+1) = -2(9z^2+6z+1) + (18z^2+3z) \]
\[ N(y) = -18z^2 - 12z - 2 + 18z^2 + 3z = -9z - 2 \]
Substitute back $z=y^2+y$:
\[ N(y) = -9(y^2+y) - 2 = -9y^2 - 9y - 2 \]
Since $y \ge 1$, $y^2 \ge 1$ and $y \ge 1$. Thus $9y^2+9y+2 \ge 9(1)+9(1)+2 = 20 > 0$.
Therefore, $N(y) = -(9y^2+9y+2) < 0$ for all $y \ge 1$.
The denominator $D(y) = y(y+1)(3y^2+3y+1)^2$. Since $y \ge 1$, $y>0$, $y+1>0$. Also $3y^2+3y+1 \ge 3+3+1=7 > 0$, so $(3y^2+3y+1)^2 > 0$. Thus $D(y) > 0$.
So, $h'(y) = N(y)/D(y) < 0$ for all $y \ge 1$.
This means that $h(y)$ is a strictly decreasing function on $[1, \infty)$.

Now let's find the limit of $h(y)$ as $y \to \infty$:
\[ \lim_{y \to \infty} h(y) = \lim_{y \to \infty} \left[ 2 \ln\left(1+\frac{1}{y}\right) - \frac{6y+3}{3y^2+3y+1} \right] \]
As $y \to \infty$, $1/y \to 0$. So $\ln(1+1/y) \to \ln(1) = 0$. The first term tends to 0.
The second term is $\frac{6y+3}{3y^2+3y+1} = \frac{y(6+3/y)}{y^2(3+3/y+1/y^2)} = \frac{1}{y} \frac{6+3/y}{3+3/y+1/y^2}$.
As $y \to \infty$, this term tends to $\lim_{y \to \infty} \frac{1}{y} \frac{6}{3} = \lim_{y \to \infty} \frac{2}{y} = 0$.
Therefore, $\lim_{y \to \infty} h(y) = 0 - 0 = 0$.

Since $h(y)$ is strictly decreasing on $[1, \infty)$ and its limit as $y \to \infty$ is 0, it must be that $h(y) > 0$ for all $y \in [1, \infty)$.
To see this, suppose for contradiction that there exists some $y_0 \ge 1$ such that $h(y_0) \le 0$. Since $h(y)$ is strictly decreasing, for any $y > y_0$, we must have $h(y) < h(y_0) \le 0$. This contradicts the fact that $\lim_{y \to \infty} h(y) = 0$. Thus, $h(y)$ must be strictly positive for all $y \ge 1$.

Since $h(y) = (\ln g(y))'$, we have shown that $(\ln g(y))' > 0$ for all $y \ge 1$.
This implies that $\ln g(y)$ is a strictly increasing function on $[1, \infty)$.
Since the natural logarithm function $\ln(x)$ is strictly increasing, $g(y)$ must also be a strictly increasing function on $[1, \infty)$.
Finally, since $a_n = g(n)$, and $g(y)$ is strictly increasing for $y \ge 1$, we have $g(n+1) > g(n)$ for all integers $n \ge 1$.
Therefore, $a_{n+1} > a_n$ for all $n \ge 1$.
This proves that the sequence $(a_n)$ is strictly increasing.

Final check:
$h(1) = 2 \ln(2) - \frac{3(2(1)+1)}{3(1)^2+3(1)+1} = 2 \ln 2 - \frac{9}{7} = \ln 4 - 9/7$. Since $e \approx 2.718$, $e^2 \approx 7.389$. $4 < e^2$, so $\ln 4 < 2$. $9/7 \approx 1.28$. $\ln 4 \approx 1.386$. So $h(1) \approx 1.386 - 1.286 = 0.1 > 0$. This is consistent with $h(y)>0$.

Conclusion: The sequence $(a_n)$ is strictly increasing.

```markdown
Let the sequence be denoted by $(a_n)$, where
\[ a_n=\frac{\left(1+\frac 1n\right)^{3n+2}}{\left(1+\frac 1n\right)^n+\left(1+\frac 1n\right)^{n+1}+\left(1+\frac 1n\right)^{n+2}} \]
We want to prove that $a_{n+1} > a_n$ for all $n \ge 1$.
Let $x_n = 1 + \frac{1}{n}$. Then $x_n > 1$ for $n \ge 1$. We can rewrite $a_n$ as:
\[ a_n = \frac{x_n^{3n+2}}{x_n^n + x_n^{n+1} + x_n^{n+2}} = \frac{x_n^{3n+2}}{x_n^n (1 + x_n + x_n^2)} = \frac{x_n^{2n+2}}{1 + x_n + x_n^2} \]
Substituting $x_n = 1+\frac{1}{n}$, we get:
\[ a_n = \frac{\left(1+\frac 1n\right)^{2n+2}}{1 + \left(1+\frac 1n\right) + \left(1+\frac 1n\right)^2} \]
The denominator is $1 + (1+\frac{1}{n}) + (1+\frac{2}{n}+\frac{1}{n^2}) = 3 + \frac{3}{n} + \frac{1}{n^2}$.
So,
\[ a_n = \frac{\left(1+\frac 1n\right)^{2n+2}}{3 + \frac{3}{n} + \frac{1}{n^2}} \]
To show $(a_n)$ is strictly increasing, we consider the function $g(y)$ for real $y \ge 1$ by replacing $n$ with $y$:
\[ g(y) = \frac{\left(1+\frac 1y\right)^{2y+2}}{3 + \frac{3}{y} + \frac{1}{y^2}} \]
Then $a_n = g(n)$. We will show that $g(y)$ is strictly increasing for $y \ge 1$.
We can write $g(y)$ as:
\[ g(y) = \frac{\left(\frac{y+1}{y}\right)^{2y+2}}{\frac{3y^2+3y+1}{y^2}} = \frac{(y+1)^{2y+2}}{y^{2y+2}} \frac{y^2}{3y^2+3y+1} = \frac{(y+1)^{2y+2}}{y^{2y}(3y^2+3y+1)} \]
To show $g(y)$ is strictly increasing, we examine the derivative of its natural logarithm, $\ln g(y)$.
\[ \ln g(y) = (2y+2) \ln(y+1) - 2y \ln y - \ln(3y^2+3y+1) \]
The derivative with respect to $y$ is:
\begin{align*} (\ln g(y))' &= \left( 2 \ln(y+1) + (2y+2) \frac{1}{y+1} \right) - \left( 2 \ln y + 2y \frac{1}{y} \right) - \frac{6y+3}{3y^2+3y+1} \\ &= 2 \ln(y+1) + 2 - 2 \ln y - 2 - \frac{6y+3}{3y^2+3y+1} \\ &= 2 (\ln(y+1) - \ln y) - \frac{3(2y+1)}{3y^2+3y+1} \\ &= 2 \ln\left(1+\frac{1}{y}\right) - \frac{6y+3}{3y^2+3y+1} \end{align*}
Let $h(y) = (\ln g(y))'$. We want to show $h(y)>0$ for $y \ge 1$. We compute the derivative of $h(y)$:
\begin{align*} h'(y) &= 2 \frac{1}{1+\frac{1}{y}} \left(-\frac{1}{y^2}\right) - \frac{6(3y^2+3y+1) - (6y+3)(6y+3)}{(3y^2+3y+1)^2} \\ &= -\frac{2}{y(y+1)} - \frac{18y^2+18y+6 - (36y^2+36y+9)}{(3y^2+3y+1)^2} \\ &= -\frac{2}{y(y+1)} - \frac{-18y^2-18y-3}{(3y^2+3y+1)^2} \\ &= -\frac{2}{y(y+1)} + \frac{3(6y^2+6y+1)}{(3y^2+3y+1)^2} \end{align*}
The numerator of $h'(y)$ is $N(y) = -2(3y^2+3y+1)^2 + 3y(y+1)(6y^2+6y+1)$. Let $z=y(y+1)$. Then $N(y) = -2(3z+1)^2 + 3z(6z+1) = -2(9z^2+6z+1) + 18z^2+3z = -18z^2-12z-2+18z^2+3z = -9z-2$. Substituting back $z=y^2+y$, we get $N(y) = -9(y^2+y)-2 = -9y^2-9y-2$.
For $y \ge 1$, $y^2 \ge 1$ and $y \ge 1$, so $9y^2+9y+2 > 0$. Hence $N(y) < 0$.
The denominator of $h'(y)$ is $y(y+1)(3y^2+3y+1)^2$. For $y \ge 1$, this denominator is positive.
Thus, $h'(y) < 0$ for all $y \ge 1$. This means $h(y)$ is a strictly decreasing function on $[1, \infty)$.
We examine the limit of $h(y)$ as $y \to \infty$:
\[ \lim_{y \to \infty} h(y) = \lim_{y \to \infty} \left[ 2 \ln\left(1+\frac{1}{y}\right) - \frac{6y+3}{3y^2+3y+1} \right] \]
As $y \to \infty$, $\ln(1+1/y) \to \ln(1)=0$. The term $\frac{6y+3}{3y^2+3y+1} = \frac{1}{y} \frac{6+3/y}{3+3/y+1/y^2} \to 0$.
So, $\lim_{y \to \infty} h(y) = 0$.
Since $h(y)$ is strictly decreasing on $[1, \infty)$ and its limit is 0, it must be that $h(y) > 0$ for all $y \in [1, \infty)$.
Since $h(y) = (\ln g(y))'$, we have $(\ln g(y))' > 0$ for all $y \ge 1$. This implies that $\ln g(y)$ is strictly increasing on $[1, \infty)$.
Since $\ln(x)$ is a strictly increasing function, $g(y)$ must also be strictly increasing on $[1, \infty)$.
As $a_n = g(n)$, we have $a_{n+1} = g(n+1) > g(n) = a_n$ for all integers $n \ge 1$.
Therefore, the sequence $(a_n)$ is strictly increasing.

Final Answer: The final answer is $\boxed{The sequence $(a_n)$ is strictly increasing.}$
```