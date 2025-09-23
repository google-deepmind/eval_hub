Let $b_n = \frac{a_n}{3^n}$. The recurrence relation for $a_n$ is $a_{n+2}=4a_{n+1}-3a_n+\frac{3^n}{a_n}$ for $n\geq 1$.
Divide by $3^{n+2}$:
$$ \frac{a_{n+2}}{3^{n+2}} = \frac{4a_{n+1}}{3^{n+2}} - \frac{3a_n}{3^{n+2}} + \frac{3^n}{a_n 3^{n+2}} $$
$$ b_{n+2} = \frac{4}{3} \frac{a_{n+1}}{3^{n+1}} - \frac{3}{3^2} \frac{a_n}{3^n} + \frac{3^n}{a_n 3^n 3^2} $$
$$ b_{n+2} = \frac{4}{3} b_{n+1} - \frac{1}{3} b_n + \frac{1}{(a_n/3^n) 3^2} = \frac{4}{3} b_{n+1} - \frac{1}{3} b_n + \frac{1}{9 b_n} $$
This derivation of the recurrence relation for $b_n$ seems correct. However, let's check the first few terms.
$a_1=3, a_2=10$.
$b_1 = a_1/3^1 = 3/3 = 1$.
$b_2 = a_2/3^2 = 10/9$.
$a_3 = 4a_2 - 3a_1 + 3^1/a_1 = 4(10) - 3(3) + 3/3 = 40 - 9 + 1 = 32$.
$b_3 = a_3/3^3 = 32/27$.
Let's check if $b_1, b_2, b_3$ satisfy $b_{n+2} = \frac{4}{3} b_{n+1} - \frac{1}{3} b_n + \frac{1}{9 b_n}$ for $n=1$:
$b_3 = \frac{4}{3} b_2 - \frac{1}{3} b_1 + \frac{1}{9 b_1} = \frac{4}{3}(10/9) - \frac{1}{3}(1) + \frac{1}{9(1)} = \frac{40}{27} - \frac{1}{3} + \frac{1}{9} = \frac{40-9+3}{27} = \frac{34}{27}$.
$32/27 \neq 34/27$. This indicates that the recurrence relation for $b_n$ obtained by dividing by $3^{n+2}$ is not the one that the sequence $a_n/3^n$ satisfies for small $n$.

Let's re-examine the term $\frac{3^n}{a_n 3^{n+2}}$. It is $\frac{3^n}{a_n 3^n 3^2} = \frac{1}{(a_n/3^n) 3^2} = \frac{1}{b_n 9}$. This step was correct.
The recurrence for $a_n$ is $a_{n+2} = 4a_{n+1} - 3a_n + \frac{3^n}{a_n}$ for $n\geq 1$.
Let $c_n = a_{n+1} - 3a_n$.
For $n \geq 1$, $c_{n+1} = a_{n+2} - 3a_{n+1} = (4a_{n+1} - 3a_n + \frac{3^n}{a_n}) - 3a_{n+1} = a_{n+1} - 3a_n + \frac{3^n}{a_n} = c_n + \frac{3^n}{a_n}$.
$c_1 = a_2 - 3a_1 = 10 - 3(3) = 1$.
$c_2 = c_1 + 3^1/a_1 = 1 + 3/3 = 2$.
$c_3 = c_2 + 3^2/a_2 = 2 + 9/10 = 2.9$.
$c_4 = c_3 + 3^3/a_3 = 2.9 + 27/32 = 2.9 + 0.84375 = 3.74375$.

Now relate $c_n$ to $b_n = a_n/3^n$.
$c_n = a_{n+1} - 3a_n = b_{n+1} 3^{n+1} - 3 b_n 3^n = 3^{n+1} (b_{n+1} - b_n)$.
So $b_{n+1} - b_n = \frac{c_n}{3^{n+1}}$ for $n \geq 1$.
$b_n = b_1 + \sum_{k=1}^{n-1} (b_{k+1}-b_k) = b_1 + \sum_{k=1}^{n-1} \frac{c_k}{3^{k+1}}$ for $n > 1$. $b_1 = 1$.
$c_{n+1} = c_n + \frac{3^n}{a_n} = c_n + \frac{3^n}{b_n 3^n} = c_n + \frac{1}{b_n}$ for $n \geq 1$.
$c_1=1$. $c_2=c_1+1/b_1 = 1+1/1=2$. $c_3=c_2+1/b_2 = 2+1/(10/9)=2+9/10=2.9$. $c_4=c_3+1/b_3 = 2.9+1/(32/27)=2.9+27/32=3.74375$.
These values match the calculation from $a_n$.

