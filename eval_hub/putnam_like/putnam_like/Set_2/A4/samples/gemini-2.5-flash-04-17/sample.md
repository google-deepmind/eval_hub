Let $M$ be a square matrix of dimension 3. We are given that 1 is an eigenvalue of $M$ with algebraic multiplicity 3. This means the characteristic polynomial of $M$ is $p(\lambda) = \det(M - \lambda I) = (1-\lambda)^3 = -(\lambda-1)^3$.
By the Cayley-Hamilton theorem, $M$ satisfies its characteristic equation: $(M-I)^3 = 0$.

We are asked to find coefficients $a_m, b_m, c_m$ for any natural number $m \geq 3$ such that $M^m = a_m M^2 + b_m M + c_m I_3$.

Let $f(\lambda) = \lambda^m$. We are looking for coefficients $a_m, b_m, c_m$ such that $M^m = a_m M^2 + b_m M + c_m I$.
This is equivalent to finding a polynomial $r(\lambda) = a_m \lambda^2 + b_m \lambda + c_m$ of degree at most 2 such that $M^m = r(M)$.
By the theory of matrix functions, $M^m = r(M)$ if and only if $r(\lambda)$ is the remainder of the polynomial division of $\lambda^m$ by the minimal polynomial of $M$, $m_M(\lambda)$.
The minimal polynomial $m_M(\lambda)$ divides the characteristic polynomial $(\lambda-1)^3$. Thus, $m_M(\lambda)$ must be $(\lambda-1)$, $(\lambda-1)^2$, or $(\lambda-1)^3$.

The coefficients $a_m, b_m, c_m$ must be independent of the specific matrix $M$, as long as it satisfies the given condition (characteristic polynomial is $(\lambda-1)^3$). This means the relation $M^m = a_m M^2 + b_m M + c_m I$ must hold for any matrix $M$ with characteristic polynomial $(\lambda-1)^3$.
This implies that the polynomial $g(\lambda) = \lambda^m - (a_m \lambda^2 + b_m \lambda + c_m)$ must be divisible by the minimal polynomial $m_M(\lambda)$ for any such $M$. For the coefficients to be universally applicable to any $M$ with this characteristic polynomial, $g(\lambda)$ must be divisible by the "worst-case" minimal polynomial, which is $(\lambda-1)^3$. If $g(\lambda)$ is divisible by $(\lambda-1)^3$, it is also divisible by $(\lambda-1)^2$ and $(\lambda-1)$, covering all possible minimal polynomials.

For $g(\lambda)$ to be divisible by $(\lambda-1)^3$, $\lambda=1$ must be a root of $g(\lambda)$ with multiplicity at least 3. This means $g(1)=0$, $g'(1)=0$, and $g''(1)=0$.

Let $g(\lambda) = \lambda^m - a_m \lambda^2 - b_m \lambda - c_m$.

1. $g(1)=0$:
$1^m - a_m(1)^2 - b_m(1) - c_m = 0$
$1 - a_m - b_m - c_m = 0 \implies a_m + b_m + c_m = 1$.

2. $g'(\lambda) = m\lambda^{m-1} - 2a_m \lambda - b_m$.
$g'(1)=0$:
$m(1)^{m-1} - 2a_m(1) - b_m = 0$
$m - 2a_m - b_m = 0 \implies 2a_m + b_m = m$. This holds for $m \geq 1$.

3. $g''(\lambda) = m(m-1)\lambda^{m-2} - 2a_m$.
$g''(1)=0$:
$m(m-1)(1)^{m-2} - 2a_m = 0$
$m(m-1) - 2a_m = 0 \implies 2a_m = m(m-1)$. This holds for $m \geq 2$.

We have a system of linear equations for $a_m, b_m, c_m$:
(1) $a_m + b_m + c_m = 1$
(2) $2a_m + b_m = m$
(3) $2a_m = m(m-1)$

From equation (3), we find $a_m$:
$a_m = \frac{m(m-1)}{2}$.

Substitute $a_m$ into equation (2):
$2 \left(\frac{m(m-1)}{2}\right) + b_m = m$
$m(m-1) + b_m = m$
$m^2 - m + b_m = m$
$b_m = m - m^2 + m = 2m - m^2 = m(2-m)$.

Substitute $a_m$ and $b_m$ into equation (1):
$\frac{m(m-1)}{2} + m(2-m) + c_m = 1$
$\frac{m^2-m}{2} + \frac{2m(2-m)}{2} + c_m = 1$
$\frac{m^2-m + 4m-2m^2}{2} + c_m = 1$
$\frac{-m^2+3m}{2} + c_m = 1$
$c_m = 1 - \frac{-m^2+3m}{2} = \frac{2 - (-m^2+3m)}{2} = \frac{2 + m^2 - 3m}{2} = \frac{m^2 - 3m + 2}{2} = \frac{(m-1)(m-2)}{2}$.

These formulas for $a_m, b_m, c_m$ were derived using conditions that require $m \geq 2$ for $g''(1)$ to provide a constraint on $a_m$. For $m \geq 3$, all three equations provide valid constraints, yielding the unique solution for $a_m, b_m, c_m$. The question asks for $m \geq 3$, so these formulas are applicable.

The coefficients are:
$a_m = \frac{m(m-1)}{2}$
$b_m = m(2-m)$
$c_m = \frac{(m-1)(m-2)}{2}$

These formulas hold for $m \geq 3$.

The final answer is $\boxed{a_m = \frac{m(m-1)}{2}, b_m = m(2-m), c_m = \frac{(m-1)(m-2)}{2}}$.