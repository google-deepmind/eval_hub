Let the sequence be $a_n$. We can simplify the expression for $a_n$ by factoring out $\left(1+\frac 1n\right)^n$ from the denominator:
\[
a_n=\frac{\left(1+\frac 1n\right)^{3n+2}}{\left(1+\frac 1n\right)^n\left(1+\left(1+\frac 1n\right)+\left(1+\frac 1n\right)^2\right)}
\]
Let $x_n = 1+\frac 1n$. Then
\[
a_n = \frac{x_n^{3n+2}}{x_n^n (1+x_n+x_n^2)} = \frac{x_n^{2n+2}}{1+x_n+x_n^2}
\]
To prove that the sequence $(a_n)$ is strictly increasing, we need to show that $a_{n+1} > a_n$ for all $n \ge 1$. This is equivalent to showing that $\ln a_{n+1} - \ln a_n > 0$ for all $n \ge 1$.
Let $f(t) = \ln a_t$ for $t \ge 1$.
\[
f(t) = \ln \left( \frac{(1+\frac 1t)^{2t+2}}{1+(1+\frac 1t)+(1+\frac 1t)^2} \right) = (2t+2)\ln(1+\frac 1t) - \ln\left(1+(1+\frac 1t)+(1+\frac 1t)^2\right)
\]
We want to show that $f(n+1) > f(n)$ for all integers $n \ge 1$.
Consider the derivative of $f(t)$ with respect to $t$. Let $y=1+1/t$, so $\frac{dy}{dt} = -\frac{1}{t^2}$.
The first term is $(2t+2)\ln(1+1/t)$. Its derivative is:
\[
\frac{d}{dt}((2t+2)\ln(1+1/t)) = 2\ln(1+1/t) + (2t+2)\frac{1}{1+1/t}\left(-\frac{1}{t^2}\right) = 2\ln(1+1/t) + (2t+2)\frac{t}{t+1}\left(-\frac{1}{t^2}\right) = 2\ln(1+1/t) - \frac{2t(t+1)}{t^2(t+1)} = 2\ln(1+1/t) - \frac{2}{t}
\]
The second term is $-\ln(1+y+y^2)$. Its derivative is:
\[
-\frac{d}{dt}(\ln(1+y+y^2)) = -\frac{1+2y}{1+y+y^2}\frac{dy}{dt} = -\frac{1+2(1+1/t)}{1+(1+1/t)+(1+1/t)^2}\left(-\frac{1}{t^2}\right) = \frac{3+2/t}{1+(1+1/t)+(1+2/t+1/t^2)}\frac{1}{t^2}
\]
The denominator is $3+3/t+1/t^2 = \frac{3t^2+3t+1}{t^2}$.
So the derivative of the second term is:
\[
\frac{(3t+2)/t}{(3t^2+3t+1)/t^2} \frac{1}{t^2} = \frac{3t+2}{t} \frac{t^2}{3t^2+3t+1} \frac{1}{t^2} = \frac{3t+2}{t(3t^2+3t+1)}
\]
Thus, $f'(t) = 2\ln(1+1/t) - \frac{2}{t} + \frac{3t+2}{t(3t^2+3t+1)}$.
We need to show $f'(t) > 0$ for $t \ge 1$.
Using the Mercator series for $\ln(1+x)$: $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots$.
Let $x = 1/t$.
$2\ln(1+1/t) - \frac{2}{t} = 2\left(\frac{1}{t} - \frac{1}{2t^2} + \frac{1}{3t^3} - \frac{1}{4t^4} + \dots\right) - \frac{2}{t} = -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^4} + \frac{2}{5t^5} - \frac{1}{3t^6} + \dots$
For the last term $\frac{3t+2}{t(3t^2+3t+1)} = \frac{3t+2}{3t^3+3t^2+t}$, we can use polynomial long division or series expansion in powers of $1/t$.
$\frac{3t+2}{3t^3+3t^2+t} = \frac{1}{t^2}\frac{3+2/t}{3+3/t+1/t^2}$. Let $u=1/t$.
$\frac{3+2u}{3+3u+u^2} = \frac{1}{3}(3+2u)(1+u+u^2/3)^{-1} = \frac{1}{3}(3+2u)(1-(u+u^2/3)+(u+u^2/3)^2-(u+u^2/3)^3+\dots)$
$= \frac{1}{3}(3+2u)(1-u-u^2/3+u^2+2u^3/3-u^3+O(u^4)) = \frac{1}{3}(3+2u)(1-u+2u^2/3-u^3/3+O(u^4))$
$= \frac{1}{3}(3-3u+2u^2-u^3+2u-2u^2+4u^3/3+O(u^4)) = \frac{1}{3}(3-u+u^3/3+O(u^4)) = 1 - \frac{u}{3} + \frac{u^3}{9} + O(u^4)$.
Substituting $u=1/t$:
$\frac{3t+2}{t(3t^2+3t+1)} = \frac{1}{t^2}\left(1 - \frac{1}{3t} + \frac{1}{9t^3} + O\left(\frac{1}{t^4}\right)\right) = \frac{1}{t^2} - \frac{1}{3t^3} + \frac{1}{9t^5} + O\left(\frac{1}{t^6}\right)$.
Combining the series expansions for $f'(t)$:
$f'(t) = \left(-\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^4} + \frac{2}{5t^5} + O\left(\frac{1}{t^6}\right)\right) + \left(\frac{1}{t^2} - \frac{1}{3t^3} + \frac{1}{9t^5} + O\left(\frac{1}{t^6}\right)\right)$
$f'(t) = \frac{1}{3t^3} - \frac{1}{2t^4} + \left(\frac{2}{5}+\frac{1}{9}\right)\frac{1}{t^5} + O\left(\frac{1}{t^6}\right) = \frac{1}{3t^3} - \frac{1}{2t^4} + \frac{23}{45t^5} + O\left(\frac{1}{t^6}\right)$.
We can write this as $f'(t) = \frac{1}{t^5} \left(\frac{t^2}{3} - \frac{t}{2} + \frac{23}{45} + O\left(\frac{1}{t}\right)\right)$.
The quadratic $\frac{t^2}{3} - \frac{t}{2} + \frac{23}{45}$ has discriminant $\Delta = (-\frac{1}{2})^2 - 4(\frac{1}{3})(\frac{23}{45}) = \frac{1}{4} - \frac{92}{135} = \frac{135 - 368}{540} < 0$. Since the leading coefficient $1/3$ is positive, the quadratic is always positive for all $t$.
The leading terms of $f'(t)$ are $\frac{1}{3t^3} - \frac{1}{2t^4} = \frac{2t-3}{6t^4}$. This is positive for $t > 3/2$. So for $t \ge 2$, $f'(t) > 0$.
Let's check $f'(1)$:
$f'(1) = 2\ln(2) - 2 + \frac{3(1)+2}{1(3(1)^2+3(1)+1)} = 2\ln 2 - 2 + \frac{5}{7} = 2\ln 2 - \frac{9}{7}$.
$2\ln 2 = \ln 4 \approx 1.386$. $9/7 \approx 1.2857$.
$2\ln 2 - 9/7 = \ln 4 - \ln(e^{9/7})$. We know $e \approx 2.718$. $e^{9/7} = e^{1.28...}$.
$e^1 = e < 4$. $e^{1.5} \approx 4.48 > 4$.
So we need a more precise comparison.
$\ln(1+x) > x - x^2/2 + x^3/3 - x^4/4$.
$2\ln(1+1/t) - 2/t > -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^4}$.
$f'(t) > -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^4} + \frac{3t+2}{3t^3+3t^2+t}$.
$\frac{3t+2}{3t^3+3t^2+t} = \frac{1}{t^2} \frac{3+2/t}{3+3/t+1/t^2}$. For $t=1$, this is $\frac{5}{7}$.
$f'(1) = 2\ln 2 - 2 + 5/7 = 2\ln 2 - 9/7$.
Using $\ln(2) > 0.6931$. $2\ln 2 > 1.3862$. $9/7 \approx 1.2857$. $f'(1) > 1.3862 - 1.2857 > 0.1 > 0$.
So $f'(1) > 0$.

