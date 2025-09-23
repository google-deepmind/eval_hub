Let $x(t)$ be a solution of the system $\dot{x}(t) = A(t)x(t)$ with $x(0) \neq 0$. We are given the matrix
$$A(t)=\begin{pmatrix}
  1+\sin^2 t & -1 & -1 \\
  1 & 1/(1+\sin^2 t) & -1 \\
  1 & 1 & 1+\cos^2 t
\end{pmatrix}.$$
We want to show that the function $t \mapsto \|x(t)\|$ is increasing, where $\|\cdot\|$ denotes the Euclidean norm. This is equivalent to showing that its derivative with respect to $t$ is non-negative for all $t$.

Let's consider the square of the Euclidean norm, $\|x(t)\|^2 = x(t) \cdot x(t) = x(t)^T x(t)$.
Differentiating $\|x(t)\|^2$ with respect to $t$, we use the product rule:
$$\frac{d}{dt}\|x(t)\|^2 = \frac{d}{dt}(x(t)^T x(t)) = \dot{x}(t)^T x(t) + x(t)^T \dot{x}(t).$$
Since $\dot{x}(t) = A(t)x(t)$, we have:
$$\frac{d}{dt}\|x(t)\|^2 = (A(t)x(t))^T x(t) + x(t)^T (A(t)x(t)) = x(t)^T A(t)^T x(t) + x(t)^T A(t) x(t).$$
This can be written as:
$$\frac{d}{dt}\|x(t)\|^2 = x(t)^T (A(t)^T + A(t)) x(t).$$
Let $A_s(t) = \frac{1}{2}(A(t)^T + A(t))$ be the symmetric part of $A(t)$. Then $\frac{d}{dt}\|x(t)\|^2 = 2 x(t)^T A_s(t) x(t)$.
Let's compute $A_s(t)$:
$$A(t)^T = \begin{pmatrix}
  1+\sin^2 t & 1 & 1 \\
  -1 & 1/(1+\sin^2 t) & 1 \\
  -1 & -1 & 1+\cos^2 t
\end{pmatrix}.$$
$$A(t)^T + A(t) = \begin{pmatrix}
  (1+\sin^2 t)+(1+\sin^2 t) & 1+(-1) & 1+(-1) \\
  -1+1 & 1/(1+\sin^2 t)+1/(1+\sin^2 t) & -1+1 \\
  -1+1 & 1+(-1) & (1+\cos^2 t)+(1+\cos^2 t)
\end{pmatrix} = \begin{pmatrix}
  2(1+\sin^2 t) & 0 & 0 \\
  0 & 2/(1+\sin^2 t) & 0 \\
  0 & 0 & 2(1+\cos^2 t)
\end{pmatrix}.$$
$$A_s(t) = \begin{pmatrix}
  1+\sin^2 t & 0 & 0 \\
  0 & 1/(1+\sin^2 t) & 0 \\
  0 & 0 & 1+\cos^2 t
