# Solution

I'll solve this problem by analyzing what $A^{k+1} = A^k$ tells us about the structure of the matrix $A$.

## Step 1: Rewrite the condition in terms of the minimal polynomial

From $A^{k+1} = A^k$, we can rewrite this as:
$$A^k(A-I) = 0$$

This means that the minimal polynomial of $A$ must divide $x^k(x-1)$.

## Step 2: Analyze the minimal polynomial of $A$

Since $A \in \mathbb{M}_2 (\mathbb{C})$, the minimal polynomial of $A$ has degree at most 2. Therefore, the minimal polynomial must be one of:
1. $x$
2. $(x-1)$
3. $x^2$
4. $(x-1)^2$
5. $x(x-1)$

Let's examine each case.

## Step 3: Check each possible minimal polynomial

**Case 1:** If the minimal polynomial is $x$, then $A = 0$. Thus, $A^2 = A^3 = 0$, so $A^3 = A^2$.

**Case 2:** If the minimal polynomial is $(x-1)$, then $A = I$. Thus, $A^2 = A^3 = I$, so $A^3 = A^2$.

**Case 3:** If the minimal polynomial is $x^2$, then $A^2 = 0$. Thus, $A^3 = A \cdot A^2 = A \cdot 0 = 0$, so $A^3 = A^2$.

**Case 4:** If the minimal polynomial is $(x-1)^2$, then $A$ is similar to the Jordan block $J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

For this Jordan block, we can compute $J^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ for all $n \geq 1$. Therefore, $J^{k+1} \neq J^k$ for any $k \geq 1$ because the entries differ. This means $A^{k+1} \neq A^k$, contradicting our given condition.

**Case 5:** If the minimal polynomial is $x(x-1)$, then $A$ is diagonalizable with eigenvalues 0 and 1. Thus, $A$ is similar to the diagonal matrix $D = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.

For this matrix, $D^2 = D$ and $D^3 = D$, so $D^3 = D^2$. Since $A$ is similar to $D$, we have $A^3 = A^2$.

## Conclusion

After analyzing all possible cases, we find that if the minimal polynomial is $(x-1)^2$, then $A^{k+1} \neq A^k$ for any $k$, contradicting our given condition. For all other cases of the minimal polynomial, we have $A^3 = A^2$.

Therefore, any matrix $A \in \mathbb{M}_2 (\mathbb{C})$ that satisfies $A^{k+1} = A^k$ for some $k \geq 3$ must also satisfy $A^3 = A^2$.