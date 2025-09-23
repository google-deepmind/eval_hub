This step is worth 2 points.
Since the function $t \mapsto A(t)$ is bounded on $\mathbb{R}$, it follows that $\eqref{Row}$ admits a unique solution on the entire real line $\mathbb{R}$ for any initial condition $x(0)$. In particular, the uniqueness property of the solution to $\eqref{Row}$ ensures that if the solution $x(\cdot)$ satisfies $x(0) \neq 0$, then $x(t) \neq 0$ for all $t \in \mathbb{R}$.

This step is worth 8 points.
Now, let us observe that it suffices to show that
$$
\frac{d}{dt}\|x(t)\|^2> 0
$$
for all $t\in \mathbb{R}$. We have
$$
\begin{aligned}
\frac{d}{dt}\|x(t)\|^2=\frac{d}{dt}\langle
x(t),x(t)\rangle&=\langle \dot{x}(t),x(t)\rangle + \langle
x(t),\dot{x}(t)\rangle\\
&=\langle A(t)x(t),x(t)\rangle+\langle x(t),A(t)x(t)\rangle\\
&=\langle A(t)x(t),x(t)\rangle+\langle A^T(t)x(t),x(t)\rangle\\
&=\langle (A(t)+A^T(t))x(t),x(t)\rangle.
\end{aligned}
$$
On the other hand,
$$
\begin{aligned}
&A(t)+A^T(t)=\\
&=\begin{pmatrix}
  1+\sin^2 t  & -1 & -1 \\
  1 & 1/(1+\sin^2 t) & -1 \\
  1 & 1 & 1+\cos^2 t
\end{pmatrix}+\begin{pmatrix}
  1+\sin^2 t & 1 & 1 \\
  -1 & 1/(1+\sin^2 t) & 1 \\
  -1 & -1 & 1+\cos^2 t
\end{pmatrix}=\\
&=
\begin{pmatrix}
  2(1+\sin^2 t) & 0 & 0 \\
  0 & 2/(1+\sin^2 t) & 0 \\
  0 & 0 & 2(1+\cos^2 t)
\end{pmatrix}.
\end{aligned}
$$
Since the determinant of the principal minors are positive:
$$
\det(2(1+\sin^2 t) )>0, \quad\det\begin{pmatrix}
  2(1+\sin^2 t)  & 0 \\
  0 & 2/(1+\sin^2 t)
\end{pmatrix}>0
$$
and
$$
\det\begin{pmatrix}
  2(1+\sin^2 t) & 0 & 0 \\
  0 & 2/(1+\sin^2 t) & 0 \\
  0 & 0 & 2(1+\cos^2 t)
\end{pmatrix}>0,
$$
we deduce that $A(t)+A^T(t)$ is positive definite for all $t\in \mathbb{R}$, which implies that
$$
\langle (A(t)+A^T(t))y,y\rangle>0
$$
for all $t\in \mathbb{R}$ and $y\neq 0$. In particular, we have
$$
\langle (A(t)+A^T(t))x(t),x(t)\rangle>0 \text{ for all }t\in \mathbb{R}.
$$
Thus, we have proved that
$$
\frac{d}{dt}\|x(t)\|^2> 0
$$
for all $t\in \mathbb{R}$. This completes the solution.
