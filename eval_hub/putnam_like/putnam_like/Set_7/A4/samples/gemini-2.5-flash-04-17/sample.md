Let $B = \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix}$. We are looking for a matrix $A \in \mathbb{M}_{2\times 2}(\mathbb{R})$ such that $\cos A = B$.
The matrix $B$ is an upper triangular matrix with eigenvalues 1, 1. $B = I + N$ where $N = \begin{bmatrix} 0 & 2025 \\ 0 & 0 \end{bmatrix}$ and $N^2=0$.

If $\cos A = B$, then $A$ must commute with $\cos A$, i.e., $AB = BA$.
Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ be a real matrix.
$AB = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} a & 2025a+b \\ c & 2025c+d \end{bmatrix}$.
$BA = \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} a+2025c & b+2025d \\ c & d \end{bmatrix}$.
For $AB=BA$, we must have:
$a = a+2025c \implies 2025c=0 \implies c=0$.
$2025a+b = b+2025d \implies 2025a=2025d \implies a=d$.
$c = c$ (which is $0=0$).
$2025c+d = d$ (which is $0+d=d$).
So $A$ must be of the form $\begin{bmatrix} a & b \\ 0 & a \end{bmatrix}$ for some $a, b \in \mathbb{R}$.

The eigenvalues of $A = \begin{bmatrix} a & b \\ 0 & a \end{bmatrix}$ are $a, a$.
Let $\lambda_1, \lambda_2$ be the eigenvalues of $A$. They are both equal to $a$.
The eigenvalues of $\cos A$ are $\cos \lambda_1$ and $\cos \lambda_2$, which are $\cos a$ and $\cos a$.
The eigenvalues of $B = \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix}$ are 1, 1.
Since $\cos A = B$, their eigenvalues must match. So $\cos a = 1$.
This implies $a = 2\pi k$ for some integer $k$.

So $A$ must be of the form $A = \begin{bmatrix} 2\pi k & b \\ 0 & 2\pi k \end{bmatrix}$ for some $k \in \mathbb{Z}$ and $b \in \mathbb{R}$.

Now we compute $\cos A$ for $A = \begin{bmatrix} \lambda & b \\ 0 & \lambda \end{bmatrix}$ with $\lambda = 2\pi k$.
$A = \lambda I + bN$, where $N = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$. Note $N^2=0$.
The series expansion for $\cos A$ is $\cos A = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} A^{2n}$.
$A^{2n} = (\lambda I + bN)^{2n}$.
For $m \ge 1$, $(\lambda I + bN)^m = \lambda^m I + m\lambda^{m-1} (bN) + \binom{m}{2}\lambda^{m-2}(bN)^2 + \dots = \lambda^m I + mb\lambda^{m-1} N$ since $(bN)^2=b^2N^2=0$.
$A^{2n} = \lambda^{2n} I + 2nb\lambda^{2n-1} N$ for $2n \ge 1$.
$A^0 = I$.
$\cos A = \frac{(-1)^0}{0!} A^0 + \sum_{n=1}^\infty \frac{(-1)^n}{(2n)!} (\lambda^{2n} I + 2nb\lambda^{2n-1} N)$
$\cos A = I + \sum_{n=1}^\infty \frac{(-1)^n \lambda^{2n}}{(2n)!} I + \sum_{n=1}^\infty \frac{(-1)^n 2nb\lambda^{2n-1}}{(2n)!} N$
$\cos A = \left( \sum_{n=0}^\infty \frac{(-1)^n \lambda^{2n}}{(2n)!} \right) I + b \left( \sum_{n=1}^\infty \frac{(-1)^n \lambda^{2n-1}}{(2n-1)!} \right) N$.
The first series is $\cos \lambda$. The second series is the derivative of $\cos x$ with respect to $x$ evaluated at $\lambda$, which is $-\sin \lambda$.
So $\cos A = (\cos \lambda) I - (b\sin \lambda) N = \begin{bmatrix} \cos \lambda & 0 \\ 0 & \cos \lambda \end{bmatrix} - \begin{bmatrix} 0 & b\sin \lambda \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} \cos \lambda & -b\sin \lambda \\ 0 & \cos \lambda \end{bmatrix}$.

We require $\cos A = B = \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix}$.
$\begin{bmatrix} \cos \lambda & -b\sin \lambda \\ 0 & \cos \lambda \end{bmatrix} = \begin{bmatrix} 1 & 2025 \\ 0 & 1 \end{bmatrix}$.
This gives the equations:
1) $\cos \lambda = 1$
2) $-b\sin \lambda = 2025$

From (1), $\lambda = 2\pi k$ for some integer $k$.
Substitute this into (2):
$-b\sin(2\pi k) = 2025$.
Since $\sin(2\pi k) = 0$ for all integers $k$, this becomes $-b \cdot 0 = 2025$, which is $0 = 2025$.
This is a contradiction.

Therefore, there is no real matrix $A$ of the form $\begin{bmatrix} a & b \\ 0 & a \end{bmatrix}$ satisfying $\cos A = B$. Since we showed that $A$ must be of this form by commuting with $B$, no such matrix $A \in \mathbb{M}_{2\times 2}(\mathbb{R})$ exists.

The final answer is $\boxed{No}$.