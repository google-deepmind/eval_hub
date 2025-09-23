Let $P=(p, 1/p)$ and $Q=(q, 1/q)$ be two distinct points on the positive branch of the hyperbola $\mathcal{H}$, so $p, q > 0$ and $p \neq q$. The derivative of $y=1/x$ is $y'=-1/x^2$.

The tangent line $k$ at $P(p, 1/p)$ has slope $m_P = -1/p^2$. Its equation is $y - 1/p = (-1/p^2)(x - p)$, which simplifies to $y = -x/p^2 + 2/p$.
The tangent line $l$ at $Q(q, 1/q)$ has slope $m_Q = -1/q^2$. Its equation is $y - 1/q = (-1/q^2)(x - q)$, which simplifies to $y = -x/q^2 + 2/q$.

The point $R$ is the intersection of $k$ and $l$. Equating the $y$-values:
$-x/p^2 + 2/p = -x/q^2 + 2/q$
$x(1/q^2 - 1/p^2) = 2(1/q - 1/p)$
$x \frac{p^2 - q^2}{p^2 q^2} = 2 \frac{p - q}{pq}$
Since $p \neq q$, $p-q \neq 0$. We can divide by $p-q$:
$x \frac{p+q}{p^2 q^2} = \frac{2}{pq} \implies x_R = \frac{2pq}{p+q}$.
Substitute $x_R$ into the equation for $k$:
$y_R = -\frac{1}{p^2}\left(\frac{2pq}{p+q}\right) + \frac{2}{p} = -\frac{2q}{p(p+q)} + \frac{2p}{p(p+q)} = \frac{2p-2q}{p(p+q)}$. There is a calculation mistake here.
$y_R = -\frac{2q}{p(p+q)} + \frac{2}{p} = \frac{-2q + 2(p+q)}{p(p+q)} = \frac{2p}{p(p+q)} = \frac{2}{p+q}$.
So $R = \left(\frac{2pq}{p+q}, \frac{2}{p+q}\right)$.

The radius of the circumcircle of $\triangle PQR$ is given by $r = \frac{a b c}{4K}$, where $a,b,c$ are side lengths and $K$ is the area. Alternatively, $r = \frac{d}{2\sin\theta}$, where $d$ is the length of a side and $\theta$ is the angle opposite that side. Let's use $r = \frac{PQ}{2\sin R}$.

The distance $PQ$ is $\sqrt{(p-q)^2 + (1/p-1/q)^2} = \sqrt{(p-q)^2 + \frac{(p-q)^2}{p^2q^2}} = |p-q|\sqrt{1+\frac{1}{p^2q^2}} = \frac{|p-q|\sqrt{p^2q^2+1}}{pq}$.

The angle $R$ is the angle between the tangent lines $k$ and $l$. The slopes are $m_P = -1/p^2$ and $m_Q = -1/q^2$. The angle $\theta$ between two lines with slopes $m_1, m_2$ is given by $\tan\theta = \frac{m_1-m_2}{1+m_1m_2}$. The angle $R$ of the triangle is the angle between vectors along the lines $k$ and $l$ originating from $R$.
$\tan R = \left|\frac{-1/p^2 - (-1/q^2)}{1+(-1/p^2)(-1/q^2)}\right| = \left|\frac{1/q^2 - 1/p^2}{1+1/(p^2q^2)}\right| = \left|\frac{(p^2-q^2)/p^2q^2}{(p^2q^2+1)/p^2q^2}\right| = \frac{|p^2-q^2|}{p^2q^2+1}$.
Since $\tan R \ge 0$, $R$ is an angle in $[0, \pi/2]$. $\sin R = \frac{\tan R}{\sqrt{1+\tan^2 R}}$.
$\sin^2 R = \frac{(p^2-q^2)^2/(p^2q^2+1)^2}{1+(p^2-q^2)^2/(p^2q^2+1)^2} = \frac{(p^2-q^2)^2}{(p^2q^2+1)^2+(p^2-q^2)^2}$.
$(p^2q^2+1)^2+(p^2-q^2)^2 = p^4q^4+2p^2q^2+1 + p^4-2p^2q^2+q^4 = p^4q^4+p^4+q^4+1 = (p^4+1)(q^4+1)$.
$\sin R = \sqrt{\frac{(p^2-q^2)^2}{(p^4+1)(q^4+1)}} = \frac{|p^2-q^2|}{\sqrt{(p^4+1)(q^4+1)}}$.