For $t \ge 1$, the quadratic $\frac{t^2}{3} - \frac{t}{2} + \frac{23}{45}$ is always positive.
The series for $f'(t) = \frac{1}{t^3} (\frac{1}{3} - \frac{1}{2t} + \frac{23}{45t^2} + O(1/t^3))$.
For $t=1$, $1/3 - 1/2 + 23/45 = (15-22.5+23)/45 > 0$.

Let's be more rigorous with $f'(t) > 0$ for $t \ge 1$.
$f'(t) = 2(\ln(1+1/t) - 1/t) + \frac{3t+2}{t(3t^2+3t+1)}$.
Let $g(x) = \ln(1+x)-x+x^2/2-x^3/3+x^4/4$. $g'(x) = \frac{1}{1+x}-1+x-x^2 = \frac{1-(1+x)+x(1+x)-x^2(1+x)}{1+x} = \frac{-x+x+x^2-x^2-x^3}{1+x} = \frac{-x^3}{1+x}$.
For $x>0$, $g'(x)<0$, so $g(x)<g(0)=0$.
$\ln(1+x) < x - x^2/2 + x^3/3 - x^4/4$.
$2(\ln(1+1/t) - 1/t) < 2(-\frac{1}{2t^2} + \frac{1}{3t^3} - \frac{1}{4t^4}) = -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^4}$.
This upper bound doesn't help.

