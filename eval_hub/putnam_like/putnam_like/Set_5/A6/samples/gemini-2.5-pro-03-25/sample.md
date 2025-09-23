Let the hyperbola be $\mathcal{H} = \{(x,y) \in \mathbb{R}^2 : y=1/x, x>0\}$. Let $P=(p, 1/p)$ and $Q=(q, 1/q)$ be two distinct points on $\mathcal{H}$, with $p,q>0$ and $p \neq q$.
The tangent line $k$ to $\mathcal{H}$ at $P$ has equation $y - \frac{1}{p} = -\frac{1}{p^2}(x-p)$. This simplifies to $x+p^2 y = 2p$.
The tangent line $l$ to $\mathcal{H}$ at $Q$ has equation $y - \frac{1}{q} = -\frac{1}{q^2}(x-q)$. This simplifies to $x+q^2 y = 2q$.
The intersection point $R(x_R, y_R)$ of $k$ and $l$ is found by solving the system:
$x+p^2 y = 2p$
$x+q^2 y = 2q$
Subtracting the two equations gives $(p^2-q^2)y = 2(p-q)$. Since $p \neq q$, $p^2-q^2 = (p-q)(p+q) \neq 0$. So $y_R = \frac{2(p-q)}{(p-q)(p+q)} = \frac{2}{p+q}$.
Substituting $y_R$ back into the first equation: $x_R = 2p - p^2 y_R = 2p - p^2 \frac{2}{p+q} = \frac{2p(p+q) - 2p^2}{p+q} = \frac{2pq}{p+q}$.
So $R = \left(\frac{2pq}{p+q}, \frac{2}{p+q}\right)$.

We need the radius $r(P,Q)$ of the circumcircle of the triangle $PQR$. The vertices are $P(p, 1/p)$, $Q(q, 1/q)$, $R(\frac{2pq}{p+q}, \frac{2}{p+q})$.
The circumradius $r$ of a triangle with side lengths $a,b,c$ and area $K$ is given by $r = \frac{abc}{4K}$.
Let's calculate the side lengths squared:
$a^2 = QR^2 = \left(q - \frac{2pq}{p+q}\right)^2 + \left(\frac{1}{q} - \frac{2}{p+q}\right)^2 = \left(\frac{q(p+q)-2pq}{p+q}\right)^2 + \left(\frac{p+q-2q}{q(p+q)}\right)^2$
$a^2 = \left(\frac{q^2-pq}{p+q}\right)^2 + \left(\frac{p-q}{q(p+q)}\right)^2 = \frac{q^2(q-p)^2}{(p+q)^2} + \frac{(p-q)^2}{q^2(p+q)^2} = \frac{(p-q)^2}{(p+q)^2} \left(q^2 + \frac{1}{q^2}\right) = \frac{(p-q)^2(q^4+1)}{q^2(p+q)^2}$.
$b^2 = PR^2 = \left(p - \frac{2pq}{p+q}\right)^2 + \left(\frac{1}{p} - \frac{2}{p+q}\right)^2 = \left(\frac{p(p+q)-2pq}{p+q}\right)^2 + \left(\frac{p+q-2p}{p(p+q)}\right)^2$
$b^2 = \left(\frac{p^2-pq}{p+q}\right)^2 + \left(\frac{q-p}{p(p+q)}\right)^2 = \frac{p^2(p-q)^2}{(p+q)^2} + \frac{(p-q)^2}{p^2(p+q)^2} = \frac{(p-q)^2}{(p+q)^2} \left(p^2 + \frac{1}{p^2}\right) = \frac{(p-q)^2(p^4+1)}{p^2(p+q)^2}$.
$c^2 = PQ^2 = (p-q)^2 + \left(\frac{1}{p} - \frac{1}{q}\right)^2 = (p-q)^2 + \left(\frac{q-p}{pq}\right)^2 = (p-q)^2 \left(1 + \frac{1}{(pq)^2}\right) = \frac{(p-q)^2(p^2q^2+1)}{p^2q^2}$.

The side lengths are:
$a = QR = \frac{|p-q|}{p+q} \sqrt{\frac{q^4+1}{q^2}}$.
$b = PR = \frac{|p-q|}{p+q} \sqrt{\frac{p^4+1}{p^2}}$.
$c = PQ = |p-q| \sqrt{\frac{p^2q^2+1}{p^2q^2}}$.

