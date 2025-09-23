Let $x(t)$ be a solution to the system $\dot{x}(t) = A(t)x(t)$ with $x(0) \neq 0$. We want to show that the function $f(t) = \|x(t)\|$ is increasing for $t \in \mathbb{R}$. Here $\|\cdot\|$ denotes the Euclidean norm, so $\|x(t)\| = \sqrt{x_1(t)^2 + x_2(t)^2 + x_3(t)^2}$.

Let's consider the square of the norm, $g(t) = \|x(t)\|^2 = x(t)^T x(t)$.
We compute the derivative of $g(t)$ with respect to $t$:
$$ g'(t) = \frac{d}{dt} (x(t)^T x(t)) = \dot{x}(t)^T x(t) + x(t)^T \dot{x}(t) $$
Substitute $\dot{x}(t) = A(t)x(t)$ into the expression for $g'(t)$:
$$ g'(t) = (A(t)x(t))^T x(t) + x(t)^T (A(t)x(t)) $$
Using the property $(AB)^T = B^T A^T$, we get:
$$ g'(t) = x(t)^T A(t)^T x(t) + x(t)^T A(t) x(t) $$
$$ g'(t) = x(t)^T (A(t)^T + A(t)) x(t) $$
Let $S(t) = A(t)^T + A(t)$. We need to compute this matrix.
The matrix $A(t)$ is given by:
$$ A(t)=\begin{pmatrix} 1+\sin^2 t & -1 & -1 \\ 1 & 1/(1+\sin^2 t) & -1 \\ 1 & 1 & 1+\cos^2 t \end{pmatrix} $$
Its transpose $A(t)^T$ is:
$$ A(t)^T = \begin{pmatrix} 1+\sin^2 t & 1 & 1 \\ -1 & 1/(1+\sin^2 t) & 1 \\ -1 & -1 & 1+\cos^2 t \end{pmatrix} $$
Now, we compute the sum $S(t) = A(t) + A(t)^T$:
$$ S(t) = \begin{pmatrix} (1+\sin^2 t) + (1+\sin^2 t) & -1+1 & -1+1 \\ 1-1 & 1/(1+\sin^2 t) + 1/(1+\sin^2 t) & -1+1 \\ 1-1 & 1-1 & (1+\cos^2 t) + (1+\cos^2 t) \end{pmatrix} $$
$$ S(t) = \begin{pmatrix} 2(1+\sin^2 t) & 0 & 0 \\ 0 & 2/(1+\sin^2 t) & 0 \\ 0 & 0 & 2(1+\cos^2 t) \end{pmatrix} $$
$S(t)$ is a diagonal matrix. Let $x(t) = (x_1(t), x_2(t), x_3(t))^T$. Then $g'(t)$ becomes:
$$ g'(t) = \begin{pmatrix} x_1(t) & x_2(t) & x_3(t) \end{pmatrix} \begin{pmatrix} 2(1+\sin^2 t) & 0 & 0 \\ 0 & 2/(1+\sin^2 t) & 0 \\ 0 & 0 & 2(1+\cos^2 t) \end{pmatrix} \begin{pmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \end{pmatrix} $$
$$ g'(t) = 2(1+\sin^2 t) x_1(t)^2 + \frac{2}{1+\sin^2 t} x_2(t)^2 + 2(1+\cos^2 t) x_3(t)^2 $$
To determine the sign of $g'(t)$, we examine the coefficients of $x_i(t)^2$:
1.  $2(1+\sin^2 t)$: Since $0 \le \sin^2 t \le 1$, we have $1 \le 1+\sin^2 t \le 2$. Thus, $2 \le 2(1+\sin^2 t) \le 4$. The coefficient is strictly positive.
2.  $2/(1+\sin^2 t)$: Since $1 \le 1+\sin^2 t \le 2$, we have $1/2 \le 1/(1+\sin^2 t) \le 1$. Thus, $1 \le 2/(1+\sin^2 t) \le 2$. The coefficient is strictly positive.
3.  $2(1+\cos^2 t)$: Since $0 \le \cos^2 t \le 1$, we have $1 \le 1+\cos^2 t \le 2$. Thus, $2 \le 2(1+\cos^2 t) \le 4$. The coefficient is strictly positive.

All coefficients are strictly positive for all $t \in \mathbb{R}$. The terms $x_1(t)^2$, $x_2(t)^2$, $x_3(t)^2$ are non-negative.
Therefore, $g'(t) = 2(1+\sin^2 t) x_1(t)^2 + \frac{2}{1+\sin^2 t} x_2(t)^2 + 2(1+\cos^2 t) x_3(t)^2 \ge 0$ for all $t$.
This shows that $g(t) = \|x(t)\|^2$ is a non-decreasing function.

Now let's consider the function $f(t) = \|x(t)\| = \sqrt{g(t)}$. The derivative of $f(t)$ is:
$$ f'(t) = \frac{1}{2\sqrt{g(t)}} g'(t) = \frac{g'(t)}{2\|x(t)\|} $$
Since $x(t)$ is a solution to a linear homogeneous ODE system $\dot{x} = A(t)x$ with continuous $A(t)$, and $x(0) \neq 0$, the unique solution $x(t)$ cannot be the zero vector for any $t \in \mathbb{R}$. If $x(t_0) = 0$ for some $t_0$, then by uniqueness of solutions, $x(t)$ must be identically zero for all $t$, which contradicts $x(0) \neq 0$.
Thus, $\|x(t)\| > 0$ for all $t \in \mathbb{R}$.
Since $g'(t) \ge 0$ and $\|x(t)\| > 0$, we have $f'(t) = \frac{g'(t)}{2\|x(t)\|} \ge 0$ for all $t$.
A function with a non-negative derivative is increasing (non-decreasing).
Therefore, the function $\mathbb{R} \ni t \mapsto \|x(t)\| \in \mathbb{R}$ is increasing.

Furthermore, we can show that $g'(t) > 0$ for all $t$. Since the coefficients $S_{ii}(t)$ are strictly positive, $g'(t) = 0$ if and only if $x_1(t) = x_2(t) = x_3(t) = 0$, which means $x(t)=0$. As we have argued, $x(t)$ is never zero. Therefore, $g'(t) > 0$ for all $t$.
This implies $f'(t) > 0$ for all $t$, which means that $f(t) = \|x(t)\|$ is strictly increasing. A strictly increasing function is also an increasing function (in the non-decreasing sense).

Final Conclusion: The function $\mathbb{R}\ni t \mapsto \|x(t)\|\in \mathbb{R}$ is increasing.

Final Answer: The final answer is $\boxed{The function \mathbb{R}\ni t \mapsto \|x(t)\|\in \mathbb{R} \text{ is increasing}}$