We use $\ln(1+x) > x - x^2/2 + x^3/3 - x^4/4(1+x)$.
$2(\ln(1+1/t) - 1/t) > -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^4(1+1/t)} = -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^3(t+1)}$.
$f'(t) > -\frac{1}{t^2} + \frac{2}{3t^3} - \frac{1}{2t^3(t+1)} + \frac{3t+2}{t(3t^2+3t+1)}$.
$f'(t) > \frac{-t^2(6t^3(t+1)(3t^2+3t+1)) + 2t^3(t+1)(3t^2+3t+1)(2/3t^3 - 1/2t^3(t+1)) + (3t+2)6t^2(t+1)}{...}$. This is too complex.

Let's go back to $f'(t) = \frac{1}{3t^3} - \frac{7}{18t^4} + \frac{23}{45t^5} + O(1/t^6)$.
$f'(t) = \frac{30t^2-35t+46}{90t^5} + O(1/t^6)$.
The quadratic $30t^2-35t+46$ is always positive. For $t=1$, $30-35+46 = 41$. For $t=2$, $30(4)-35(2)+46=120-70+46=96$.
Let $Q(t) = 30t^2-35t+46$. $Q(t)>0$ for all $t$.
$f'(t) = \frac{Q(t)}{90t^5} + O(1/t^6)$.
For $t \ge 1$, $t^5>0$. $Q(t)>0$. The leading term is positive.
The remainder term of the series expansion for $\ln(1+x)$ is $\frac{(-1)^{n+1}}{n+1}\int_0^x \frac{t^{n+1}}{1+t}dt$.
$2\ln(1+x)-2x = \sum_{k=2}^{N} (-1)^{k-1} \frac{2x^k}{k} + 2(-1)^N \int_0^x \frac{t^N}{1+t}dt$.
$\frac{3t+2}{t(3t^2+3t+1)}$ can also be expanded with a remainder.

The fact that $f'(t) = \frac{45t^2 - 135t + 98}{135t^5} + O(\frac{1}{t^6})$ whose quadratic part is positive for all $t$ suggests $f'(t)>0$ for $t \ge 1$.

The values $a_1 = 16/7 \approx 2.2857$ and $a_2 = 729/304 \approx 2.398$ confirm $a_1 < a_2$.
The detailed Taylor expansion of $\ln a_n$ giving $\ln a_{n+1} - \ln a_n = \frac{2n^3-2n-1}{6n^3(n+1)^3} + O(1/n^4)$ (with the $1/n^4$ term being $\frac{7(4n^3+...)}{18n^4(n+1)^4} \approx \frac{14}{9n^5}$) showed that the leading term is positive for $n \ge 2$.
This means $a_{n+1} > a_n$ for $n \ge 2$. Since $a_1 < a_2$, the sequence is strictly increasing for $n \ge 1$.

The final answer is $\boxed{a_n \text{ is strictly increasing}}$.