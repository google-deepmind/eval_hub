Of course. Here is a detailed, step-by-step solution to the problem.

### Statement of the Problem

Let $A$ and $B$ be two square invertible matrices of size $m \times m$, where $m = 2n+1$ for $n\geq 1$. We want to determine if there exist real numbers $a$ and $b$, not both zero (i.e., $a^2+b^2\neq 0$), such that the matrix $aA+bB$ is singular, which means $\det(aA+bB)=0$.

### Step 1: Reformulating the Determinant Condition

Our goal is to find non-trivial real numbers $a, b$ that satisfy the equation:
$$ \det(aA+bB) = 0 $$
Since matrix $A$ is invertible, its determinant $\det(A)$ is non-zero, and its inverse $A^{-1}$ exists. We can factor out $A$ from the expression $aA+bB$:
$$ aA+bB = A(aI + bA^{-1}B) $$
Here, $I$ is the identity matrix of size $m \times m$.

Using the property that $\det(XY) = \det(X)\det(Y)$ for square matrices $X$ and $Y$, we have:
$$ \det(aA+bB) = \det(A(aI + bA^{-1}B)) = \det(A)\det(aI + bA^{-1}B) $$
Since $A$ is invertible, we know $\det(A) \neq 0$. Therefore, the condition $\det(aA+bB)=0$ is equivalent to:
$$ \det(aI + bA^{-1}B) = 0 $$
Let's define a new matrix $C = A^{-1}B$. Since $A$ and $B$ are real matrices of size $m \times m$, $A^{-1}$ is also a real matrix, and thus $C$ is a real matrix of size $m \times m$. The problem now is to find real numbers $a$ and $b$ (not both zero) such that:
$$ \det(aI + bC) = 0 $$

### Step 2: Analyzing the Equation in Terms of $a$ and $b$

We need to solve $\det(aI + bC) = 0$ for $a, b \in \mathbb{R}$ where $a^2+b^2 \neq 0$. Let's consider two cases.

**Case 1: $b=0$**
If $b=0$, the condition $a^2+b^2 \neq 0$ implies $a \neq 0$. The equation becomes:
$$ \det(aI + 0 \cdot C) = \det(aI) = a^m \det(I) = a^m $$
For this to be zero, we must have $a^m = 0$, which implies $a=0$. This contradicts our assumption that $a \neq 0$. So, there is no solution with $b=0$.

**Case 2: $b \neq 0$**
Since $b \neq 0$, we can manipulate the expression inside the determinant:
$$ aI + bC = b \left( \frac{a}{b}I + C \right) $$
Using the property $\det(kX) = k^m \det(X)$ for a scalar $k$ and an $m \times m$ matrix $X$:
$$ \det(aI + bC) = \det\left(b \left( \frac{a}{b}I + C \right)\right) = b^m \det\left(\frac{a}{b}I + C\right) $$
Since $b \neq 0$, the equation $\det(aI+bC)=0$ is equivalent to:
$$ \det\left(\frac{a}{b}I + C\right) = 0 $$
Let's define a new variable $\lambda = -a/b$. This is a real number since $a$ and $b$ are real. The equation can be rewritten as:
$$ \det(C - \lambda I) = 0 $$

### Step 3: Connecting the Problem to Eigenvalues

The equation $\det(C - \lambda I) = 0$ is the characteristic equation for the matrix $C$. The solutions $\lambda$ to this equation are the eigenvalues of $C$.

So, the original problem is equivalent to the following question:
**"Does the matrix $C = A^{-1}B$ necessarily have at least one real eigenvalue?"**

If we can show that $C$ always has a real eigenvalue, let's call it $\lambda_0$, then we can find the required $a$ and $b$.

### Step 4: Proving the Existence of a Real Eigenvalue

Let's analyze the characteristic polynomial of $C$, which is $p(\lambda) = \det(C - \lambda I)$.

1.  **Nature of the polynomial:** The matrix $C=A^{-1}B$ is a product of real matrices, so its entries are real numbers. The characteristic polynomial $p(\lambda)$ of a real matrix is a polynomial with real coefficients.

