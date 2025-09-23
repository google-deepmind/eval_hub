Solution step (1 point)
The characteristic polynomial of $M$ is
$$
\chi_M(t)=\det(tI_3-M)=(t-1)^3.
$$

Solution step (1 point)
Dividing the polynomial $t^m$ by $\chi_M(t)$, we obtain the following decomposition:
$$
t^{m}=w(t)\chi_M(t)+a_mt^2+b_mt+c_m,
$$
where $a_m,b_m,c_m\in \mathbb{R}$ and $w(t)$ is a polynomial of degree $m-3$.

Solution step (6 points)
Differentiating twice with respect to $t$, we get
$$
mt^{m-1}=\dot{w}(t)\chi_M(t)+w(t)\dot{\chi}_M(t)+2a_mt+b_m,
$$
$$
m(m-1)t^{m-2}=\ddot{w}(t)\chi_M(t)+2\dot{w}(t)\dot{\chi}_M(t)+w(t)\ddot{\chi}_M(t)+2a_m.
$$
Consequently, substituting the number $1$, we obtain the following system:
$$
\begin{cases}
1  = a_m+b_m+c_m\\
m = 2a_m+b_m\\
m(m-1)= 2a_m.
\end{cases}
$$
Hence, we get
$$
a_m=\frac{m(m-1)}{2},\;b_m=m(2-m) \text{ and } c_m=\frac{m^2-3m+2}{2}.
$$

Solution step (2 points)
Now, substituting $M$
and using the Cayley-Hamilton theorem (which
states that every square matrix satisfies its own characteristic
polynomial), we deduce that
$$
M^{m}=\frac{m(m-1)}{2}M^2+m(2-m) M+\frac{m^2-3m+2}{2}I_3.
$$
This completes the solution.