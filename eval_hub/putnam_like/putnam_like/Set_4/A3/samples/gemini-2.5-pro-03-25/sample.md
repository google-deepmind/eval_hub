Solution:

Let $A \in \mathbb{M}_n (\mathbb{F}_p)$ be a symmetric matrix such that all its eigenvalues $\lambda_1, \dots, \lambda_n$ are in $\mathbb{F}_p$.
Let $D_k = \det(A_k)$ for $k=1, \dots, n$ be the leading principal minors (LPMs) of $A$, where $A_k$ is the top-left $k \times k$ submatrix of $A$.
An element $x \in \mathbb{F}_p$ is defined as "positive" if it is a square in $\mathbb{F}_p$, i.e., $x = y^2$ for some $y \in \mathbb{F}_p$. Note that $0 = 0^2$ is considered positive by this definition.

The question asks whether the following equivalence holds:
(All eigenvalues $\lambda_i$ are positive in $\mathbb{F}_p$) $\iff$ (All leading principal minors $D_k$ are positive in $\mathbb{F}_p$).
Using the definition of "positive", this translates to:
(All $\lambda_i$ are squares in $\mathbb{F}_p$) $\iff$ (All $D_k$ are squares in $\mathbb{F}_p$).

We examine the statement based on the prime $p$.

**Case 1: $p=2$**
In $\mathbb{F}_2 = \{0, 1\}$, the squares are $0^2=0$ and $1^2=1$. Thus, every element in $\mathbb{F}_2$ is a square ("positive").
The problem statement assumes $A$ is symmetric and all its eigenvalues are in $\mathbb{F}_2$.
The LPMs $D_k$ are determinants of submatrices of $A$. Since the entries of $A$ are in $\mathbb{F}_2$, the determinants $D_k$ will also be in $\mathbb{F}_2$.
The statement becomes:
(All $\lambda_i \in \{0, 1\}$) $\iff$ (All $D_k \in \{0, 1\}$).
The left side is true by the assumption that eigenvalues are in $\mathbb{F}_p = \mathbb{F}_2$.
The right side is true because the LPMs are computed within $\mathbb{F}_2$.
Since both sides of the equivalence are always true under the given conditions for $p=2$, the statement holds for $p=2$.

**Case 2: $p > 2$**
In this case, not all elements of $\mathbb{F}_p$ are squares. The non-zero elements $\mathbb{F}_p^*$ form a cyclic group of order $p-1$. The non-zero squares (quadratic residues) form a subgroup of index 2. There are $(p-1)/2$ non-zero squares and $(p-1)/2$ non-squares (quadratic non-residues). Zero is also a square.

We need to check two implications:
1.  (All $\lambda_i$ are squares) $\implies$ (All $D_k$ are squares).
2.  (All $D_k$ are squares) $\implies$ (All $\lambda_i$ are squares).

Let's test these implications with a counterexample. Consider $n=2$ and $p=5$.
In $\mathbb{F}_5 = \{0, 1, 2, 3, 4\}$, the squares are $0^2=0$, $1^2=1$, $2^2=4$, $3^2=9 \equiv 4$, $4^2=16 \equiv 1$. The squares ("positive" elements) are $\{0, 1, 4\}$. The non-squares are $\{2, 3\}$.

**Testing Implication 1: (All $\lambda_i$ are squares) $\implies$ (All $D_k$ are squares)**
Let $A = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix} \in \mathbb{M}_2 (\mathbb{F}_5)$. $A$ is symmetric.
The characteristic polynomial is $\det(A - \lambda I) = \det \begin{pmatrix} 2-\lambda & 2 \\ 2 & -\lambda \end{pmatrix} = (2-\lambda)(-\lambda) - 2^2 = -2\lambda + \lambda^2 - 4 = \lambda^2 - 2\lambda + 1 = (\lambda-1)^2$.
The eigenvalues are $\lambda_1 = 1, \lambda_2 = 1$. Both are in $\mathbb{F}_5$.
Are the eigenvalues squares? Yes, $1 = 1^2$ is a square in $\mathbb{F}_5$. So, all eigenvalues are squares.
Now let's check the LPMs:
$D_1 = \det(A_1) = \det([2]) = 2$.
$D_2 = \det(A) = \det \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix} = 2(0) - 2(2) = -4 \equiv 1$.
The LPMs are $\{2, 1\}$.
Are all LPMs squares? $D_1 = 2$ is *not* a square in $\mathbb{F}_5$. $D_2 = 1$ is a square.
Since $D_1$ is not a square, the condition "All $D_k$ are squares" is false.
We have found a case where all eigenvalues are squares (1, 1), but not all LPMs are squares (2, 1).
Therefore, the implication (All $\lambda_i$ are squares) $\implies$ (All $D_k$ are squares) is **FALSE** for $p > 2$.

**Testing Implication 2: (All $D_k$ are squares) $\implies$ (All $\lambda_i$ are squares)**
Let $A = \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} \in \mathbb{M}_2 (\mathbb{F}_5)$. $A$ is symmetric.
Let's check the LPMs:
$D_1 = \det(A_1) = \det([0]) = 0$.
$D_2 = \det(A) = \det \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} = 0(0) - 2(2) = -4 \equiv 1$.
The LPMs are $\{0, 1\}$.
Are all LPMs squares? $D_1=0=0^2$ is a square. $D_2=1=1^2$ is a square. Yes, all LPMs are squares.
Now let's find the eigenvalues:
The characteristic polynomial is $\det(A - \lambda I) = \det \begin{pmatrix} -\lambda & 2 \\ 2 & -\lambda \end{pmatrix} = (-\lambda)(-\lambda) - 2^2 = \lambda^2 - 4 = \lambda^2 + 1$.
The eigenvalues are the roots of $\lambda^2 + 1 = 0$ in $\mathbb{F}_5$. $\lambda^2 = -1 \equiv 4$. The roots are $\lambda = \pm 2$. So, $\lambda_1 = 2, \lambda_2 = -2 \equiv 3$. The eigenvalues are $\{2, 3\}$. Both are in $\mathbb{F}_5$.
Are the eigenvalues squares? $\lambda_1 = 2$ is not a square in $\mathbb{F}_5$. $\lambda_2 = 3$ is not a square in $\mathbb{F}_5$.
So, not all eigenvalues are squares.
We have found a case where all LPMs are squares (0, 1), but not all eigenvalues are squares (2, 3).
Therefore, the implication (All $D_k$ are squares) $\implies$ (All $\lambda_i$ are squares) is **FALSE** for $p > 2$.

**Conclusion**

The statement "all eigenvalues of A are positive in $\mathbb{F}_p$ if and only if all its leading principal minors are positive in $\mathbb{F}_p$" (where positive means square) holds for $p=2$.
However, for any prime $p > 2$, the statement is **false**.
Both implications fail for $p>2$:
1.  Having all eigenvalues as squares does not guarantee all LPMs are squares.
2.  Having all LPMs as squares does not guarantee all eigenvalues are squares.

The analogy to Sylvester's criterion for real symmetric matrices does not hold in general for symmetric matrices over finite fields $\mathbb{F}_p$ when $p>2$, using the definition of "positive" as being a square.

Final Answer: The final answer is $\boxed{The statement is not true in general. It holds for p=2, but fails for p>2. Both implications fail for p>2.}$