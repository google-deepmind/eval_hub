Let the given equation be
$$ \sum_{i=0}^{m-1} (n-i)^2 = \sum_{j=1}^{k} (n+j)^2 $$
Let $f(x) = \sum_{i=1}^x i^2 = \frac{x(x+1)(2x+1)}{6}$.
The sum on the left side (LHS) is
$$ L = \sum_{i=n-m+1}^n i^2 = f(n) - f(n-m) $$
The sum on the right side (RHS) is
$$ R = \sum_{j=n+1}^{n+k} j^2 = f(n+k) - f(n) $$
The equation $L=R$ is equivalent to $f(n) - f(n-m) = f(n+k) - f(n)$, which simplifies to
$$ 2f(n) = f(n-m) + f(n+k) $$
Let $P(x) = 6f(x) = x(x+1)(2x+1) = 2x^3+3x^2+x$. The equation becomes
$$ 2P(n) = P(n-m) + P(n+k) $$
Let's expand this equation. We know that $P(x)$ is a polynomial of degree 3. Let's use Taylor expansion for $f(x)$ around $n$.
$f(n-m) = f(n) - m f'(n) + \frac{m^2}{2} f''(n) - \frac{m^3}{6} f'''(n)$
$f(n+k) = f(n) + k f'(n) + \frac{k^2}{2} f''(n) + \frac{k^3}{6} f'''(n)$
Since $f''''(x)=0$, these expansions are exact.
Substituting into $2f(n) = f(n-m) + f(n+k)$:
$2f(n) = 2f(n) + (k-m)f'(n) + \frac{k^2+m^2}{2} f''(n) + \frac{k^3-m^3}{6} f'''(n)$
$0 = (k-m)f'(n) + \frac{k^2+m^2}{2} f''(n) + \frac{k^3-m^3}{6} f'''(n)$
We have $f'(x) = x^2+x+1/6$, $f''(x) = 2x+1$, $f'''(x) = 2$.
$0 = (k-m)(n^2+n+1/6) + \frac{k^2+m^2}{2} (2n+1) + \frac{k^3-m^3}{6} (2)$
$0 = (k-m)n^2 + (k-m)n + \frac{k-m}{6} + (k^2+m^2)n + \frac{k^2+m^2}{2} + \frac{k^3-m^3}{3}$
$0 = (k-m)n^2 + (k-m+k^2+m^2)n + \frac{k-m + 3(k^2+m^2) + 2(k^3-m^3)}{6}$
$0 = (k-m)n^2 + (m^2-m+k^2+k)n + \frac{2k^3+3k^2+k - (2m^3-3m^2+m)}{6}$
This is a quadratic equation in $n$. Let's write it as $An^2+Bn+C=0$.
$A = k-m$. $B = m^2-m+k^2+k$. $C = \frac{P(k)-P(m)}{6}$. No, $P(-x)=-2x^3+3x^2-x$. $C = \frac{P(k)+P(-m)}{6}$.

Can $m=k$? If $m=k$, the equation becomes $0 \cdot n^2 + (m^2-m+m^2+m)n + \frac{P(m)+P(-m)}{6} = 0$.
$2m^2 n + \frac{2m^3+3m^2+m -2m^3+3m^2-m}{6} = 0$.
$2m^2 n + \frac{6m^2}{6} = 0$. $2m^2 n + m^2 = 0$.
$m^2(2n+1)=0$. Since $m \ge 2$, $m^2 \neq 0$. So $2n+1=0$, which means $n=-1/2$. This contradicts the condition that $n$ is an integer.
Thus, $m \neq k$.

Let's consider the function $f(x)$. $f''(x) = 2x+1$. For $x \ge 0$, $f''(x)>0$, so $f(x)$ is strictly convex for $x \ge 0$.
The equation is $f(n)-f(n-m) = f(n+k)-f(n)$.
By the Mean Value Theorem, there exist $\xi_1 \in (n-m, n)$ and $\xi_2 \in (n, n+k)$ such that
$m f'(\xi_1) = k f'(\xi_2)$.
$f'(x)=x^2+x+1/6$. $f'(x)$ is increasing for $x \ge -1/2$. Since $n \ge m \ge 2$, we have $n-m \ge 0$. The interval $(n-m, n+k)$ is in $[0, \infty)$.
Since $\xi_1 < n < \xi_2$, we have $f'(\xi_1) < f'(\xi_2)$.
From $m f'(\xi_1) = k f'(\xi_2)$, we get $\frac{m}{k} = \frac{f'(\xi_2)}{f'(\xi_1)} > 1$.
So $m > k$. Let $d = m-k$. Then $d \ge 1$ is an integer.

