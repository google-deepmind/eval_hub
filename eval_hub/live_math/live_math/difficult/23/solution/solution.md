Let $AL$ be an altitude of the triangle. We know from Ceva and Menelaos theorem that $(B,C;L,F)$ is a harmonic quadruple. Let $a$ be the length of $BC$. From Pythagorean theorem we have
 $$BL^2 - CL^2 = BA^2-AC^2 = 99^2 - 126^2.$$
 Let $y =  126^2-99^2 = 3\cdot 45^2$. We also know that $\overrightarrow{BL}+\overrightarrow{LC} = \overrightarrow{BC} = a$. Here, by convention, we identify the direction $\overrightarrow{BC}$ as positive on the line $BC$. Therefore we get
 $$\overrightarrow{BL}-\overrightarrow{LC}=-\frac ya.$$
From this and the previous one, we get
$$\overrightarrow{BL} = 1/2(a-\frac{ya})$$
and
 $$\overrightarrow{LC} = 1/2(a+\frac{ya}).$$
Therefore
$$\frac{\overrightarrow{BL}}{\overrightarrow{LC}} = \frac{a^2-y}{a^2+y}.$$
From harmonicity of $(B,C;L,H)$ we get
$$\frac{\overrightarrow{BF}}{\overrightarrow{FC}} = \frac{a^2-y}{-a^2-y}.$$
Hence
$$\frac{\overrightarrow{BF}}{\overrightarrow{FC}+\overrightarrow{BF}} = -\frac{a^2-y}{2y}.$$


As $\overrightarrow{BF}+\overrightarrow{FC} = \overrightarrow{BC} = a,$
this means
$$\overrightarrow{BF} = - \frac{a(a^2-y)}{2y}.$$
We know that this equals $\pm 135$. Assume first that it equals $-135$.
$$- \frac{a(a^2-y)}{2y} = -135.$$
This gives
$$a^3-ay-270y = 0.$$
Recall that $y=3\cdot 45^2$. Hence
$$a^3-3\cdot 45^2a - 270\cdot 3\cdot 45^2 = 0.$$
Let $a=45t$. Then we have
$$45^3 t^3 - 3\cdot 45^3 t - 18\cdot 45^3 = 0.$$
Dividing both sides by $99^3$, we obtain
$$t^3 - 3t - 18 = 0.$$
Note that $t^3-3t-18 = (t-3)(t^2+3t+6)$. The expression in the second delimeter is positive, as $t$ is positive, hence we must have $t=3$. This gives $c=135$ and the perimeter of the triangle equal to $99+126+135 = 360$, hence $p+q=361$.


Now assume that 
$$- \frac{a(a^2-y)}{2y} = 135.$$
Then analogously we get
$$t^3 - 3t + 18 = 0.$$
Now notice that LHS equals
$$ (t^3-3t+2) + 16 = (t+2)(t-1)^2 +16 >0$$.
Therefore the only possible value of $p+q$ is $361$.