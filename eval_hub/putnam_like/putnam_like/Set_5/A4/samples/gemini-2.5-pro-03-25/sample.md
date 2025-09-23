Solution:
Let the sequence $(a_n)$ be defined by $a_1=3$, $a_2=10$ and the recurrence relation
\[a_{n+2}=4a_{n+1}-3a_n+\frac{3^n}{a_n}\quad\text{for } n\geq 1.\]
We want to prove that $\lim_{n\to\infty} \frac{a_n}{3^n}$ exists and is not greater than $\frac 74$.

Let $b_n = a_n/3^n$. We want to show that $\lim_{n\to\infty} b_n$ exists and its value $L$ satisfies $L \le 7/4$.
We substitute $a_n = 3^n b_n$ into the recurrence relation:
$3^{n+2} b_{n+2} = 4 \cdot 3^{n+1} b_{n+1} - 3 \cdot 3^n b_n + \frac{3^n}{3^n b_n}$.
$9 \cdot 3^n b_{n+2} = 12 \cdot 3^n b_{n+1} - 3 \cdot 3^n b_n + \frac{1}{b_n}$.
Dividing by $3^n$, we obtain the recurrence relation for $b_n$:
\[9 b_{n+2} = 12 b_{n+1} - 3 b_n + \frac{1}{3^n b_n}.\]
The first few terms of $(a_n)$ are $a_1=3$, $a_2=10$, $a_3 = 4(10) - 3(3) + 3/3 = 40 - 9 + 1 = 32$.
The first few terms of $(b_n)$ are $b_1 = a_1/3^1 = 3/3 = 1$, $b_2 = a_2/3^2 = 10/9$, $b_3 = a_3/3^3 = 32/27$.

First, we show that $a_n > 0$ for all $n$. $a_1=3 > 0$, $a_2=10 > 0$. Let's assume $a_k > 0$ for $k \le n+1$. Then $\frac{3^n}{a_n} > 0$. $a_{n+2} = 4a_{n+1} - 3a_n + \frac{3^n}{a_n}$. This expression is not obviously positive.
Let's show $b_n \ge 1$ for all $n$. $b_1=1$. $b_2=10/9 > 1$. Assume $b_k \ge 1$ for $k \le n+1$.
The recurrence can be written as $b_{n+2} = \frac{4}{3} b_{n+1} - \frac{1}{3} b_n + \frac{1}{9 \cdot 3^n b_n}$.
Let $d_n = b_{n+1} - b_n$. Then $b_{n+2} - b_{n+1} = \frac{1}{3} b_{n+1} - \frac{1}{3} b_n + \frac{1}{9 \cdot 3^n b_n}$.
$d_{n+1} = \frac{1}{3} (b_{n+1} - b_n) + \frac{1}{9 \cdot 3^n b_n} = \frac{1}{3} d_n + \frac{1}{9 \cdot 3^n b_n}$.
$d_1 = b_2 - b_1 = 10/9 - 1 = 1/9$.
Since $b_1=1>0$, $b_2=10/9>0$. Assume $b_k>0$ for $k \le n+1$. Then $d_{n+1} = \frac{1}{3}d_n + \frac{1}{9 \cdot 3^n b_n}$. The last term is positive.
Since $d_1=1/9 > 0$, and the recurrence shows that if $d_n > 0$ then $d_{n+1} > 0$ (as long as $b_n > 0$), by induction $d_n > 0$ for all $n \ge 1$.
This means $b_{n+1} > b_n$ for all $n \ge 1$. The sequence $(b_n)$ is strictly increasing.
Since $b_1=1$, we have $b_n \ge 1$ for all $n \ge 1$.
Since $b_n \ge 1$, $a_n = 3^n b_n \ge 3^n > 0$ for all $n$. This confirms that $a_n$ is always positive.

Since $(b_n)$ is strictly increasing, to show that the limit exists, we only need to show that $(b_n)$ is bounded above.
Let's analyze the structure of $a_n$. The homogeneous recurrence $h_{n+2} = 4h_{n+1} - 3h_n$ has characteristic equation $r^2 - 4r + 3 = 0$, which factors as $(r-1)(r-3)=0$. The roots are $r=1, r=3$. The general solution is $h_n = c_1 \cdot 1^n + c_2 \cdot 3^n$.
Let's find $c_1, c_2$ such that $h_1=a_1=3$ and $h_2=a_2=10$.
$h_1 = c_1 + 3c_2 = 3$.
$h_2 = c_1 + 9c_2 = 10$.
Subtracting the first from the second gives $6c_2 = 7$, so $c_2 = 7/6$.
Then $c_1 = 3 - 3c_2 = 3 - 3(7/6) = 3 - 7/2 = -1/2$.
So $h_n = -\frac{1}{2} + \frac{7}{6} 3^n$.