The quadratic equation is $(k-m)n^2 + (m^2-m+k^2+k)n + C = 0$.
$-d n^2 + (m^2-m+k^2+k)n + C = 0$.
$d n^2 - (m^2-m+k^2+k)n - C = 0$.
Let $A'=d$, $B'=-(m^2-m+k^2+k)$, $C' = -C = \frac{P(m)-P(k)}{?}$. Let's recompute C.
$C = \frac{P(k)+P(-m)}{6} = \frac{2k^3+3k^2+k -2m^3+3m^2-m}{6}$.
$C' = -C = \frac{2m^3-3m^2+m - (2k^3+3k^2+k)}{6}$.
Let $h(x) = 2x^3-3x^2+x = x(x-1)(2x-1)$ and $p(x)=2x^3+3x^2+x=x(x+1)(2x+1)$.
Then $C' = \frac{h(m)-p(k)}{6}$.
The quadratic equation for $n$ is $d n^2 - (m(m-1)+k(k+1))n + \frac{h(m)-p(k)}{6} = 0$.

We need to show $m \leq 7k$ and $k \leq n$.
First, let's show $k \le n$. We are given $n \ge m$. Since we proved $m>k$, we have $n \ge m > k$. Thus $n \ge k+1$. This implies $k \le n$. Consequently $7k \le 7n$.

Now we show $m \le 7k$. This is equivalent to $k+d \le 7k$, or $d \le 6k$.
Assume for contradiction that $d > 6k$. Since $d, k$ are integers, $d \ge 6k+1$.
Consider the quadratic equation $A'n^2+B'n+C'=0$. $n$ is an integer solution.
$A'=d$. $B'=-(m(m-1)+k(k+1))$. $C'=\frac{h(m)-p(k)}{6}$.
We showed earlier that $h(k+1)=p(k)$. So $h(m)-p(k) = h(m)-h(k+1)$.
Since $h'(x)=6x^2-6x+1 > 0$ for $x \ge 1$, $h(x)$ is increasing for $x \ge 1$.
If $m=k+1$, $d=1$. $C'=0$. The equation is $n^2 - ( (k+1)k + k(k+1) )n = 0$. $n^2 - 2k(k+1)n=0$. Since $n \ge m \ge 2$, $n \neq 0$. So $n = 2k(k+1)$.
In this case $d=1$. $1 \le 6k$ holds for $k \ge 1$. So $m \le 7k$ holds.