\end{pmatrix}.$$
Now we compute the quadratic form $x(t)^T A_s(t) x(t)$. Let $x(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \end{pmatrix}$.
$$x(t)^T A_s(t) x(t) = \begin{pmatrix} x_1(t) & x_2(t) & x_3(t) \end{pmatrix} \begin{pmatrix}
  1+\sin^2 t & 0 & 0 \\
  0 & 1/(1+\sin^2 t) & 0 \\
  0 & 0 & 1+\cos^2 t
\end{pmatrix} \begin{pmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \end{pmatrix}$$
$$= (1+\sin^2 t)x_1(t)^2 + \frac{1}{1+\sin^2 t}x_2(t)^2 + (1+\cos^2 t)x_3(t)^2.$$
So, $\frac{d}{dt}\|x(t)\|^2 = 2 \left( (1+\sin^2 t)x_1(t)^2 + \frac{1}{1+\sin^2 t}x_2(t)^2 + (1+\cos^2 t)x_3(t)^2 \right)$.

Now we analyze the terms in the sum. For all $t \in \mathbb{R}$:
$1+\sin^2 t$: Since $0 \le \sin^2 t \le 1$, we have $1 \le 1+\sin^2 t \le 2$. Thus $1+\sin^2 t > 0$.
$\frac{1}{1+\sin^2 t}$: Since $1 \le 1+\sin^2 t \le 2$, we have $\frac{1}{2} \le \frac{1}{1+\sin^2 t} \le 1$. Thus $\frac{1}{1+\sin^2 t} > 0$.
$1+\cos^2 t$: Since $0 \le \cos^2 t \le 1$, we have $1 \le 1+\cos^2 t \le 2$. Thus $1+\cos^2 t > 0$.

All coefficients $(1+\sin^2 t)$, $\frac{1}{1+\sin^2 t}$, and $(1+\cos^2 t)$ are strictly positive for all $t$.
The expression $x(t)^T A_s(t) x(t) = (1+\sin^2 t)x_1(t)^2 + \frac{1}{1+\sin^2 t}x_2(t)^2 + (1+\cos^2 t)x_3(t)^2$ is a sum of non-negative terms.
This sum is equal to zero if and only if all terms are zero, i.e., $(1+\sin^2 t)x_1(t)^2 = 0$, $\frac{1}{1+\sin^2 t}x_2(t)^2 = 0$, and $(1+\cos^2 t)x_3(t)^2 = 0$. Since the coefficients are strictly positive, this implies $x_1(t)^2 = 0$, $x_2(t)^2 = 0$, and $x_3(t)^2 = 0$, which means $x_1(t)=0$, $x_2(t)=0$, and $x_3(t)=0$. So, $x(t)^T A_s(t) x(t) = 0$ if and only if $x(t) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$.

The problem states that $x(t)$ is a solution with $x(0) \neq 0$. For a linear homogeneous system of ODEs $\dot{x} = A(t)x$, the trivial solution is $x(t) = 0$ for all $t$. By the uniqueness theorem for linear ODEs, if a solution is non-zero at some point, it must be non-zero for all points in its domain. Since $x(0) \neq 0$, we must have $x(t) \neq 0$ for all $t \in \mathbb{R}$.

Since $x(t) \neq 0$ for all $t$, we have $x(t)^T A_s(t) x(t) > 0$ for all $t$.
Therefore, $\frac{d}{dt}\|x(t)\|^2 = 2 x(t)^T A_s(t) x(t) > 0$ for all $t$.

Now consider the derivative of $\|x(t)\|$. Since $\|x(t)\| = \sqrt{\|x(t)\|^2}$ and $\|x(t)\|^2 > 0$ (as $x(t) \neq 0$), we can use the chain rule:
$$\frac{d}{dt}\|x(t)\| = \frac{d}{dt}\sqrt{\|x(t)\|^2} = \frac{1}{2\sqrt{\|x(t)\|^2}} \frac{d}{dt}\|x(t)\|^2 = \frac{1}{2\|x(t)\|} \frac{d}{dt}\|x(t)\|^2.$$
Since $\frac{d}{dt}\|x(t)\|^2 > 0$ and $\|x(t)\| > 0$, we have:
$$\frac{d}{dt}\|x(t)\| = \frac{2 x(t)^T A_s(t) x(t)}{2\|x(t)\|} = \frac{x(t)^T A_s(t) x(t)}{\|x(t)\|} > 0$$
for all $t \in \mathbb{R}$.

Since the derivative of $\|x(t)\|$ with respect to $t$ is strictly positive for all $t$, the function $t \mapsto \|x(t)\|$ is strictly increasing. A strictly increasing function is also an increasing function.

Thus, the function $\mathbb{R}\ni t \mapsto \|x(t)\|\in \mathbb{R}$ is increasing.

The final answer is $\boxed{The function $\mathbb{R}\ni t \mapsto \|x(t)\|\in \mathbb{R}$ is increasing}$.