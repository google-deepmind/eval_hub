Let the given equation be
\begin{equation*}
A^{4m+1}+A^{4m}+A^{2m+1}+A^{2m}+A+I=0 \quad (*).
\end{equation*}
We are given that $A$ is a real symmetric matrix of size $n\times n$.
Let $P(x) = x^{4m+1}+x^{4m}+x^{2m+1}+x^{2m}+x+1$. Then the equation $(*)$ can be written as $P(A)=0$.

Since $A$ is a real symmetric matrix, we know two important properties:
1.  All eigenvalues of $A$ are real numbers.
2.  $A$ is diagonalizable over $\mathbb{R}$. That is, there exists an invertible matrix $P$ (which can be chosen to be orthogonal) such that $A = PDP^{-1}$, where $D$ is a diagonal matrix whose diagonal entries are the eigenvalues of $A$.

Let $\lambda_1, \dots, \lambda_n$ be the eigenvalues of $A$. Since $A$ is real symmetric, all $\lambda_i \in \mathbb{R}$.
From $A = PDP^{-1}$, we have $A^k = PD^kP^{-1}$ for any integer $k \ge 0$.
Then $P(A) = P(A^{4m+1}+A^{4m}+A^{2m+1}+A^{2m}+A+I) = P(D^{4m+1}+D^{4m}+D^{2m+1}+D^{2m}+D+I)P^{-1} = P P(D) P^{-1}$.
The equation $P(A)=0$ is equivalent to $P P(D) P^{-1} = 0$, which implies $P(D)=0$.

$D$ is a diagonal matrix, say $D = \text{diag}(\lambda_1, \dots, \lambda_n)$.
$P(D)$ is also a diagonal matrix:
\begin{equation*}
P(D) = \text{diag}(P(\lambda_1), \dots, P(\lambda_n)).
\end{equation*}
The condition $P(D)=0$ means that all diagonal entries must be zero. So, $P(\lambda_i)=0$ for all eigenvalues $\lambda_i$ of $A$.
Since all eigenvalues $\lambda_i$ are real numbers, they must be real roots of the polynomial $P(x)$.

Let's find the real roots of $P(x) = x^{4m+1}+x^{4m}+x^{2m+1}+x^{2m}+x+1$.
We can factor $P(x)$ by grouping terms:
\begin{align*} P(x) &= x^{4m}(x+1) + x^{2m}(x+1) + (x+1) \\ &= (x+1)(x^{4m}+x^{2m}+1) \end{align*}
The roots of $P(x)$ are the roots of $x+1=0$ or $x^{4m}+x^{2m}+1=0$.
The equation $x+1=0$ gives the real root $x=-1$.

Now consider the equation $Q(x) = x^{4m}+x^{2m}+1=0$. We are looking for real roots $x \in \mathbb{R}$.
Let $y = x^{2m}$. Since $m \in \mathbb{N}$, $m \ge 1$, $2m$ is an even positive integer.
For any real number $x$, $x^{2m} \ge 0$. So $y \ge 0$.
The equation $Q(x)=0$ can be written in terms of $y$ as:
\begin{equation*} y^2 + y + 1 = 0 \end{equation*}
We want to find if this equation has any solution $y \ge 0$.
The quadratic equation $y^2+y+1=0$ has discriminant $\Delta = 1^2 - 4(1)(1) = 1-4 = -3$. Since the discriminant is negative, the quadratic equation has no real roots. Its roots are $y = \frac{-1 \pm i\sqrt{3}}{2}$, which are complex numbers.
Alternatively, if $y \ge 0$, then $y^2 \ge 0$.
So, $y^2+y+1 \ge 0+0+1 = 1$.
Thus, $y^2+y+1$ can never be equal to 0 for $y \ge 0$.
Since $y = x^{2m}$ must be non-negative for real $x$, the equation $x^{4m}+x^{2m}+1=0$ has no real solutions for $x$.

Therefore, the only real root of $P(x)=0$ is $x=-1$.
Since all eigenvalues $\lambda_i$ of $A$ must be real roots of $P(x)$, all eigenvalues must be equal to $-1$.
$\lambda_1 = \lambda_2 = \dots = \lambda_n = -1$.

Since $A$ is diagonalizable, $A = PDP^{-1}$ where $D$ is the diagonal matrix of eigenvalues.
So $D = \begin{pmatrix} -1 & 0 & \dots & 0 \\ 0 & -1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & -1 \end{pmatrix} = -I$.
Substituting $D=-I$ into the diagonalization equation:
\begin{equation*} A = P(-I)P^{-1} = -P I P^{-1} = -P P^{-1} = -I \end{equation*}
So, the only possible solution is $A=-I$.

Finally, we must check if $A=-I$ is indeed a solution.
First, $A=-I$ is a symmetric matrix since $(-I)^T = -I^T = -I$.
Now, substitute $A=-I$ into the equation $(*)$:
\begin{align*} LHS &= (-I)^{4m+1}+(-I)^{4m}+(-I)^{2m+1}+(-I)^{2m}+(-I)+I \\ &= (-1)^{4m+1}I + (-1)^{4m}I + (-1)^{2m+1}I + (-1)^{2m}I - I + I \end{align*}
Since $m \in \mathbb{N}$, $m \ge 1$. Thus $2m$ and $4m$ are even positive integers, and $2m+1$ and $4m+1$ are odd positive integers.
Therefore, $(-1)^{4m+1}=-1$, $(-1)^{4m}=1$, $(-1)^{2m+1}=-1$, $(-1)^{2m}=1$.
\begin{align*} LHS &= (-1)I + (1)I + (-1)I + (1)I - I + I \\ &= -I + I - I + I - I + I \\ &= 0 \end{align*}
The equation $(*)$ holds for $A=-I$.
Thus, the only symmetric matrix satisfying the given equation is $A=-I$.

Final Answer: The final answer is $\boxed{A=-I}$