Let $AL$ be an altitude of the triangle. We know from Ceva and Menelaos theorem that $(B,C;L,F)$ is a harmonic quadruple. Let $a$ be the length of $BC$. From Pythagorean theorem we have
 $$AL^2 - CL^2 = BA^2-AC^2 = 181^2-424^2.$$
 Let $y = 424^2-181^2 = 15*99^2$. We also know that $\overrightarrow{BL}+\overrightarrow{LC} = \overrightarrow{BC} = a$. Here, by convention, we identify the direction $\overrightarrow{BC}$ as positive on the line $BC$. Therefore we get
 $$\overrightarrow{BL}-\overrightarrow{LC}=-\frac ya.$$
From this and the previous one, we get
$$\overrightarrow{BL} = 1/2(a-\frac{ya})$$
and
 $$\overrightarrow{LC} = 1/2(a+ \frac{ya}).$$
Therefore
$$\frac{\overrightarrow{BL}}{\overrightarrow{LC}} = \frac{a^2-y}{a^2+y}.$$
From harmonicity of $(B,C;L,H)$ we get
$$\frac{\overrightarrow{BF}}{\overrightarrow{FC}} = \frac{a^2-y}{-y-a^2}.$$
Hence
$$\frac{\overrightarrow{BF}}{\overrightarrow{FC}+\overrightarrow{BF}} = \frac{a^2-y}{-2y}.$$


As $\overrightarrow{BF}+\overrightarrow{FC} = \overrightarrow{BC} = a,$
this means
$$\overrightarrow{BF} = - \frac{a(a^2+y)}{2y}.$$
We know that this equals $\pm 165$. Assume first that it equals $-165$.
$$- \frac{a(a^2-y)}{2y} = -165.$$
This gives
$$a^3-ay-330y = 0.$$
Recall that $y=15*\cdot 99^2$. Hence
$$a^3-15\cdot 99^2a - 330\cdot15\cdot 99^2 = 0.$$
Let $a=99t$. Then we have
$$99^3 t^3 - 15\cdot 99^3 t - 50\cdot 99^3 = 0.$$
Dividing both sides by $99^3$, we obtain
$$t^3 - 15t - 50 = 0.$$
Note that $t^3-15t-50 = (t-5)(t^2+5t+10)$. The expression in the second delimeter is positive, as $t$ is positive, hence we must have $t=5$. This gives $a= 495$ and the perimeter of the triangle equal to $181+424+495 = 1100$, hence $p+q=1101$.


Now assume that 
$$- \frac{c(c^2-y)}{2y} = 165.$$
Then analogously we get
$$t^3 - 15t + 50 = 0.$$
Now notice that LHS equals
$$(t^3-75/4t^2+125/4) + 15/4t + 75/4 = (t+5)(t-5/2)^2 + 15/4t + 75/4 > 0.$$


Therefore the only possible value of $p+q$ is $1101$.