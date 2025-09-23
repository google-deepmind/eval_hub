Solution:
Let $P_1(x) = ax+b$ with $a, b \in \mathbb{R}$ and $a \neq 0$.
Let $P_2(x) = cx^2+dx+e$ with $c, d, e \in \mathbb{R}$ and $c \neq 0$.
We are given that $0 \not\in P_2(\mathbb{Z})$, which means $P_2(k) \neq 0$ for all integers $k$. In particular, $P_2(0) = e \neq 0$.

Part (a):
We are looking for a polynomial $P(x)$ with real coefficients such that $k^2 P\left( \frac{1}{k} \right) = P_2(k)$ for all $k \in \mathbb{Z}$.
Let $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ be a polynomial of degree $n$.
Let $f(k) = k^2 P\left( \frac{1}{k} \right)$. For $k \neq 0$, we have
$$ f(k) = k^2 \sum_{i=0}^n a_i \left(\frac{1}{k}\right)^i = k^2 \left( a_n \frac{1}{k^n} + \dots + a_1 \frac{1}{k} + a_0 \right) = \sum_{i=0}^n a_i k^{2-i} $$
$$ f(k) = a_0 k^2 + a_1 k + a_2 + a_3 k^{-1} + \dots + a_n k^{2-n} $$
The condition is that $f(k) = P_2(k)$ for all $k \in \mathbb{Z}$. This requires that the expression $f(k)$ is defined for all $k \in \mathbb{Z}$, including $k=0$.
The terms $a_i k^{2-i}$ involve negative powers of $k$ if $2-i < 0$, i.e., $i > 2$.
For $f(k)$ to be defined at $k=0$, we must have $a_i = 0$ for all $i > 2$.
Thus, $P(x)$ must be a polynomial of degree at most 2. Let $P(x) = a_2 x^2 + a_1 x + a_0$.
Then $f(k) = a_0 k^2 + a_1 k + a_2$.
The condition becomes $a_0 k^2 + a_1 k + a_2 = P_2(k)$ for all $k \in \mathbb{Z}$.
Since $P_2(k) = ck^2+dk+e$, we must have
$$ a_0 k^2 + a_1 k + a_2 = ck^2 + dk + e $$
for all $k \in \mathbb{Z}$.
Let $R(k) = (a_0 - c) k^2 + (a_1 - d) k + (a_2 - e)$. We require $R(k) = 0$ for all $k \in \mathbb{Z}$.
A non-zero polynomial can only have a finite number of roots. Since $R(k)=0$ for infinitely many values of $k$, $R(k)$ must be the zero polynomial.
This means its coefficients must all be zero:
$a_0 - c = 0 \implies a_0 = c$
$a_1 - d = 0 \implies a_1 = d$
$a_2 - e = 0 \implies a_2 = e$
Thus, the polynomial $P(x)$ must be $P(x) = e x^2 + d x + c$.
Since $P_2(x)$ has real coefficients $c, d, e$, $P(x)$ has real coefficients.
Since $P_2(x)$ has degree 2, $c \neq 0$. Therefore, $P(x)$ has degree 2.
Such a polynomial $P(x)$ exists.

We verify the solution. Let $P(x) = ex^2+dx+c$.
For $k \neq 0$, $k^2 P(1/k) = k^2 (e(1/k)^2 + d(1/k) + c) = k^2(e/k^2 + d/k + c) = e + dk + ck^2$.
Let $E(k) = ck^2+dk+e$. Then $E(k) = P_2(k)$ for all $k$.
The expression $k^2 P(1/k)$ is equal to the polynomial $E(k)$ for $k \neq 0$.
Interpreting the condition $k^2 P(1/k) = P_2(k)$ for all $k \in \mathbb{Z}$ to mean that the function $k \mapsto k^2 P(1/k)$ defined for $k \neq 0$ extends to a function defined for all $k \in \mathbb{Z}$ which equals $P_2(k)$, the polynomial $P(x) = ex^2+dx+c$ is the solution.

Answer to (a): Yes, such a polynomial exists. It is $P(x) = ex^2+dx+c$.

