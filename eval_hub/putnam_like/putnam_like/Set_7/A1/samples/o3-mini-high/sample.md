```markdown
We are given that
\[
A^{k+1} = A^k \quad \text{for some integer } k \ge 3
\]
with \( A \in \mathbb{M}_2(\mathbb{C}) \). Our goal is to prove that
\[
A^3 = A^2.
\]

### Step 1. Eigenvalue Analysis

Let \(\lambda\) be an eigenvalue of \(A\) with corresponding eigenvector \(v \neq 0\). Then
\[
A^{k+1} v = A^k v.
\]
Since \(A v = \lambda v\), it follows that
\[
A^m v = \lambda^m v \quad \text{for any positive integer } m.
\]
Thus, applying this to our equation:
\[
\lambda^{k+1} v = \lambda^k v.
\]
Since \(v \neq 0\), we must have
\[
\lambda^{k+1} = \lambda^k.
\]
This can be rewritten as
\[
\lambda^k (\lambda - 1) = 0.
\]
Thus, for each eigenvalue \(\lambda\) of \(A\), either
\[
\lambda^k = 0 \quad \text{or} \quad \lambda - 1 = 0.
\]
In other words, the only possible eigenvalues are
\[
\lambda = 0 \quad \text{or} \quad \lambda = 1.
\]

### Step 2. Minimal Polynomial Considerations

Since \(A \in \mathbb{M}_2(\mathbb{C})\), its minimal polynomial has degree at most 2 and must divide
\[
x^k (x-1).
\]
Therefore, the minimal polynomial of \(A\) can only be one of the following:
- \(m_A(x) = x\),
- \(m_A(x) = x - 1\),
- \(m_A(x) = x(x-1)\),
- or a repeated linear factor such as \(x^2\) or \((x-1)^2\).

Let us consider these possibilities:

1. **Case \(m_A(x) = x\):**  
   Then \(A = 0\), and clearly
   \[
   A^3 = 0 = A^2.
   \]

2. **Case \(m_A(x) = x-1\):**  
   Then \(A = I\) (the identity matrix), and again
   \[
   A^3 = I = A^2.
   \]

3. **Case \(m_A(x) = x(x-1)\):**  
   In this case, \(A\) has eigenvalues 0 and 1 and is diagonalizable. A diagonalizable matrix with these eigenvalues is a projection, so
   \[
   A^2 = A.
   \]
   Hence
   \[
   A^3 = A^2 A = A A = A^2.
   \]

4. **Case \(m_A(x) = (x-1)^2\):**  
   Here, \(A\) has a single eigenvalue \(1\) with a Jordan block of size 2. Write
   \[
   A = I + N,
   \]
   where \(N\) is nilpotent and \(N^2 = 0\). Then
   \[
   A^m = (I+N)^m = I + mN \quad \text{for any } m \ge 1.
   \]
   In particular,
   \[
   A^k = I + kN \quad \text{and} \quad A^{k+1} = I + (k+1)N.
   \]
   In order for \(A^{k+1} = A^k\) to hold, we must have
   \[
   I + (k+1)N = I + kN,
   \]
   which implies
   \[
   N = 0.
   \]
   Thus, \(A = I\) and we are reduced to the previous case.

5. **Case \(m_A(x) = x^2\):**  
   Here, \(A\) is nilpotent, so 
   \[
   A^2 = 0,
   \]
   and consequently,
   \[
   A^3 = A \cdot A^2 = A \cdot 0 = 0 = A^2.
   \]

### Step 3. Conclusion

In all cases, we have shown that
\[
A^3 = A^2.
\]

Thus, if \(A \in \mathbb{M}_2(\mathbb{C})\) satisfies
\[
A^{k+1} = A^k \quad \text{for some } k \ge 3,
\]
then it necessarily follows that
\[
A^3 = A^2.
\]
```