Let $\epsilon_n = a_n - h_n$. Then $\epsilon_1 = a_1 - h_1 = 3-3=0$ and $\epsilon_2 = a_2 - h_2 = 10-10=0$.
Substituting $a_n = h_n + \epsilon_n$ into the recurrence for $a_n$:
$h_{n+2} + \epsilon_{n+2} = 4(h_{n+1} + \epsilon_{n+1}) - 3(h_n + \epsilon_n) + \frac{3^n}{a_n}$.
Since $h_{n+2} = 4h_{n+1} - 3h_n$, this simplifies to
$\epsilon_{n+2} = 4\epsilon_{n+1} - 3\epsilon_n + \frac{3^n}{a_n}$.

Let $f_n = \epsilon_n / 3^n$. Then $f_1 = 0/3 = 0$ and $f_2 = 0/9 = 0$.
Substitute $\epsilon_n = 3^n f_n$ into the recurrence for $\epsilon_n$:
$3^{n+2} f_{n+2} = 4 \cdot 3^{n+1} f_{n+1} - 3 \cdot 3^n f_n + \frac{3^n}{a_n}$.
$9 \cdot 3^n f_{n+2} = 12 \cdot 3^n f_{n+1} - 3 \cdot 3^n f_n + \frac{3^n}{a_n}$.
Dividing by $3^n$, we get the recurrence for $f_n$:
\[9 f_{n+2} = 12 f_{n+1} - 3 f_n + \frac{1}{a_n}.\]
Since $a_n = 3^n b_n$, we have $\frac{1}{a_n} = \frac{1}{3^n b_n}$.
So $9 f_{n+2} = 12 f_{n+1} - 3 f_n + \frac{1}{3^n b_n}$.

Let $e_n = f_{n+1} - f_n$. Then $e_1 = f_2 - f_1 = 0 - 0 = 0$.
The recurrence for $f_n$ can be written as $9 f_{n+2} - 12 f_{n+1} + 3 f_n = \frac{1}{3^n b_n}$.
$9 (f_{n+2} - f_{n+1}) = 3 (f_{n+1} - f_n) + \frac{1}{3^n b_n}$.
$9 e_{n+1} = 3 e_n + \frac{1}{3^n b_n}$.
$e_{n+1} = \frac{1}{3} e_n + \frac{1}{9 \cdot 3^n b_n}$.
Since $b_n \ge 1$, we have $\frac{1}{9 \cdot 3^n b_n} > 0$.
Since $e_1 = 0$, $e_2 = \frac{1}{3} e_1 + \frac{1}{9 \cdot 3^1 b_1} = 0 + \frac{1}{9 \cdot 3 \cdot 1} = \frac{1}{27}$.
Since $e_2 > 0$ and the recurrence relation implies $e_{n+1} > \frac{1}{3} e_n$ for $n \ge 1$, by induction $e_n \ge 0$ for all $n \ge 1$. Specifically, $e_n > 0$ for $n \ge 2$.
Since $e_n = f_{n+1} - f_n \ge 0$, the sequence $(f_n)$ is non-decreasing.

We have $b_n = a_n/3^n = (h_n + \epsilon_n)/3^n = h_n/3^n + \epsilon_n/3^n = (-\frac{1}{2} + \frac{7}{6} 3^n)/3^n + f_n$.
$b_n = -\frac{1}{2 \cdot 3^n} + \frac{7}{6} + f_n$.
Since $(f_n)$ is non-decreasing, it either converges to a finite limit or diverges to $+\infty$.
If $f_n \to \infty$, then $b_n \to \infty$. If $f_n \to F$ (finite), then $b_n \to 7/6 + F$.