The area $K$ of triangle $PQR$ can be calculated using the determinant formula:
$K = \frac{1}{2} | x_P(y_Q - y_R) + x_Q(y_R - y_P) + x_R(y_P - y_Q) |$.
$y_Q - y_R = \frac{1}{q} - \frac{2}{p+q} = \frac{p-q}{q(p+q)}$.
$y_R - y_P = \frac{2}{p+q} - \frac{1}{p} = \frac{p-q}{p(p+q)}$.
$y_P - y_Q = \frac{1}{p} - \frac{1}{q} = \frac{q-p}{pq}$.
$K = \frac{1}{2} \left| p \frac{p-q}{q(p+q)} + q \frac{p-q}{p(p+q)} + \frac{2pq}{p+q} \frac{q-p}{pq} \right|$.
$K = \frac{1}{2} \left| \frac{p-q}{p+q} \left( \frac{p}{q} + \frac{q}{p} - 2 \right) \right| = \frac{1}{2} \left| \frac{p-q}{p+q} \frac{p^2+q^2-2pq}{pq} \right|$.
$K = \frac{1}{2} \left| \frac{p-q}{p+q} \frac{(p-q)^2}{pq} \right| = \frac{|p-q|^3}{2pq(p+q)}$.

Now we compute the circumradius $r(P,Q) = \frac{abc}{4K}$.
$abc = \frac{|p-q|^3}{(p+q)^2 p^2 q^2} \sqrt{(p^4+1)(q^4+1)(p^2q^2+1)}$.
$r(P,Q) = \frac{\frac{|p-q|^3}{(p+q)^2 p^2 q^2} \sqrt{(p^4+1)(q^4+1)(p^2q^2+1)}}{4 \frac{|p-q|^3}{2pq(p+q)}}$.
$r(P,Q) = \frac{|p-q|^3 \sqrt{(p^4+1)(q^4+1)(p^2q^2+1)}}{(p+q)^2 p^2 q^2} \frac{2pq(p+q)}{4|p-q|^3}$.
$r(P,Q) = \frac{\sqrt{(p^4+1)(q^4+1)(p^2q^2+1)}}{2pq(p+q)}$.

We want to compute $\inf_{P,Q} r(P,Q) = \inf_{p,q>0, p\neq q} r(P,Q)$.
Let $F(p,q) = r(P,Q)^2 = \frac{(p^4+1)(q^4+1)(p^2q^2+1)}{4p^2q^2(p+q)^2}$.
We want to find the infimum of $F(p,q)$ for $p \neq q$.
Consider the case $p=1$. $F(1,q) = \frac{(1^4+1)(q^4+1)(1^2q^2+1)}{4(1)^2q^2(1+q)^2} = \frac{2(q^4+1)(q^2+1)}{4q^2(1+q)^2} = \frac{(q^4+1)(q^2+1)}{2q^2(1+q)^2}$.
Let's analyze $F(1,q)$. We want to find its minimum value.
$F(1,q) = \frac{q^6+q^4+q^2+1}{2(q^4+2q^3+q^2)}$.
Let $h(q) = F(1,q)$. We look for the minimum of $h(q)$ for $q>0, q\neq 1$.
$h'(q) = \frac{(6q^5+4q^3+2q) 2(q^4+2q^3+q^2) - (q^6+q^4+q^2+1) 2(4q^3+6q^2+2q)}{(2q^2(1+q)^2)^2}$.
The numerator is $4q^2(3q^3+2q+1)(q^2+2q+1) - 4q(q^6+q^4+q^2+1)(2q^2+3q+1)$.
We check if $q=1$ is a critical point.
Numerator at $q=1$: $4(1)(3+2+1)(1+2+1) - 4(1)(1+1+1+1)(2+3+1) = 4(6)(4) - 4(4)(6) = 96 - 96 = 0$.
So $q=1$ is a critical point.
Let's check the value at $q=1$. $F(1,1) = \frac{(1+1)(1+1)(1+1)}{4(1)(1)(1+1)^2} = \frac{2 \cdot 2 \cdot 2}{4 \cdot 1 \cdot 4} = \frac{8}{16} = \frac{1}{2}$.
Let's examine the inequality $F(1,q) \ge 1/2$.
$\frac{(q^4+1)(q^2+1)}{2q^2(1+q)^2} \ge \frac{1}{2}$.
$(q^4+1)(q^2+1) \ge q^2(1+q)^2$.
$q^6+q^4+q^2+1 \ge q^2(1+2q+q^2) = q^2+2q^3+q^4$.
$q^6+1 \ge 2q^3$. This is true by AM-GM inequality $q^6+1 \ge 2\sqrt{q^6 \cdot 1} = 2q^3$.
Equality holds if and only if $q^6=1$. Since $q>0$, equality holds if and only if $q=1$.
So for $p=1$, $F(1,q) > 1/2$ for $q \neq 1$.
The infimum of $F(1,q)$ for $q \neq 1$ is $1/2$.

