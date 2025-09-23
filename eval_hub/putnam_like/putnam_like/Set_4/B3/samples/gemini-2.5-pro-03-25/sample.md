Solution:
Let $f(x) = \left( x + \frac{1}{x} \right)^p$ for $x > 0$. The problem asks us to show that $\sum_{i=1}^n f(a_i) \geq \frac{(n^2+1)^p}{n^{p-1}}$ given that $a_1, a_2, \ldots, a_n > 0$ and $\sum_{i=1}^n a_i = 1$.

We will use Jensen's inequality for convex functions. Let's determine the convexity of $f(x)$ by examining its second derivative.
The first derivative is:
$$ f'(x) = p \left( x + \frac{1}{x} \right)^{p-1} \left( 1 - \frac{1}{x^2} \right) $$
The second derivative is:
$$ f''(x) = p(p-1) \left( x + \frac{1}{x} \right)^{p-2} \left( 1 - \frac{1}{x^2} \right)^2 + p \left( x + \frac{1}{x} \right)^{p-1} \left( \frac{2}{x^3} \right) $$
We can factor out $p \left( x + \frac{1}{x} \right)^{p-2}$:
$$ f''(x) = p \left( x + \frac{1}{x} \right)^{p-2} \left[ (p-1) \left( 1 - \frac{1}{x^2} \right)^2 + \left( x + \frac{1}{x} \right) \left( \frac{2}{x^3} \right) \right] $$
Let's analyze the term in the square brackets:
$$ (p-1) \left( 1 - \frac{2}{x^2} + \frac{1}{x^4} \right) + \left( \frac{2}{x^2} + \frac{2}{x^4} \right) $$
$$ = (p-1) + \frac{-2(p-1)+2}{x^2} + \frac{(p-1)+2}{x^4} $$
$$ = (p-1) + \frac{4-2p}{x^2} + \frac{p+1}{x^4} $$
Let $y = 1/x^2$. Since $x>0$, we have $y>0$. The expression becomes a quadratic in $y$:
$$ h(y) = (p+1)y^2 + (4-2p)y + (p-1) $$
Since $p>0$, $x+1/x > 0$. Thus, $f''(x)$ has the same sign as $h(1/x^2)$.
$$ f''(x) = p \left( x + \frac{1}{x} \right)^{p-2} h(1/x^2) $$

We consider two cases based on the value of $p$.

Case 1: $p \geq 1$.
In this case, $p+1 > 0$ and $p-1 \ge 0$.
The discriminant of the quadratic $h(y)$ is $\Delta = (4-2p)^2 - 4(p+1)(p-1) = 16 - 16p + 4p^2 - 4(p^2-1) = 16 - 16p + 4p^2 - 4p^2 + 4 = 20 - 16p$.
If $\Delta \le 0$, then $h(y) \ge 0$ for all $y$ since the leading coefficient $p+1$ is positive. $\Delta \le 0$ when $20 - 16p \le 0$, which means $p \ge 20/16 = 5/4$. So for $p \ge 5/4$, $h(y) \ge 0$ for all $y>0$.
If $1 \le p < 5/4$, then $\Delta > 0$. The roots of $h(y)=0$ are $y_{1,2} = \frac{-(4-2p) \pm \sqrt{\Delta}}{2(p+1)}$.
Since $p \ge 1$, $p-1 \ge 0$. $p+1 > 0$. $4-2p$ is non-positive for $p \ge 2$. For $1 \le p < 2$, $4-2p > 0$.
Let's analyze the roots for $1 \le p < 5/4$. The term $4-2p > 0$.
Compare $(4-2p)^2$ and $\Delta = 20-16p$.
$(4-2p)^2 - \Delta = (16-16p+4p^2) - (20-16p) = 4p^2 - 4 = 4(p^2-1)$.
Since $p \ge 1$, $p^2 \ge 1$, so $4(p^2-1) \ge 0$. Thus $(4-2p)^2 \ge \Delta$.
This means $4-2p \ge \sqrt{\Delta}$.
The roots are $y_1 = \frac{-(4-2p) - \sqrt{\Delta}}{2(p+1)}$ and $y_2 = \frac{-(4-2p) + \sqrt{\Delta}}{2(p+1)}$.
Since $4-2p \ge \sqrt{\Delta} \ge 0$, both $-(4-2p)-\sqrt{\Delta} \le 0$ and $-(4-2p)+\sqrt{\Delta} \le 0$.
Thus, both roots $y_1, y_2$ are non-positive ($y_2=0$ if $p=1$).
Since $h(y)$ is a quadratic with a positive leading coefficient $(p+1>0)$, $h(y) \ge 0$ for $y \ge y_2$. Since $y=1/x^2 > 0$, and $y_2 \le 0$, it means $h(y) \ge 0$ for all $y>0$.
Therefore, for all $p \ge 1$, $h(y) \ge 0$ for $y>0$. This means $f''(x) \ge 0$ for all $x>0$.
So $f(x)$ is convex on $(0, \infty)$ for $p \ge 1$.

