

The problem asks whether the equivalence between all eigenvalues being positive (squares in $\mathbb{F}_p$) and all leading principal minors being positive (squares in $\mathbb{F}_p$) holds for a symmetric matrix $A \in \mathbb{M}_n(\mathbb{F}_p)$ with eigenvalues in $\mathbb{F}_p$. 

### Key Steps and Analysis:

1. **Definitions and Real Case Analogy**:
   - In $\mathbb{F}_p$, an element is positive if it is a square (including 0).
   - Sylvester's criterion in the real case states that a symmetric matrix is positive definite (all eigenvalues positive) if and only if all leading principal minors are positive.

2. **Examples in $\mathbb{F}_p$**:
   - **Counterexample for Forward Direction**: Consider a symmetric matrix in $\mathbb{F}_7$ with eigenvalues 1 and 4 (both squares) but leading principal minor 3 (non-square). This shows eigenvalues being squares do not imply leading minors are squares.
   - **Counterexample for Converse Direction**: Consider a diagonal matrix in $\mathbb{F}_7$ with leading minors 0 (squares) but one eigenvalue 3 (non-square). This shows leading minors being squares do not imply eigenvalues are squares.

3. **Detailed Analysis**:
   - **Forward Direction**: A matrix with eigenvalues as squares does not guarantee leading principal minors are squares. Example: Matrix $\begin{pmatrix} 3 & 3 \\ 3 & 2 \end{pmatrix}$ in $\mathbb{F}_7$ has eigenvalues 1 and 4 (squares) but the first leading minor is 3 (non-square).
   - **Converse Direction**: A matrix with leading minors as squares does not guarantee eigenvalues are squares. Example: Diagonal matrix $\begin{pmatrix} 0 & 0 \\ 0 & 3 \end{pmatrix}$ in $\mathbb{F}_7$ has leading minors 0 (squares) but eigenvalues 0 and 3 (non-square).

4. **Conclusion**:
   - Both implications fail. There exist matrices where eigenvalues are squares but leading minors are not, and vice versa.

### Final Answer
\boxed{\text{No, neither implication holds.}}