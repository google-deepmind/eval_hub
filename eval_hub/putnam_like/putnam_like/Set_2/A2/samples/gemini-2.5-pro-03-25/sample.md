Let the given equation be
\begin{equation} \label{eq:1}
\left(\int_{a}^b g(x)f(x)^2\ dx\right)^2=\left(\int_{a}^b f(x)^2\ dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\ dx\right).
\end{equation}
Let $h_1(x) = f(x)$ and $h_2(x) = g(x)f(x)$. Since $f$ and $g$ are continuous on $[a,b]$, $h_1$ and $h_2$ are also continuous on $[a,b]$. Continuous functions on a closed interval are square integrable.
The equation \eqref{eq:1} can be rewritten in terms of $h_1$ and $h_2$ as:
$$ \left(\int_{a}^b h_2(x) f(x) dx\right)^2 = \left(\int_{a}^b h_1(x)^2 dx\right) \left(\int_{a}^b h_2(x)^2 dx\right) $$
Wait, this is not correct. Let's redefine $h_1$ and $h_2$.
Let $h_1(x) = f(x)$ and $h_2(x) = g(x)f(x)$. Then the equation becomes:
$$ \left(\int_{a}^b g(x)f(x)^2\ dx\right)^2 = \left(\int_{a}^b h_1(x)^2 dx\right) \left(\int_{a}^b h_2(x)^2 dx\right) $$
The middle term is $\int_a^b g(x)f(x)^2 dx = \int_a^b f(x) (g(x)f(x)) dx = \int_a^b h_1(x) h_2(x) dx$.
So the equation \eqref{eq:1} is
$$ \left(\int_{a}^b h_1(x) h_2(x) dx\right)^2 = \left(\int_{a}^b h_1(x)^2 dx\right) \left(\int_{a}^b h_2(x)^2 dx\right) $$
This is exactly the equality case of the Cauchy-Schwarz inequality for integrals.
The Cauchy-Schwarz inequality states that for square-integrable functions $h_1, h_2$:
$$ \left(\int_{a}^b h_1(x) h_2(x) dx\right)^2 \le \left(\int_{a}^b h_1(x)^2 dx\right) \left(\int_{a}^b h_2(x)^2 dx\right) $$
Equality holds if and only if $h_1$ and $h_2$ are linearly dependent almost everywhere.
Since $h_1(x)=f(x)$ and $h_2(x)=g(x)f(x)$ are continuous functions, the equality holds if and only if $h_1$ and $h_2$ are linearly dependent everywhere on $[a,b]$.
This means there exists a constant $c \in \mathbb{R}$ such that $h_2(x) = c h_1(x)$ for all $x \in [a,b]$ or $h_1(x) = c h_2(x)$ for all $x \in [a,b]$.

Case 1: $h_2(x) = c h_1(x)$ for all $x \in [a,b]$.
This means $g(x)f(x) = c f(x)$ for all $x \in [a,b]$. This can be written as $(g(x)-c)f(x) = 0$.

Case 2: $h_1(x) = c h_2(x)$ for all $x \in [a,b]$.
This means $f(x) = c g(x) f(x)$ for all $x \in [a,b]$. This can be written as $(1 - c g(x))f(x) = 0$.
If $c=0$, this implies $f(x)=0$ for all $x$.
If $c \ne 0$, let $\lambda = 1/c$. Then $(1 - c g(x))f(x) = 0 \implies c(\frac{1}{c} - g(x))f(x) = 0 \implies (\lambda - g(x))f(x) = 0$. This is equivalent to $(g(x)-\lambda)f(x)=0$. This is the same form as Case 1 with constant $\lambda$.

So, the condition for equation \eqref{eq:1} to hold is that there must exist a constant $c \in \mathbb{R}$ such that
\begin{equation} \label{eq:2}
(g(x)-c)f(x) = 0 \quad \text{for all } x \in [a,b].
\end{equation}
We need to find all continuous functions $g: [a,b] \to \mathbb{R}$ satisfying this condition for some $c \in \mathbb{R}$.

Let's analyze the condition \eqref{eq:2}.
Let $N = \{x \in [a,b] \mid f(x) \ne 0\}$ and $Z = \{x \in [a,b] \mid f(x) = 0\}$.
For $x \in N$, $f(x) \ne 0$, so the condition \eqref{eq:2} implies $g(x)-c = 0$, i.e., $g(x)=c$.
For $x \in Z$, $f(x)=0$, so the condition \eqref{eq:2} becomes $(g(x)-c) \cdot 0 = 0$, which is always true for any value of $g(x)$.

So, the condition requires that $g(x) = c$ for all $x \in N$.
Since $g$ must be continuous on $[a,b]$, its values on $Z$ are related to its values on $N$.
Let $x_0 \in Z$. If $x_0$ is a limit point of $N$, then there exists a sequence $(x_n)$ in $N$ such that $x_n \to x_0$. By continuity of $g$:
$$ g(x_0) = \lim_{n \to \infty} g(x_n) $$
Since $x_n \in N$, we have $g(x_n) = c$. Thus
$$ g(x_0) = \lim_{n \to \infty} c = c $$
So, $g(x)$ must be equal to $c$ for all $x \in N$ and for all limit points of $N$ that are in $Z$. The set of limit points of $N$ is $\overline{N}$. So $g(x)=c$ for all $x \in N \cup (Z \cap \overline{N})$.
The set $Z \cap \overline{N}$ is the boundary of $Z$, denoted $\partial Z$. Note $\partial Z = \partial N$.

