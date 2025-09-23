```markdown
# Problem Solution

Let $A$ and $B$ be $n\times n$ invertible matrices such that $A+B=I$ and $A^4+B^4=I$, where $I$ is the identity matrix. We want to compute $\det(AB)$.

From the condition $A+B=I$, we can write $B = I-A$.
Substitute this into the second condition:
$A^4 + (I-A)^4 = I$.

We expand $(I-A)^4$ using the binomial theorem. Since $I$ and $A$ commute ($IA=AI=A$), the binomial expansion is valid:
$(I-A)^4 = \binom{4}{0}I^4(-A)^0 + \binom{4}{1}I^3(-A)^1 + \binom{4}{2}I^2(-A)^2 + \binom{4}{3}I^1(-A)^3 + \binom{4}{4}I^0(-A)^4$
$(I-A)^4 = I - 4A + 6A^2 - 4A^3 + A^4$.

Substitute this back into the equation $A^4+(I-A)^4=I$:
$A^4 + (I - 4A + 6A^2 - 4A^3 + A^4) = I$
$2A^4 - 4A^3 + 6A^2 - 4A + I = I$
$2A^4 - 4A^3 + 6A^2 - 4A = 0$.

Since $A$ is invertible, we can multiply this equation by $A^{-1}$.
$A(2A^3 - 4A^2 + 6A - 4I) = 0$.
Multiplying by $A^{-1}$ on the left gives:
$A^{-1}A(2A^3 - 4A^2 + 6A - 4I) = A^{-1}0$
$I(2A^3 - 4A^2 + 6A - 4I) = 0$
$2A^3 - 4A^2 + 6A - 4I = 0$.
Divide by 2:
$A^3 - 2A^2 + 3A - 2I = 0$.

Let $P(x) = x^3 - 2x^2 + 3x - 2$. The matrix $A$ satisfies the polynomial equation $P(A)=0$. The eigenvalues of $A$ must be roots of the polynomial $P(x)$.
We find the roots of $P(x)$. We can test for integer roots that are divisors of -2: $\pm 1, \pm 2$.
$P(1) = 1^3 - 2(1)^2 + 3(1) - 2 = 1 - 2 + 3 - 2 = 0$. So $x=1$ is a root.
We divide $P(x)$ by $(x-1)$:
$(x^3 - 2x^2 + 3x - 2) \div (x-1) = x^2 - x + 2$.
So $P(x) = (x-1)(x^2 - x + 2)$.
The roots of $x^2 - x + 2 = 0$ are given by the quadratic formula:
$x = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(2)}}{2(1)} = \frac{1 \pm \sqrt{1 - 8}}{2} = \frac{1 \pm \sqrt{-7}}{2} = \frac{1 \pm i\sqrt{7}}{2}$.
Let $\alpha = \frac{1+i\sqrt{7}}{2}$ and $\beta = \frac{1-i\sqrt{7}}{2}$.
The roots of $P(x)$ are $1, \alpha, \beta$.
So, the eigenvalues of $A$ must belong to the set $\{1, \alpha, \beta\}$.

Since $A$ is invertible, its determinant is non-zero. The determinant is the product of the eigenvalues, so none of the eigenvalues of $A$ can be zero. $1, \alpha, \beta$ are all non-zero.

The matrix $B=I-A$ is also invertible, so its determinant is non-zero. The eigenvalues of $B$ are $1-\lambda$, where $\lambda$ are the eigenvalues of $A$.
If $\lambda$ is an eigenvalue of $A$, then $1-\lambda$ must be a non-zero eigenvalue of $B$.
$1-\lambda \neq 0 \implies \lambda \neq 1$.
Thus, $1$ cannot be an eigenvalue of $A$.
The eigenvalues of $A$ must therefore belong to the set $\{\alpha, \beta\}$.

Let $\lambda_1, \dots, \lambda_n$ be the eigenvalues of $A$, repeated according to their algebraic multiplicity. Each $\lambda_j$ is either $\alpha$ or $\beta$.

We want to compute $\det(AB)$. Since $B=I-A$, $AB = A(I-A) = A-A^2$.
The eigenvalues of $AB = A-A^2$ are $\lambda_j - \lambda_j^2$, where $\lambda_j$ are the eigenvalues of $A$.
Since $\lambda_j \in \{\alpha, \beta\}$, $\lambda_j$ satisfies the quadratic equation $x^2-x+2=0$.
So, $\lambda_j^2 - \lambda_j + 2 = 0$ for each eigenvalue $\lambda_j$ of $A$.
This implies $\lambda_j - \lambda_j^2 = 2$ for each eigenvalue $\lambda_j$ of $A$.
Thus, all eigenvalues of $AB$ are equal to 2.

The determinant of a matrix is the product of its eigenvalues. Let $\mu_1, \dots, \mu_n$ be the eigenvalues of $AB$. We have $\mu_j = 2$ for all $j=1, \dots, n$.
$\det(AB) = \prod_{j=1}^n \mu_j = \prod_{j=1}^n 2 = 2^n$.

The final answer is $\boxed{2^n}$.