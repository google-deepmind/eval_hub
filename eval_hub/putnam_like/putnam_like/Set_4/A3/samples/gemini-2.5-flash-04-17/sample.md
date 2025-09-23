Let the statement be $S$: "all eigenvalues of $A$ are positive in $\mathbb{F}_p$ if and only if all its leading principal minors are positive in $\mathbb{F}_p$".
Let $P$ be the proposition "all eigenvalues of $A$ are positive in $\mathbb{F}_p$" and $Q$ be the proposition "all leading principal minors of $A$ are positive in $\mathbb{F}_p$". The statement $S$ is $P \iff Q$.
We are asked if $S$ is true. If not, which implication ($P \implies Q$ or $Q \implies P$) doesn't hold?

First, let's understand the term "positive" in $\mathbb{F}_p$. An element $x \in \mathbb{F}_p$ is positive if $x = y^2$ for some $y \in \mathbb{F}_p$. The set of positive elements is the set of quadratic residues in $\mathbb{F}_p$, including 0.

Case 1: $p = 2$.
$\mathbb{F}_2 = \{0, 1\}$. The squares are $0^2=0$ and $1^2=1$. Thus, every element in $\mathbb{F}_2$ is a square.
In this case, an element $x \in \mathbb{F}_2$ is positive if and only if $x \in \{0, 1\}$. This is always true for any element in $\mathbb{F}_2$.
The proposition $P$ "all eigenvalues of $A$ are positive in $\mathbb{F}_2$" means "all eigenvalues of $A$ are in $\mathbb{F}_2$".
The proposition $Q$ "all leading principal minors of $A$ are positive in $\mathbb{F}_2$" means "all leading principal minors of $A$ are in $\mathbb{F}_2$".
The problem statement assumes that $A \in \mathbb{M}_n(\mathbb{F}_p)$ is symmetric and all its eigenvalues are in $\mathbb{F}_p$. For $p=2$, this assumption means "A is symmetric and all its eigenvalues are in $\mathbb{F}_2$". So $P$ is true by assumption.
A leading principal minor of $A$ is the determinant of a submatrix of $A$. Since $A \in \mathbb{M}_n(\mathbb{F}_2)$, the entries of the submatrix are in $\mathbb{F}_2$, and thus its determinant is also in $\mathbb{F}_2$. So $Q$ is always true for any $A \in \mathbb{M}_n(\mathbb{F}_2)$.
Under the problem's assumption for $p=2$, $P$ is true and $Q$ is true. Thus, $P \iff Q$ is true for $p=2$.

Case 2: $p > 2$.
The set of squares in $\mathbb{F}_p$ is a proper subset of $\mathbb{F}_p$ (it has $(p-1)/2 + 1$ elements). There exist non-square elements.

Let's check Implication 1 ($P \implies Q$): If all eigenvalues of $A$ are positive, then all leading principal minors are positive.
Let $n=2$ and $p=5$. The squares in $\mathbb{F}_5$ are $\{0, 1, 4\}$. The non-squares are $\{2, 3\}$.
Consider the matrix $A = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix} \in \mathbb{M}_2(\mathbb{F}_5)$. $A$ is symmetric.
The eigenvalues of $A$ are the roots of the characteristic polynomial $\det(A - \lambda I) = \det \begin{pmatrix} 2-\lambda & 2 \\ 2 & -\lambda \end{pmatrix} = (2-\lambda)(-\lambda) - 2^2 = -2\lambda + \lambda^2 - 4 = \lambda^2 - 2\lambda - 4$.
In $\mathbb{F}_5$, this is $\lambda^2 - 2\lambda + 1 = (\lambda-1)^2$.
The eigenvalues are $\lambda_1 = 1$ and $\lambda_2 = 1$. Both $1$ and $1$ are squares in $\mathbb{F}_5$ ($1=1^2$), so both eigenvalues are positive in $\mathbb{F}_5$. This matrix satisfies the assumption that its eigenvalues are in $\mathbb{F}_5$ and are positive.
The leading principal minors are:
$\det(A_1) = \det(2) = 2$. $2$ is not a square in $\mathbb{F}_5$, so $2$ is not positive in $\mathbb{F}_5$.
$\det(A_2) = \det(A) = 1$. $1$ is a square in $\mathbb{F}_5$, so $1$ is positive in $\mathbb{F}_5$.
Not all leading principal minors are positive.
Thus, for $p=5$, we have a symmetric matrix $A$ whose eigenvalues are all positive, but not all leading principal minors are positive. This is a counterexample to Implication 1 ($P \implies Q$). This matrix $A$ works as a counterexample for any prime $p>2$ where $2$ is a non-square (i.e., $p \equiv 3, 5 \pmod 8$) and $1$ is a square. We can construct similar counterexamples for any $p>2$.

Let's check Implication 2 ($Q \implies P$): If all leading principal minors of $A$ are positive, then all its eigenvalues are positive.
Let $n=2$ and $p=5$.
Consider the matrix $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \in \mathbb{M}_2(\mathbb{F}_5)$. $A$ is symmetric.
The leading principal minors are:
$\det(A_1) = \det(1) = 1$. $1$ is a square in $\mathbb{F}_5$, so $1$ is positive.
$\det(A_2) = \det(A) = 1 \times 1 - 1 \times 1 = 0$. $0$ is a square in $\mathbb{F}_5$ ($0=0^2$), so $0$ is positive.
All leading principal minors are positive in $\mathbb{F}_5$.
The eigenvalues of $A$ are the roots of $\det(A - \lambda I) = \det \begin{pmatrix} 1-\lambda & 1 \\ 1 & 1-\lambda \end{pmatrix} = (1-\lambda)^2 - 1^2 = (1-\lambda-1)(1-\lambda+1) = (-\lambda)(2-\lambda) = \lambda(\lambda-2)$.
The eigenvalues are $\lambda_1 = 0$ and $\lambda_2 = 2$. $0$ is a square ($0^2$), so $0$ is positive. $2$ is not a square in $\mathbb{F}_5$, so $2$ is not positive.
The eigenvalues $0, 2$ are in $\mathbb{F}_5$, so this matrix satisfies the problem's assumption.
Not all eigenvalues are positive.
Thus, for $p=5$, we have a symmetric matrix $A$ whose leading principal minors are all positive, but not all eigenvalues are positive. This is a counterexample to Implication 2 ($Q \implies P$). This matrix $A$ works as a counterexample for any prime $p>2$ where $2$ is a non-square. We can construct similar counterexamples for any $p>2$ (as shown in thought process for $p=17$).

Conclusion:
The statement is true for $p=2$.
The statement is false for $p>2$. Since the question asks "Is that true that...", and it's not true for all $p \ge 2$, the answer is No.
For $p>2$, both implications ($P \implies Q$ and $Q \implies P$) fail, as demonstrated by the counterexamples for $p=5$.

The final answer is $\boxed{No}$.