Since $b_1=1 > 0$, and $c_n = 1+\sum_{k=1}^{n-1} 1/b_k$ for $n \ge 2$ ($c_1=1$), $c_n$ is a sum of positive terms, so $c_n > 0$ for all $n \ge 1$.
$b_{n+1} - b_n = \frac{c_n}{3^{n+1}} > 0$ for all $n \geq 1$.
This means the sequence $(b_n)$ is strictly increasing.

Now we need to show that $(b_n)$ is bounded above.
$c_{n+1} = c_n + 1/b_n$. Since $b_n$ is strictly increasing, $b_n \ge b_1 = 1$.
$c_{n+1} = c_n + 1/b_n \le c_n + 1$.
$c_1=1$. $c_2=2$. $c_3=2.9 < 3$. $c_4=3.74375 < 4$.
We can prove $c_n \le n$ for $n \ge 1$ by induction. Base cases $n=1,2,3,4$ hold.
Assume $c_k \le k$ for $1 \le k \le n$.
$b_k = b_1 + \sum_{j=1}^{k-1} \frac{c_j}{3^{j+1}} \le 1 + \sum_{j=1}^{k-1} \frac{j}{3^{j+1}}$.
$\sum_{j=1}^{k-1} \frac{j}{3^{j+1}} = \frac{1}{3} \sum_{j=1}^{k-1} j (1/3)^j$.
The series $\sum_{j=1}^{\infty} j x^j = x/(1-x)^2$. For $x=1/3$, $\sum_{j=1}^{\infty} j (1/3)^j = (1/3)/(1-1/3)^2 = (1/3)/(2/3)^2 = (1/3)/(4/9) = 3/4$.
So $\sum_{j=1}^{k-1} \frac{j}{3^{j+1}} < \frac{1}{3} \sum_{j=1}^{\infty} j (1/3)^j = \frac{1}{3} (3/4) = 1/4$.
$b_k \le 1 + 1/4 = 5/4$.
This bound holds for all $k$. $b_k \le 5/4$.
$c_{n+1} = c_n + 1/b_n$. Since $b_n \ge b_1 = 1$, $c_{n+1} \le c_n+1$. This was not enough.
$b_k \ge 1$ for all $k \ge 1$. $c_{k+1} = c_k + 1/b_k$. $c_k=1+\sum_{j=1}^{k-1} 1/b_j$.
$c_k \le 1 + \sum_{j=1}^{k-1} 1/1 = k$. This is what we needed. $c_k \le k$ for $k \ge 1$.
$b_n = 1 + \sum_{k=1}^{n-1} c_k/3^{k+1} \le 1 + \sum_{k=1}^{n-1} k/3^{k+1}$.
As shown above, $\sum_{k=1}^{n-1} k/3^{k+1} < \sum_{k=1}^{\infty} k/3^{k+1} = 1/4$.
So $b_n < 1 + 1/4 = 5/4$ for all $n \ge 1$.
The sequence $(b_n)$ is strictly increasing and bounded above by $5/4$. Therefore, $\lim_{n\to\infty} b_n$ exists.
Let $L = \lim_{n\to\infty} b_n$. Since $b_n$ is increasing, $b_n < 5/4$ for all $n$, so $L \le 5/4$.
The required inequality is $L \le 7/4$. Since $5/4 = 1.25$ and $7/4 = 1.75$, $5/4 < 7/4$.
Thus, $L \le 5/4 < 7/4$.

The limit exists and is not greater than $7/4$.

The final answer is $\boxed{\lim_{n\to\infty} \frac{a_n}{3^n} \text{ exists and is not greater then } \frac 74}$.