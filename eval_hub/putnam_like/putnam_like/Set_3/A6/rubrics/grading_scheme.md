This step is worth 3 points.
Let $A$ be a matrix with entries in $\{0,1\}$ such that $J=A^2$ and put $n=2k$. Let $r_i$ denote the number of ones in the $i$-th row of $A$ and let $\bar{c}_i$ denote the number of ones on *odd* positions in the $i$-th column of $A$.

Observe that
$$
\begin{pmatrix}
r_1 & 0 &r_1 & \ldots & r_1 & 0\\
r_2 & 0 &r_2 & \ldots & r_2 & 0\\
\vdots & \vdots & \vdots & \ddots &\vdots &\vdots \\
r_n & 0 &r_n & \ldots & r_n & 0
\end{pmatrix}= AJ_n=A^3=J_nA=
\begin{pmatrix}
\bar{c}_1 & \bar{c}_2 &\bar{c}_3 & \ldots & \bar{c}_{n-1}& \bar{c}_n\\
\bar{c}_1 & \bar{c}_2 &\bar{c}_3 & \ldots & \bar{c}_{n-1}& \bar{c}_n\\
\vdots & \vdots & \vdots & \ddots &\vdots &\vdots \\
\bar{c}_1 & \bar{c}_2 &\bar{c}_3 & \ldots & \bar{c}_{n-1}& \bar{c}_n\\
\end{pmatrix}.
$$
Thus, there is $d\in\mathbb{N}$ such that $r_i=d$ for $i=1,\ldots,n$, $\bar{c}_{2j}=0$ and $\bar{c}_{2j-1}=d$ for $j=1,\ldots,k$. Therefore, $AJ_n=dJ_n$.


This step is worth 2 points.
Note that $J_n^2=\left\lceil \frac n2\right\rceil J=kJ$. Moreover,
$$
kJ=J^2=(A^2)^2=A(AJ_n)=A(dJ_n)=dAJ_n=d^2J_n,
$$
hence $k=d^2$ and the necessary condition is $n=2k=2d^2$ for some $d\in\mathbb{N}$.


This step is worth 5 points.
Now we construct a matrix $A$ for $n=2d^2$. Denote by $B_r$ for $r=0,\ldots d-1$ the  $d\times d$ matrix whose $(i,j)$-th entry is $1$ if $j-i \equiv r \,(\text{mod}\, d)$ and $0$ otherwise. Put $C_r$ for the $d\times (2d)$ matrix whose columns are columns of $B_r$ and vectors of zeros, alternately. Finally, let $D_r$ be a $(2d)\times (2d)$ matrix where the $(2j-1)$-th and $(2j)$-th rows are the $j$-th row of $C_r$. For example, for $d=3$:
$$
B_1=\begin{pmatrix}
0& 1 &0 \\
0&0&1\\
1&0&0
\end{pmatrix},\quad
C_1=\begin{pmatrix}
0& 0 &1& 0 &0& 0 \\
0& 0&0& 0&1& 0\\
1& 0&0& 0&0& 0
\end{pmatrix},\quad
D_1=\begin{pmatrix}
0& 0 &1& 0 &0& 0 \\
0& 0 &1& 0 &0& 0 \\
0& 0&0& 0&1& 0\\
0&0&0&0&1&0\\
1&0&0&0&0&0\\
1&0&0&0&0&0
\end{pmatrix}
$$
Note that $B_0+B_1+\ldots+B_{d-1}$ is a matrix of ones and therefore $D_0+D_1+\ldots+D_{d-1}=J_d$. Put $A=\begin{pmatrix}
D_0& D_1 &\ldots &D_{d-1} \\
D_0& D_1 &\ldots &D_{d-1} \\
\vdots & \vdots &\ddots &\vdots \\
D_0& D_1 &\ldots &D_{d-1}
\end{pmatrix}$.

Then the $(i,j)$-th block of the matrix $A^2$ is
$$
(D_0\quad D_1\quad \ldots\quad D_{d-1}) \begin{pmatrix}
D_{j-1} \\
\vdots \\
D_{j-1}
\end{pmatrix}=(D_0+\ldots+D_{d-1})D_{j-1}=J_dD_{j-1} =J_d
$$
and therefore $A^2=J_n$.