Let $Z^\circ$ be the interior of $Z$. $Z = Z^\circ \cup \partial Z$.
We must have $g(x)=c$ on $N \cup \partial Z$.
For $x \in Z^\circ$, $f(x)=0$, and $x$ is not a limit point of $N$. In fact, $Z^\circ$ is an open set consisting of points $x$ such that $f(y)=0$ in a neighborhood of $x$. The condition \eqref{eq:2} does not impose any restriction on the value of $g(x)$ for $x \in Z^\circ$.
However, $g$ must be continuous on $[a,b]$. If $Z^\circ$ is not empty, it is a union of disjoint open intervals. Let $(u, v)$ be such an interval. Then $u, v \in \partial Z$. (Unless $u=a$ or $v=b$. If $u=a \in Z^\circ$, not possible. If $u=a$ and $a \in \partial Z$, then $g(a)=c$. Same for $v=b$.)
So $g(u)=c$ and $g(v)=c$. The function $g$ must be continuous on $[u,v]$. Any continuous function on $[u,v]$ such that $g(u)=c$ and $g(v)=c$ would satisfy the continuity requirement on $[u,v]$.

Let's verify this conclusion. Suppose $g$ is a continuous function on $[a,b]$ and there exists $c \in \mathbb{R}$ such that $g(x)=c$ for all $x \in N$. Does $g$ satisfy the original equation \eqref{eq:1}?
We showed that this condition implies $(g(x)-c)f(x)=0$ for all $x \in [a,b]$.
Let's re-evaluate the integrals in \eqref{eq:1}:
The left hand side is:
$$ \left(\int_{a}^b g(x)f(x)^2\ dx\right)^2 $$
We have $g(x)f(x)^2 = c f(x)^2$ if $x \in N$.
If $x \in Z$, $f(x)=0$, so $f(x)^2=0$. Then $g(x)f(x)^2 = g(x) \cdot 0 = 0$.
Also $c f(x)^2 = c \cdot 0 = 0$.
So $g(x)f(x)^2 = c f(x)^2$ for all $x \in [a,b]$.
Therefore, $\int_a^b g(x)f(x)^2 dx = \int_a^b c f(x)^2 dx = c \int_a^b f(x)^2 dx$.
The LHS is $(c \int_a^b f(x)^2 dx)^2 = c^2 \left(\int_a^b f(x)^2 dx\right)^2$.

The right hand side is:
$$ \left(\int_{a}^b f(x)^2\ dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\ dx\right) $$
Let's look at the second integral $\int_a^b g(x)^2 f(x)^2 dx$.
$g(x)^2 f(x)^2 = (g(x)f(x))^2$.
We know $g(x)f(x) = c f(x)$ for all $x \in [a,b]$.
So $g(x)^2 f(x)^2 = (c f(x))^2 = c^2 f(x)^2$ for all $x \in [a,b]$.
Therefore, $\int_a^b g(x)^2 f(x)^2 dx = \int_a^b c^2 f(x)^2 dx = c^2 \int_a^b f(x)^2 dx$.
The RHS is $\left(\int_{a}^b f(x)^2\ dx\right) \left(c^2 \int_{a}^b f(x)^2\ dx\right) = c^2 \left(\int_{a}^b f(x)^2\ dx\right)^2$.

Since LHS = RHS, the equation \eqref{eq:1} is satisfied for any continuous function $g$ such that there exists $c \in \mathbb{R}$ with $g(x)=c$ whenever $f(x) \ne 0$.

Special Case: $f(x) = 0$ for all $x \in [a,b]$.
In this case, $N = \emptyset$. The condition $g(x)=c$ for all $x \in N$ is vacuously true for any continuous function $g$ and any constant $c$.
The original equation \eqref{eq:1} becomes $(0)^2 = (0)(0)$, which is $0=0$. So any continuous function $g$ is a solution. This is consistent with our derived condition.

Summary:
The solutions are all continuous functions $g: [a,b] \to \mathbb{R}$ such that there exists a constant $c \in \mathbb{R}$ with the property that $g(x)=c$ for all $x \in [a,b]$ for which $f(x) \ne 0$.

Let $N = \{x \in [a,b] \mid f(x) \ne 0\}$. The set of solutions is
$$ G = \{ g \in C[a,b] \mid \exists c \in \mathbb{R} \text{ such that } g(x)=c \text{ for all } x \in N \} $$

If $f(x)=0$ for all $x$, then $N=\emptyset$, and $G = C[a,b]$.
If $f(x) \ne 0$ for all $x$, then $N=[a,b]$, and $G = \{ g(x)=c \mid c \in \mathbb{R} \}$. The solutions are constant functions.
If $f(x)$ is zero on some points but not identically zero, let $Z = \{x \mid f(x)=0\}$. $N = [a,b] \setminus Z$.
The condition requires $g(x)$ to be equal to some constant $c$ on $N$.
By continuity, $g(x)$ must also be equal to $c$ on the boundary points of $N$ that belong to $Z$. Let $B = \overline{N} \cap Z$. So $g(x)=c$ on $N \cup B$.
On the interior of $Z$, $Z^\circ = Z \setminus B$, the values of $g(x)$ are only constrained by the continuity requirement. For any component $(u,v)$ of $Z^\circ$, $g$ must be continuous on $[u,v]$ with $g(u)=g(v)=c$.

Final Answer: The final answer is $\boxed{g \in C[a,b] \mid \exists c \in \mathbb{R} \text{ such that } g(x)=c \text{ for all } x \in \{y \in [a,b] \mid f(y) \ne 0\}}$