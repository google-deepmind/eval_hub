Let $N = 2n+1$ be the size of the matrices $A$ and $B$. Since $n \geq 1$, $N \geq 3$. $N$ is an odd integer.
$A$ and $B$ are square invertible matrices of size $N \times N$ with real entries.
We want to determine if there exist real numbers $a$ and $b$ such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.

The condition $a^2+b^2 \neq 0$ means that at least one of $a$ or $b$ is non-zero.
Let's consider the equation $\det(aA+bB) = 0$.
If $a=0$, then $b \neq 0$ (since $a^2+b^2 \neq 0$). The equation becomes $\det(bB) = 0$. Since $B$ is an $N \times N$ matrix, $\det(bB) = b^N \det(B)$. As $B$ is invertible, $\det(B) \neq 0$. So $b^N \det(B) = 0$ implies $b^N = 0$, which means $b=0$. This contradicts our assumption that $b \neq 0$. So $a$ cannot be zero.
If $b=0$, then $a \neq 0$. The equation becomes $\det(aA) = 0$. Since $A$ is an $N \times N$ matrix, $\det(aA) = a^N \det(A)$. As $A$ is invertible, $\det(A) \neq 0$. So $a^N \det(A) = 0$ implies $a^N = 0$, which means $a=0$. This contradicts our assumption that $a \neq 0$. So $b$ cannot be zero.
Therefore, if such $a, b$ exist with $a^2+b^2 \neq 0$ satisfying $\det(aA+bB)=0$, then both $a$ and $b$ must be non-zero.

Since $a \neq 0$, we can divide the matrix $aA+bB$ by $a$.
$\det(aA+bB) = \det(a(A+(b/a)B)) = a^N \det(A+(b/a)B)$.
Since $a \neq 0$ and $N \geq 1$, $a^N \neq 0$. Thus, $\det(aA+bB)=0$ if and only if $\det(A+(b/a)B)=0$.
Let $\lambda = -b/a$. Since $a \neq 0$ and $b \neq 0$, $\lambda$ is a non-zero real number.
The condition $\det(aA+bB)=0$ is equivalent to finding a non-zero real number $\lambda$ such that $\det(A - \lambda B) = 0$.

Since $B$ is an invertible matrix, its determinant $\det(B)$ is non-zero. We can write:
$\det(A - \lambda B) = \det((A B^{-1}) B - \lambda I B) = \det((A B^{-1} - \lambda I) B) = \det(A B^{-1} - \lambda I) \det(B)$.
Since $\det(B) \neq 0$, the equation $\det(A - \lambda B) = 0$ is equivalent to $\det(A B^{-1} - \lambda I) = 0$.

Let $C = A B^{-1}$. Since $A$ and $B$ are real matrices, $C$ is also a real matrix of size $N \times N$.
The equation $\det(C - \lambda I) = 0$ is the characteristic equation of the matrix $C$. The roots $\lambda$ of this equation are the eigenvalues of $C$.
The characteristic polynomial $p(\lambda) = \det(C - \lambda I)$ is a polynomial in $\lambda$ of degree $N$ with real coefficients.
The degree of this polynomial is $N = 2n+1$. Since $n \geq 1$, $N \geq 3$, which is an odd integer.
A fundamental property of polynomials with real coefficients is that if they have odd degree, they must have at least one real root.
Thus, the characteristic polynomial $p(\lambda)$ must have at least one real root. Let $\lambda_0$ be a real root of $p(\lambda)=0$.
So, $C$ has at least one real eigenvalue $\lambda_0$, which satisfies $\det(C - \lambda_0 I) = 0$.

Now we must check if this real eigenvalue $\lambda_0$ can be zero.
If $\lambda_0 = 0$ were an eigenvalue of $C$, then $\det(C - 0I) = \det(C) = 0$.
However, $C = AB^{-1}$. Since $A$ and $B$ are invertible, $A^{-1}$ and $B^{-1}$ exist and are invertible. The product of invertible matrices $A$ and $B^{-1}$ is also an invertible matrix. So $C$ is invertible.
The determinant of an invertible matrix is non-zero. So $\det(C) \neq 0$.
This implies that $\lambda_0 = 0$ cannot be an eigenvalue of $C$.
Therefore, the real eigenvalue $\lambda_0$ must be non-zero.

We have found a real number $\lambda_0 \neq 0$ such that $\det(A B^{-1} - \lambda_0 I) = 0$.
This is equivalent to $\det(A - \lambda_0 B) = 0$.

We are looking for real numbers $a$ and $b$ such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.
We can choose $a=1$ and $b=-\lambda_0$.
Since $\lambda_0$ is a real number, $a=1$ and $b=-\lambda_0$ are real numbers.
We check the condition $a^2+b^2 \neq 0$:
$a^2+b^2 = 1^2 + (-\lambda_0)^2 = 1 + \lambda_0^2$.
Since $\lambda_0$ is a real number and $\lambda_0 \neq 0$, $\lambda_0^2 > 0$. Thus $1+\lambda_0^2 > 1 > 0$.
So $a^2+b^2 \neq 0$ is satisfied.
Now we check the condition $\det(aA+bB)=0$:
$\det(aA+bB) = \det(1 \cdot A + (-\lambda_0) B) = \det(A - \lambda_0 B)$.
We know that $\det(A - \lambda_0 B) = 0$ for our chosen $\lambda_0$.

Thus, there exist real numbers $a=1$ and $b=-\lambda_0$ (where $\lambda_0$ is a non-zero real eigenvalue of $AB^{-1}$) such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.

The final answer is $\boxed{Yes}$.