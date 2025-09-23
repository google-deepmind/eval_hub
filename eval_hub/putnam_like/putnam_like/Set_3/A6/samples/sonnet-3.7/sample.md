# Solution

I need to find the even integers $n$ for which there exists an $n \times n$ matrix $A$ with entries in $\{0,1\}$ such that $A^2 = J_n$.

## Understanding $J_n$

First, I'll analyze the structure of $J_n$:
- $J_n$ is an $n \times n$ matrix with ones in odd columns and zeros in even columns
- For example, $J_4 = \begin{pmatrix} 1&0&1&0 \\ 1&0&1&0 \\ 1&0&1&0 \\ 1&0&1&0 \end{pmatrix}$

## Spectral Analysis

If $A^2 = J_n$, I can determine constraints by examining eigenvalues.

1. Note that $J_n$ can be expressed as $J_n = \mathbf{1}_n \mathbf{e}_n^T$, where:
   - $\mathbf{1}_n$ is the $n \times 1$ column vector of all ones
   - $\mathbf{e}_n^T$ is the $1 \times n$ row vector $[1, 0, 1, 0, \ldots]$ (alternating 1,0)

2. Let's compute $J_n^2$:
   $J_n^2 = (\mathbf{1}_n \mathbf{e}_n^T)(\mathbf{1}_n \mathbf{e}_n^T) = \mathbf{1}_n (\mathbf{e}_n^T \mathbf{1}_n) \mathbf{e}_n^T$
   
   Since $\mathbf{e}_n^T \mathbf{1}_n = \frac{n}{2}$ (the sum of the entries in $\mathbf{e}_n^T$), we have:
   $J_n^2 = \frac{n}{2} \cdot J_n$

3. From this, the eigenvalues of $J_n$ must be 0 (with multiplicity $n-1$) and $\frac{n}{2}$ (with multiplicity 1).

4. If $A^2 = J_n$, then the eigenvalues of $A$ must be:
   - 0 (with multiplicity $n-2$)
   - $\sqrt{\frac{n}{2}}$ (with multiplicity 1)
   - $-\sqrt{\frac{n}{2}}$ (with multiplicity 1)

## The Key Constraint

For a matrix with entries in $\{0,1\}$ to have eigenvalues 0, $\sqrt{\frac{n}{2}}$, and $-\sqrt{\frac{n}{2}}$, there's a key constraint:

The characteristic polynomial must have integer coefficients, which means:
1. The trace of $A$ must be 0 (sum of eigenvalues is 0)
2. The product of non-zero eigenvalues, $\sqrt{\frac{n}{2}} \cdot (-\sqrt{\frac{n}{2}}) = -\frac{n}{2}$, must be an integer.

The first constraint is automatically satisfied. For the second constraint, $\frac{n}{2}$ must be a perfect square for the matrix to exist.

Therefore, $n = 2m^2$ for some positive integer $m$.

## Verification

For $n = 2$ (i.e., $m = 1$), we can directly verify that $A = \begin{pmatrix} 1&0 \\ 1&0 \end{pmatrix}$ works, as $A^2 = A = J_2$.

For $n = 8$ (i.e., $m = 2$), we can construct an $8 \times 8$ matrix with eigenvalues 0 (multiplicity 6), 2, and -2.

## Conclusion

The even integers $n$ for which there exists an $n \times n$ matrix $A$ with entries in $\{0,1\}$ such that $A^2 = J_n$ are those of the form $n = 2m^2$ where $m$ is a positive integer.

Therefore, the answer is: $n = 2, 8, 18, 32, 50, 72, ...$