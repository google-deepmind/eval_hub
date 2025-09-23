Solution:

Let $M$ be a $3 \times 3$ matrix. We are given that $1$ is an eigenvalue of $M$ with algebraic multiplicity $3$.
The characteristic polynomial of $M$ is $p(\lambda) = \det(M - \lambda I)$. Since $M$ is a $3 \times 3$ matrix, $p(\lambda)$ is a polynomial of degree $3$.
The fact that $\lambda=1$ is an eigenvalue with algebraic multiplicity $3$ means that $p(\lambda)$ must be of the form $c(\lambda - 1)^3$. The leading term of $p(\lambda)$ is $(-1)^3 \lambda^3 = -\lambda^3$. So $c=-1$.
The characteristic polynomial of $M$ is $p(\lambda) = -(\lambda - 1)^3 = (1 - \lambda)^3$.

By the Cayley-Hamilton theorem, a matrix satisfies its own characteristic polynomial. Thus, $p(M) = O$, where $O$ is the $3 \times 3$ zero matrix.
$(I - M)^3 = O$.
Expanding this equation, we get:
$I^3 - \binom{3}{1} I^2 M + \binom{3}{2} I M^2 - \binom{3}{3} M^3 = O$
$I - 3M + 3M^2 - M^3 = O$
$M^3 = 3M^2 - 3M + I$.

We are asked to find coefficients $a_m, b_m, c_m$ such that for any natural number $m \geq 3$,
\begin{equation*}
M^m = a_m M^2 + b_m M + c_m I
\end{equation*}
where $I$ is the identity matrix $I_3$.

We can use the property that $M^m$ can be expressed in terms of $I, M, M^2$ using the remainder of the polynomial division of $x^m$ by the annihilating polynomial $(x-1)^3$.
Let $P(x) = x^m$ and $Q(x) = (x-1)^3$. By the polynomial division algorithm, there exist polynomials $q(x)$ and $r(x)$ such that $P(x) = q(x)Q(x) + r(x)$, where the degree of $r(x)$ is strictly less than the degree of $Q(x)$, which is $3$.
So, $\deg(r(x)) \leq 2$. Let $r(x) = \alpha x^2 + \beta x + \gamma$.
Substituting $x=M$ into the polynomial equation, we get:
$M^m = q(M)(M-I)^3 + r(M)$.
Since $(M-I)^3 = O$, we have $M^m = r(M)$.
$M^m = \alpha M^2 + \beta M + \gamma I$.
Thus, we need to find the coefficients $\alpha, \beta, \gamma$. These are the coefficients $a_m, b_m, c_m$.

The equation $x^m = q(x)(x-1)^3 + r(x)$ implies that $x^m$ and $r(x)$ must have the same value and derivatives at the root $x=1$, up to the order of multiplicity minus 1. Since the root $x=1$ has multiplicity $3$, we must match the function value and the first two derivatives.
Let $f(x) = x^m$ and $r(x) = a_m x^2 + b_m x + c_m$.
We evaluate the function and its first two derivatives at $x=1$:
$f(x) = x^m \implies f(1) = 1^m = 1$.
$f'(x) = mx^{m-1} \implies f'(1) = m(1)^{m-1} = m$. (Requires $m \ge 1$)
$f''(x) = m(m-1)x^{m-2} \implies f''(1) = m(m-1)(1)^{m-2} = m(m-1)$. (Requires $m \ge 2$)

Now we evaluate $r(x)$ and its derivatives at $x=1$:
$r(x) = a_m x^2 + b_m x + c_m \implies r(1) = a_m + b_m + c_m$.
$r'(x) = 2a_m x + b_m \implies r'(1) = 2a_m + b_m$.
$r''(x) = 2a_m \implies r''(1) = 2a_m$.

Equating the values and derivatives of $f(x)$ and $r(x)$ at $x=1$:
1. $r(1) = f(1) \implies a_m + b_m + c_m = 1$.
2. $r'(1) = f'(1) \implies 2a_m + b_m = m$.
3. $r''(1) = f''(1) \implies 2a_m = m(m-1)$.

We can solve this system of linear equations for $a_m, b_m, c_m$.
From equation (3):
$a_m = \frac{m(m-1)}{2}$.
Substitute $a_m$ into equation (2):
$2 \left( \frac{m(m-1)}{2} \right) + b_m = m$
$m(m-1) + b_m = m$
$b_m = m - m(m-1) = m(1 - (m-1)) = m(1 - m + 1) = m(2-m)$.
$b_m = -m(m-2)$.
Substitute $a_m$ and $b_m$ into equation (1):
$\frac{m(m-1)}{2} - m(m-2) + c_m = 1$
$c_m = 1 - \frac{m(m-1)}{2} + m(m-2)$
$c_m = \frac{2 - (m^2-m) + 2(m^2-2m)}{2}$
$c_m = \frac{2 - m^2 + m + 2m^2 - 4m}{2}$
$c_m = \frac{m^2 - 3m + 2}{2}$
$c_m = \frac{(m-1)(m-2)}{2}$.

The derivation requires $m \ge 2$ for the second derivative $f''(x)$ to be defined this way. However, the resulting formulas are also valid for $m=0, 1, 2$. The problem states $m \geq 3$.

The coefficients are:
$a_m = \frac{m(m-1)}{2}$
$b_m = -m(m-2)$
$c_m = \frac{(m-1)(m-2)}{2}$

These coefficients can also be expressed using binomial coefficients:
$a_m = \binom{m}{2}$
$b_m = -m(m-2)$
$c_m = \binom{m-1}{2}$

These coefficients satisfy the equation $M^m = a_m M^2 + b_m M + c_m I$ for all $m \geq 3$.

Final Answer: The final answer is $\boxed{a_m = \frac{m(m-1)}{2}, b_m = -m(m-2), c_m = \frac{(m-1)(m-2)}{2}}$