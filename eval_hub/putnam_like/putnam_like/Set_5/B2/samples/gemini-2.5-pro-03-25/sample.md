Solution:
Let $A$ and $B$ be $n \times n$ invertible matrices such that $A+B=I$ and $A^4+B^4=I$, where $I$ is the $n \times n$ identity matrix. We want to compute $\det(AB)$.

From the condition $A+B=I$, we can express $B$ as $B = I-A$.
Substitute this expression for $B$ into the second condition $A^4+B^4=I$:
$A^4 + (I-A)^4 = I$.

Expand $(I-A)^4$ using the binomial theorem for matrices (since $I$ and $-A$ commute):
$(I-A)^4 = \binom{4}{0}I^4 - \binom{4}{1}I^3A + \binom{4}{2}I^2A^2 - \binom{4}{3}IA^3 + \binom{4}{4}(-A)^4$
$(I-A)^4 = I - 4A + 6A^2 - 4A^3 + A^4$.

Substitute this expansion back into the equation $A^4 + (I-A)^4 = I$:
$A^4 + (I - 4A + 6A^2 - 4A^3 + A^4) = I$.
$2A^4 - 4A^3 + 6A^2 - 4A + I = I$.
Subtract $I$ from both sides:
$2A^4 - 4A^3 + 6A^2 - 4A = 0$.
Divide by 2 (assuming the characteristic of the underlying field is not 2, which is standard for such problems unless specified otherwise):
$A^4 - 2A^3 + 3A^2 - 2A = 0$.

Factor out $A$ from the left side:
$A(A^3 - 2A^2 + 3A - 2I) = 0$.
Since $A$ is given to be invertible, $\det(A) \neq 0$, and $A^{-1}$ exists. Multiply the equation by $A^{-1}$ on the left:
$A^{-1}A(A^3 - 2A^2 + 3A - 2I) = A^{-1}0$.
$I(A^3 - 2A^2 + 3A - 2I) = 0$.
$A^3 - 2A^2 + 3A - 2I = 0$.

Let $p(x) = x^3 - 2x^2 + 3x - 2$. We have shown that $p(A)=0$. This means that the minimal polynomial of $A$ must divide $p(x)$. The eigenvalues of $A$ must be roots of $p(x)$.
Let's find the roots of $p(x)$. We test for integer roots that divide $-2$.
$p(1) = 1^3 - 2(1)^2 + 3(1) - 2 = 1 - 2 + 3 - 2 = 0$.
So $x=1$ is a root, and $(x-1)$ is a factor of $p(x)$.
Perform polynomial division:
$(x^3 - 2x^2 + 3x - 2) \div (x-1) = x^2 - x + 2$.
So $p(x) = (x-1)(x^2 - x + 2)$.
The roots of $x^2 - x + 2 = 0$ are given by the quadratic formula:
$x = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(2)}}{2(1)} = \frac{1 \pm \sqrt{1 - 8}}{2} = \frac{1 \pm \sqrt{-7}}{2}$.
Let $\omega = \frac{1+i\sqrt{7}}{2}$ and $\bar{\omega} = \frac{1-i\sqrt{7}}{2}$. The roots of $p(x)$ are $1, \omega, \bar{\omega}$.
The eigenvalues of $A$, denoted by $\lambda$, must be among these roots.

We are given that $B$ is invertible. Since $B=I-A$, the eigenvalues of $B$ are $1-\lambda$, where $\lambda$ is an eigenvalue of $A$.
The determinant of $B$ is the product of its eigenvalues: $\det(B) = \prod (1-\lambda_i)$.
Since $B$ is invertible, $\det(B) \neq 0$. This implies that none of the eigenvalues of $B$ can be zero.
So $1-\lambda_i \neq 0$ for all eigenvalues $\lambda_i$ of $A$.
This means $\lambda_i \neq 1$ for all eigenvalues of $A$.

Therefore, the eigenvalues of $A$ must be chosen from the roots of $p(x)$ excluding $1$. The possible eigenvalues of $A$ are $\omega$ and $\bar{\omega}$.
Both $\omega$ and $\bar{\omega}$ are roots of $x^2 - x + 2 = 0$.
So for any eigenvalue $\lambda$ of $A$, we must have $\lambda^2 - \lambda + 2 = 0$.

We need to compute $\det(AB)$. Since $A$ and $B$ commute ($AB = A(I-A) = A-A^2$ and $BA = (I-A)A = A-A^2$), we have $AB = A-A^2$.
Let $f(x) = x-x^2$. Then $AB = f(A)$.
The eigenvalues of $f(A)$ are $f(\lambda)$, where $\lambda$ are the eigenvalues of $A$.
The eigenvalues of $AB = A-A^2$ are $\lambda - \lambda^2$.
From the equation $\lambda^2 - \lambda + 2 = 0$, we can rearrange it to $\lambda - \lambda^2 = 2$.
So, every eigenvalue of $AB$ is equal to 2.

The determinant of a matrix is the product of its eigenvalues, counted with their algebraic multiplicities. Let $\mu_1, \dots, \mu_n$ be the eigenvalues of $AB$. We have shown that $\mu_i = 2$ for all $i=1, \dots, n$.
Therefore, $\det(AB) = \prod_{i=1}^n \mu_i = \prod_{i=1}^n 2 = 2^n$.

Final check: The steps rely on standard matrix properties and eigenvalue theory. The invertibility conditions on $A$ and $B$ are crucial for restricting the possible eigenvalues. The derivation holds over complex numbers and can be adapted for real matrices (where $n$ must be even) or fields of characteristic $p \neq 2$. Assuming the standard context of complex matrices, the result is $2^n$.

Final Answer: The final answer is $\boxed{2^n}$