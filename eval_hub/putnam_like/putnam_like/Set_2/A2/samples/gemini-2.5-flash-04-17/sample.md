Let the given equation be
\begin{equation}\label{eq:1}
\left(\int_{a}^b g(x)f(x)^2\ dx\right)^2=\left(\int_{a}^b f(x)^2\ dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\ dx\right).
\end{equation}
Let $w(x) = f(x)^2$. Since $f$ is continuous, $w(x)$ is continuous and $w(x) \ge 0$ for all $x \in [a,b]$. The equation becomes
$$ \left(\int_{a}^b g(x)w(x)\ dx\right)^2=\left(\int_{a}^b w(x)\ dx\right)\left(\int_{a}^b g(x)^2 w(x)\ dx\right). $$
This equation has the form of the Cauchy-Schwarz inequality for integrals with equality. The Cauchy-Schwarz inequality states that for real-valued functions $u(x)$ and $v(x)$,
$$ \left(\int_a^b u(x)v(x)\ dx\right)^2 \le \left(\int_a^b u(x)^2\ dx\right)\left(\int_a^b v(x)^2\ dx\right). $$
The equality holds if and only if $u(x)$ and $v(x)$ are linearly dependent, i.e., there exist constants $c_1, c_2$, not both zero, such that $c_1 u(x) + c_2 v(x) = 0$ for all $x \in [a,b]$ (since the functions here are continuous).

Let's apply this to our equation. Let $u(x) = g(x)\sqrt{w(x)}$ and $v(x) = \sqrt{w(x)}$. Then $u(x)v(x) = g(x)w(x)$, $u(x)^2 = g(x)^2 w(x)$, and $v(x)^2 = w(x)$.
The equation $\eqref{eq:1}$ is exactly the equality condition for the Cauchy-Schwarz inequality applied to $u(x) = g(x)\sqrt{f(x)^2} = g(x)|f(x)|$ and $v(x) = \sqrt{f(x)^2} = |f(x)|$.

Case 1: $v(x) = |f(x)|$ is identically zero on $[a,b]$.
This means $f(x) = 0$ for all $x \in [a,b]$. In this case, $f(x)^2 = 0$ for all $x$, and equation $\eqref{eq:1}$ becomes
$$ \left(\int_{a}^b g(x)\cdot 0\ dx\right)^2=\left(\int_{a}^b 0\ dx\right)\left(\int_{a}^b g(x)^2 \cdot 0\ dx\right) $$
$$ 0^2 = 0 \cdot 0 $$
$$ 0 = 0. $$
This equation holds true for any continuous function $g: [a,b] \to \mathbb{R}$.
So, if $f(x) = 0$ for all $x \in [a,b]$, any continuous function $g: [a,b] \to \mathbb{R}$ is a solution.

Case 2: $v(x) = |f(x)|$ is not identically zero on $[a,b]$.
In this case, the equality in Cauchy-Schwarz holds if and only if there exists a constant $\lambda$ such that $u(x) = \lambda v(x)$ for all $x \in [a,b]$. (If $v$ is not identically zero, the linear dependence $c_1 u + c_2 v = 0$ implies $u = (-c_2/c_1) v$ if $c_1 \ne 0$, or $v=0$ if $c_1=0$, which contradicts $v$ not identically zero. So $c_1 \ne 0$ and we can set $\lambda = -c_2/c_1$).
The condition $u(x) = \lambda v(x)$ becomes
$$ g(x)|f(x)| = \lambda |f(x)| \quad \text{ for all } x \in [a,b]. $$
This can be rewritten as
$$ |f(x)| (g(x) - \lambda) = 0 \quad \text{ for all } x \in [a,b]. $$
This means that for each $x \in [a,b]$, either $f(x) = 0$ or $g(x) - \lambda = 0$.

Let $A = \{x \in [a,b] : f(x) \ne 0\}$. Let $B = \{x \in [a,b] : f(x) = 0\}$. $[a,b] = A \cup B$.
The condition $|f(x)| (g(x) - \lambda) = 0$ means:
- For $x \in A$, since $f(x) \ne 0$, we must have $g(x) - \lambda = 0$, so $g(x) = \lambda$.
- For $x \in B$, since $f(x) = 0$, the equation becomes $0 \cdot (g(x) - \lambda) = 0$, which is $0=0$. This equation provides no constraint on $g(x)$ for $x \in B$.

So, for some constant $\lambda$, $g(x)$ must be equal to $\lambda$ for all $x \in A$.
We are given that $g$ is a continuous function on $[a,b]$.
The set $A = \{x \in [a,b] : f(x) \ne 0\}$ is open because $f$ is continuous.
Since $g(x) = \lambda$ for all $x \in A$, and $g$ is continuous, $g(x)$ must also be equal to $\lambda$ for all $x$ in the closure of $A$, denoted $\bar{A}$.
$\bar{A} = \overline{\{x \in [a,b] : f(x) \ne 0\}}$.
If $x_0 \in \bar{A}$, then there exists a sequence $x_n \in A$ such that $x_n \to x_0$. Since $g$ is continuous, $g(x_0) = \lim_{n\to\infty} g(x_n)$. As $x_n \in A$, $g(x_n) = \lambda$ for all $n$. Thus $g(x_0) = \lambda$.
So, any continuous function $g$ satisfying the equation must satisfy $g(x) = \lambda$ for all $x \in \bar{A}$, for some constant $\lambda$.

