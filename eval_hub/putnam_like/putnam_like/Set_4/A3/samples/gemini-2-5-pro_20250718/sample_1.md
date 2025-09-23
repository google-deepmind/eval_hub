Excellent question. This problem asks us to investigate whether Sylvester's criterion for positive-definite matrices, a cornerstone result for real symmetric matrices, has a direct analogue in the setting of finite fields $\mathbb{F}_p$.

Let's break down the problem and the proposed equivalence.

### Problem Definition

*   **Field:** $\mathbb{F}_p$, the finite field with $p$ elements, where $p$ is a prime number.
*   **Matrix:** $A \in \mathbb{M}_n(\mathbb{F}_p)$ is a symmetric matrix ($A^T = A$) with $n \geq 2$.
*   **Assumption:** All eigenvalues of $A$ are in the base field $\mathbb{F}_p$.
*   **Definition of "Positive":** An element $x \in \mathbb{F}_p$ is called "positive" if it is a quadratic residue modulo $p$ or it is 0. That is, there exists $y \in \mathbb{F}_p$ such that $x = y^2$.
*   **Leading Principal Minors (LPMs):** For $k=1, \dots, n$, let $A_k$ be the top-left $k \times k$ submatrix of $A$. The $k$-th LPM is $d_k = \det(A_k)$.
*   **The Question:** Is the following statement true?
    *(All eigenvalues of $A$ are positive in $\mathbb{F}_p$) $\iff$ (All leading principal minors of $A$ are positive in $\mathbb{F}_p$)*

To answer this, we must check both directions of the "if and only if" statement.

1.  **Forward Implication ($\Rightarrow$):** If all eigenvalues of $A$ are squares in $\mathbb{F}_p$, are all its leading principal minors necessarily squares in $\mathbb{F}_p$?
2.  **Backward Implication ($\Leftarrow$):** If all leading principal minors of $A$ are squares in $\mathbb{F}_p$, are all its eigenvalues necessarily squares in $\mathbb{F}_p$?

We will find that **neither implication holds**, and thus the overall statement is **false**. We will demonstrate this using counterexamples.

---

### Analysis of the Backward Implication ($\Leftarrow$)

**Statement:** If all leading principal minors of $A$ are squares in $\mathbb{F}_p$, then all eigenvalues of $A$ are squares in $\mathbb{F}_p$.

**Conclusion:** This statement is **FALSE**.

**Counterexample:**
Let's choose a small prime $p$ and dimension $n$. Let $n=2$ and $p=5$.
The elements of $\mathbb{F}_5$ are $\{0, 1, 2, 3, 4\}$.
The squares ("positive" elements) in $\mathbb{F}_5$ are:
$0^2 = 0$
$1^2 = 1$
$2^2 = 4$
$3^2 = 9 \equiv 4 \pmod 5$
$4^2 = 16 \equiv 1 \pmod 5$
So, the set of squares is $\{0, 1, 4\}$. The non-squares are $\{2, 3\}$.

We need to find a symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix} \in \mathbb{M}_2(\mathbb{F}_5)$ such that:
1.  Its leading principal minors, $d_1 = a$ and $d_2 = ac-b^2$, are squares (in $\{0, 1, 4\}$).
2.  At least one of its eigenvalues is a non-square (in $\{2, 3\}$).

Let's try to construct such a matrix.
Let's set the leading principal minors to be squares.
*   Choose $d_1 = a = 1$. This is a square ($1=1^2$).
*   Choose $d_2 = \det(A) = 4$. This is a square ($4=2^2$).

Our matrix is $A = \begin{pmatrix} 1 & b \\ b & c \end{pmatrix}$. We have $d_2 = c - b^2 = 4$, so $c = 4+b^2$.

Now, let's find the eigenvalues. The characteristic polynomial is $\det(A-\lambda I)=0$:
$\det \begin{pmatrix} 1-\lambda & b \\ b & c-\lambda \end{pmatrix} = (1-\lambda)(c-\lambda) - b^2 = 0$
$\lambda^2 - (1+c)\lambda + (c-b^2) = 0$
$\lambda^2 - (1+c)\lambda + 4 = 0$

We need to choose $b$ such that the roots of this polynomial are non-squares. Let's try a value for $b$, for instance $b=2$.
If $b=2$, then $c = 4 + 2^2 = 4+4 = 8 \equiv 3 \pmod 5$.
The matrix is $A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$.

Let's verify the properties of this matrix $A$:
1.  **Symmetry:** It is symmetric.
2.  **Leading Principal Minors:**
    *   $d_1 = a = 1$. This is a square in $\mathbb{F}_5$.
    *   $d_2 = \det(A) = (1)(3) - (2)(2) = 3 - 4 = -1 \equiv 4$. This is a square in $\mathbb{F}_5$.
    Both LPMs are positive (squares).

