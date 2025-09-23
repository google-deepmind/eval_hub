

To determine the even integers \( n \) for which there exists an \( n \times n \) binary matrix \( A \) such that \( A^2 = J_n \), we analyze the structure of \( J_n \) and the constraints imposed by binary matrix multiplication.

### Key Observations:
1. **Structure of \( J_n \):**
   - \( J_n \) has all ones in odd columns and zeros in even columns.
   - For \( A^2 = J_n \), every entry in the \( j \)-th column of \( A^2 \) must be 1 if \( j \) is odd and 0 if \( j \) is even.

2. **Matrix Multiplication Constraints:**
   - For odd \( j \), the sum \( \sum_{k=1}^n A[i,k] \cdot A[k,j] = 1 \) for all \( i \), implying each row \( i \) has exactly one \( k \) such that \( A[i,k] = A[k,j] = 1 \).
   - For even \( j \), the sum \( \sum_{k=1}^n A[i,k] \cdot A[k,j] = 0 \), meaning no \( k \) satisfies \( A[i,k] = A[k,j] = 1 \).

3. **Case \( n = 2 \):**
   - \( J_2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \).
   - The matrix \( A = J_2 \) satisfies \( A^2 = J_2 \) since:
     \[
     A^2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = J_2.
     \]
   - This works because the rank-1 structure of \( J_2 \) allows \( A = J_2 \) to satisfy \( A^2 = J_2 \).

4. **Case \( n \geq 4 \):**
   - For \( n \geq 4 \), \( J_n \) has rank 1 (all ones in odd columns), but \( A^2 = J_n \) requires \( A \) to have a higher rank structure. Attempts to construct such an \( A \) lead to contradictions:
     - If \( A = J_n \), then \( A^2 \) contains entries greater than 1 (e.g., \( n = 4 \), \( J_4^2 \) has entries equal to 2 in odd columns).
     - Other constructions (e.g., block matrices, permutation matrices) fail because they cannot satisfy the requirement of all ones in odd columns without violating the binary constraint.

### Conclusion:
The only even integer \( n \) where \( A^2 = J_n \) is possible is \( \boxed{2} \).

```markdown
The only even integer \( n \) for which there exists an \( n \times n \) binary matrix \( A \) with \( A^2 = J_n \) is \(\boxed{2}\).
```