By Jensen's inequality for convex functions, for $a_i > 0$ with $\sum_{i=1}^n a_i = 1$:
$$ \frac{1}{n} \sum_{i=1}^n f(a_i) \geq f\left( \frac{1}{n} \sum_{i=1}^n a_i \right) = f\left( \frac{1}{n} \right) $$
$$ \sum_{i=1}^n f(a_i) \geq n f\left( \frac{1}{n} \right) = n \left( \frac{1}{n} + n \right)^p = n \left( \frac{1+n^2}{n} \right)^p = n \frac{(n^2+1)^p}{n^p} = \frac{(n^2+1)^p}{n^{p-1}} $$
This proves the inequality for $p \geq 1$.

Case 2: $0 < p < 1$.
In this case, $p-1 < 0$. $p+1 > 0$. $4-2p > 0$. The discriminant $\Delta = 20-16p > 0$ since $p<1 < 5/4$.
The roots $y_{1,2}$ are real and distinct.
$y_1 = \frac{-(4-2p) - \sqrt{\Delta}}{2(p+1)}$. Since $4-2p>0$ and $\sqrt{\Delta}>0$, $y_1 < 0$.
$y_2 = \frac{-(4-2p) + \sqrt{\Delta}}{2(p+1)}$. To determine the sign of $y_2$, we compare $\sqrt{\Delta}$ with $4-2p$.
$\Delta - (4-2p)^2 = (20-16p) - (16-16p+4p^2) = 4 - 4p^2 = 4(1-p^2)$.
Since $0 < p < 1$, $p^2 < 1$, so $1-p^2 > 0$. Thus $\Delta > (4-2p)^2$.
Since $4-2p > 0$, this implies $\sqrt{\Delta} > 4-2p$.
Therefore, the numerator $-(4-2p) + \sqrt{\Delta} > 0$. So $y_2 > 0$.
$h(y) = (p+1)(y-y_1)(y-y_2)$. Since $p+1>0$, $y_1<0$, $y_2>0$. $h(y) < 0$ for $y \in (y_1, y_2)$. $h(y) > 0$ for $y \in (-\infty, y_1) \cup (y_2, \infty)$.
Since we consider $y = 1/x^2 > 0$, $h(y) < 0$ for $y \in (0, y_2)$ and $h(y) > 0$ for $y \in (y_2, \infty)$.
This means $f''(x) < 0$ if $1/x^2 \in (0, y_2)$, which means $x^2 > 1/y_2$, so $x > 1/\sqrt{y_2}$.
And $f''(x) > 0$ if $1/x^2 \in (y_2, \infty)$, which means $x^2 < 1/y_2$, so $x < 1/\sqrt{y_2}$.
Let $x_0 = 1/\sqrt{y_2}$. Then $f(x)$ is convex on $(0, x_0)$ and concave on $(x_0, \infty)$.

Let's determine if $x_0$ is greater or smaller than 1. This is equivalent to checking if $y_2$ is smaller or greater than 1.
We need to compare $y_2$ with 1.
$y_2 < 1 \iff \frac{-(4-2p) + \sqrt{20-16p}}{2(p+1)} < 1$.
$\iff \sqrt{20-16p} < 2(p+1) + (4-2p) = 2p+2+4-2p = 6$.
Squaring both sides (both are positive): $20-16p < 36$.
$-16p < 16$, which means $p > -1$.
This is true since $p>0$. So $y_2 < 1$.
Since $y_2 < 1$, $1/y_2 > 1$, and $x_0 = 1/\sqrt{y_2} > 1$.

The function $f(x)$ is convex on the interval $(0, x_0)$, where $x_0 > 1$.
The given condition is $\sum_{i=1}^n a_i = 1$ with $a_i > 0$.
This implies that for each $i$, $0 < a_i \le 1$.
If $a_k > 1$ for some $k$, then $\sum a_i > a_k > 1$, which contradicts the condition.
If $a_k = 1$, then $\sum_{j \ne k} a_j = 0$. Since $a_j > 0$, this is only possible if $n=1$, so $a_1=1$.
If $n>1$, then $0 < a_i < 1$ for all $i$.
In all cases, $a_i \in (0, 1]$ for all $i$.
The interval $(0, 1]$ is a subset of the interval $(0, x_0)$, since $x_0 > 1$.
Therefore, $f(x)$ is convex on $(0, 1]$.
The average of the $a_i$ values is $\bar{a} = \frac{1}{n} \sum_{i=1}^n a_i = \frac{1}{n}$.
Since $n \ge 1$, $0 < 1/n \le 1$. So $\bar{a} \in (0, 1]$.
Since all $a_i \in (0, 1]$, $\bar{a} \in (0, 1]$, and $f(x)$ is convex on $(0, 1]$, we can apply Jensen's inequality:
$$ \frac{1}{n} \sum_{i=1}^n f(a_i) \geq f\left( \bar{a} \right) = f\left( \frac{1}{n} \right) $$
$$ \sum_{i=1}^n f(a_i) \geq n f\left( \frac{1}{n} \right) = n \left( \frac{1}{n} + n \right)^p = n \left( \frac{1+n^2}{n} \right)^p = n \frac{(n^2+1)^p}{n^p} = \frac{(n^2+1)^p}{n^{p-1}} $$
This proves the inequality for $0 < p < 1$.

Combining Case 1 and Case 2, the inequality holds for all $p>0$.

Final Result: The final result is $\boxed{\sum_{i=1}^n \left( a_i + \frac{1}{a_i} \right)^p \geq \frac{(n^2+1)^p}{n^{p-1}}}$