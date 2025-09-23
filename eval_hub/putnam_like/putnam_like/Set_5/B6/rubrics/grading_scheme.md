This step is worth 2 points.

Consider the function $g(t)=f(1-t)=\sum_{A\in\mathcal{F}} (1-t)^{|A|}t^{|S\setminus A|}$. The expression $(1-t)^{|A|}t^{|S\setminus A|}$ one can recognize as a volume of the set $I_{t,A}:=\prod_{j=1}^n I_{t,A}^{(j)}\subset \mathbb{R}^n$, where

$$
I_{t,A}^{(j)}:=\begin{cases}
[t,1] &\text{if } j\in A\\
[0,t) &\text{if } j\notin A
\end{cases}.
$$

If $j\in (A\setminus B)\cup (B\setminus A)$ then the sets $I_{t,A}^{(j)}$ and $I_{t,B}^{(j)}$ are disjoint, so $A\neq B$ implies that $I_{t,A}$ and $I_{t,B}$ are disjoint. Therefore $g(t)$ is a volume of the set $\bigcup_{A\in\mathcal{F}} I_{t,A}$. 

This step is worth 8 points.

Fix $t_1,\,t_2$ such that $0\leq t_1<t_2\leq 1$ and take $x=(x_1,\ldots,x_n)\in I_{t_1,A}$, for some $A\in \mathcal{F}$. Then we have the equivalence $j\in A \Leftrightarrow x_j\geq t_1$. Construct the set $B$ by the relation

$$
j\in B \Leftrightarrow x_j\geq t_2.
$$

If $j\in B$ then $x_j\geq t_2>t_1$, so $j\in A$. It means $B\subset A$, and $B\in \mathcal{F}$, by the definition of the family $\mathcal{F}$. Moreover, $x\in I_{t_2,B}$, by the construction. Therefore

$$
\bigcup_{A\in\mathcal{F}} I_{t_1,A} \subset \bigcup_{A\in\mathcal{F}} I_{t_2,A},\quad \text{for } 0\leq t_1<t_2\leq 1,
$$

i.e. the volume function $g(t)$ is non-decreasing. Therefore the function $f(t)$ is non-increasing.