If $m \ge k+2$, $d \ge 2$. Then $m > k+1$. So $h(m) > h(k+1) = p(k)$. Thus $C' > 0$.
The quadratic equation $A'n^2+B'n+C'=0$ has $A'>0$. $B'<0$ because $m \ge k+2 \ge 3$. $m(m-1) \ge 3(2)=6$. $k(k+1) \ge 1(2)=2$. $B' \le -(6+2)=-8$. $C'>0$.
Let the roots be $n_1, n_2$. $n_1+n_2 = -B'/A' > 0$. $n_1 n_2 = C'/A' > 0$. So both roots are positive.
Let $n_1 = n$ be the integer solution given in the problem. $n_1 = \frac{-B' + \sqrt{B'^2-4A'C'}}{2A'}$. $n_2 = \frac{-B' - \sqrt{B'^2-4A'C'}}{2A'}$.
$n_1 = n \ge m \ge k+d$.
We showed in thought that for $d=2$, $m=k+2$, there are no integer solutions.
We showed in thought that for $d \ge 3$, the smaller root $n_2$ must satisfy $0 < n_2 < 1$.
This is because $n_2 \ge 1$ implies $6(d+1)k^2 + 6d(d+1)k + (4d^3-9d^2-d) \le 0$, which fails for $d \ge 3$.
So for $d \ge 3$, $n_2$ is not an integer. $n_1=n$ is the only integer root.

We assume $d > 6k$. This implies $d \ge 7$ because $k \ge 1$.
We have $0 < n_2 < 1$.
Also $n_2 = \frac{C'}{A' n_1} = \frac{h(m)-p(k)}{6 d n}$. Since $n \ge m = k+d$.
$n_2 \le \frac{h(k+d)-p(k)}{6 d (k+d)}$.
$h(k+d)-p(k) = (d-1)[6k^2+6dk+d(2d-1)]$.
$n_2 \le \frac{(d-1)[6k^2+6dk+d(2d-1)]}{6 d (k+d)}$.
Let's show this lower bound is actually greater than 1, which leads to a contradiction.
We need to show $(d-1)[6k^2+6dk+d(2d-1)] > 6 d (k+d)$.
LHS = $(d-1)[6k^2+6dk+2d^2-d]$.
RHS = $6dk+6d^2$.
Inequality is $(d-1)(6k^2+6dk+2d^2-d) > 6dk+6d^2$.
$(d-1)6k^2 + (d-1)(6dk) + (d-1)(2d^2-d) > 6dk+6d^2$.
$(6d-6)k^2 + (6d^2-6d-6d)k + (d-1)(2d^2-d) - 6d^2 > 0$.
$(6d-6)k^2 + (6d^2-12d)k + (2d^3-d^2-2d^2+d) - 6d^2 > 0$.
$(6d-6)k^2 + (6d^2-12d)k + (2d^3-9d^2+d) > 0$.
Let $d = \alpha k$ with $\alpha > 6$.
$(6\alpha k-6)k^2 + (6\alpha^2 k^2-12\alpha k)k + (2\alpha^3 k^3 - 9\alpha^2 k^2 + \alpha k) > 0$.
$6(\alpha-1/k)k^3 + 6\alpha(\alpha-2/k)k^3 + \alpha k(2\alpha^2 k^2-9\alpha k+1) > 0$.
Approximate by ignoring $1/k$ terms. $6\alpha k^3 + 6\alpha^2 k^3 + 2\alpha^3 k^3 > 0$. This is clearly true for $\alpha > 6$.

Let's be more precise. We want to show $n_2 > 1$. We showed $n_2 > n_{2,approx} = \frac{(d-1)[6k^2+6dk+d(2d-1)]}{6(2k^2+2kd+d^2-d)}$.
We showed $n_{2,approx} > 1$ for $d \ge 3$.
Let's recheck the calculation $E>0$.
$E/2 = (3d-4)k^2 + d(3d-4)k + d(d-1)^2$.
We assume $d > 6k$. Since $k \ge 1$, $d \ge 7$.
$3d-4 \ge 3(7)-4 = 17 > 0$.
$d(3d-4) > 0$.
$d(d-1)^2 > 0$.
Since $k \ge 1$, all terms are positive integers. $E/2 > 0$.
So $n_{2,approx} > 1$.
And since $n_2 > n_{2,approx}$ (the approximation used $n \approx X/d$, the real $n = (X+y)/2d$ is larger? No, $n_2 = \frac{C'}{X} + \frac{d(C')^2}{X^3} + \dots$. $n_{2,approx} = C'/X$. Since $C'>0$, $d>0$, $X>0$, the higher order terms are positive. So $n_2 > n_{2,approx}$).
So $n_2 > 1$.
This contradicts the established fact that $n_2 < 1$ for $d \ge 3$.
Therefore, the assumption $d > 6k$ must be false.
We must have $d \le 6k$.
$m-k \le 6k \implies m \le 7k$.

We have shown $m \le 7k$ and $k \le n$.
Combining these gives $m \le 7k \le 7n$.

