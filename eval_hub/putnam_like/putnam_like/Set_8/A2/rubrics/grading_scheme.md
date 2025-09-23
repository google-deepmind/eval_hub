Solution step (worth 4 points):
Consider a general equation of parabola:
$$
p(x,y) = (ax+by)^2 + cx + dy + e = 0.
$$
We know that polynomial $p(x,0)=0$ has one root equal to $\alpha$ and $p(0,y)=0$ has one root equal to $\beta$. Therefore we have
$$
a^2x^2 + cx + e = a^2(x-\alpha)^2
$$
and 
$$
b^2y^2 + dy + e = b^2(y-\beta)^2.
$$

Solution step (worth 3 points):
This gives us a system of equations
$$
\begin{cases}
c = -2\alpha a^2,\\
d = -2\beta b^2,\\
e = a^2\alpha^2,\\
e = b^2\beta^2.
\end{cases}
$$
Let $e=\alpha^2\beta^2$. Then $a^2 = \beta^2$, $b^2=\alpha^2$, $c = -2\alpha\beta^2$ and $d = -2\alpha^2\beta$.

Solution step (worth 2 points):
We have four cases:
* $a=\beta$, $b=\alpha$;
* $a=-\beta$, $b=-\alpha$;
* $a=-\beta$, $b=\alpha$;
* $a=\beta$, $b=-\alpha$.
The cases 1. and 2. give us the equation
$$
(\beta x+\alpha y)^2 -2\alpha\beta^2x - 2\alpha^2\beta y + \alpha^2\beta^2 = 0.
$$
Meanwhile, in 3. and 4. we have
$$
(\beta x-\alpha y)^2 -2\alpha\beta^2x - 2\alpha^2\beta y + \alpha^2\beta^2 = 0.
$$
Observe that the last equation could be reformulated as follows
$$
(\beta x - \alpha y + \alpha\beta)^2 = 0
$$
and it is an equation of line.

Solution step (worth 1 point):
Answer: $(\beta x+\alpha y)^2 -2\alpha\beta^2x - 2\alpha^2\beta y + \alpha^2\beta^2 = 0$.