Part (b):
We are looking for a polynomial $Q(x)$ with real coefficients such that $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z}$.
Let $Q(x) = b_m x^m + \dots + b_1 x + b_0$ be a polynomial of degree $m$. Assume $Q(x)$ is not the zero polynomial, so $b_m \neq 0$.
Let $g(k) = \frac{1}{k} Q \left( \frac{1}{k} \right)$. For $k \neq 0$, we have
$$ g(k) = \frac{1}{k} \sum_{i=0}^m b_i \left(\frac{1}{k}\right)^i = \sum_{i=0}^m b_i k^{-i-1} = b_0 k^{-1} + b_1 k^{-2} + \dots + b_m k^{-m-1} $$
Let $h(k) = \frac{P_1(k)}{P_2(k)} = \frac{ak+b}{ck^2+dk+e}$.
The condition is $g(k) = h(k)$ for all $k \in \mathbb{Z}$.
This requires that both $g(k)$ and $h(k)$ are defined for all $k \in \mathbb{Z}$.
The function $h(k)$ is defined for all $k \in \mathbb{Z}$ because $P_2(k) \neq 0$ for all $k \in \mathbb{Z}$. In particular, $h(0) = P_1(0)/P_2(0) = b/e$. Since $P_2(0)=e$, we know $e \neq 0$.
The function $g(k)$ can be written as:
$$ g(k) = \frac{b_0 k^m + b_1 k^{m-1} + \dots + b_m}{k^{m+1}} $$
This expression involves division by $k^{m+1}$. For $g(k)$ to be defined at $k=0$, the pole at $k=0$ must be removable. This means the numerator polynomial $N(k) = b_0 k^m + b_1 k^{m-1} + \dots + b_m$ must be divisible by $k^{m+1}$.
If $Q(x)$ is not the zero polynomial, then $N(k)$ is a polynomial of degree at most $m$. A non-zero polynomial of degree $\le m$ cannot be divisible by $k^{m+1}$ (since $m+1 > m$).
Therefore, the only possibility for $N(k)$ to be divisible by $k^{m+1}$ is if $N(k)$ is the zero polynomial.
$N(k)=0$ implies $b_0 = b_1 = \dots = b_m = 0$.
This means $Q(x)$ must be the zero polynomial.
If $Q(x)=0$, then $g(k)=0$ for all $k \neq 0$.
The condition $g(k)=h(k)$ for all $k \in \mathbb{Z}$ implies that $h(k)=0$ for all $k \in \mathbb{Z}$.
$h(k) = \frac{P_1(k)}{P_2(k)} = 0$ for all $k \in \mathbb{Z}$.
This implies $P_1(k) = 0$ for all $k \in \mathbb{Z}$.
$P_1(k) = ak+b$. $P_1(k)=0$ for all $k \in \mathbb{Z}$ implies that $a=0$ and $b=0$.
However, we are given that $P_1(x)$ is a polynomial of degree 1, so $a \neq 0$.
This leads to a contradiction.
Therefore, no such polynomial $Q(x)$ exists.

Alternative consideration for Part (b):
Suppose the condition was meant to hold only for $k \in \mathbb{Z} \setminus \{0\}$.
Then $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z} \setminus \{0\}$.
Let $Q(x) = \sum_{i=0}^m b_i x^i$ with $b_m \ne 0$.
Let $\hat{Q}(k) = b_0 k^m + b_1 k^{m-1} + \dots + b_m$. Note that $\hat{Q}(k) = k^m Q(1/k)$.
Then $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{\hat{Q}(k)}{k^{m+1}}$.
The condition becomes $\frac{\hat{Q}(k)}{k^{m+1}} = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z} \setminus \{0\}$.
This implies $\hat{Q}(k) P_2(k) = k^{m+1} P_1(k)$ for all $k \in \mathbb{Z} \setminus \{0\}$.
The expressions on both sides are polynomials in $k$. Since they agree on an infinite set ($\mathbb{Z} \setminus \{0\}$), they must be equal as polynomials.
So the identity $\hat{Q}(k) P_2(k) = k^{m+1} P_1(k)$ holds for all $k \in \mathbb{R}$.
Let's evaluate this identity at $k=0$.
$\hat{Q}(0) P_2(0) = 0^{m+1} P_1(0)$.
We have $\hat{Q}(0) = b_m$. Also $P_2(0)=e$ and $P_1(0)=b$.
So $b_m e = 0^{m+1} b$.
Since $Q(x)$ has degree $m$, $b_m \neq 0$. Since $P_2(0)=e \neq 0$, the left side $b_m e \neq 0$.
The right side depends on $m$.
If $m=0$, $Q(x)=b_0$. $m+1=1$. The RHS is $0^1 b = 0$. So $b_0 e = 0$. Since $e \neq 0$, $b_0=0$. This contradicts $m=0$ implies $b_0 \ne 0$.
If $m \ge 1$, $m+1 \ge 2$. The RHS is $0^{m+1} b = 0$. So $b_m e = 0$. Since $e \neq 0$, $b_m=0$. This contradicts $m=\deg Q$, which requires $b_m \neq 0$.
In both cases, we reach a contradiction, assuming $Q(x)$ is not the zero polynomial.
If $Q(x)=0$, then $\hat{Q}(k)=0$. The identity becomes $0 = k^{m+1} P_1(k)$. This implies $P_1(k)=0$ for $k \neq 0$. Since $P_1$ is degree 1, $a \ne 0$, $P_1(k)=ak+b$ has at most one root. It cannot be zero for infinitely many integers. So $Q(x)=0$ is not a solution.

Conclusion for (b): No such polynomial $Q$ exists, regardless of whether the condition is required for all $k \in \mathbb{Z}$ or $k \in \mathbb{Z} \setminus \{0\}$.

Final Answer: The final answer is $\boxed{Yes for (a), No for (b)}$