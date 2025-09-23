Suppose that there were $M$ discussions and that this is the biggest possible number. Denote people on the corridor by $A_1, A_2, \ldots, A_{20}$. For every $k \in \{1, 2, \ldots, 20\}$ let $d(k)$ be the number of people with whom $A_k$ had a discussion.
If $A_i$ talked to $A_j$, then let us write $A_i \sim A_j$.

\noindent Fix $i,j$ such that $A_i \sim A_j$. Notice that of course $d(i) + d(j) \leqslant n$ (every one of the rest of the players could have had a discussion only with at most one of $A_i$ or $A_j$, otherwise the condition form the problem would have been violated). Notice that
\begin{align*}
    \sum_{k=1}^{20} d^2(k) = \sum_{i,j: \text{ } A_i \sim A_j}\big(d(i) + d(j)\big) \leqslant 20M.
\end{align*}
We can bound the sum of squares from below in the following way.
\begin{align*}
    \sum_{k=1}^{20} d^2(k) \stackrel{\text{C-S inequality}}{\geqslant} \frac{\big(\sum_{k=1}^{20} d(k)\big)^2}{20} \geqslant \frac{4M^2}{20} = \frac{M^2}{5},
\end{align*}
because the sum of all $d(k)$ equals twice the number of all discussions.
Therefore we need
\begin{align*}
    \frac{M^2}{5} \leqslant 20M,
\end{align*}
so $M \leqslant 100$. Thus the biggest possible number of discussions that took place is 100. To see that it was indeed possible to have exactly 100 discussions, divide those 20 people in the two disjoint groups $A$ and $B$ of equal size. We allow people from every group to talk only to people from the other group. This way we indeed obtain $10 \cdot 10 = 100$ discussions.