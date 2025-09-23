This step is worth 7 points.
Consider the point $R'$ being the reflection of $R$ in the line $PQ$. Of course, the radius of circumcircle $\omega$ of the triangle $PQR'$ equals $r(P,Q)$. Let $O$ be the origin. We are going to show that $O\in\omega$.

Let $P=(P_x,P_y)$ and $Q=(Q_x,Q_y)$. Assume, without loss of generality, $Q_x>P_x$. By the $3$-point-degeneration of the Pascal's theorem the line $k$ is parallel to the segment $P_xP_y$ (this is the classical construction of a tangent to hyperbola). Similarly, $l$ is parallel to the segment $Q_xQ_y$. Denote by $S$ the intersection of $P_xP_y$ and $Q_xQ_y$.

Then
$$
\begin{split}
\angle PR'Q&=\angle PRQ=\angle P_y S Q_x=\angle Q_y S P_x=2\pi- \left(\frac\pi 2+\angle OP_xP_y+\angle OQ_yQ_x\right)\\
&=\frac{3\pi}2- \left(\frac\pi 2-\angle P_yOP+\frac\pi 2-\angle Q_xOQ \right)=\frac\pi 2+\angle P_yOP+\angle Q_xOQ
\end{split}
$$

On the other hand
$$
\angle POQ=\frac\pi 2-(\angle P_yOP+\angle Q_xOQ),
$$
so $\angle POQ+\angle PR'Q=\pi$, i.e. $POQR'$ is cyclic. Therefore $r(P,Q)$ is equal to the radius of the circumcircle of the triangle $OPQ$.

This step is worth 1 point.
Since the diameter of the circle is $2r$, we have $2r(P,Q)\geq \max\{OP,OQ\}$. Therefore
$$
\inf_{P,Q} r(P,Q)\geq \frac 12\mathrm{dist}(O,\text{hyperbola})=
\frac 12\mathrm{dist}(O, (1,1))=\frac{\sqrt{2}}2.
$$

This step is worth 2 points.
When both $P$ and $Q$ tend to the point $W=(1,1)$ then the triangle $OPQ$ tends to be the segment $OW$ and therefore $r(P,Q)$ can be arbitrarily close to the half of its length. More precisely, take the points $P_n,Q_n\in\mathcal{H}$ that are symmetric to each other with respect to the line $OW$ (the axis of symmetry of $\mathcal{H}$). Then the triangle $OPQ$ is an isoceles one and denoting $\alpha_n=\angle P_nOQ_n$ we have be the law of sines
$$
r(P_n,Q_n)=\frac{|P_nQ_n|}{2\sin{\alpha_n}}=\frac{\frac{|P_nQ_n|}2}{2\sin\frac{\alpha_n} 2\cos\frac{\alpha_n}2}=\frac{|OP_n|}{2\cos\frac{\alpha_n}2}.
$$
However, with $P_n\to W$ we have $|OP_n|\to \sqrt{2}$ and $\alpha_n\to 0$, so $r(P_n,Q_n)\to \frac{\sqrt{2}}2$ and therefore
$$
\inf_{P,Q} r(P,Q)=\frac{\sqrt{2}}2.
$$