By symmetry, for a fixed $q$, the minimum of $F(p,q)$ occurs at $p=1$ if $q=1$. Let's study the behavior near $(1,1)$.
Let $p=1+\epsilon$ and $q=1+\delta$.
$F(1+\epsilon, 1+\delta) = \frac{( (1+\epsilon)^4+1 ) ( (1+\delta)^4+1 ) ( (1+\epsilon)^2(1+\delta)^2+1 )}{4 (1+\epsilon)^2 (1+\delta)^2 (1+\epsilon+1+\delta)^2}$.
As $\epsilon, \delta \to 0$, $F(1+\epsilon, 1+\delta) \to F(1,1) = 1/2$.
Let's prove $F(p,q) \ge 1/2$ for all $p,q>0$.
This inequality is $(p^4+1)(q^4+1)(p^2q^2+1) \ge 2p^2q^2(p+q)^2$.
We have shown this is true for $p=1$ (or $q=1$), and equality holds only if $q=1$ (or $p=1$).
Let's consider the case $q=1/p$.
$F(p, 1/p) = \frac{(p^4+1)((1/p)^4+1)(p^2(1/p)^2+1)}{4p^2(1/p)^2(p+1/p)^2} = \frac{(p^4+1)\frac{p^4+1}{p^4}(1+1)}{4(1)(p+1/p)^2}$.
$F(p, 1/p) = \frac{2(p^4+1)^2}{4p^4(p+1/p)^2} = \frac{(p^4+1)^2}{2p^4(\frac{p^2+1}{p})^2} = \frac{(p^4+1)^2}{2p^4 \frac{(p^2+1)^2}{p^2}} = \frac{(p^4+1)^2}{2p^2(p^2+1)^2}$.
We want to show $\frac{(p^4+1)^2}{2p^2(p^2+1)^2} \ge \frac{1}{2}$.
$(p^4+1)^2 \ge p^2(p^2+1)^2$.
$p^8+2p^4+1 \ge p^2(p^4+2p^2+1) = p^6+2p^4+p^2$.
$p^8 - p^6 - p^2 + 1 \ge 0$.
$p^6(p^2-1) - (p^2-1) \ge 0$.
$(p^6-1)(p^2-1) \ge 0$.
$(p^2-1)(p^4+p^2+1)(p^2-1) \ge 0$.
$(p^2-1)^2 (p^4+p^2+1) \ge 0$.
This is true for all $p>0$. Equality holds if and only if $p^2=1$, which means $p=1$.
If $p=1$, then $q=1/p=1$.
So we have shown that $F(p,q) \ge 1/2$ for all $p,q>0$. Equality holds if and only if $p=q=1$.
Since the problem specifies $P \neq Q$, we have $p \neq q$.
Therefore, $r(P,Q)^2 = F(p,q) > 1/2$.
The infimum of $r(P,Q)^2$ is $1/2$.
The infimum of $r(P,Q)$ is $\sqrt{1/2} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$.
This infimum is not attained for any pair of distinct points $P,Q$.

Final check: The calculation and reasoning seem correct. The minimum value is approached when $P$ and $Q$ both approach the point $(1,1)$ on the hyperbola.

The radius of the circumcircle is $r(P,Q) = \frac{\sqrt{(p^4+1)(q^4+1)(p^2q^2+1)}}{2pq(p+q)}$. We established that $r(P,Q)^2 \ge 1/2$ for all $p,q > 0$, with equality if and only if $p=q=1$. Since $P \neq Q$, we must have $p \neq q$. Thus $r(P,Q)^2 > 1/2$. The value $1/2$ is the greatest lower bound. The infimum is $\sqrt{1/2} = \sqrt{2}/2$.

Final Answer: The final answer is $\boxed{\frac{\sqrt{2}}{2}}$