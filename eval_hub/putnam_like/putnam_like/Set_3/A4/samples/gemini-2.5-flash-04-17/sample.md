Let $x = \sqrt{11}+3$. We want to prove that $\lceil x^{2n} \rceil$ is divisible by $2^{n+1}$ for any $n\geq 1$.
Let $y = 3-\sqrt{11}$. Note that $x = 3+\sqrt{11}$.
We have $x+y = (3+\sqrt{11}) + (3-\sqrt{11}) = 6$ and $xy = (3+\sqrt{11})(3-\sqrt{11}) = 3^2 - (\sqrt{11})^2 = 9 - 11 = -2$.

Consider $x^{2n} = (\sqrt{11}+3)^{2n}$ and $y^{2n} = (3-\sqrt{11})^{2n}$.
Since $2n$ is an even exponent, $y^{2n} = (\sqrt{11}-3)^{2n}$.
We know that $3^2 = 9$ and $4^2 = 16$, so $3 < \sqrt{11} < 4$.
Therefore, $0 < \sqrt{11}-3 < 1$.
This implies that for $n \ge 1$, $0 < y^{2n} = (\sqrt{11}-3)^{2n} < 1$.

Let $a_n = x^{2n} + y^{2n} = (3+\sqrt{11})^{2n} + (3-\sqrt{11})^{2n}$.
Using the binomial expansion,
$(3+\sqrt{11})^{2n} = \sum_{k=0}^{2n} \binom{2n}{k} 3^{2n-k} (\sqrt{11})^k$
$(3-\sqrt{11})^{2n} = \sum_{k=0}^{2n} \binom{2n}{k} 3^{2n-k} (-\sqrt{11})^k$
Let's look at the sum $a_n$:
$a_n = \sum_{k=0}^{2n} \binom{2n}{k} 3^{2n-k} (\sqrt{11})^k + \sum_{k=0}^{2n} \binom{2n}{k} 3^{2n-k} (-\sqrt{11})^k$
$a_n = \sum_{k=0}^{2n} \binom{2n}{k} 3^{2n-k} ((\sqrt{11})^k + (-\sqrt{11})^k)$.
If $k$ is odd, $(\sqrt{11})^k + (-\sqrt{11})^k = \sqrt{11}^k - \sqrt{11}^k = 0$.
If $k$ is even, let $k=2j$, $(\sqrt{11})^{2j} + (-\sqrt{11})^{2j} = 11^j + 11^j = 2 \cdot 11^j$.
So, $a_n = \sum_{j=0}^n \binom{2n}{2j} 3^{2n-2j} (2 \cdot 11^j) = 2 \sum_{j=0}^n \binom{2n}{2j} 3^{2n-2j} 11^j$.
Since the sum is a sum of products of integers, it is an integer. Thus, $a_n$ is an integer for all $n \ge 0$.

We have $x^{2n} = a_n - y^{2n}$. Since $a_n$ is an integer and $0 < y^{2n} < 1$ for $n \ge 1$, we can determine $\lceil x^{2n} \rceil$.
We need to check if $y^{2n}$ can be an integer. $y^{2n} = (3-\sqrt{11})^{2n} = \sum_{k=0}^{2n} \binom{2n}{k} 3^{2n-k} (-\sqrt{11})^k$.
This expansion is of the form $U_n - V_n\sqrt{11}$, where $U_n = \sum_{j=0}^n \binom{2n}{2j} 3^{2n-2j} 11^j$ and $V_n = \sum_{j=0}^{n-1} \binom{2n}{2j+1} 3^{2n-2j-1} 11^j$.
$U_n$ and $V_n$ are integers. $y^{2n}$ is an integer if and only if $V_n=0$.
For $n \ge 1$, $V_n = \binom{2n}{1} 3^{2n-1} + \binom{2n}{3} 3^{2n-3} 11 + \dots$. The first term is $2n \cdot 3^{2n-1}$. For $n \ge 1$, this term is $2n \cdot 3^{2n-1} \ge 2 \cdot 3^1 = 6$. All terms in the sum for $V_n$ are non-negative integers. Thus $V_n > 0$ for $n \ge 1$.
So $y^{2n}$ is never an integer for $n \ge 1$.
Since $a_n$ is an integer and $0 < y^{2n} < 1$ and $y^{2n}$ is not an integer, $x^{2n} = a_n - y^{2n}$ is not an integer.
Therefore, $\lceil x^{2n} \rceil = a_n$ for $n \ge 1$.