Let's show that $f_n$ is bounded above.
We have $e_{n+1} = \frac{1}{3} e_n + \frac{1}{9 \cdot 3^n b_n}$. Since $b_n \ge 1$, $0 < \frac{1}{9 \cdot 3^n b_n} \le \frac{1}{9 \cdot 3^n}$.
Consider the sequence $\tilde{e}_n$ defined by $\tilde{e}_1 = 0$ and $\tilde{e}_{n+1} = \frac{1}{3} \tilde{e}_n + \frac{1}{9 \cdot 3^n}$.
By induction, $e_n \le \tilde{e}_n$ for all $n$. $e_1 = \tilde{e}_1 = 0$. Assume $e_k \le \tilde{e}_k$. Then $e_{k+1} = \frac{1}{3} e_k + \frac{1}{9 \cdot 3^k b_k} \le \frac{1}{3} \tilde{e}_k + \frac{1}{9 \cdot 3^k} = \tilde{e}_{k+1}$.
We can find an explicit formula for $\tilde{e}_n$.
$\tilde{e}_n = \sum_{k=1}^{n-1} \left(\frac{1}{3}\right)^{n-1-k} \frac{1}{9 \cdot 3^k} = \frac{1}{9} \sum_{k=1}^{n-1} \frac{1}{3^{n-1-k} 3^k} = \frac{1}{9} \sum_{k=1}^{n-1} \frac{1}{3^{n-1}} = \frac{1}{9 \cdot 3^{n-1}} (n-1) = \frac{n-1}{3^{n+1}}$.
So $e_n \le \frac{n-1}{3^{n+1}}$ for $n \ge 1$.

Now we consider $f_n$. Since $f_1 = 0$, $f_n = f_1 + \sum_{k=1}^{n-1} e_k = \sum_{k=1}^{n-1} e_k$.
$f_n \le \sum_{k=1}^{n-1} \tilde{e}_k = \sum_{k=1}^{n-1} \frac{k-1}{3^{k+1}}$.
The series $\sum_{k=1}^\infty \tilde{e}_k = \sum_{k=1}^\infty \frac{k-1}{3^{k+1}}$ converges. Let's compute its sum.
$\sum_{k=1}^\infty \frac{k-1}{3^{k+1}} = \sum_{j=0}^\infty \frac{j}{3^{j+2}} = \frac{1}{9} \sum_{j=0}^\infty j \left(\frac{1}{3}\right)^j$.
Let $S = \sum_{j=0}^\infty j x^j$. This is $x \frac{d}{dx} \sum_{j=0}^\infty x^j = x \frac{d}{dx} \left(\frac{1}{1-x}\right) = x \frac{1}{(1-x)^2}$.
For $x=1/3$, $S = \frac{1/3}{(1-1/3)^2} = \frac{1/3}{(2/3)^2} = \frac{1/3}{4/9} = \frac{1}{3} \cdot \frac{9}{4} = \frac{3}{4}$.
So $\sum_{k=1}^\infty \tilde{e}_k = \frac{1}{9} S = \frac{1}{9} \cdot \frac{3}{4} = \frac{1}{12}$.
Since $e_k \le \tilde{e}_k$, the series $\sum_{k=1}^\infty e_k$ converges by comparison test.
Let $F = \sum_{k=1}^\infty e_k$. Then $F \le \sum_{k=1}^\infty \tilde{e}_k = 1/12$.
Since $f_n = \sum_{k=1}^{n-1} e_k$, the sequence $(f_n)$ converges to $F$.
Thus, the limit $L = \lim_{n\to\infty} b_n$ exists.
$L = \lim_{n\to\infty} \left( \frac{7}{6} - \frac{1}{2 \cdot 3^n} + f_n \right) = \frac{7}{6} - 0 + F = \frac{7}{6} + F$.

We need to show $L \le 7/4$.
We have shown $F \le 1/12$.
So $L \le 7/6 + 1/12 = 14/12 + 1/12 = 15/12 = 5/4$.
Since $5/4 = 1.25$ and $7/4 = 1.75$, we have $5/4 < 7/4$.
Therefore, $L \le 5/4 \le 7/4$.

We have proved that $\lim_{n\to\infty} \frac{a_n}{3^n}$ exists and is not greater than $7/4$.

Final check:
The sequence $(b_n)$ is strictly increasing. $b_1=1, b_2=10/9 \approx 1.11, b_3=32/27 \approx 1.185$.
The limit $L = 7/6+F$. $7/6 \approx 1.1667$.
$F = \sum e_k \ge e_1+e_2+e_3 = 0 + 1/27 + 19/810 \approx 0.037 + 0.023 = 0.06$.
$L \ge 7/6 + 1/27 + 19/810 \approx 1.1667 + 0.06 = 1.2267$.
The bound $L \le 5/4 = 1.25$ is consistent with this.

The steps and reasoning are correct.

Final Answer: The final answer is $\boxed{The limit exists and is not greater than $\frac 74$}$