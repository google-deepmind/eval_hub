Let $f(x) = \sum_{i=0}^\infty a_i x^i$ where $a_i \in \{0,1\}$ for all $i \geq 0$. The series converges absolutely for $|x|<1$.
Let $n \in \mathbb{N}$ be such that $f(1/2^n) \in \mathbb{Q}$. Let $x_0 = 1/2^n$.
$f(x_0) = \sum_{i=0}^\infty a_i x_0^i = \sum_{i=0}^\infty a_i (1/2^n)^i = \sum_{i=0}^\infty a_i 2^{-ni}$.
Let $r = f(x_0)$. So $r = a_0 + a_1 2^{-n} + a_2 2^{-2n} + a_3 2^{-3n} + \dots$.
Consider the binary representation of $r$. Let $r = (b_0 . b_1 b_2 b_3 \dots)_2$, where $b_0 = \lfloor r \rfloor$ and $0 . b_1 b_2 b_3 \dots = \{r\}$.
The expression $r = \sum_{i=0}^\infty a_i 2^{-ni}$ gives a specific binary representation. We have $b_0 = a_0$ (since $a_i \in \{0,1\}$, $r = a_0 + \sum_{i=1}^\infty a_i 2^{-ni}$. Since $x_0 = 1/2^n \le 1/2$, $f(x_0) = a_0 + a_1 x_0 + a_2 x_0^2 + \dots \le a_0 + \sum_{i=1}^\infty (1/2)^i = a_0+1$. If $a_0=0$, $f(x_0) \le 1$. If $a_0=1$, $f(x_0) = 1 + \sum a_i x_0^i \le 1 + \sum x_0^i = 1 + \frac{x_0}{1-x_0} = 1 + \frac{1/2^n}{1-1/2^n} = 1 + \frac{1}{2^n-1}$. If $n=1$, $f(1/2) \le a_0+1$. $f(1/2) = a_0 + a_1/2 + a_2/4 + \dots$. If $a_0=1$, $f(1/2) \le 1 + 1/2 + 1/4 + \dots = 2$. $r = a_0.00\dots0 a_1 00\dots0 a_2 \dots$ in base 2, where there are $n-1$ zeros between $a_i$ and $a_{i+1}$. The binary digits $b_j$ for $j \geq 1$ are given by $b_{ni} = a_i$ for $i \geq 1$, and $b_j = 0$ if $j$ is not a multiple of $n$. $b_0 = a_0$.
We are given that $r \in \mathbb{Q}$. A number is rational if and only if its binary representation is eventually periodic. This means the sequence of digits $(b_j)_{j \geq 1}$ is eventually periodic. Let $P \geq 1$ be the period length and $J_0 \geq 1$ be the starting index of the periodic part. So $b_{j+P} = b_j$ for all $j \geq J_0$.
Let $j = ni$ for $i$ large enough such that $ni \geq J_0$. Then $b_{ni} = a_i$. The periodicity implies $b_{ni+P} = b_{ni} = a_i$.
The digit $b_{ni+P}$ must be $a_{(ni+P)/n}$ if $n$ divides $ni+P$, and 0 otherwise.
If $n$ does not divide $P$, then $n$ does not divide $ni+P$. So $b_{ni+P} = 0$. This means $a_i = 0$ for all $i$ large enough ($ni \geq J_0$). Let $I_0 = \lceil J_0/n \rceil$. Then $a_i = 0$ for all $i \geq I_0$.
If $n$ divides $P$, let $P = Kn$ for some integer $K \geq 1$. Then $ni+P = ni+Kn = n(i+K)$. So $b_{ni+P} = b_{n(i+K)} = a_{i+K}$. The periodicity condition $b_{ni+P} = b_{ni}$ translates to $a_{i+K} = a_i$ for all $i$ large enough ($ni \geq J_0$). Let $I_0 = \lceil J_0/n \rceil$. Then $a_{i+K} = a_i$ for all $i \geq I_0$.
Also we must check the zero digits. If $j$ is not a multiple of $n$, $b_j = 0$. For $j \geq J_0$, we need $b_{j+P}=b_j=0$. If $n|P$, $P=Kn$. $j+P = j+Kn$. If $n \nmid j$, then $n \nmid j+Kn$. So $b_{j+P}=0$. This condition is satisfied.
In both cases ($n|P$ or $n \nmid P$), the sequence $(a_i)_{i \geq 0}$ is eventually periodic. That is, there exist integers $I_0 \geq 0$ and $K \geq 1$ such that $a_{i+K} = a_i$ for all $i \geq I_0$.
(Note that if $a_i=0$ for $i \ge I_0$, this corresponds to $K=1$ and $a_{I_0}=0$).

Now we want to evaluate $f(x)$ for $x=2/q$ where $q \geq 3$ is an odd natural number. Since $q \geq 3$, $0 < x = 2/q \leq 2/3 < 1$. The power series converges absolutely at $x=2/q$.
We can split the sum:
$$
f(x) = \sum_{i=0}^{I_0-1} a_i x^i + \sum_{i=I_0}^\infty a_i x^i
$$
The first part is a finite sum (a polynomial in $x$), let $Q(x) = \sum_{i=0}^{I_0-1} a_i x^i$.
The second part is an infinite series where the coefficients are periodic:
$$
S(x) = \sum_{i=I_0}^\infty a_i x^i = a_{I_0} x^{I_0} + a_{I_0+1} x^{I_0+1} + \dots
$$
Let $j=i-I_0$. $S(x) = \sum_{j=0}^\infty a_{I_0+j} x^{I_0+j}$. Since $a_{I_0+j+K} = a_{I_0+j}$ for $j \geq 0$.
$S(x) = (a_{I_0} x^{I_0} + \dots + a_{I_0+K-1} x^{I_0+K-1}) + (a_{I_0+K} x^{I_0+K} + \dots + a_{I_0+2K-1} x^{I_0+2K-1}) + \dots$
$S(x) = (a_{I_0} x^{I_0} + \dots + a_{I_0+K-1} x^{I_0+K-1}) + x^K (a_{I_0} x^{I_0} + \dots + a_{I_0+K-1} x^{I_0+K-1}) + x^{2K}(\dots) + \dots$
Let $P(x) = \sum_{j=0}^{K-1} a_{I_0+j} x^{I_0+j}$. Then
$S(x) = P(x) + x^K P(x) + x^{2K} P(x) + \dots = P(x) (1 + x^K + x^{2K} + \dots)$
Since $|x| < 1$, we have $|x^K| < 1$. The geometric series $1 + x^K + x^{2K} + \dots$ converges to $1/(1-x^K)$.
So, $S(x) = \frac{P(x)}{1-x^K} = \frac{\sum_{j=I_0}^{I_0+K-1} a_j x^j}{1-x^K}$.
Therefore, $f(x) = Q(x) + S(x) = \sum_{i=0}^{I_0-1} a_i x^i + \frac{\sum_{j=I_0}^{I_0+K-1} a_j x^j}{1-x^K}$.
This can be combined into a single fraction:
$$
f(x) = \frac{(\sum_{i=0}^{I_0-1} a_i x^i)(1-x^K) + \sum_{j=I_0}^{I_0+K-1} a_j x^j}{1-x^K}
$$
Let $N(x) = (\sum_{i=0}^{I_0-1} a_i x^i)(1-x^K) + \sum_{j=I_0}^{I_0+K-1} a_j x^j$. $N(x)$ is a polynomial in $x$. The coefficients $a_i$ are integers (0 or 1), so $N(x)$ is a polynomial with integer coefficients.
Let $x=2/q$. Since $q \ge 3$, $x=2/q$ is a rational number with $0 < x < 1$.
$f(2/q) = \frac{N(2/q)}{1-(2/q)^K}$.
Since $N(x)$ is a polynomial with integer coefficients, $N(2/q)$ is a rational number.
$1-(2/q)^K = 1 - 2^K/q^K = (q^K - 2^K)/q^K$. This is a non-zero rational number since $x=2/q \ne 1$.
Thus $f(2/q) = \frac{N(2/q)}{(q^K - 2^K)/q^K}$ is a rational number. This proves the first part.

Now we need to show that if $f(2/q) = \alpha/\beta$ with $\gcd(\alpha, \beta)=1$, then $\beta$ is odd.
Let's evaluate the expression for $f(2/q)$.
$N(x)$ is a polynomial. Let the degree of $N(x)$ be $M$. A quick check shows $M = I_0+K-1$.
$N(2/q)$ is of the form $I_N / q^M$ for some integer $I_N$, where $M$ is the maximum power of $q$ in the denominator needed to express $N(2/q)$.
$N(x) = \sum_{i=0}^{I_0-1} a_i x^i - \sum_{i=0}^{I_0-1} a_i x^{i+K} + \sum_{j=I_0}^{I_0+K-1} a_j x^j$.
The highest power of $x$ is $\max(I_0-1+K, I_0+K-1) = I_0+K-1$. Let $M = I_0+K-1$.
$N(2/q) = \sum c_k (2/q)^k$. To clear denominators, we multiply by $q^M$.
$q^M N(2/q) = q^{I_0+K-1} N(2/q)$ is an integer. Let $I_N = q^M N(2/q)$.
So $N(2/q) = I_N / q^M$.
$f(2/q) = \frac{I_N / q^M}{(q^K - 2^K)/q^K} = \frac{I_N q^K}{q^M (q^K - 2^K)} = \frac{I_N q^K}{q^{I_0+K-1} (q^K - 2^K)} = \frac{I_N q}{q^{I_0} (q^K - 2^K)}$.
Let this fraction be $Num/Den$. $Num = I_N q$ and $Den = q^{I_0} (q^K - 2^K)$.
We are given that $q$ is an odd natural number, $q \ge 3$.
$q$ is odd $\implies q^{I_0}$ is odd.
$q$ is odd $\implies q^K$ is odd.
$K \ge 1$, so $2^K$ is even.
Therefore, $q^K - 2^K$ is odd - even = odd.
The denominator $Den = q^{I_0} (q^K - 2^K)$ is a product of two odd integers, so $Den$ is odd.
We have $f(2/q) = \frac{Num}{Den}$. We want to write this fraction in reduced form $\alpha/\beta$ where $\gcd(\alpha, \beta) = 1$.
$\beta = \frac{Den}{\gcd(Num, Den)}$.
Since $Den$ is odd, all of its divisors are odd.
$\gcd(Num, Den)$ is a divisor of $Den$. Therefore, $\gcd(Num, Den)$ is odd.
$\beta$ is the result of dividing an odd integer ($Den$) by an odd integer ($\gcd(Num, Den)$).
The result $\beta$ must be odd.

This completes the proof. Both claims have been demonstrated. $f(2/q)$ is rational, and its reduced denominator $\beta$ is odd.

Final check: The case $K=1$ requires $2^K=2$. $q^K-2^K = q-2$. If $q=3$, $q-2=1$. If $q \ge 5$ is odd, $q-2$ is odd. So $q^K-2^K$ is odd for $K=1$. The argument holds. What if $I_0=0$? Then $f(x) = \frac{\sum_{j=0}^{K-1} a_j x^j}{1-x^K}$. $M=K-1$. $N(x) = \sum_{j=0}^{K-1} a_j x^j$. $I_N = q^{K-1} N(2/q) = q^{K-1} \sum_{j=0}^{K-1} a_j (2/q)^j = \sum_{j=0}^{K-1} a_j 2^j q^{K-1-j}$. This is an integer.
$f(2/q) = \frac{I_N / q^{K-1}}{(q^K - 2^K)/q^K} = \frac{I_N q^K}{q^{K-1}(q^K - 2^K)} = \frac{I_N q}{q^K - 2^K}$.
The denominator is $Den = q^K - 2^K$. This is odd. The numerator is $Num = I_N q$.
The reduced denominator $\beta = Den / \gcd(Num, Den)$ is odd since $Den$ is odd. The argument holds for $I_0=0$ too.


```markdown
Let $f(x) = \sum_{i=0}^\infty a_i x^i$ where $a_i \in \{0,1\}$. The series converges absolutely for $|x|<1$.
We are given that there exists $n \in \mathbb{N}$ such that $f(1/2^n) \in \mathbb{Q}$. Let $x_0 = 1/2^n$.
$f(x_0) = \sum_{i=0}^\infty a_i (1/2^n)^i = \sum_{i=0}^\infty a_i 2^{-ni}$.
Let $r = f(x_0)$. $r = a_0 + a_1 2^{-n} + a_2 2^{-2n} + a_3 2^{-3n} + \dots$.
This expression relates $r$ to its base $2$ representation. Let $r = (b_0 . b_1 b_2 b_3 \dots)_2$ be the binary representation of $r$. Then $r = b_0 + \sum_{j=1}^\infty b_j 2^{-j}$.
Comparing the two expressions for $r$, we see that $b_0 = a_0$, and for $j \geq 1$, $b_j = a_{j/n}$ if $n$ divides $j$, and $b_j=0$ if $n$ does not divide $j$.
Since $r \in \mathbb{Q}$, its binary representation must be eventually periodic. That is, there exist $J_0 \geq 1$ and $P \geq 1$ such that $b_{j+P} = b_j$ for all $j \geq J_0$.
This condition imposes constraints on the sequence $(a_i)$.
If $n$ divides $P$, let $P=Kn$ for some integer $K \ge 1$. For $j=ni$ with $ni \ge J_0$, we have $b_{ni} = a_i$. Periodicity means $b_{ni+P} = b_{ni}$. $b_{ni+P} = b_{n(i+K)} = a_{i+K}$. So $a_{i+K} = a_i$ for $ni \ge J_0$. Let $I_0 = \lceil J_0/n \rceil$. Then $a_{i+K} = a_i$ for $i \ge I_0$.
If $n$ does not divide $P$. For $j=ni$ with $ni \ge J_0$, $b_{ni}=a_i$. Periodicity means $b_{ni+P} = b_{ni} = a_i$. Since $n \nmid P$, $n \nmid (ni+P)$. Thus, by definition of the digits $b_j$, $b_{ni+P}=0$. So $a_i=0$ for $ni \ge J_0$. Let $I_0 = \lceil J_0/n \rceil$. Then $a_i=0$ for $i \ge I_0$. This is a special case of being eventually periodic (with period $K=1$ and $a_{I_0}=0$).
In all cases, the sequence $(a_i)$ is eventually periodic. There exist $I_0 \ge 0$ and $K \ge 1$ such that $a_{i+K} = a_i$ for all $i \ge I_0$.

Now consider $f(2/q)$ for an odd natural number $q \ge 3$. Let $x=2/q$. Since $q \ge 3$, $0 < x \le 2/3 < 1$, so the series $f(x)$ converges.
We can write $f(x)$ using the periodicity of $(a_i)$:
$$
f(x) = \sum_{i=0}^{I_0-1} a_i x^i + \sum_{i=I_0}^\infty a_i x^i
$$
The second sum $S(x) = \sum_{i=I_0}^\infty a_i x^i$ can be written using the period $K$. Let $P(x) = \sum_{j=I_0}^{I_0+K-1} a_j x^j$.
Then $S(x) = P(x) + x^K P(x) + x^{2K} P(x) + \dots = P(x) \sum_{m=0}^\infty (x^K)^m$.
Since $|x|<1$, $|x^K|<1$, the geometric series converges to $1/(1-x^K)$.
So $S(x) = \frac{P(x)}{1-x^K} = \frac{\sum_{j=I_0}^{I_0+K-1} a_j x^j}{1-x^K}$.
Thus, $f(x) = \sum_{i=0}^{I_0-1} a_i x^i + \frac{\sum_{j=I_0}^{I_0+K-1} a_j x^j}{1-x^K}$.
Let $x=2/q$. Since $a_i \in \{0,1\}$ are integers and $x=2/q$ is rational, $f(2/q)$ is a sum and ratio of rational numbers. Therefore, $f(2/q) \in \mathbb{Q}$. This proves the first part of the statement.

To prove the second part, let's write $f(2/q)$ as a single fraction.
$$
f(x) = \frac{(\sum_{i=0}^{I_0-1} a_i x^i)(1-x^K) + \sum_{j=I_0}^{I_0+K-1} a_j x^j}{1-x^K}
$$
Let $N(x) = (\sum_{i=0}^{I_0-1} a_i x^i)(1-x^K) + \sum_{j=I_0}^{I_0+K-1} a_j x^j$. $N(x)$ is a polynomial with integer coefficients.
Let $x=2/q$. Then $f(2/q) = \frac{N(2/q)}{1-(2/q)^K}$.
The denominator is $1-(2/q)^K = 1 - 2^K/q^K = (q^K - 2^K)/q^K$.
Let $M$ be the degree of the polynomial $N(x)$. $M = I_0+K-1$. $N(2/q)$ is a rational number. We can write $N(2/q) = \frac{I_N}{q^M}$ for some integer $I_N = q^M N(2/q)$.
So,
$$
f(2/q) = \frac{I_N / q^M}{(q^K - 2^K)/q^K} = \frac{I_N q^K}{q^M (q^K - 2^K)} = \frac{I_N q^K}{q^{I_0+K-1} (q^K - 2^K)} = \frac{I_N q}{q^{I_0} (q^K - 2^K)}
$$
Let $Num = I_N q$ and $Den = q^{I_0} (q^K - 2^K)$. So $f(2/q) = Num/Den$.
We are given that $q$ is an odd natural number, $q \ge 3$.
Since $q$ is odd, $q^{I_0}$ is odd for any $I_0 \ge 0$.
Since $q$ is odd, $q^K$ is odd for any $K \ge 1$.
Since $K \ge 1$, $2^K$ is an even integer.
Thus, $q^K - 2^K$ is an odd integer (odd - even = odd).
The denominator $Den = q^{I_0} (q^K - 2^K)$ is the product of two odd integers, so $Den$ is odd.
We want to write $f(2/q)$ in reduced form $\alpha/\beta$, where $\gcd(\alpha, \beta) = 1$.
This is obtained by dividing $Num$ and $Den$ by their greatest common divisor:
$\alpha = Num / \gcd(Num, Den)$ and $\beta = Den / \gcd(Num, Den)$.
Since $Den$ is odd, all of its divisors are odd.
$\gcd(Num, Den)$ is a divisor of $Den$. Therefore, $\gcd(Num, Den)$ is an odd integer.
$\beta$ is the result of dividing an odd integer ($Den$) by an odd integer ($\gcd(Num, Den)$).
Hence, $\beta$ must be an odd integer.

This completes the proof.

```