3.  **Eigenvalues:**
    The characteristic polynomial is $\lambda^2 - (1+c)\lambda + 4 = 0$.
    With $c=3$, the polynomial is $\lambda^2 - (1+3)\lambda + 4 = 0$, which is $\lambda^2 - 4\lambda + 4 = 0$.
    This factors as $(\lambda-2)^2 = 0$.
    The eigenvalues are $\lambda_1 = 2$ and $\lambda_2 = 2$.

The value $2$ is **not a square** in $\mathbb{F}_5$.
Therefore, we have found a matrix $A$ where all leading principal minors are squares, but its eigenvalues are not squares. This disproves the backward implication.

---

### Analysis of the Forward Implication ($\Rightarrow$)

**Statement:** If all eigenvalues of $A$ are squares in $\mathbb{F}_p$, then all its leading principal minors are squares in $\mathbb{F}_p$.

**Conclusion:** This statement is also **FALSE**.

**Reasoning and Counterexample:**
The proof of Sylvester's criterion in $\mathbb{R}$ relies on properties that do not hold over finite fields. Specifically, the Spectral Theorem, which guarantees that every real symmetric matrix is orthogonally diagonalizable, does not hold in general over $\mathbb{F}_p$. A symmetric matrix over $\mathbb{F}_p$ may not be diagonalizable at all, even if its eigenvalues lie in $\mathbb{F}_p$.

Let's use the same setting, $n=2$ and $p=5$.
We need to find a symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix} \in \mathbb{M}_2(\mathbb{F}_5)$ such that:
1.  Its eigenvalues $\lambda_1, \lambda_2$ are squares (in $\{0, 1, 4\}$).
2.  At least one of its leading principal minors is a non-square (in $\{2, 3\}$).

Let's try to construct such a matrix. We can force the first LPM to be a non-square.
*   Choose $d_1 = a = 2$. This is a non-square in $\mathbb{F}_5$.

Now we need to choose $b$ and $c$ so that the eigenvalues are squares.
Let's choose the eigenvalues to be $\lambda_1 = 1$ and $\lambda_2 = 1$. Both are squares.
The characteristic polynomial must be $(\lambda-1)^2 = \lambda^2 - 2\lambda + 1 = 0$.

The characteristic polynomial of $A = \begin{pmatrix} 2 & b \\ b & c \end{pmatrix}$ is:
$\lambda^2 - (2+c)\lambda + (2c-b^2) = 0$.

Comparing the coefficients with our target polynomial $\lambda^2 - 2\lambda + 1 = 0$:
*   $\text{trace}$: $2+c = 2 \implies c=0$.
*   $\det$: $2c-b^2 = 1$.

Substitute $c=0$ into the second equation:
$2(0) - b^2 = 1 \implies -b^2 = 1 \implies b^2 = -1 \equiv 4 \pmod 5$.
This gives $b=2$ or $b=3$. Let's choose $b=2$.

This gives the matrix $A = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}$.

Let's verify the properties of this matrix $A$:
1.  **Symmetry:** It is symmetric.
2.  **Eigenvalues:**
    By construction, the characteristic polynomial is $(\lambda-1)^2=0$. The eigenvalues are $\lambda_1=1, \lambda_2=1$.
    The value $1$ is a square in $\mathbb{F}_5$. So all eigenvalues are positive (squares).

3.  **Leading Principal Minors:**
    *   $d_1 = a = 2$.
    The value $2$ is **not a square** in $\mathbb{F}_5$.

We have found a matrix $A$ where all eigenvalues are squares, but its first leading principal minor is not a square. This disproves the forward implication.

(Note: For this matrix, $d_2 = \det(A) = 2(0)-2(2) = -4 \equiv 1$, which is a square. However, the condition "all LPMs are squares" already failed at $d_1$.)

---

### Final Conclusion

The statement "all eigenvalues of a symmetric matrix $A \in \mathbb{M}_n(\mathbb{F}_p)$ (with eigenvalues in $\mathbb{F}_p$) are positive in $\mathbb{F}_p$ if and only if all its leading principal minors are positive in $\mathbb{F}_p$" is **FALSE**.

Both directions of the implication fail:

1.  **(All LPMs are squares) $\implies$ (All eigenvalues are squares)** is **FALSE**.
    Counterexample for $p=5$: $A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$.
    LPMs are $d_1=1, d_2=4$ (both squares). Eigenvalues are $\lambda_{1,2}=2$ (non-squares).

2.  **(All eigenvalues are squares) $\implies$ (All LPMs are squares)** is **FALSE**.
    Counterexample for $p=5$: $A = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}$.
    Eigenvalues are $\lambda_{1,2}=1$ (both squares). LPMs are $d_1=2$ (non-square), $d_2=1$ (square).

The analogy to Sylvester's criterion for real matrices breaks down because the underlying structure of linear algebra over finite fields is fundamentally different. Key results from the real case, such as the spectral theorem for symmetric matrices and the geometric intuition of quadratic forms, do not have direct analogues that would be needed to prove the equivalence.