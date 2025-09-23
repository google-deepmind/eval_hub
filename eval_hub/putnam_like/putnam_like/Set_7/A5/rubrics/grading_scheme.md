This step is worth 2 points.
Let $(n_k)_k$ be any sequence of positive integers diverging to $\infty$. We will show the following observation:
there is $\gamma > 1$ such that sequences $( \lfloor \gamma^{m_k} \rfloor )_k$ and $(n_k)_k$ have infinitely many common terms.

For any $1 < \alpha < \beta$ we consider the set $\mathcal{A} := \bigcup_{k=1}^\infty \left[ \alpha^{m_k}, \beta^{m_k} - 1 \right]$. We claim that there is $a > 0$ such that $(a, \infty) \subset \mathcal{A}$. Indeed, since $\left( \frac{\beta}{\alpha} \right)^{m_k} \to \infty$, there is $k_0$ such that for $k \geq k_0$ we have $\alpha^{m_{k+1}} < \beta^{m_k} - 1$. Hence $\bigcup_{k=k_0}^\infty \left[ \alpha^{m_k}, \beta^{m_k} - 1 \right] = [ \alpha^{m_{k_0}}, \infty)$. 

This step is worth 7 points.
Fix any $1 < \alpha_1 < \beta_1$. Then, from above considerations, there is $k_1$ such that $\left[ \alpha^{m_{k_1}}, \beta^{m_{k_1}} - 1 \right]$ contains at least one of the term of $(n_k)_k$. Call this term $t_1$ and define $\alpha_2 = t_1^{1/m_{k_1}}$ and $\beta_2 = \left( t_1 + \frac12 \right)^{1/m_{k_1}}$. Then $[\alpha_2, \beta_2] \subset [\alpha_1, \beta_1]$ and if $x \in [\alpha_2, \beta_2]$, then $\lfloor x^{m_{k_1}} \rfloor  = t_1$. Again, we find $k_2$ such that $[\alpha_2^{m_{k_2}}, \beta_2^{m_{k_2}} - 1]$ contains some term of $(n_k)_k$, different than $t_1$, we call it $t_2$. Then we define $\alpha_3 = t_2^{1/m_{k_2}}$ and $\beta_3 = \left( t_2 + \frac12 \right)^{1/m_{k_2}}$ and iterate the procedure. From Cantor's theorem we know that
$$
\bigcap_{j=1}^\infty [\alpha_j, \beta_j] \neq \emptyset.
$$
Take $\gamma \in \bigcap_{j=1}^\infty [\alpha_j, \beta_j]$ and note that then $\lfloor \gamma^{m_{k_j}} \rfloor = t_j$ for all $j \geq 1$. Hence the sequences $( \lfloor \gamma^{m_k} \rfloor )_k$ and $(n_k)_k$ have infinitely many common terms.

This step is worth 1 point.
Now we are ready to solve the problem. Suppose that $(a_k)_k$ does not converge to $0$. Hence it has a subsequence $(a_{n_k})_k$ such that $a_{n_k} \to a \neq 0$ or $a_{n_k} \to \pm \infty$. However, $(n_k)_k$ and $( \lfloor \gamma^{m_k} \rfloor )_k$ have infinitely many common terms, and this contradicts the fact that $a_{\lfloor \gamma^{m_k} \rfloor} \to 0$. Hence $a_n \to 0$.