This step is worth 1 point.
Consider the equation
$$
x P(x-2) = (x-2024)P(x).
$$
Putting $x = 0$ we get that $P(0) = 0$. Hence $P(x) = x P_1(x)$ for some polynomial $P_1$.

This step is worth 6 points.
Putting this form to the equation we arrive at
$$
x (x-2) P_1 (x-2) = (x-2024) x P_1 (x)
$$
and therefore $(x-2) P_1(x-2) = (x-2024) P_1(x)$. Putting $x = 2$ we obtain that $P_1(2) = 0$ and therefore $P_1(x) = (x-2) P_2(x)$ for some polynomial $P_2$. Then putting it to the equation we get
$$
(x-2) (x-4) P_2 (x-2) = (x-2024) (x-2) P_2(x)
$$
and $(x-4) P_2(x-2) = (x-2024) P_2(x)$. Again, putting $x=4$ we get $P_2(4) = 0$ and $P_2(x) = (x-4) P_3(x)$. Iterating this procedure, we generate polynomials $P_i$ such that $P_i(x) = (x-2i) P_{i+1}$ and $(x-2(i+1)) P_{i+1} (x-2) = (x-2024) P_{i+1}(x)$, up to $i=1011$. Then we get that
$$
P_{1011}(x) = (x-2022) P_{1012}(x)
$$ 
and
$$
(x-2024) P_{1012}(x - 2) = (x-2024) P_{1012}(x)
$$

This step is worth 1 point.
Denote temporarily $Q := P_{1012}$. Then we look for $Q$ such that $Q(x-2) = Q(x)$. However it means that $Q$ has to be constant. Indeed, define $R(x) := Q(x) - Q(0)$. Then $R(0)=0$, $R(2) = Q(2)-Q(0) = Q(0)-Q(0)=0$, $R(4) = Q(4)-Q(0) = Q(2) - Q(0) = 0$, ... Hence $R$ has infinitely many zeros, thus $R \equiv 0$. Hence $Q$ is constant. Denote $Q(x) = a$. 

This step is worth 1 point.
Then we obtain that
$$
P(x) = x P_1(x) = x(x-2) P_2(x) = x(x-2)(x-4) P_3(x) = \ldots
$$
$$
= x(x-2)(x-4) \ldots (x-2022) P_{1012}(x) = a x(x-2)(x-4) \ldots (x-2022).
$$

This step is worth 1 point.
One can easily check that such a polynomial satisfies the original equation. Hence all the polynomials satisfying the equation are
$$
P(x) = a x(x-2)(x-4) \ldots (x-2022),
$$
where $a \in \mathbb{R}$.