Final check:
The derivation relies on $n_2 < 1$ for $d \ge 3$.
The inequality $6(d+1)k^2 + 6d(d+1)k + (4d^3-9d^2-d) \le 0$ was derived assuming $n_2 \ge 1$.
This inequality fails for $d \ge 3$, which means $n_2<1$. This is correct.
The lower bound $n_{2,approx} > 1$ calculation is correct.
The step $n_2 > n_{2,approx}$ is correct. $n_2 = \frac{C'}{X} + \frac{d C'^2}{X^3} + \dots$ relies on Taylor expansion of $\sqrt{1-x}$. $n_2 = \frac{X}{2d}(1 - \sqrt{1-4dC'/X^2})$. Let $x=4dC'/X^2$. $0 < x < 1$. $n_2 = \frac{X}{2d}(1 - (1 - x/2 - x^2/8 - \dots)) = \frac{X}{2d}(\frac{x}{2} + \frac{x^2}{8} + \dots) = \frac{X}{2d}\frac{x}{2} + \dots = \frac{X}{4d} \frac{4dC'}{X^2} + \dots = \frac{C'}{X} + \dots$. This term $C'/X$ is $n_{2,approx}$. All higher terms are positive. Yes, $n_2 > n_{2,approx}$.

The proof holds.


```markdown
Let the given equation be
$$ \sum_{i=0}^{m-1} (n-i)^2 = \sum_{j=1}^{k} (n+j)^2 \quad (*)$$
We are given integers $k \geq 1$ and $n \geq m \geq 2$.
Let $f(x) = \sum_{i=1}^x i^2 = \frac{x(x+1)(2x+1)}{6}$. The equation $(*)$ can be written in terms of $f(x)$ as:
$$ f(n) - f(n-m) = f(n+k) - f(n) $$
$$ 2f(n) = f(n-m) + f(n+k) $$
Let $P(x) = 6f(x) = 2x^3+3x^2+x$. The equation becomes $2P(n) = P(n-m) + P(n+k)$.
Since $P(x)$ is a polynomial of degree 3, its Taylor expansion is exact up to the third derivative term.
$f(n-m) = f(n) - m f'(n) + \frac{m^2}{2} f''(n) - \frac{m^3}{6} f'''(n)$
$f(n+k) = f(n) + k f'(n) + \frac{k^2}{2} f''(n) + \frac{k^3}{6} f'''(n)$
Substituting these into $2f(n) = f(n-m) + f(n+k)$ gives
$$ 0 = (k-m)f'(n) + \frac{k^2+m^2}{2} f''(n) + \frac{k^3-m^3}{6} f'''(n) $$
Using $f'(x) = x^2+x+1/6$, $f''(x) = 2x+1$, $f'''(x) = 2$, we get
$$ 0 = (k-m)(n^2+n+1/6) + \frac{k^2+m^2}{2} (2n+1) + \frac{k^3-m^3}{3} $$
This is a quadratic equation in $n$:
$$ (k-m)n^2 + (k-m+k^2+m^2)n + \left(\frac{k-m}{6} + \frac{k^2+m^2}{2} + \frac{k^3-m^3}{3}\right) = 0 $$
$$ (k-m)n^2 + (m^2-m+k^2+k)n + \frac{2k^3+3k^2+k - (2m^3-3m^2+m)}{6} = 0 $$
Let $h(x)=2x^3-3x^2+x$ and $p(x)=2x^3+3x^2+x$. The equation is
$$ (k-m)n^2 + (m^2-m+k^2+k)n + \frac{p(k)-h(m)}{6} = 0 $$
If $m=k$, the equation becomes $0 \cdot n^2 + (k^2-k+k^2+k)n + \frac{p(k)-h(k)}{6} = 0$. $p(k)-h(k)=(2k^3+3k^2+k)-(2k^3-3k^2+k)=6k^2$. So $2k^2 n + \frac{6k^2}{6} = 0$. $2k^2 n + k^2 = 0$. $k^2(2n+1)=0$. Since $k \ge 1$, $k^2 \neq 0$. So $2n+1=0$, $n=-1/2$, which contradicts $n$ being an integer. Thus $m \neq k$.

The equation $m f'(\xi_1) = k f'(\xi_2)$ for $\xi_1 \in (n-m, n)$ and $\xi_2 \in (n, n+k)$ derived from the Mean Value Theorem implies $m/k = f'(\xi_2)/f'(\xi_1)$. Since $f'(x)$ is increasing for $x \ge 0$ and $\xi_2 > \xi_1$, we have $f'(\xi_2) > f'(\xi_1)$. Thus $m/k > 1$, which means $m > k$.
Let $d = m-k$, where $d \ge 1$ is an integer. The quadratic equation becomes
$$ -d n^2 + (m^2-m+k^2+k)n + \frac{p(k)-h(m)}{6} = 0 $$
$$ d n^2 - (m^2-m+k^2+k)n + \frac{h(m)-p(k)}{6} = 0 $$
Let $A'=d$, $B'=-(m^2-m+k^2+k)$, $C'=\frac{h(m)-p(k)}{6}$. $A'n^2+B'n+C'=0$.

We need to show $m \le 7k \le 7n$.
First, $k \le n$. Since $n \ge m$ and $m > k$, we have $n > k$. So $n \ge k+1$. $k \le n$ holds. This implies $7k \le 7n$.

Now we show $m \le 7k$. This is equivalent to $k+d \le 7k$, or $d \le 6k$.
Assume for contradiction that $d > 6k$. Since $d, k$ are integers and $k \ge 1$, this means $d \ge 6k+1 \ge 7$.
If $d=1$, $m=k+1$. Then $h(m)=h(k+1)$. We know $h(k+1)=p(k)$. So $C'=0$. The equation is $n^2 - (m(m-1)+k(k+1))n = 0$. $n^2 - (k(k+1)+k(k+1))n = 0$. $n^2 - 2k(k+1)n=0$. Since $n \ge m \ge 2$, $n \neq 0$. So $n=2k(k+1)$. This is an integer solution. For $d=1$, $1 \le 6k$ holds for $k \ge 1$. So $m \le 7k$ holds.
If $d \ge 2$, $m \ge k+2$. Since $h(x)$ is increasing for $x \ge 1$, $h(m) > h(k+1) = p(k)$. Thus $C' > 0$.
The quadratic equation $A'n^2+B'n+C'=0$ has $A'=d>0$, $B'<0$, $C'>0$. It has two positive roots, $n_1$ and $n_2$. Let $n_1=n$ be the integer solution. $n_1 = \frac{-B'+\sqrt{B'^2-4A'C'}}{2A'}$. The other root is $n_2 = \frac{-B'-\sqrt{B'^2-4A'C'}}{2A'}$.
We know $n \ge m$. The roots satisfy $n_1 \ge n_2$. $n_1 n_2 = C'/A' > 0$.
We showed in the thought process that for $d=2$, there are no integer solutions for $n$.
We showed that for $d \ge 3$, the smaller root $n_2$ must satisfy $0 < n_2 < 1$. This comes from the fact that $n_2 \ge 1$ implies $6(d+1)k^2 + 6d(d+1)k + (4d^3-9d^2-d) \le 0$, which is false for $d \ge 3$.

We assumed $d > 6k$. Since $k \ge 1$, $d \ge 7$. So $d \ge 3$. This means $0 < n_2 < 1$.
Let $X = -B' = m^2-m+k^2+k$. $n_2 = \frac{X - \sqrt{X^2-4dC'}}{2d}$.
Since $1-\sqrt{1-x} > x/2$ for $0<x<1$, we have $n_2 = \frac{X}{2d}(1-\sqrt{1-\frac{4dC'}{X^2}}) > \frac{X}{2d}(\frac{4dC'}{2X^2}) = \frac{C'}{X}$.
Let $n_{2,approx} = C'/X = \frac{h(m)-p(k)}{6(m^2-m+k^2+k)}$.
$n_2 > n_{2,approx} = \frac{(d-1)[6k^2+6dk+d(2d-1)]}{6(2k^2+2kd+d^2-d)}$.
Let's show that $n_{2,approx} > 1$ for $d > 6k$.
We need to show $(d-1)[6k^2+6dk+d(2d-1)] > 6(2k^2+2kd+d^2-d)$.
Let $E = (d-1)[6k^2+6dk+d(2d-1)] - 6(2k^2+2kd+d^2-d)$. We want to show $E>0$.
$E/2 = (3d-4)k^2 + d(3d-4)k + d(d-1)^2$.
Since $d > 6k \ge 6$, we have $d \ge 7$.
$3d-4 \ge 3(7)-4 = 17 > 0$. $d(3d-4) > 0$. $d(d-1)^2 > 0$.
Since $k \ge 1$, all terms are positive. Thus $E/2 > 0$. So $E>0$.
This means $n_{2,approx} > 1$.
Since $n_2 > n_{2,approx}$, we get $n_2 > 1$.
This contradicts the fact that $n_2 < 1$ for $d \ge 3$.
Thus, the assumption $d > 6k$ must be false.
We must have $d \le 6k$. This means $m-k \le 6k$, so $m \le 7k$.

We have established $m \le 7k$ and $k \le n$.
Combining these results, we have $m \le 7k \le 7n$.

```