The circumradius $r(P,Q) = \frac{PQ}{2\sin R} = \frac{\frac{|p-q|\sqrt{p^2q^2+1}}{pq}}{2\frac{|p^2-q^2|}{\sqrt{(p^4+1)(q^4+1)}}} = \frac{|p-q|\sqrt{p^2q^2+1}\sqrt{(p^4+1)(q^4+1)}}{2pq|p-q|(p+q)}$.
Since $p\neq q$, $|p-q|>0$. $p^2-q^2=(p-q)(p+q)$, so $|p^2-q^2|=|p-q|(p+q)$.
$r(p,q) = \frac{\sqrt{(p^2q^2+1)(p^4+1)(q^4+1)}}{2pq(p+q)}$ for $p,q>0, p\neq q$.

To find the infimum, let $p=e^u, q=e^v$ with $u,v \in \mathbb{R}, u\neq v$.
$r(u,v) = \frac{\sqrt{(e^{2(u+v)}+1)(e^{4u}+1)(e^{4v}+1)}}{2e^{u+v}(e^u+e^v)}$.
Let $s=(u+v)/2$ and $t=(u-v)/2$. Then $u=s+t, v=s-t$. $t \neq 0$.
$u+v=2s, u-v=2t$. $e^{u+v}=e^{2s}, e^u=e^{s+t}, e^v=e^{s-t}$.
$p=e^{s+t}, q=e^{s-t}$.
$r(s,t) = \frac{\sqrt{(e^{4s}+1)(e^{4(s+t)}+1)(e^{4(s-t)}+1)}}{2e^{2s}(e^{s+t}+e^{s-t})}$.
$e^{s+t}+e^{s-t} = e^s(e^t+e^{-t}) = 2e^s\cosh t$.
$r(s,t) = \frac{\sqrt{(e^{4s}+1)(e^{4s+4t}+1)(e^{4s-4t}+1)}}{2e^{2s}(2e^s\cosh t)} = \frac{\sqrt{(e^{4s}+1)(e^{4s+4t}+1)(e^{4s-4t}+1)}}{4e^{3s}\cosh t}$.

Consider the case $s=0$, which means $u+v=0$, so $v=-u$, i.e., $q=1/p$. In this case $pq=1$.
$r(0,t) = \frac{\sqrt{(1+1)(e^{4t}+1)(e^{-4t}+1)}}{4\cosh t} = \frac{\sqrt{2(e^{4t}+1)(e^{-4t}+1)}}{4\cosh t}$.
$(e^{4t}+1)(e^{-4t}+1) = e^{-4t}(e^{4t}+1)^2 = e^{-4t}(e^{8t}+2e^{4t}+1) = e^{4t}+2+e^{-4t} = (e^{2t}+e^{-2t})^2$. No, this is wrong.
$(e^{4t}+1)(e^{-4t}+1) = 1+e^{4t}+e^{-4t}+1 = e^{4t}+e^{-4t}+2$. This is wrong too.
$(e^{4t}+1)(e^{-4t}+1)=1+e^{4t}e^{-4t}+e^{4t}+e^{-4t} = 1+1+e^{4t}+e^{-4t} = 2+e^{4t}+e^{-4t}$.
$\sqrt{2(e^{4t}+1)(e^{-4t}+1)} = \sqrt{2(e^{4t}+e^{-4t}+2)}$. This seems not easily simplified.
Let's go back to $\sqrt{2(e^{4t}+1)(e^{-4t}+1)} = \sqrt{2 e^{-4t}(e^{4t}+1)^2} = \sqrt{2} e^{-2t} (e^{4t}+1) = \sqrt{2}(e^{2t}+e^{-2t}) = 2\sqrt{2}\cosh(2t)$.
So $r(0,t) = \frac{2\sqrt{2}\cosh(2t)}{4\cosh t} = \frac{\sqrt{2}\cosh(2t)}{2\cosh t}$.
Let $X=\cosh t$. Since $t \neq 0$, $\cosh t > 1$. We minimize $f(X) = \frac{\sqrt{2}(2X^2-1)}{2X} = \frac{\sqrt{2}}{2}(2X - 1/X)$ for $X>1$.
$f'(X) = \frac{\sqrt{2}}{2}(2 + 1/X^2) > 0$ for $X>1$.
$f(X)$ is strictly increasing for $X>1$. The infimum is approached as $X \to 1^+$.
The infimum value for $f(X)$ is $\frac{\sqrt{2}}{2}(2(1)-1/1) = \frac{\sqrt{2}}{2}$.

