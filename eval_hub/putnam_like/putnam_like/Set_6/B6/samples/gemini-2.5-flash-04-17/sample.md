Let $X_n = (R_n, S_n, T_n)$ be i.i.d. random variables uniformly distributed on the set of $3! = 6$ permutations of $(1,2,3)$. The set of possible values for $(R_n, S_n, T_n)$ is $\{(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)\}$. Each outcome has probability $1/6$.
Let $\hat X_n = (\hat R_n, \hat S_n, \hat T_n) = (\sum_{i=1}^n R_i, \sum_{i=1}^n S_i, \sum_{i=1}^n T_i)$.
For any permutation $(r,s,t)$ of $(1,2,3)$, $r+s+t = 1+2+3 = 6$. Thus, $\hat R_n + \hat S_n + \hat T_n = \sum_{i=1}^n (R_i+S_i+T_i) = \sum_{i=1}^n 6 = 6n$. This holds almost surely.

$p_n = P(\hat R_n = \hat S_n = \hat T_n)$. Since $\hat R_n + \hat S_n + \hat T_n = 6n$, the condition $\hat R_n = \hat S_n = \hat T_n$ is equivalent to $\hat R_n = \hat S_n = \hat T_n = 2n$.

$q_n = P(\hat R_n, \hat S_n, \hat T_n \in \{2n-1, 2n, 2n+1\}, \hat R_n \neq \hat S_n)$.
Let $\hat R_n = 2n+a, \hat S_n = 2n+b, \hat T_n = 2n+c$, where $a,b,c \in \{-1,0,1\}$. The condition $\hat R_n + \hat S_n + \hat T_n = 6n$ implies $(2n+a)+(2n+b)+(2n+c)=6n$, so $a+b+c=0$.
The possible integer values for $(a,b,c)$ in $\{-1,0,1\}^3$ such that $a+b+c=0$ are $(0,0,0)$ and the permutations of $(1,-1,0)$.
The case $(a,b,c)=(0,0,0)$ corresponds to $(\hat R_n, \hat S_n, \hat T_n)=(2n,2n,2n)$, which is the event for $p_n$.
The condition $\hat R_n \neq \hat S_n$ excludes the $(2n,2n,2n)$ case. Thus, $q_n$ is the probability that $(\hat R_n, \hat S_n, \hat T_n)$ is one of the $3!=6$ permutations of $(2n-1, 2n, 2n+1)$.

Let $Z_i = R_i-S_i$ and $W_i = S_i-T_i$. For a permutation $(r,s,t)$ of $(1,2,3)$:
If $(R_i,S_i,T_i)=(1,2,3)$, $(Z_i,W_i)=(-1,-1)$.
If $(R_i,S_i,T_i)=(1,3,2)$, $(Z_i,W_i)=(-2,1)$.
If $(R_i,S_i,T_i)=(2,1,3)$, $(Z_i,W_i)=(1,-2)$.
If $(R_i,S_i,T_i)=(2,3,1)$, $(Z_i,W_i)=(-1,2)$.
If $(R_i,S_i,T_i)=(3,1,2)$, $(Z_i,W_i)=(2,-1)$.
If $(R_i,S_i,T_i)=(3,2,1)$, $(Z_i,W_i)=(1,1)$.
Let $K_0 = \{(-1,-1), (-2,1), (1,-2), (-1,2), (2,-1), (1,1)\}$. Each $(Z_i,W_i)$ is uniformly distributed on $K_0$.
Let $Y_i = (Z_i, W_i)$. $Y_1, \dots, Y_n$ are i.i.d. vectors with mean $E[Y_i]=(E[Z_i], E[W_i])=(0,0)$.
$\hat R_n-\hat S_n = \sum_{i=1}^n (R_i-S_i) = \sum_{i=1}^n Z_i$. $\hat S_n-\hat T_n = \sum_{i=1}^n (S_i-T_i) = \sum_{i=1}^n W_i$.
Let $(U_n, V_n) = (\sum_{i=1}^n Z_i, \sum_{i=1}^n W_i)$.
$\hat R_n = \hat S_n = \hat T_n = 2n \iff U_n=0, V_n=0$. So $p_n=P(U_n=0, V_n=0)$.
The 6 permutations of $(2n-1, 2n, 2n+1)$ correspond to $(\hat R_n, \hat S_n, \hat T_n) = (2n+a, 2n+b, 2n+c)$ where $(a,b,c)$ is a permutation of $(1,-1,0)$.
The values $(U_n, V_n)=(a-b, b-c)$ for these $(a,b,c)$ are:
$(1,-1,0) \implies (2,-1)$
$(1,0,-1) \implies (1,1)$
$(-1,1,0) \implies (-2,1)$
$(-1,0,1) \implies (-1,-1)$
$(0,1,-1) \implies (-1,2)$
$(0,-1,1) \implies (1,-2)$
This set of points is exactly $K_0$.
So $q_n = P((U_n, V_n) \in K_0) = \sum_{(u,v) \in K_0} P(U_n=u, V_n=v)$.

