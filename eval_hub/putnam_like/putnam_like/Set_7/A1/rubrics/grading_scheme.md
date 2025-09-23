Solution step (2 points):
Let $m_A$ and $\chi_A$ denote minimal and characteristic polynomials of $A$ respectively. Of course, $\deg \chi_A = 2$ and from Cayley-Hamilton theorem
$$
\chi_A (A) = 0.
$$
Therefore $m_A$ divides $\chi_A$ and $\deg m_A \leq 2$. Define the polynomial $$P(x) = x^{k+1} - x^k = x^k (x - 1).$$ Then, the assumption rewrites as $P(A) = 0$, and therefore $m_A$ divides $P$ as well. 

Solution step (8 points):
Note that all the roots of $P$ are $0$ and $1$. Hence the set of roots of $m_A$ is contained in $\{0,1\}$. Clearly, if $1$ is a root of $m_A$, then its multiplicity is equal to $1$. Now we will consider few cases.

If the multiplicity of $1$ is zero (namely - it is not a root), then $m_A (x) = x$ or $m_A (x) = x^2$. In the first case we have $A = 0$, in the second case $A^2 = 0$ and in both cases $A^3 = A^2$.

If the multiplicity of $1$ is equal to $1$, then $m_A (x) = x - 1$ or $m_A (x) = x (x-1)$. In the first case $A = I$ and clearly $A^3 = A^2$. In the second case we get $A^2 = A$, and again $A^3 = A^2$.