To show that the infimum must occur at $s=0$. Let $x=e^{4s}$ and $y=e^{4t}$ for $y>0, y\neq 1$.
$r^2 = \frac{(x+1)(xy+1)(x/y+1)}{4x^{3/2}(y^{1/2}+y^{-1/2})^2} = \frac{(x+1)(x^2+x(y+1/y)+1)}{4x^{3/2}(y+1/y+2)}$.
Let $g(x) = \frac{(x+1)(x^2+x(y+1/y)+1)}{x^{3/2}}$ for fixed $y$. We want to minimize $g(x)$ for $x>0$.
$g(x) = (x^{1/2}+x^{-1/2})(x^2+x(y+1/y)+1) = x^{5/2}+x^{3/2}(y+1/y)+x^{1/2} + x^{3/2}+x^{1/2}(y+1/y)+x^{-1/2}$.
$g(x) = x^{5/2} + x^{3/2}(y+1/y+1) + x^{1/2}(y+1/y+1) + x^{-1/2}$.
$g'(x) = \frac{5}{2}x^{3/2} + \frac{3}{2}x^{1/2}(y+1/y+1) + \frac{1}{2}x^{-1/2}(y+1/y+1) - \frac{1}{2}x^{-3/2}$.
This does not look easy to show minimum at $x=1$.

Let's check the derivatives of $r(x,y)^2 = \frac{(x+1)(xy+1)(x/y+1)}{4x^{3/2}(y^{1/2}+y^{-1/2})^2}$.
Let $y$ be fixed, $y \neq 1$. Let $h(x) = (x+1)(xy+1)(x/y+1)/x^{3/2}$.
$h(x) = (x+1)(x^2 + x(y+1/y)+1) x^{-3/2} = (x^3 + x^2(y+1/y+1) + x(y+1/y+1) + 1)x^{-3/2}$.
$h(x) = x^{3/2} + x^{1/2}(y+1/y+1) + x^{-1/2}(y+1/y+1) + x^{-3/2}$.
$h'(x) = \frac{3}{2}x^{1/2} + \frac{1}{2}x^{-1/2}(y+1/y+1) - \frac{1}{2}x^{-3/2}(y+1/y+1) - \frac{3}{2}x^{-5/2}$.
$h'(x) = \frac{3}{2}(x^{1/2}-x^{-5/2}) + \frac{1}{2}(y+1/y+1)(x^{-1/2}-x^{-3/2})$.
$h'(x) = \frac{3}{2}x^{-5/2}(x^3-1) + \frac{1}{2}(y+1/y+1)x^{-3/2}(x-1)$.
$h'(x) = \frac{x-1}{2x^{5/2}}[3(x^2+x+1) + x(y+1/y+1)]$.
$h'(x)=0$ if $x=1$ or $3x^2+x(y+1/y+1)+3=0$. Since $y>0$, $y+1/y+1 \ge 2+1=3$. The quadratic equation has no positive solution.
$3x^2+x(y+1/y+1)+3>0$ for $x>0$.
Thus $h'(x)=0$ only for $x=1$.
If $x>1$, $h'(x)>0$. If $x<1$, $h'(x)<0$. Thus $x=1$ is a minimum.
$x=e^{4s}$, so $e^{4s}=1 \implies s=0$.
So for any fixed $t \neq 0$, the minimum of $r(s,t)$ with respect to $s$ occurs at $s=0$.
The minimum value of $r(s,t)$ for $t \neq 0$ is $\inf_{t \neq 0} r(0,t) = \inf_{t \neq 0} \frac{\sqrt{2}\cosh(2t)}{2\cosh t}$.
Let $X=\cosh t$. $t\neq 0 \implies X>1$. The infimum is $\inf_{X>1} \frac{\sqrt{2}}{2}(2X - 1/X)$.
As $X \to 1^+$, $2X-1/X \to 2-1=1$.
The infimum is $\frac{\sqrt{2}}{2}$. This value is not attained because $p \neq q$ requires $t \neq 0$, hence $\cosh t > 1$.

The final answer is $\boxed{\frac{\sqrt{2}}{2}}$.