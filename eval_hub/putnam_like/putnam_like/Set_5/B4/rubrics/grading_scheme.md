Solution step (1 point)
Denote $S=\{x^3\,:\, x\in R\}$. The first property can be rewritten as $S+S\subset S$.

Solution step (2 points)
For fixed $y\in S$ the function $S\ni x\mapsto x+y\in S$ is injective. Moreover, since $S$ is a finite set, this function is a bijection. It means that, for fixed $y\in S$, any $z\in S$ can be written as $z=x+y$, where $x\in S$. In other words: $z-y=x\in S$ i.e. $S$ is closed under subtraction.

Solution step (7 points)
If $a=b$ then $aba+bab=a^3+b^3=c^3$ by the first property. For any $a,b\in R$, $a\neq b$, we have
$$
S\ni(a+b)^3-a^3-b^3=a^2b+aba+ba^2+ab^2+bab+b^2a.
$$
However, thanks to the second property some terms cancel and then
$$
aba+bab\in S,
$$
so $aba+bab$ is a cube of some element $d\in R$.