Let $x = (\sqrt{5}+2)^{2n}$. We are looking for the smallest integer greater than $x$.
Let $\alpha = \sqrt{5}+2$ and $\beta = \sqrt{5}-2$.
Then $x = \alpha^{2n}$.
Consider $\beta^{2n} = (\sqrt{5}-2)^{2n}$.
We know that $2 < \sqrt{5} < 3$, so $0 < \sqrt{5}-2 < 1$.
Since $n$ is a positive integer, $2n$ is a positive even integer.
$0 < \sqrt{5}-2 < 1$ implies $0 < (\sqrt{5}-2)^{2n} < 1$ for $n \ge 1$.
Let $y = (\sqrt{5}-2)^{2n}$. So $0 < y < 1$.

Let's consider the sum $x+y = (\sqrt{5}+2)^{2n} + (\sqrt{5}-2)^{2n}$.
We can expand $(\sqrt{5}+2)^{2n}$ and $(\sqrt{5}-2)^{2n}$ using the binomial theorem.
$(\sqrt{5}+2)^{2n} = \sum_{k=0}^{2n} \binom{2n}{k} (\sqrt{5})^k 2^{2n-k}$
$(\sqrt{5}-2)^{2n} = \sum_{k=0}^{2n} \binom{2n}{k} (\sqrt{5})^k (-2)^{2n-k}$

Adding these two expansions:
$x+y = \sum_{k=0}^{2n} \binom{2n}{k} \sqrt{5}^k (2^{2n-k} + (-2)^{2n-k})$.
The term $2^{2n-k} + (-2)^{2n-k}$ is $2 \cdot 2^{2n-k}$ if $2n-k$ is even, and $0$ if $2n-k$ is odd.
$2n-k$ is even if and only if $k$ is even (since $2n$ is even).
So, the sum becomes:
$x+y = \sum_{k \text{ is even}} \binom{2n}{k} (\sqrt{5})^k 2^{2n-k+1}$.
Let $k=2j$ for $j=0, 1, \dots, n$.
$x+y = \sum_{j=0}^{n} \binom{2n}{2j} (\sqrt{5})^{2j} 2^{2n-2j+1} = \sum_{j=0}^{n} \binom{2n}{2j} 5^j 2^{2n-2j+1}$.
This is a sum of integers, so $x+y$ is an integer.

Let $K = x+y$. We have shown $K$ is an integer.
We know $x = (\sqrt{5}+2)^{2n}$ and $y = (\sqrt{5}-2)^{2n}$.
Since $n$ is a positive integer, $y > 0$, so $x < x+y = K$.
Since $n$ is a positive integer, $0 < y < 1$, so $x+y < x+1$.
Thus, $x < K < x+1$.

Now we need to check if $x = (\sqrt{5}+2)^{2n}$ is an integer.
$x = ((\sqrt{5}+2)^2)^n = (5+4\sqrt{5}+4)^n = (9+4\sqrt{5})^n$.
Let $(9+4\sqrt{5})^n = A_n + B_n\sqrt{5}$ for integers $A_n, B_n$.
For $n=1$, $(9+4\sqrt{5})^1 = 9+4\sqrt{5}$, so $A_1=9, B_1=4$.
For $n=2$, $(9+4\sqrt{5})^2 = 81 + 72\sqrt{5} + 16 \cdot 5 = 161+72\sqrt{5}$, so $A_2=161, B_2=72$.
In general, $A_{n+1} + B_{n+1}\sqrt{5} = (A_n+B_n\sqrt{5})(9+4\sqrt{5}) = (9A_n+20B_n) + (4A_n+9B_n)\sqrt{5}$.
$A_{n+1}=9A_n+20B_n$ and $B_{n+1}=4A_n+9B_n$.
Since $A_1=9, B_1=4$, which are positive, $A_n, B_n$ are positive integers for all $n \ge 1$.
We can show $B_n \ne 0$ for $n \ge 1$. $B_1=4$. Assume $B_k \ne 0$. $B_{k+1} = 4A_k+9B_k$. Since $A_k, B_k$ are positive, $B_{k+1} > 0$.
So $B_n \ne 0$ for all $n \ge 1$.
Since $B_n \ne 0$ and $\sqrt{5}$ is irrational, $(\sqrt{5}+2)^{2n} = A_n+B_n\sqrt{5}$ is irrational for $n \ge 1$.

Since $x$ is irrational for $n \ge 1$, $x$ is not an integer.
We have shown that $K = x+y$ is an integer and $x < K < x+1$.
By definition, the smallest integer greater than $x$ is $\lfloor x \rfloor + 1$.
Since $x$ is not an integer, $\lfloor x \rfloor < x < \lfloor x \rfloor + 1$.
The integer $K$ lies between $x$ and $x+1$. Therefore, $K$ must be equal to $\lfloor x \rfloor + 1$.
So the smallest integer greater than $x$ is $K = (\sqrt{5}+2)^{2n} + (\sqrt{5}-2)^{2n}$.

The final answer is $\boxed{(\sqrt{5}+2)^{2n} + (\sqrt{5}-2)^{2n}}$.