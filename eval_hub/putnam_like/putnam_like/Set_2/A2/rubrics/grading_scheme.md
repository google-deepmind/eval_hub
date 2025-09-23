This step is worth 8 points.
Let $g: [a,b]\to \mathbb{R}$ satisfy \eqref{E-Q}. Then we have
$$
\left(\int_{a}^b g(x)f(x)^2dx\right)^2=\left(\int_{a}^b\left (g(x)f(x)\right)f(x)dx\right)^2.
$$
Furthermore, the Cauchy-Schwarz inequality implies that
$$
\left(\int_{a}^b (g(x)f(x))f(x)\ dx\right)^2\leq \left(\int_{a}^b (g(x)f(x))^2dx\right)\left(\int_{a}^b f(x)^2dx\right).
$$
Consequently, we obtain the following estimation:
$$
\begin{aligned}
\left(\int_{a}^b g(x)f(x)^2\ dx\right)^2&=\left(\int_{a}^b\left (g(x)f(x)\right)f(x)dx\right)^2\leq\\
&\leq \left(\int_{a}^b (g(x) f(x))^2\ dx\right)\left(\int_{a}^b f(x)^2\ dx\right)=\\
&= \left(\int_{a}^b f(x)^2\ dx\right)\left(\int_{a}^b g(x)^2 f(x)^2\ dx\right).
\end{aligned}
$$

This step is worth 2 points.
It is well known that the equality in the Cauchy-Schwarz inequality holds if and only if $g(x)f(x)$ is a constant multiple of $f(x)$. Therefore, we can conclude that there exists $c\in \mathbb{R}$ such that
$$
g(x)f(x)=c\cdot f(x) \text{ for all }x\in [a,b] \Longleftrightarrow (g(x)-c)\cdot f(x)=0  \text{ for all }x\in [a,b].
$$
Then we have two possibilities:
\begin{enumerate}
\item If $f(x) \equiv 0$, then any continuous function $g(x)$ is a solution.
\item If $f(x) \neq 0$ for some $x \in [a,b]$, then the set of solutions consists of all continuous functions $g: [a,b] \to \mathbb{R}$ such that
$$
g(x) = c \quad \text{for all } x \in [a,b] \text{ with } f(x) \neq 0,
$$
for some constant $c \in \mathbb{R}$.
\end{enumerate}
