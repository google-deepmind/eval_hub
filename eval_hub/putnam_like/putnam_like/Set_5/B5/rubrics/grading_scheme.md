This step is worth 2 points.
Since $P(-z)=z^8+5z^3+10$ has no positive roots, by Descarte's rule of signs, $P(z)$ has no real negative roots.
Moreover, it has no imaginary roots. Indeed, if $z=iy$ is a root then
$$0=P(iy)=y^8+5iy^3+10,$$
so imaginary part $5y^3$ is zero and therefore $z=0$, a contradiction.

This step is worth 6 points.
Fix $R>0$ and consider a counterclockwise oriented contour constructed by the segment $A=[0\to Ri]$, the arc $B=\{|z|=R\,:\,\frac\pi 2  \leq \arg z\leq\pi\}$  and the segment $C=[(-R)\to 0]$. For sufficiently large $R$ all the roots of the polynomial $P(z)$ in the set $A$ lie inside the contour, since the modulus of the roots of any polynomial are bounded.

By the argument principle the number of zeros of $P(z)$ inside the contour equals $\frac{ \Delta}{2\pi}$ where $\Delta=\Delta_A+\Delta_B+\Delta_C$ is a change of $\arg P(z)$ along the contour (and each part of it, respectively).  

On the real line $\arg P(z)$ is constant and equal to $0$, so $\Delta_C=0$. 

To study the change of $\arg P(z)$ along the arc $B$ note that $P(z)=z^8(1+\frac{5}{z^5}+\frac{10}{z^8})$, so 
$$|\arg P(z)-\arg z^8|=|\arg (1+\frac{5}{z^5}+\frac{10}{z^8})|<\arg (1) +\frac{\pi}{4}=\frac{\pi}4$$
if $|z|=R$ is sufficiently large. Since the change of $\arg z^8$ along $B$ is $8\cdot\frac\pi 2=4\pi$ we conclude 
$$4\pi-\frac\pi 2\leq \Delta_B \leq 4\pi+\frac\pi 2.$$

On the imaginary positive semi-axis we have $\arg P(iy)=\arg (y^8+5iy^3+10)\in (0,\pi)$, since the imaginary part is non-negative. Therefore $\Delta_A\in (0,\pi)$ since $\arg P(z)$ cannot cross $2\pi$.

This step is worth 2 points.
Note that, by continuity, the change of $\arg P(z)$ along any closed curve has to be a multiplicity of $2\pi$. Therefore
$$(4\pi-\frac\pi 2)+0+0\leq \Delta_A+\Delta_B+\Delta_C\leq  (4\pi+\frac\pi 2) +\pi+0$$
implies $\Delta =4\pi$, so there are two roots of $P(z)$ in the given set.