Now we need to check if any continuous function $g$ satisfying $g(x) = \lambda$ for all $x \in \bar{A}$ (for some $\lambda$) is a solution.
Let $g$ be a continuous function such that $g(x) = \lambda$ for all $x \in \bar{A}$.
The set $B = \{x \in [a,b] : f(x) = 0\}$ is closed. Its interior $B^\circ = \{x \in [a,b] : \exists \delta>0 \text{ s.t. } (x-\delta, x+\delta)\cap[a,b] \subseteq B\}$ is an open set.
$[a,b] = \bar{A} \cup B^\circ$ (disjoint union except possibly at boundary points). More precisely, $\bar{A} = [a,b]\setminus B^\circ$.
We know $g(x)=\lambda$ for $x \in \bar{A}$.
The equation is $\left(\int_{a}^b g(x)f(x)^2\ dx\right)^2=\left(\int_{a}^b f(x)^2\ dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\ dx\right)$.
Let $w(x) = f(x)^2$.
$\int_a^b g(x)w(x)\ dx = \int_{\bar{A}} g(x)w(x)\ dx + \int_{B^\circ} g(x)w(x)\ dx$.
For $x \in B^\circ$, $f(x)=0$, so $w(x)=0$. The integral over $B^\circ$ is 0.
$\bar{A} = A \cup (\bar{A} \cap B)$. For $x \in \bar{A} \cap B$, $f(x)=0$, so $w(x)=0$.
So $\int_a^b g(x)w(x)\ dx = \int_A g(x)w(x)\ dx$.
For $x \in A$, $g(x)=\lambda$.
$\int_A g(x)w(x)\ dx = \int_A \lambda w(x)\ dx = \lambda \int_A w(x)\ dx$.
Note that $\int_A w(x)\ dx = \int_{\{x: f(x)\ne 0\}} f(x)^2 dx$. Since $f(x)=0$ on $B$, $\int_A f(x)^2 dx = \int_{A \cup B} f(x)^2 dx = \int_a^b f(x)^2 dx$. Let $W = \int_a^b f(x)^2 dx$.
So $\int_a^b g(x)w(x)\ dx = \lambda W$.

Now consider $\int_a^b g(x)^2 w(x)\ dx$.
$\int_a^b g(x)^2 w(x)\ dx = \int_{\bar{A}} g(x)^2 w(x)\ dx + \int_{B^\circ} g(x)^2 w(x)\ dx$.
For $x \in B^\circ$, $w(x)=0$. The integral over $B^\circ$ is 0.
For $x \in \bar{A}$, $g(x)=\lambda$.
$\int_{\bar{A}} g(x)^2 w(x)\ dx = \int_{\bar{A}} \lambda^2 w(x)\ dx = \lambda^2 \int_{\bar{A}} w(x)\ dx$.
As before, $\int_{\bar{A}} w(x)\ dx = \int_A w(x)\ dx = W$.
So $\int_a^b g(x)^2 w(x)\ dx = \lambda^2 W$.

Substitute these into the original equation:
$(\lambda W)^2 = W (\lambda^2 W)$
$\lambda^2 W^2 = \lambda^2 W^2$.
This equation is satisfied for any constant $\lambda$.
So, any continuous function $g: [a,b] \to \mathbb{R}$ such that $g(x)$ is constant on $\bar{A} = \overline{\{x \in [a,b] : f(x) \ne 0\}}$ is a solution.

Note that if $f(x)=0$ for all $x$, then $A=\emptyset$, $\bar{A}=\emptyset$. The condition $g(x)=\lambda$ for $x \in \emptyset$ is vacuously true for any $g$ and any $\lambda$. This doesn't restrict $g$. In this case, any continuous $g$ is a solution. This matches our finding in Case 1.

If $f(x)$ is not identically zero, then $\bar{A}$ is a non-empty closed set. The solutions are continuous functions $g$ which are constant on this set $\bar{A}$.

The set $\bar{A}$ is the set of points $x \in [a,b]$ such that every neighborhood of $x$ contains points where $f(y) \ne 0$. This is the complement of the interior of the set of zeros of $f$.

The set of solutions is:
If $f(x) = 0$ for all $x \in [a,b]$, then $g$ can be any continuous function on $[a,b]$.
If $f(x)$ is not identically zero on $[a,b]$, let $C = \overline{\{x \in [a,b] : f(x) \ne 0\}}$. The solutions are continuous functions $g: [a,b] \to \mathbb{R}$ such that $g(x)$ is constant on $C$. That is, there exists a constant $\lambda \in \mathbb{R}$ such that $g(x) = \lambda$ for all $x \in C$.

The final answer is $\boxed{g \text{ is a continuous function on } [a,b] \text{ such that there exists a constant } \lambda \in \mathbb{R} \text{ for which } g(x) = \lambda \text{ for all } x \in \overline{\{y \in [a,b] : f(y) \ne 0\}}}$.