```markdown
## Solution

Let \(A\in M_2(\mathbb{C})\) satisfy
\[
A^{k+1} \;=\; A^k
\qquad(k\ge3).
\]
We shall prove that
\[
A^3 \;=\; A^2.
\]

### Method 1: Minimal polynomial

1.  The given relation can be rewritten as
    \[
    A^{k+1} - A^k \;=\; 0
    \quad\Longrightarrow\quad
    A^k\,(A - I) \;=\; 0.
    \]
    Hence the polynomial
    \[
    p(x) \;=\; x^k\,(x - 1)
    \]
    annihilates \(A\), i.e.\ \(p(A)=0\).

2.  The minimal polynomial \(m_A(x)\) of \(A\) divides \(p(x)\).  But
    \(\deg m_A\le2\), so the only possible monic divisors of
    \(x^k(x-1)\) of degree \(\le2\) are
    \[
      x,\quad x-1,\quad x(x-1).
    \]
    In each case \(m_A(x)\) has no repeated roots, hence \(A\) is
    diagonalizable with spectrum contained in \(\{0,1\}\).

3.  A diagonalizable matrix whose eigenvalues lie in \(\{0,1\}\)
    satisfies
    \[
    A^2 \;=\; A.
    \]
    Consequently
    \[
    A^3 \;=\; A\cdot A^2 \;=\; A\cdot A \;=\; A^2,
    \]
    as required.

---

### Method 2: Jordan normal form

Since \(A\) is a \(2\times2\) complex matrix, up to similarity it splits
into at most two Jordan blocks.  Let \(J\) be any Jordan block of size
\(\le2\) with eigenvalue \(\lambda\).  Then
\[
J = \lambda I + N,
\]
where \(N\) is nilpotent of index \(\le2\).  One computes
\[
J^m \;=\;\lambda^m I \;+\; m\,\lambda^{m-1} N.
\]
Thus
\[
J^{k+1} - J^k
= \lambda^k\bigl((\lambda-1)I + N\bigr).
\]
Imposing \(J^{k+1}=J^k\) gives
\[
\lambda^k\bigl((\lambda-1)I + N\bigr)=0.
\]
- If \(\lambda=0\), then \(J^k=0\) for \(k\ge2\), hence \(J^2=0\) and
  \(J^3=0\), so \(J^3=J^2\).
- If \(\lambda\ne0\), then \((\lambda-1)I+N=0\).  Taking traces shows
  \(\lambda=1\) and \(N=0\), so \(J=I\) and again \(J^3=J^2\).

In every case each Jordan block of \(A\) satisfies \(J^3=J^2\).  Therefore
\(A^3=A^2\).

\(\boxed{A^3 = A^2.}\)