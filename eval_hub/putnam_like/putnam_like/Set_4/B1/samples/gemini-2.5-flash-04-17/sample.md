Solution:
Let $P_1(x) = ax+b$ with $a,b \in \mathbb{R}, a \neq 0$.
Let $P_2(x) = cx^2+dx+e$ with $c,d,e \in \mathbb{R}, c \neq 0$.
We are given that $P_2(k) \neq 0$ for all $k \in \mathbb{Z}$.

Part (a): Does there exist a polynomial $P$ of real coefficients such that $k^2 P\left( \frac{1}{k} \right) = P_2(k)$ for all $k \in \mathbb{Z}$?
The expression $\frac{1}{k}$ is undefined for $k=0$. So the condition must hold for all $k \in \mathbb{Z} \setminus \{0\}$.
Let $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ be a polynomial with real coefficients $a_i \in \mathbb{R}$.
For $k \in \mathbb{Z} \setminus \{0\}$, we have
$k^2 P\left( \frac{1}{k} \right) = k^2 \left( a_n \left(\frac{1}{k}\right)^n + a_{n-1} \left(\frac{1}{k}\right)^{n-1} + \dots + a_1 \left(\frac{1}{k}\right) + a_0 \right)$
$= k^2 \left( \frac{a_n}{k^n} + \frac{a_{n-1}}{k^{n-1}} + \dots + \frac{a_1}{k} + a_0 \right)$
$= \frac{a_n}{k^{n-2}} + \frac{a_{n-1}}{k^{n-3}} + \dots + a_1 k + a_0 k^2$.
Rearranging in powers of $k$:
$a_0 k^2 + a_1 k + a_2 + a_3 k^{-1} + \dots + a_n k^{2-n}$.

This expression must be equal to $P_2(k) = c k^2 + d k + e$ for all $k \in \mathbb{Z} \setminus \{0\}$.
$a_0 k^2 + a_1 k + a_2 + a_3 k^{-1} + \dots + a_n k^{2-n} = c k^2 + d k + e$ for all $k \in \mathbb{Z} \setminus \{0\}$.
For the left side to be a polynomial in $k$, all terms with negative powers of $k$ must vanish. The powers with negative exponents are $k^{-1}, k^{-2}, \dots, k^{2-n}$ (if $n>2$).
For this equality to hold for infinitely many values of $k$, both sides must be equal as functions of $k$. For the left side to be a polynomial, we must have $a_j = 0$ for all $j$ such that $2-j < 0$, i.e., for $j > 2$.
So, $a_3=0, a_4=0, \dots, a_n=0$.
This implies that $P(x)$ must be of degree at most 2. Let $P(x) = a_2 x^2 + a_1 x + a_0$.
Then $k^2 P(1/k) = k^2 (a_2/k^2 + a_1/k + a_0) = a_2 + a_1 k + a_0 k^2$.
So we must have $a_0 k^2 + a_1 k + a_2 = c k^2 + d k + e$ for all $k \in \mathbb{Z} \setminus \{0\}$.
Since this equality holds for infinitely many values of $k$, the two polynomials must be identical. Comparing coefficients:
$a_0 = c$
$a_1 = d$
$a_2 = e$
Thus, the polynomial $P(x)$ must be $P(x) = e x^2 + d x + c$.
Let's check if this polynomial satisfies the condition. $P(x)$ has real coefficients $e,d,c$.
For $k \in \mathbb{Z} \setminus \{0\}$,
$k^2 P(1/k) = k^2 (e(1/k)^2 + d(1/k) + c) = k^2 (e/k^2 + d/k + c) = e + dk + ck^2 = ck^2 + dk + e = P_2(k)$.
This holds for all $k \in \mathbb{Z} \setminus \{0\}$.
Such a polynomial exists.

Part (a) Answer: Yes.

Part (b): Does there exist a polynomial $Q$ of real coefficients such that $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z}$?
This condition must hold for $k \in \mathbb{Z}$ where both sides are defined. $1/k$ is defined for $k \neq 0$. $P_2(k)$ is in the denominator, and $P_2(k) \neq 0$ for all $k \in \mathbb{Z}$. So the condition holds for all $k \in \mathbb{Z} \setminus \{0\}$.
Let $y = 1/k$. As $k$ ranges over $\mathbb{Z} \setminus \{0\}$, $y$ ranges over the set $\{1, -1, 1/2, -1/2, 1/3, -1/3, \dots\}$. This set is infinite and has an accumulation point at $y=0$.
The given condition can be rewritten in terms of $y$. Since $k=1/y$:
$y Q(y) = \frac{P_1(1/y)}{P_2(1/y)}$ for $y \in \{1/k : k \in \mathbb{Z} \setminus \{0\}\}$.
$y Q(y) = \frac{a(1/y)+b}{c(1/y)^2+d(1/y)+e} = \frac{(a+by)/y}{(c+dy+ey^2)/y^2} = \frac{y(a+by)}{c+dy+ey^2}$.
For $y \neq 0$, we can divide by $y$:
$Q(y) = \frac{a+by}{c+dy+ey^2}$ for all $y \in \{1/k : k \in \mathbb{Z} \setminus \{0\}\}$.

Let $R(y) = \frac{a+by}{ey^2+dy+c}$. $Q(y)$ must be equal to the rational function $R(y)$ for all $y$ in the set $\{1/k : k \in \mathbb{Z} \setminus \{0\}\}$.
If a polynomial $Q(y)$ equals a rational function $R(y)$ on an infinite set with an accumulation point, then $Q(y)$ must be equal to $R(y)$ for all values of $y$ where $R(y)$ is defined.
$R(y) = \frac{a+by}{ey^2+dy+c}$.
The denominator is $D(y) = ey^2+dy+c$. The numerator is $N(y) = a+by$.
$P_2(x)=cx^2+dx+e$. The condition $P_2(k) \neq 0$ for all $k \in \mathbb{Z}$ implies $P_2(0)=e \neq 0$.
Thus, the degree of the denominator $D(y) = ey^2+dy+c$ as a polynomial in $y$ is 2 (since $e \neq 0$).
The numerator $N(y) = a+by$ has degree 1 (since $a \neq 0$).
For a rational function $\frac{N(y)}{D(y)}$ to be a polynomial, $D(y)$ must divide $N(y)$.
A polynomial of degree 2 ($D(y)$) can divide a polynomial of degree 1 ($N(y)$) only if $N(y)$ is the zero polynomial.
$N(y) = a+by = 0$ for all $y$. This would require $a=0$ and $b=0$.
But $P_1(x)=ax+b$ is a polynomial of degree 1, so $a \neq 0$.
Thus, $N(y)$ is not the zero polynomial.
Therefore, the rational function $R(y) = \frac{a+by}{ey^2+dy+c}$ is not a polynomial.

Since $Q(y)$ must be equal to $R(y)$ on an infinite set with an accumulation point, $Q(y)$ must be identical to $R(y)$. But $R(y)$ is not a polynomial. This is a contradiction.
Therefore, no such polynomial $Q(x)$ exists.

Part (b) Answer: No.

The final answer is $\boxed{a) Yes, b) No}$.