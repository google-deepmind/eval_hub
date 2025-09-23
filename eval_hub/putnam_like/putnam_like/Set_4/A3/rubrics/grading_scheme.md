Solution step (2 points):
We will provide counterexamples for both implications. Consider the field $\mathbb{F}_7$ and compute all positive elements of it
$$
0^2 = 0, \ 1^2 = 1, \ 2^2 = 4, \ 3^2 = 2, \ 4^2 = 2, \ 5^2 = 4, \ 6^2 = 1.
$$
Hence the set of all positive elements in $\mathbb{F}_7$ is $\{0,1,2,4\}$.

Solution step (4 points):
Consider the matrix $A \in \mathbb{M}_2 (\mathbb{F}_7)$ given by
$$
A := \begin{bmatrix}
2 & 3 \\ 3 & 2
\end{bmatrix}.
$$
Then it is symmetric and all its leading principal minors are positive, indeed
$$
\det [2] = 2, \quad \det A = 2.
$$
We will now look for eigenvalues of $A$. Clearly
$$
\det \begin{bmatrix}
2 -\lambda & 3 \\ 3 & 2 - \lambda
\end{bmatrix} = (2-\lambda)^2 + 5 = \lambda^2 + 3\lambda + 2 = (\lambda + 1) (\lambda + 2).
$$
Hence $\sigma (A) = \{ 5, 6 \}$. However both eigenvalues are not positive.

Solution step (4 points):
Consider now the matrix $B \in \mathbb{M}_2 (\mathbb{F}_7)$ given by
$$
B := \begin{bmatrix}
3 & 3 \\ 3 & 2
\end{bmatrix}.
$$
Then the first leading minor is not positive: $\det [3] = 3$. However, if we compute the eigenvalues
$$
\det \begin{bmatrix}
3 -\lambda & 3 \\ 3 & 2-\lambda
\end{bmatrix} = (3-\lambda)(2-\lambda) + 5 = \lambda^2 +2 \lambda +  4 = (\lambda + 3)(\lambda + 6)
$$
we find that $\sigma(B) = \{1,4\}$, so both eigenvalues are positive in $\mathbb{F}_7$.