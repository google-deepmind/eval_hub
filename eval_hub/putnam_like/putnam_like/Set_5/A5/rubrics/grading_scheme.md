This step is worth 3 points.
Fix $u\in F$ and put
$$
v(t)=1+6\int_0^t s^2|u(s)|\, ds,\quad \forall t\in[0,1],
$$
and note that $v(t)$ is a positive function and $v(0)=1$. Differentiating we get
$$
v'(t)=6t^2|u(t)|\leq 6t^2\sqrt{v(t)},
$$
so
$$
\sqrt{v(t)}-1=\int_0^t \frac{v'(s)}{2\sqrt{v(s)}}\,ds\leq \int_0^t 3s^2\,ds=t^3.
$$

This step is worth 4 points.
Therefore
$$
|u(t)|\leq \sqrt{v(t)}\leq t^3+1\quad \text{and} \quad |u(t)-1|\leq|u(t)|+1\leq t^3+2.
$$
Now we can bound the absolute value of functional values
$$
|J(u)|\leq\int_0^1 |u^3(t)-u^2(t)|\,dt=\int_0^1 |u(t)|^2\cdot|u(t)-1|\,dt\leq \int_0^1 (t^3+1)^2(t^3+2)\,dt=\frac{549}{140}.
$$

This step is worth 2 points.
In the last inequality there is an equality when $|u(t)|=t^3+1$ and $|u(t)-1|=t^3+2$. These conditions are satisfied for $u_0(t)=-(t^3+1)$. 
Note that
$$
J(u_0)=\int_0^1 u_0^2(t)(u_0(t)-1)\,dt=-\int_0^1 |u_0(t)|^2\cdot|u_0(t)-1|\,dt=-\frac{549}{140}.
$$

This step is worth 1 point.
To finish the solution it is sufficient to show that $u_0\in F$. It is straightforward: $|u_0(t)|^2=t^6+2t^3+1$ and
$$
1+6\int_0^t s^2|u_0(s)|\, ds=1+6\int_0^t s^2(s^3+1)\,ds=1+6\int_0^t  s^5+s^2\,ds=1+t^6+2t^3,
$$
so the condition defining the family $F$ is satisfied.

Finally, the minimum value of $J$ on $F$ is $-\frac{549}{140}$.