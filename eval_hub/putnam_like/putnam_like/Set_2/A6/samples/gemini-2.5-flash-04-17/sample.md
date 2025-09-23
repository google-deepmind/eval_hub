Let $P(x, y)$ be the assertion $\frac{f(x)+f(y)}{f(xy)}=\frac{1}{f(x+y)}-2xy$.
The function $f: \mathbb{R}^+ \to \mathbb{R}^+$ is continuous. This means $f(x)>0$ for all $x \in \mathbb{R}^+$ and $f$ is continuous on $(0, \infty)$.

$P(1, 1) \implies \frac{f(1)+f(1)}{f(1 \cdot 1)} = \frac{1}{f(1+1)}-2(1)(1)$.
$\frac{2f(1)}{f(1)} = \frac{1}{f(2)}-2$.
$2 = \frac{1}{f(2)}-2$, which gives $\frac{1}{f(2)} = 4$, so $f(2) = \frac{1}{4}$.

Let $f(1)=c$, where $c>0$.
$P(x, 1) \implies \frac{f(x)+f(1)}{f(x \cdot 1)} = \frac{1}{f(x+1)}-2x(1)$.
$\frac{f(x)+c}{f(x)} = \frac{1}{f(x+1)}-2x$.
$1+\frac{c}{f(x)} = \frac{1}{f(x+1)}-2x$.
$\frac{1}{f(x+1)} = 1+\frac{c}{f(x)}+2x$ for all $x \in \mathbb{R}^+$.

Let $g(x) = 1/f(x)$. Since $f(x)>0$, $g(x)>0$. The equation becomes
$g(x+1) = 1+c g(x)+2x$ for all $x \in \mathbb{R}^+$.
$g(1) = 1/f(1) = 1/c$.
For $x=1$, $g(2) = 1+c g(1)+2(1) = 1+c(1/c)+2 = 1+1+2=4$. This matches $f(2)=1/4$, so $g(2)=4$.
For $x=2$, $g(3) = 1+c g(2)+2(2) = 1+c(4)+4 = 4c+5$. So $f(3) = 1/(4c+5)$.
For $x=3$, $g(4) = 1+c g(3)+2(3) = 1+c(4c+5)+6 = 1+4c^2+5c+6 = 4c^2+5c+7$. So $f(4) = 1/(4c^2+5c+7)$.

$P(x, x) \implies \frac{f(x)+f(x)}{f(x \cdot x)} = \frac{1}{f(x+x)}-2x(x)$.
$\frac{2f(x)}{f(x^2)} = \frac{1}{f(2x)}-2x^2$.

For $x=2$, $\frac{2f(2)}{f(2^2)} = \frac{1}{f(2 \cdot 2)}-2(2^2)$.
$\frac{2f(2)}{f(4)} = \frac{1}{f(4)}-8$.
$2f(2) = 1-8f(4)$.
Substitute $f(2)=1/4$: $2(1/4) = 1-8f(4) \implies 1/2 = 1-8f(4) \implies 8f(4)=1/2 \implies f(4)=1/16$.

Now we equate the two expressions for $f(4)$:
$1/(4c^2+5c+7) = 1/16$.
$4c^2+5c+7=16$.
$4c^2+5c-9=0$.
This is a quadratic equation in $c$. The solutions are $c = \frac{-5 \pm \sqrt{5^2 - 4(4)(-9)}}{2(4)} = \frac{-5 \pm \sqrt{25+144}}{8} = \frac{-5 \pm \sqrt{169}}{8} = \frac{-5 \pm 13}{8}$.
The possible values for $c$ are $c = \frac{-5+13}{8} = \frac{8}{8}=1$ and $c = \frac{-5-13}{8} = \frac{-18}{8}=-9/4$.
Since the codomain of $f$ is $\mathbb{R}^+$, $f(1)=c$ must be positive. Thus, $c=1$.

So $f(1)=1$.
The relation $g(x+1) = 1+c g(x)+2x$ becomes $g(x+1) = g(x)+2x+1$.
Let $h(x) = g(x)-x^2$.
$h(x+1) = g(x+1)-(x+1)^2 = (g(x)+2x+1)-(x^2+2x+1) = g(x)-x^2 = h(x)$.
So $h(x)$ is a periodic function with period 1, i.e., $h(x+1)=h(x)$ for all $x \in \mathbb{R}^+$.
$g(x)=x^2+h(x)$, so $f(x)=1/(x^2+h(x))$.
Since $f(x)>0$, $x^2+h(x)>0$ for all $x \in \mathbb{R}^+$.
$f(1)=1 \implies g(1)=1 \implies 1^2+h(1)=1 \implies h(1)=0$.
Since $h(x)$ has period 1, $h(n)=h(1)=0$ for all integers $n \ge 1$.
$g(n)=n^2+h(n)=n^2+0=n^2$, so $f(n)=1/n^2$ for all integers $n \ge 1$.

