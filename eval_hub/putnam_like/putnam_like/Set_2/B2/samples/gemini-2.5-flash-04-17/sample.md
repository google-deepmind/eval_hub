Let $P(x) = x^{4m+1}+x^{4m}+x^{2m+1}+x^{2m}+x+1$. The given equation is $P(A) = 0$.
Since $A$ is a real symmetric matrix, it is diagonalizable over $\mathbb{R}$. This means there exists an orthogonal matrix $Q$ such that $A = Q D Q^T$, where $D$ is a real diagonal matrix whose entries are the eigenvalues of $A$.
If $v$ is an eigenvector of $A$ with eigenvalue $\lambda$, then $Av = \lambda v$. Applying the polynomial $P$ to $A$ and $v$:
$P(A)v = (A^{4m+1}+A^{4m}+A^{2m+1}+A^{2m}+A+I)v = A^{4m+1}v+A^{4m}v+A^{2m+1}v+A^{2m}v+Av+Iv$.
Using $A^k v = \lambda^k v$:
$P(A)v = \lambda^{4m+1}v+\lambda^{4m}v+\lambda^{2m+1}v+\lambda^{2m}v+\lambda v+Iv = (\lambda^{4m+1}+\lambda^{4m}+\lambda^{2m+1}+\lambda^{2m}+\lambda+1)v = P(\lambda)v$.
Since $P(A)=0$, we have $P(A)v=0$ for all $v$, so $P(\lambda)v=0$. For any eigenvector $v\neq 0$, this implies $P(\lambda)=0$.
Thus, the eigenvalues of $A$ must be roots of the polynomial $P(x)$.

We factorize the polynomial $P(x)$:
$P(x) = x^{4m}(x+1) + x^{2m}(x+1) + (x+1) = (x+1)(x^{4m} + x^{2m} + 1)$.
The roots of $P(x)$ are $x=-1$ and the roots of $x^{4m} + x^{2m} + 1 = 0$.
Let $y = x^{2m}$. The equation $x^{4m} + x^{2m} + 1 = 0$ becomes $y^2 + y + 1 = 0$.
The roots of $y^2 + y + 1 = 0$ are $y = \frac{-1 \pm \sqrt{1-4}}{2} = \frac{-1 \pm i\sqrt{3}}{2}$. These are the complex cube roots of unity $e^{i2\pi/3}$ and $e^{i4\pi/3}$.
So, the roots of $x^{4m} + x^{2m} + 1 = 0$ are the solutions to $x^{2m} = e^{i2\pi/3}$ or $x^{2m} = e^{i4\pi/3}$.

Since $A$ is a real symmetric matrix, all its eigenvalues must be real. We need to find the real roots of $P(x)$.
The only real root from the factor $(x+1)$ is $x=-1$.
Now consider the roots from $x^{2m} = e^{i2\pi/3}$ and $x^{2m} = e^{i4\pi/3}$.
Let $x = re^{i\theta}$ be a root.
For $x^{2m} = e^{i2\pi/3}$: $r^{2m}e^{i2m\theta} = e^{i2\pi/3}$. Thus $r^{2m}=1$ and $2m\theta = 2\pi/3 + 2k\pi$ for $k \in \mathbb{Z}$. Since $r$ is a non-negative real number, $r=1$. The roots are $x_k = e^{i\frac{2\pi/3 + 2k\pi}{2m}} = e^{i\frac{\pi(1+3k)}{3m}}$ for $k=0, 1, \dots, 2m-1$.
For a root $x_k$ to be real, its argument $\frac{\pi(1+3k)}{3m}$ must be a multiple of $\pi$. Let $\frac{\pi(1+3k)}{3m} = j\pi$ for some integer $j$. This implies $1+3k = 3mj$. The left side $1+3k \equiv 1 \pmod 3$, while the right side $3mj \equiv 0 \pmod 3$. This is a contradiction, so there are no real roots from $x^{2m} = e^{i2\pi/3}$.

For $x^{2m} = e^{i4\pi/3}$: $r^{2m}e^{i2m\theta} = e^{i4\pi/3}$. Thus $r^{2m}=1$ and $2m\theta = 4\pi/3 + 2k\pi$ for $k \in \mathbb{Z}$. $r=1$. The roots are $x'_k = e^{i\frac{4\pi/3 + 2k\pi}{2m}} = e^{i\frac{2\pi(2+3k)}{3m}}$ for $k=0, 1, \dots, 2m-1$.
For a root $x'_k$ to be real, its argument $\frac{2\pi(2+3k)}{3m}$ must be a multiple of $\pi$. Let $\frac{2\pi(2+3k)}{3m} = j\pi$ for some integer $j$. This implies $2(2+3k) = 3mj$. The left side $2(2+3k) = 4+6k \equiv 4 \equiv 1 \pmod 3$, while the right side $3mj \equiv 0 \pmod 3$. This is a contradiction, so there are no real roots from $x^{2m} = e^{i4\pi/3}$.

The only real root of $P(x)$ is $x=-1$.
Since $A$ is a real symmetric matrix, all its eigenvalues must be real. Therefore, the only possible eigenvalue for $A$ is $\lambda = -1$.

Since $A$ is a real symmetric matrix, it is diagonalizable. If a diagonalizable matrix has only one eigenvalue $\lambda$, then it must be equal to $\lambda I$.
In this case, the only eigenvalue is $\lambda = -1$.
So $A$ must be equal to $-I$.

Let's verify if $A=-I$ is a solution for any $m \in \mathbb{N}$.
If $A = -I$, then $A$ is symmetric since $(-I)^T = -I$.
Substituting $A=-I$ into the equation:
$(-I)^{4m+1}+(-I)^{4m}+(-I)^{2m+1}+(-I)^{2m}+(-I)+I = 0$.
Since $m \in \mathbb{N} = \{1, 2, 3, \dots\}$, $4m+1$ is odd, $4m$ is even, $2m+1$ is odd, and $2m$ is even.
$(-I)^{odd} = -I$ and $(-I)^{even} = I$.
So the equation becomes:
$(-I) + I + (-I) + I + (-I) + I = 0$
$-I + I - I + I - I + I = 0$
$0 = 0$.
The equation is satisfied for $A=-I$.

Thus, the only symmetric matrix satisfying the given equation for any $m \in \mathbb{N}$ is $A = -I$.

The final answer is $\boxed{A = -I}$.