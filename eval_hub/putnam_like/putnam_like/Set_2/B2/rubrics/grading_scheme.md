This step is worth 1 point.
Consider the following polynomial:
$$
w(x)= x^{4m+1}+x^{4m}+x^{2m+1}+x^{2m}+x+1.
$$
It is not hard to see that $w(-1)=0$ and hence
$$
w(x)=(x^{4m}+x^{2m}+1)(x+1).
$$
Consequently, $w(x)$ has only one real root.

This step is worth 1 point.
Since $A$ is symmetric, it follows that $\sigma(A)\subset \mathbb{R}$, where $\sigma(A)$ stands for the spectrum of $A$, and there exists an invertible matrix $D$ such that
$$
A=D^{-1}J_A D,
$$
where
$$
J_A=\begin{pmatrix}
\lambda_1 & 0 & ...& 0 & 0 \\
0 & \lambda_2 & ...& 0 & 0 \\
0 & 0 & \ddots & 0 & 0 \\
0 & 0 & ... & \lambda_{n-1} & 0 \\
0 & 0 & ... &  0 & \lambda_n \\
\end{pmatrix}.
$$

This step is worth 8 points.
Now we will show that
$$
\sigma(A)=\{-1\}.
$$
Let $\lambda\in \sigma(A)$. Then there exists a nontrivial vector $v\in \mathbb{C}^n$ such that
$$
Av=\lambda v.
$$
On the other hand, since $w(A)=0$, one gets
$$
v^{\top}(A^{4m+1}+A^{4m}+A^{2m+1}+A^{2m}+A)v=v^{\top}(-I)v.
$$
By applying $Av = \lambda v$, one can conclude that
$$
v^{\top}(A^{4m+1}+A^{4m}+A^{2m+1}+A^{2m}+A)v=(\lambda^{4m+1}+\lambda^{4m}+\lambda^{2m+1}+\lambda^{2m}+\lambda)|v|^2
$$
and $v^{\top}(-I)v=-|v|^2.$ Hence the equation takes the following equivalent form:
$$
|v|^2w(\lambda)=0 \Longleftrightarrow w(\lambda)=0.
$$
Thus
$$
\lambda\in\sigma(A) \Longrightarrow w(\lambda)=0.
$$
But $\sigma(A)\subset \mathbb{R}$ and hence $\sigma(A)=\{-1\}$ because $w(x)=0$ has only one real root. Thus
$$
J_A=\begin{pmatrix}
-1 & 0 & ...& 0 & 0 \\
0 & -1 & ...& 0 & 0 \\
0 & 0 & \ddots & 0 & 0 \\
0 & 0 & ... & -1 & 0 \\
0 & 0 & ... &  0 & -1 \\
\end{pmatrix}=-I.
$$
Finally, one has
$$
A=D^{-1}J_A D=D^{-1}(-I) D=-I,
$$
which completes the solution.