Substitute $f(x)=1/(x^2+h(x))$ into the original equation. Using $h(u+v)=h(u+v)$:
LHS: $\frac{1/(x^2+h(x)) + 1/(y^2+h(y))}{1/((xy)^2+h(xy))} = \frac{y^2+h(y)+x^2+h(x)}{(x^2+h(x))(y^2+h(y))} ((xy)^2+h(xy))$.
RHS: $\frac{1}{1/((x+y)^2+h(x+y))} - 2xy = (x+y)^2+h(x+y)-2xy = x^2+2xy+y^2+h(x+y)-2xy = x^2+y^2+h(x+y)$.
So $\frac{x^2+y^2+h(x)+h(y)}{(x^2+h(x))(y^2+h(y))} ((xy)^2+h(xy)) = x^2+y^2+h(x+y)$.
Since $h(x+y)=h(x+y)$, let's use $h(x+1)=h(x)$.

Let $x=n$ where $n \in \mathbb{N}$. Then $h(n)=0$ and $h(n+y)=h(y)$.
$\frac{n^2+y^2+h(n)+h(y)}{(n^2+h(n))(y^2+h(y))} ((ny)^2+h(ny)) = n^2+y^2+h(n+y)$.
$\frac{n^2+y^2+h(y)}{n^2(y^2+h(y))} ((ny)^2+h(ny)) = n^2+y^2+h(y)$.
Since $f(y)>0$, $y^2+h(y)>0$. $n \in \mathbb{N} \implies n^2>0$. The denominator $n^2(y^2+h(y))$ is positive.
If $n^2+y^2+h(y)=0$, then $n^2+y^2=-h(y)$. Since $n^2>0, y^2>0$, $n^2+y^2>0$. So $h(y)$ must be negative.
However, let $y=1$. $n^2+1+h(1)=0 \implies n^2+1=0$, which is impossible for $n \in \mathbb{N}$.
So $n^2+y^2+h(y) \ne 0$. We can divide by it:
$\frac{(ny)^2+h(ny)}{n^2(y^2+h(y))} = 1$.
$(ny)^2+h(ny) = n^2(y^2+h(y))$.
$n^2y^2+h(ny) = n^2y^2+n^2h(y)$.
$h(ny) = n^2h(y)$ for all $n \in \mathbb{N}$ and $y \in \mathbb{R}^+$.

Let $y=1/n$. $h(n \cdot 1/n) = n^2 h(1/n) \implies h(1)=n^2 h(1/n)$.
Since $h(1)=0$, we have $0 = n^2 h(1/n)$, which implies $h(1/n)=0$ for all $n \in \mathbb{N}$.
Let $x=m/n$ be any positive rational number, $m,n \in \mathbb{N}$.
$h(m/n) = h(m \cdot (1/n))$. Using $h(ny)=n^2h(y)$ with $n=m$ and $y=1/n$:
$h(m/n) = m^2 h(1/n) = m^2 \cdot 0 = 0$.
So $h(x)=0$ for all $x \in \mathbb{Q}^+$.

We know that $h(x)=1/f(x)-x^2$. Since $f$ is continuous, $h$ is also continuous.
The set of positive rational numbers $\mathbb{Q}^+$ is dense in $\mathbb{R}^+$.
Since $h$ is continuous on $\mathbb{R}^+$ and $h(x)=0$ for all $x \in \mathbb{Q}^+$, it must be that $h(x)=0$ for all $x \in \mathbb{R}^+$.
For any $x \in \mathbb{R}^+$, there exists a sequence $(q_n)$ in $\mathbb{Q}^+$ such that $q_n \to x$.
By continuity of $h$, $h(x) = \lim_{n\to\infty} h(q_n)$. Since $q_n \in \mathbb{Q}^+$, $h(q_n)=0$.
$h(x) = \lim_{n\to\infty} 0 = 0$.

So $h(x)=0$ for all $x \in \mathbb{R}^+$.
$1/f(x)-x^2=0 \implies f(x)=1/x^2$.

We verify that $f(x)=1/x^2$ is a solution.
$f: \mathbb{R}^+ \to \mathbb{R}^+$. For $x>0$, $1/x^2>0$. This condition is satisfied.
$f(x)=1/x^2$ is a continuous function on $\mathbb{R}^+$. This condition is satisfied.
Substitute into the equation:
LHS: $\frac{f(x)+f(y)}{f(xy)} = \frac{1/x^2+1/y^2}{1/(xy)^2} = \frac{(y^2+x^2)/(xy)^2}{1/(xy)^2} = x^2+y^2$.
RHS: $\frac{1}{f(x+y)}-2xy = \frac{1}{1/(x+y)^2}-2xy = (x+y)^2-2xy = x^2+2xy+y^2-2xy = x^2+y^2$.
LHS=RHS. The equation is satisfied.

Thus, the only continuous function $f: \mathbb{R}^+ \to \mathbb{R}^+$ satisfying the given equation is $f(x)=1/x^2$.

The final answer is $\boxed{f(x) = \frac{1}{x^2}}$.