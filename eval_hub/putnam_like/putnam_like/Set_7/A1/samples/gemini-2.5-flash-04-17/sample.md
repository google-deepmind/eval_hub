Let $A \in \mathbb{M}_2 (\mathbb{C})$ satisfy $A^{k+1} = A^k$ for some integer $k \geq 3$.
We can rewrite the given condition as $A^{k+1} - A^k = 0$, which is $A^k(A - I) = 0$, where $I$ is the $2 \times 2$ identity matrix.

Let $m(x)$ be the minimal polynomial of the matrix $A$. The minimal polynomial is the monic polynomial of least degree such that $m(A) = 0$.
Since $A^k(A - I) = 0$, the polynomial $p(x) = x^k(x-1)$ annihilates $A$. This implies that the minimal polynomial $m(x)$ must divide $p(x)$.
$$ m(x) \mid x^k(x-1) $$
Since $A \in \mathbb{M}_2 (\mathbb{C})$, the degree of its minimal polynomial $m(x)$ is at most 2.
The roots of $m(x)$ must be a subset of the roots of $x^k(x-1)$, which are 0 and 1.
Therefore, the minimal polynomial $m(x)$ must be of the form $x^a (x-1)^b$ for some non-negative integers $a$ and $b$.

From $m(x) \mid x^k(x-1)$, we must have $a \le k$ and $b \le 1$.
From $\deg(m(x)) \le 2$, we must have $a+b \le 2$.
Also, since $A$ is a $2 \times 2$ matrix, its minimal polynomial has degree at least 1.

Let's list the possible forms for $m(x) = x^a (x-1)^b$ under these constraints, given $k \geq 3$.

Case 1: $b=0$. $m(x) = x^a$. We need $a \le k$ and $a \le 2$. Since $\deg(m(x)) \ge 1$, $a \ge 1$.
Given $k \geq 3$, $a \le k$ is satisfied for $a=1, 2$.
- If $a=1$, $m(x)=x$. This satisfies $1 \le 2$ and $1 \le k$. $m(x)=x$ implies $A=0$.
- If $a=2$, $m(x)=x^2$. This satisfies $2 \le 2$ and $2 \le k$ (since $k \ge 3$). $m(x)=x^2$ implies $A^2=0$.

Case 2: $b=1$. $m(x) = x^a(x-1)$. We need $a \le k$, $b=1 \le 1$, and $a+b = a+1 \le 2$, which means $a \le 1$.
Given $k \geq 3$, $a \le k$ is satisfied for $a=0, 1$.
- If $a=0$, $m(x)=x^0(x-1)=x-1$. This satisfies $0 \le 1$ and $0 \le k$. $m(x)=x-1$ implies $A-I=0$, so $A=I$.
- If $a=1$, $m(x)=x^1(x-1)=x(x-1)$. This satisfies $1 \le 1$ and $1 \le k$. $m(x)=x(x-1)$ implies $A(A-I)=0$, so $A^2-A=0 \implies A^2=A$.

The possible minimal polynomials for $A$ are $x$, $x^2$, $x-1$, and $x(x-1)$.
We need to show that $A^3=A^2$ for each of these cases.

1.  If $m(x)=x$: Then $A=0$. $A^2 = 0^2 = 0$ and $A^3 = 0^3 = 0$. Thus $A^3=A^2$.
2.  If $m(x)=x^2$: Then $A^2=0$. $A^3 = A \cdot A^2 = A \cdot 0 = 0$. Thus $A^3=A^2$.
3.  If $m(x)=x-1$: Then $A-I=0$, so $A=I$. $A^2 = I^2 = I$ and $A^3 = I^3 = I$. Thus $A^3=A^2$.
4.  If $m(x)=x(x-1)$: Then $A^2-A=0$, so $A^2=A$. $A^3 = A \cdot A^2 = A \cdot A = A^2$. Thus $A^3=A^2$.

In all possible cases for the minimal polynomial of $A$, the condition $A^3=A^2$ holds.

The final answer is $\boxed{A^3 = A^2}$.