2.  **Degree of the polynomial:** The degree of the characteristic polynomial of an $m \times m$ matrix is $m$. In our problem, the matrices are of size $m = 2n+1$. Since $n \geq 1$, $m$ is an odd integer ($m \geq 3$).

So, $p(\lambda)$ is a polynomial with real coefficients and of odd degree $m = 2n+1$.

A fundamental theorem in algebra states that any polynomial with real coefficients and of odd degree must have at least one real root. We can prove this using a simple calculus argument:

Let $p(\lambda) = c_m \lambda^m + c_{m-1} \lambda^{m-1} + \dots + c_1 \lambda + c_0$, where $c_i \in \mathbb{R}$ and $c_m \neq 0$. Since $m$ is odd:
*   As $\lambda \to \infty$, the term $c_m \lambda^m$ dominates. The sign of $p(\lambda)$ will be the sign of $c_m$.
*   As $\lambda \to -\infty$, the term $c_m \lambda^m$ also dominates. Since $m$ is odd, $\lambda^m$ will be negative. The sign of $p(\lambda)$ will be the opposite of the sign of $c_m$.

For example, if $c_m > 0$:
$$ \lim_{\lambda \to \infty} p(\lambda) = \infty $$
$$ \lim_{\lambda \to -\infty} p(\lambda) = -\infty $$
Since $p(\lambda)$ is a polynomial, it is a continuous function. By the Intermediate Value Theorem, since $p(\lambda)$ takes on both positive and negative values, it must cross the $\lambda$-axis at least once. That is, there must exist at least one real number $\lambda_0$ such that $p(\lambda_0) = 0$.

This real root $\lambda_0$ is a real eigenvalue of the matrix $C$.

### Step 5: Constructing the Solution for $a$ and $b$

We have established that the matrix $C=A^{-1}B$ has at least one real eigenvalue, $\lambda_0$. We need to find $a, b \in \mathbb{R}$ with $a^2+b^2 \neq 0$ such that $\lambda_0 = -a/b$.

We can choose a value for $b$ and then solve for $a$. Since we established that $b$ cannot be zero, let's make a simple choice:
*   Let $b = 1$.

Now, we solve for $a$:
$$ \lambda_0 = -a/1 \implies a = -\lambda_0 $$

So we have found a candidate pair $(a,b) = (-\lambda_0, 1)$. Let's verify that this pair satisfies all the required conditions.

1.  **Are $a$ and $b$ real?**
    Yes. We chose $b=1$, which is real. We proved the existence of a real eigenvalue $\lambda_0$, so $a = -\lambda_0$ is also real.

2.  **Is $a^2+b^2 \neq 0$?**
    Let's compute $a^2+b^2$:
    $$ a^2+b^2 = (-\lambda_0)^2 + 1^2 = \lambda_0^2 + 1 $$
    Since $\lambda_0$ is a real number, $\lambda_0^2 \geq 0$. Therefore, $\lambda_0^2+1 \geq 1$.
    This means $a^2+b^2 \neq 0$ is always satisfied.

3.  **Is $\det(aA+bB)=0$?**
    With our choice of $a = -\lambda_0$ and $b=1$, we have:
    $$ \det(aA+bB) = \det(-\lambda_0 A + 1 \cdot B) $$
    Following the logic from Step 1:
    $$ \det(-\lambda_0 A + B) = \det(A) \det(-\lambda_0 I + A^{-1}B) = \det(A) \det(C - \lambda_0 I) $$
    Since $\lambda_0$ is an eigenvalue of $C$, by definition $\det(C - \lambda_0 I) = 0$.
    Therefore:
    $$ \det(aA+bB) = \det(A) \cdot 0 = 0 $$
    The condition is satisfied.

### Conclusion

Yes, for any two invertible square matrices $A$ and $B$ of odd size $2n+1$ ($n \geq 1$), there always exist real numbers $a$ and $b$ such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.

The crucial properties used in this proof are:
- The invertibility of $A$, which allows the problem to be reformulated in terms of an eigenvalue problem.
- The odd dimension of the matrices, which guarantees that the characteristic polynomial has an odd degree.
- The property that any real polynomial of odd degree must have at least one real root.