The problem is now equivalent to proving that $a_n$ is divisible by $2^{n+1}$ for $n \geq 1$.
Let $X = x^2 = (3+\sqrt{11})^2 = 9 + 6\sqrt{11} + 11 = 20 + 6\sqrt{11}$.
Let $Y = y^2 = (3-\sqrt{11})^2 = 9 - 6\sqrt{11} + 11 = 20 - 6\sqrt{11}$.
Then $a_n = X^n + Y^n$.
$X+Y = (20+6\sqrt{11}) + (20-6\sqrt{11}) = 40$.
$XY = (20+6\sqrt{11})(20-6\sqrt{11}) = 20^2 - (6\sqrt{11})^2 = 400 - 36 \times 11 = 400 - 396 = 4$.
$a_n = X^n + Y^n$ satisfies a linear recurrence relation with characteristic equation $t^2 - (X+Y)t + XY = 0$, which is $t^2 - 40t + 4 = 0$.
So $a_{n+2} - 40a_{n+1} + 4a_n = 0$ for $n \ge 0$.

We prove by induction that $a_n$ is divisible by $2^{n+1}$ for $n \ge 1$.
Base cases:
For $n=1$, $a_1 = X^1 + Y^1 = 40$. We need to check if $a_1$ is divisible by $2^{1+1}=4$. $40 = 10 \times 4$. This is true.
For $n=2$, $a_2 = X^2 + Y^2 = (X+Y)^2 - 2XY = 40^2 - 2(4) = 1600 - 8 = 1592$. We need to check if $a_2$ is divisible by $2^{2+1}=8$. $1592 = 199 \times 8$. This is true.

Induction step: Assume that $a_k$ is divisible by $2^{k+1}$ for all $1 \le k \le n$ for some $n \ge 2$.
So $a_n = c_n 2^{n+1}$ and $a_{n-1} = c_{n-1} 2^n$ for some integers $c_n, c_{n-1}$.
We want to show that $a_{n+1}$ is divisible by $2^{n+2}$.
Using the recurrence relation:
$a_{n+1} = 40a_n - 4a_{n-1}$.
Substitute the expressions based on the induction hypothesis:
$a_{n+1} = 40(c_n 2^{n+1}) - 4(c_{n-1} 2^n)$.
$a_{n+1} = (5 \times 8) c_n 2^{n+1} - 2^2 c_{n-1} 2^n$.
$a_{n+1} = 5 \times 2^3 \times c_n 2^{n+1} - c_{n-1} 2^{n+2}$.
$a_{n+1} = 5 c_n 2^{n+4} - c_{n-1} 2^{n+2}$.
$a_{n+1} = 2^{n+2} (5 c_n 2^2 - c_{n-1})$.
$a_{n+1} = 2^{n+2} (20 c_n - c_{n-1})$.
Since $c_n$ and $c_{n-1}$ are integers, $20 c_n - c_{n-1}$ is an integer.
This shows that $a_{n+1}$ is divisible by $2^{n+2}$.

The induction hypothesis holds for $n=1$ and $n=2$. The induction step shows that if the statement is true for $n-1$ and $n$ (for $n \ge 2$), it is also true for $n+1$. Since it is true for $n=1$ and $n=2$, it is true for $n=3, 4, 5, \dots$.
Thus, $a_n$ is divisible by $2^{n+1}$ for all $n \ge 1$.

Since $\lceil (\sqrt{11}+3)^{2n} \rceil = a_n$, we have proved that $\lceil (\sqrt{11}+3)^{2n} \rceil$ is divisible by $2^{n+1}$ for any $n\geq 1$.

The final answer is $\boxed{\lceil (\sqrt {11}+3)^{2n}\rceil \text{ is divisible by } 2^{n+1} \text{ for any } n\geq 1}$.