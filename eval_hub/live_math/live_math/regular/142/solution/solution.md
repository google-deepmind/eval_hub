Notice that the equation is equivalent to
    \begin{align*}
        [(z-2)^8 + 3(t+1)^2]\sqrt{z^2 -2z + 2+|t+1|} &= [2z(t+1) - 4(t+1)]^2\\
        &= [2(t+1)(z-2)]^2 = 4(z-2)^2(t+1)^2.
    \end{align*}
    Now, we have the following inequalities.
    \begin{align*}
        [(z-2)^8 + 3(t+1)^2]\sqrt{z^2 -2z + 2+|t+1|} &\geqslant [(z-2)^8 + 3(t+1)^2]\sqrt{|t+1|}\\
        &= 4 \cdot \frac{(z-2)^8 + (t+1)^2 + (t+1)^2 + (t+1)^2}{4} \cdot \sqrt{|t+1|}\\
        &\geqslant 4((z-2)^8(t+1)^6)^{\frac{1}{4}} \cdot \sqrt{|t+1|}\\
        &= 4(z-2)^2\cdot|t+1|\cdot |t+1|^{\frac{1}{2}}  \sqrt{|t+1|}\\
        &= 4(z-2)^2\cdot (t+1)^2.
    \end{align*}
    So, to have an equality between the left-hand side and the right-hand side, we need the 2 inequalities above to be equalities. The first one is an equality if and only if $z^2 - 2z + 2 = 0$ or $\begin{cases}z=2\\t=-1 \end{cases}$. The first of those conditions has no real solutions. The second inequality becomes an equality when $(z-2)^8 = (t+1)^2$ so $(z-2)^4 = |t+1|$, or $\begin{cases}t=-1\\z \in \mathbb{R}\end{cases}$. Both of those inequalities have to become equalities, so we end up with only one solution, that is $\begin{cases}z=2\\t=-1\end{cases}$. So $z+t=1$.