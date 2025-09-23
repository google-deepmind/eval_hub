# Solution

To show that the function $\mathbb{R}\ni t \mapsto \|x(t)\|\in \mathbb{R}$ is increasing, I'll determine if its derivative with respect to $t$ is non-negative for all $t$.

## Step 1: Compute the derivative of $\|x(t)\|$

Let me start by computing the derivative of $\|x(t)\|$:

$$\frac{d}{dt}\|x(t)\| = \frac{d}{dt}\sqrt{x(t)^T x(t)} = \frac{1}{2}(x(t)^T x(t))^{-1/2} \cdot \frac{d}{dt}(x(t)^T x(t)) = \frac{1}{2\|x(t)\|} \cdot \frac{d}{dt}(x(t)^T x(t))$$

Next, I'll find the derivative of $x(t)^T x(t)$:

$$\begin{align}
\frac{d}{dt}(x(t)^T x(t)) &= \dot{x}(t)^T x(t) + x(t)^T \dot{x}(t) \\
&= (A(t)x(t))^T x(t) + x(t)^T A(t)x(t) \\
&= x(t)^T A(t)^T x(t) + x(t)^T A(t)x(t) \\
&= x(t)^T (A(t)^T + A(t)) x(t)
\end{align}$$

Therefore:
$$\frac{d}{dt}\|x(t)\| = \frac{1}{2\|x(t)\|} x(t)^T (A(t)^T + A(t)) x(t)$$

## Step 2: Determine if $\frac{d}{dt}\|x(t)\| \geq 0$

To determine the sign of the derivative, I need to examine $A(t) + A(t)^T$.

Given:
$$A(t)=\begin{pmatrix}
  1+\sin^2 t & -1 & -1 \\
  1 & 1/(1+\sin^2 t) & -1 \\
  1 & 1 & 1+\cos^2 t
\end{pmatrix}$$

Taking the transpose:
$$A(t)^T=\begin{pmatrix}
  1+\sin^2 t & 1 & 1 \\
  -1 & 1/(1+\sin^2 t) & 1 \\
  -1 & -1 & 1+\cos^2 t
\end{pmatrix}$$

Computing $A(t) + A(t)^T$ by adding corresponding elements:
$$A(t) + A(t)^T = \begin{pmatrix}
  2(1+\sin^2 t) & 0 & 0 \\
  0 & \frac{2}{1+\sin^2 t} & 0 \\
  0 & 0 & 2(1+\cos^2 t)
\end{pmatrix}$$

## Step 3: Analyze the result

For all $t \in \mathbb{R}$, we have:
- $2(1+\sin^2 t) > 0$ because $1+\sin^2 t > 0$
- $\frac{2}{1+\sin^2 t} > 0$ because $1+\sin^2 t > 0$
- $2(1+\cos^2 t) > 0$ because $1+\cos^2 t > 0$

Therefore, $A(t) + A(t)^T$ is a diagonal matrix with all positive diagonal entries, making it positive definite.

## Step 4: Complete the proof

Since $A(t) + A(t)^T$ is positive definite, for any non-zero vector $x(t)$, we have:
$$x(t)^T (A(t)^T + A(t)) x(t) > 0$$

Given that $x(0) \neq 0$ and the system is homogeneous, by the uniqueness theorem for ODEs, $x(t) \neq 0$ for all $t$.

Therefore:
$$\frac{d}{dt}\|x(t)\| = \frac{1}{2\|x(t)\|} x(t)^T (A(t)^T + A(t)) x(t) > 0$$

Since the derivative is positive for all $t$, the function $t \mapsto \|x(t)\|$ is strictly increasing.