Solution:
Let $A$ and $B$ be two square invertible matrices of size $m = 2n+1$, where $n\geq 1$. We assume that $A$ and $B$ are real matrices, i.e., $A, B \in M_{m}(\mathbb{R})$. The size $m$ is an odd integer $m \geq 3$. Since $A$ and $B$ are invertible, their determinants are non-zero: $\det(A) \neq 0$ and $\det(B) \neq 0$.

We want to determine if there exist real numbers $a$ and $b$ such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.

Let $P(a,b) = \det(aA+bB)$. The entries of the matrix $aA+bB$ are linear combinations of $a$ and $b$ with real coefficients (since $A, B$ are real matrices). The determinant of a matrix is a polynomial in its entries. Therefore, $P(a,b)$ is a polynomial in the variables $a$ and $b$ with real coefficients.

Let $C = aA+bB$. An entry of $C$ is $C_{ij} = a A_{ij} + b B_{ij}$.
$P(a,b) = \det(C) = \sum_{\sigma \in S_m} \text{sgn}(\sigma) \prod_{i=1}^m C_{i, \sigma(i)} = \sum_{\sigma \in S_m} \text{sgn}(\sigma) \prod_{i=1}^m (a A_{i, \sigma(i)} + b B_{i, \sigma(i)})$.
Each term $\prod_{i=1}^m (a A_{i, \sigma(i)} + b B_{i, \sigma(i)})$ is a homogeneous polynomial of degree $m$. Thus, $P(a,b)$ is a homogeneous polynomial of degree $m = 2n+1$ in $a$ and $b$.

Let's consider the function $p(x) = P(x, 1) = \det(xA+B)$.
$p(x)$ is a polynomial in $x$. Let's determine its degree.
$p(x) = \det(xA+B)$. As a homogeneous polynomial, $P(a,b) = \sum_{k=0}^m c_k a^k b^{m-k}$.
Then $p(x) = P(x,1) = \sum_{k=0}^m c_k x^k$.
The coefficient $c_m$ is obtained by setting $b=0$ in $P(a,b)$ and looking at the coefficient of $a^m$. $P(a,0) = \det(aA) = a^m \det(A)$. So $c_m = \det(A)$.
The coefficient $c_0$ is obtained by setting $a=0$ in $P(a,b)$ and looking at the coefficient of $b^m$. $P(0,b) = \det(bB) = b^m \det(B)$. So $c_0 = \det(B)$.
Thus, $p(x) = \det(A) x^m + c_{m-1} x^{m-1} + \dots + c_1 x + \det(B)$.
Since $A$ is invertible, $\det(A) \neq 0$. Therefore, the degree of the polynomial $p(x)$ is $m = 2n+1$.
Since $A$ and $B$ are real matrices, the coefficients $c_k$ are real numbers. So $p(x)$ is a polynomial with real coefficients.
The degree of $p(x)$ is $m = 2n+1$, which is an odd number ($n \geq 1$, so $m \geq 3$).
A fundamental property of polynomials with real coefficients is that if the degree is odd, the polynomial must have at least one real root. This property follows from the Intermediate Value Theorem, as $p(x)$ tends to opposite infinities as $x \to \infty$ and $x \to -\infty$.
Let $x_0 \in \mathbb{R}$ be a real root of $p(x)$. Then $p(x_0)=0$.
$p(x_0) = \det(x_0 A + 1 B) = \det(x_0 A + B) = 0$.
We need to find $a, b \in \mathbb{R}$ such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.
Choose $a=x_0$ and $b=1$.
Then $a,b$ are real numbers.
We must check that $a^2+b^2 \neq 0$. $a^2+b^2 = x_0^2 + 1^2 = x_0^2+1$. Since $x_0$ is real, $x_0^2 \geq 0$, so $x_0^2+1 \geq 1$. Thus $a^2+b^2 \neq 0$.
With this choice, $\det(aA+bB) = \det(x_0 A + 1 B) = p(x_0) = 0$.
So we have found such real numbers $a$ and $b$.

Alternatively, consider the function $f: \mathbb{R} \to \mathbb{R}$ defined by $f(\theta) = \det(\cos \theta A + \sin \theta B)$. Since the determinant is a continuous function of the matrix entries, and $\cos \theta, \sin \theta$ are continuous functions, $f(\theta)$ is a continuous function.
Let's evaluate $f(\theta+\pi)$:
$f(\theta+\pi) = \det(\cos(\theta+\pi) A + \sin(\theta+\pi) B) = \det(-\cos \theta A - \sin \theta B)$
$f(\theta+\pi) = \det(- (\cos \theta A + \sin \theta B)) = (-1)^m \det(\cos \theta A + \sin \theta B)$
Since $m=2n+1$ is odd, $(-1)^m = -1$.
So $f(\theta+\pi) = -f(\theta)$.
In particular, for $\theta=0$, we have $f(\pi) = -f(0)$.
$f(0) = \det(\cos 0 A + \sin 0 B) = \det(1 A + 0 B) = \det(A)$.
Since $A$ is invertible, $\det(A) \neq 0$. Thus $f(0) \neq 0$.
Then $f(\pi) = -\det(A) \neq 0$.
We have $f(0)$ and $f(\pi)$ are non-zero real numbers with opposite signs.
Since $f(\theta)$ is a continuous function on the interval $[0, \pi]$, by the Intermediate Value Theorem, there must exist a $\theta_0 \in (0, \pi)$ such that $f(\theta_0)=0$.
Let $a = \cos \theta_0$ and $b = \sin \theta_0$. These are real numbers.
We check the condition $a^2+b^2 \neq 0$. $a^2+b^2 = \cos^2 \theta_0 + \sin^2 \theta_0 = 1$. This is clearly non-zero.
Then, $\det(aA+bB) = \det(\cos \theta_0 A + \sin \theta_0 B) = f(\theta_0) = 0$.
Thus, we have found real numbers $a$ and $b$ such that $a^2+b^2 \neq 0$ and $\det(aA+bB)=0$.

Conclusion: Yes, such real numbers $a$ and $b$ exist. The condition that the matrix size $m=2n+1$ is odd is crucial for both proofs.

Final Answer: The final answer is $\boxed{Yes}$