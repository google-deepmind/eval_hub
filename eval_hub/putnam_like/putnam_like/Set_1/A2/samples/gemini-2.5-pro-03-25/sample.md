Let $S_n$ denote the sum we want to compute:
$$ S_n = \sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n  \frac{1}{4^k} {\ell \choose 2k}. $$
The sum is over pairs of integers $(k, \ell)$ such that $0 \le k \le \lfloor n/2 \rfloor$ and $\max\{1, 2k\} \le \ell \le n$.
The condition $\ell \ge \max\{1, 2k\}$ implies $\ell \ge 1$ and $\ell \ge 2k$.
The condition $k \ge 0$ implies $2k \ge 0$. The binomial coefficient ${\ell \choose 2k}$ is non-zero only if $\ell \ge 2k$.
The condition $k \le \lfloor n/2 \rfloor$ implies $2k \le n$. Since $\ell \le n$, it is possible that $\ell \ge 2k$.

We can change the order of summation. The variable $\ell$ ranges from $1$ to $n$. For a fixed value of $\ell$, the variable $k$ must satisfy $0 \le k \le \lfloor n/2 \rfloor$ and $2k \le \ell$.
The condition $2k \le \ell$ implies $k \le \ell/2$, so $k \le \lfloor \ell/2 \rfloor$.
Since $\ell \le n$, we have $\ell/2 \le n/2$, and $\lfloor \ell/2 \rfloor \le \lfloor n/2 \rfloor$.
Thus, the condition $k \le \lfloor n/2 \rfloor$ is automatically satisfied if $k \le \lfloor \ell/2 \rfloor$.
So, for a fixed $\ell$, the range for $k$ is $0 \le k \le \lfloor \ell/2 \rfloor$.
The sum can be rewritten as:
$$ S_n = \sum_{\ell=1}^n \sum_{k=0}^{\lfloor \ell/2 \rfloor} \frac{1}{4^k} {\ell \choose 2k}. $$
Let $T_\ell$ denote the inner sum:
$$ T_\ell = \sum_{k=0}^{\lfloor \ell/2 \rfloor} \frac{1}{4^k} {\ell \choose 2k} = \sum_{k=0}^{\lfloor \ell/2 \rfloor} {\ell \choose 2k} \left(\frac{1}{2}\right)^{2k}. $$
We use the binomial expansion identity:
$$ (1+x)^\ell + (1-x)^\ell = \sum_{j=0}^\ell {\ell \choose j} x^j + \sum_{j=0}^\ell {\ell \choose j} (-x)^j = \sum_{j=0}^\ell {\ell \choose j} (x^j + (-x)^j). $$
The term $x^j + (-x)^j$ is $2x^j$ if $j$ is even, and $0$ if $j$ is odd. Let $j=2k$. The condition $0 \le j \le \ell$ becomes $0 \le 2k \le \ell$, which means $0 \le k \le \ell/2$. So $k$ ranges from $0$ to $\lfloor \ell/2 \rfloor$.
$$ (1+x)^\ell + (1-x)^\ell = \sum_{k=0}^{\lfloor \ell/2 \rfloor} {\ell \choose 2k} 2x^{2k}. $$
Dividing by 2, we get:
$$ \frac{(1+x)^\ell + (1-x)^\ell}{2} = \sum_{k=0}^{\lfloor \ell/2 \rfloor} {\ell \choose 2k} x^{2k}. $$
Let $x=1/2$. Then $x^2 = 1/4$.
$$ T_\ell = \sum_{k=0}^{\lfloor \ell/2 \rfloor} {\ell \choose 2k} \left(\frac{1}{2}\right)^{2k} = \frac{(1+1/2)^\ell + (1-1/2)^\ell}{2}. $$
$$ T_\ell = \frac{(3/2)^\ell + (1/2)^\ell}{2} = \frac{3^\ell/2^\ell + 1/2^\ell}{2} = \frac{(3^\ell+1)/2^\ell}{2} = \frac{3^\ell+1}{2^{\ell+1}}. $$
Now we compute $S_n$ by summing $T_\ell$ from $\ell=1$ to $n$:
$$ S_n = \sum_{\ell=1}^n T_\ell = \sum_{\ell=1}^n \frac{3^\ell+1}{2^{\ell+1}} = \frac{1}{2} \sum_{\ell=1}^n \left( \frac{3^\ell}{2^\ell} + \frac{1}{2^\ell} \right) = \frac{1}{2} \sum_{\ell=1}^n \left( \left(\frac{3}{2}\right)^\ell + \left(\frac{1}{2}\right)^\ell \right). $$
This sum consists of two geometric series. The sum of a finite geometric series is given by $\sum_{\ell=1}^n r^\ell = r \frac{1-r^n}{1-r}$.
For $r=3/2$:
$$ \sum_{\ell=1}^n \left(\frac{3}{2}\right)^\ell = \frac{3}{2} \frac{1 - (3/2)^n}{1 - 3/2} = \frac{3}{2} \frac{1 - 3^n/2^n}{-1/2} = -3 \left( \frac{2^n - 3^n}{2^n} \right) = 3 \frac{3^n - 2^n}{2^n}. $$
For $r=1/2$:
$$ \sum_{\ell=1}^n \left(\frac{1}{2}\right)^\ell = \frac{1}{2} \frac{1 - (1/2)^n}{1 - 1/2} = \frac{1}{2} \frac{1 - 1/2^n}{1/2} = 1 - \frac{1}{2^n} = \frac{2^n-1}{2^n}. $$
Substituting these results into the expression for $S_n$:
$$ S_n = \frac{1}{2} \left( 3 \frac{3^n - 2^n}{2^n} + \frac{2^n-1}{2^n} \right). $$
$$ S_n = \frac{1}{2} \frac{3 \cdot 3^n - 3 \cdot 2^n + 2^n - 1}{2^n} = \frac{1}{2} \frac{3^{n+1} - 2 \cdot 2^n - 1}{2^n}. $$
$$ S_n = \frac{3^{n+1} - 2^{n+1} - 1}{2 \cdot 2^n} = \frac{3^{n+1} - 2^{n+1} - 1}{2^{n+1}}. $$

Final Answer: The final answer is $\boxed{\frac{3^{n+1} - 2^{n+1} - 1}{2^{n+1}}}$