The vectors $Y_i=(Z_i, W_i)$ are integer-valued. $(U_n, V_n)$ is a sum of i.i.d. integer random vectors. The distribution of $(U_n, V_n)$ is concentrated on a lattice in $\mathbb{Z}^2$.
The possible values of $Y_i$ are $K_0$. We checked in thought process that $K_0$ generates the lattice $\Lambda=\{(u,v)\in\mathbb{Z}^2 : u \equiv v \pmod 3\}$. The index of $\Lambda$ in $\mathbb{Z}^2$ is 3.
The covariance matrix of $Y_i$ is $\Sigma = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$. $\det(\Sigma)=3$.

By the Local Limit Theorem for lattice distributions, for $(u,v) \in \Lambda$,
$P(U_n=u, V_n=v) \sim \frac{\text{vol}(\mathbb{Z}^2/\Lambda)}{(2\pi n \det\Sigma)^{1/2}} \exp\left(-\frac{1}{2n} (u,v) \Sigma^{-1} (u,v)^T\right)$ as $n\to\infty$.
vol($\mathbb{Z}^2/\Lambda$) is the index of $\Lambda$ in $\mathbb{Z}^2$, which is 3.
$\Sigma^{-1} = \frac{1}{3}\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
$P(U_n=u, V_n=v) \sim \frac{3}{(2\pi n \cdot 3)^{1/2}} \exp\left(-\frac{1}{6n} (2u^2+2uv+2v^2)\right) = \frac{3}{(6\pi n)^{1/2}} \exp\left(-\frac{2u^2+2uv+2v^2}{6n}\right)$.

For $p_n$, $(u,v)=(0,0)$. $2(0)^2+2(0)(0)+2(0)^2=0$.
$p_n = P(U_n=0, V_n=0) \sim \frac{3}{(6\pi n)^{1/2}} \exp(0) = \frac{3}{(6\pi n)^{1/2}}$.

For $q_n$, $(u,v) \in K_0$. For any $(u,v) \in K_0$, $2u^2+2uv+2v^2=6$.
$q_n = \sum_{(u,v) \in K_0} P(U_n=u, V_n=v)$. There are 6 points in $K_0$. All points in $K_0$ belong to $\Lambda$.
For $(u,v) \in K_0$, $P(U_n=u, V_n=v) \sim \frac{3}{(6\pi n)^{1/2}} \exp\left(-\frac{6}{6n}\right) = \frac{3}{(6\pi n)^{1/2}} e^{-1/n}$.
$q_n \sim 6 \cdot \frac{3}{(6\pi n)^{1/2}} e^{-1/n}$.

Let $C_n = \frac{3}{(6\pi n)^{1/2}}$. Then $p_n \sim C_n$ and $q_n \sim 6 C_n e^{-1/n}$.
The ratio $q_n/p_n \sim \frac{6 C_n e^{-1/n}}{C_n} = 6 e^{-1/n}$.
As $n \to \infty$, $e^{-1/n} \to 1$. So $q_n/p_n \to 6$.
Since $q_n/p_n$ converges to 6, for any $\epsilon > 0$, there exists $N$ such that for all $n > N$, $|q_n/p_n - 6| < \epsilon$.
Let $\epsilon = 1$. For $n>N$, $5 < q_n/p_n < 7$.
This implies $q_n/p_n > 5$ for all $n>N$.
Since $5>4$, this shows $q_n > 4p_n$ for all $n>N$.
The set of integers $\{n > N\}$ is an infinite set.
Therefore, $4p_n < q_n$ for infinitely many $n$.

The argument using the local limit theorem suggests the inequality holds for all sufficiently large $n$. We verified that it holds for $n=1$ and $n=3$, but not for $n=2$. This confirms that "infinitely many $n$" is the appropriate phrasing rather than "all sufficiently large $n$". However, the limit $q_n/p_n \to 6$ is sufficient to prove the statement for all $n>N$.

The final answer is $\boxed{4p_n< q_n \text{ for infinitely many } n}$.