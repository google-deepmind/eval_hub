Solution:
Let the sequence be $(a_n)_{n=0}^{\infty}$ with $a_n > 0$ for all $n$ and $a_{n+1} \leq \frac{1}{2} a_n$ for all $n \geq 0$.
Define $b_n = a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3}$. We want to prove that $\sum_{n=1}^\infty nb_n = a_1 - a_2$.

First, let's establish the convergence of the series $\sum_{n=1}^\infty nb_n$.
The condition $a_{n+1} \leq \frac{1}{2} a_n$ implies $a_n \leq (\frac{1}{2}) a_{n-1} \leq (\frac{1}{2})^2 a_{n-2} \leq \dots \leq (\frac{1}{2})^n a_0$.
Since $a_n > 0$, we have $0 < a_n \leq (\frac{1}{2})^n a_0$. As $n \to \infty$, $(\frac{1}{2})^n a_0 \to 0$, so by the Squeeze Theorem, $a_n \to 0$.
Now consider the terms $nb_n$:
$|b_n| = |a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3}| \leq a_n + 3a_{n+1} + 3a_{n+2} + a_{n+3}$.
Using $a_{k+1} \leq \frac{1}{2} a_k$, we have $a_{n+1} \leq \frac{1}{2} a_n$, $a_{n+2} \leq \frac{1}{2} a_{n+1} \leq \frac{1}{4} a_n$, and $a_{n+3} \leq \frac{1}{2} a_{n+2} \leq \frac{1}{8} a_n$.
So, $|b_n| \leq a_n + 3(\frac{1}{2} a_n) + 3(\frac{1}{4} a_n) + (\frac{1}{8} a_n) = (1 + \frac{3}{2} + \frac{3}{4} + \frac{1}{8}) a_n = \frac{8+12+6+1}{8} a_n = \frac{27}{8} a_n$.
Then $|nb_n| \leq \frac{27}{8} n a_n \leq \frac{27}{8} n (\frac{1}{2})^n a_0$.
The series $\sum_{n=1}^\infty n (\frac{1}{2})^n$ converges (this can be shown using the ratio test: $\lim_{n\to\infty} \frac{(n+1)(1/2)^{n+1}}{n(1/2)^n} = \lim_{n\to\infty} \frac{n+1}{2n} = \frac{1}{2} < 1$).
By the comparison test, the series $\sum_{n=1}^\infty nb_n$ converges absolutely.

Let $S = \sum_{n=1}^\infty nb_n$. Since the series converges absolutely, we can rearrange the terms.
$S = \sum_{n=1}^\infty n (a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3})$
$S = \sum_{n=1}^\infty n a_n - 3 \sum_{n=1}^\infty n a_{n+1} + 3 \sum_{n=1}^\infty n a_{n+2} - \sum_{n=1}^\infty n a_{n+3}$.

We perform index shifts on the sums.
Let $k=n+1$ in the second sum. $n=k-1$. When $n=1$, $k=2$. As $n\to\infty$, $k\to\infty$.
$ \sum_{n=1}^\infty n a_{n+1} = \sum_{k=2}^\infty (k-1) a_k $. We can rename the index $k$ back to $n$. So, $\sum_{n=2}^\infty (n-1) a_n$.
Let $k=n+2$ in the third sum. $n=k-2$. When $n=1$, $k=3$. As $n\to\infty$, $k\to\infty$.
$ \sum_{n=1}^\infty n a_{n+2} = \sum_{k=3}^\infty (k-2) a_k = \sum_{n=3}^\infty (n-2) a_n$.
Let $k=n+3$ in the fourth sum. $n=k-3$. When $n=1$, $k=4$. As $n\to\infty$, $k\to\infty$.
$ \sum_{n=1}^\infty n a_{n+3} = \sum_{k=4}^\infty (k-3) a_k = \sum_{n=4}^\infty (n-3) a_n$.

Substitute these back into the expression for $S$:
$S = \sum_{n=1}^\infty n a_n - 3 \sum_{n=2}^\infty (n-1) a_n + 3 \sum_{n=3}^\infty (n-2) a_n - \sum_{n=4}^\infty (n-3) a_n$.

Let's determine the coefficient for each term $a_n$ in the sum $S$.
For $n=1$: $a_1$ appears only in the first sum $\sum_{n=1}^\infty n a_n$ with $n=1$. The coefficient is $1$.
For $n=2$: $a_2$ appears in the first sum (with $n=2$) and the second sum (with $n=2$). The coefficient is $2 - 3(2-1) = 2 - 3(1) = -1$.
For $n=3$: $a_3$ appears in the first sum (with $n=3$), the second sum (with $n=3$), and the third sum (with $n=3$). The coefficient is $3 - 3(3-1) + 3(3-2) = 3 - 3(2) + 3(1) = 3 - 6 + 3 = 0$.
For $n \geq 4$: $a_n$ appears in all four sums. The coefficient is:
$n - 3(n-1) + 3(n-2) - (n-3)$
$= n - (3n - 3) + (3n - 6) - (n - 3)$
$= n - 3n + 3 + 3n - 6 - n + 3$
$= (1 - 3 + 3 - 1)n + (3 - 6 + 3)$
$= 0 \cdot n + 0 = 0$.

So, the coefficients for $a_n$ are zero for all $n \geq 3$. The sum simplifies to:
$S = 1 \cdot a_1 + (-1) \cdot a_2 + 0 \cdot a_3 + 0 \cdot a_4 + \dots$
$S = a_1 - a_2$.

Alternative approach using partial sums:
Let $S_N = \sum_{n=1}^N n b_n = \sum_{n=1}^N n (a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3})$.
$S_N = \sum_{n=1}^N n a_n - 3 \sum_{n=1}^N n a_{n+1} + 3 \sum_{n=1}^N n a_{n+2} - \sum_{n=1}^N n a_{n+3}$.
Change indices as before:
$S_N = \sum_{n=1}^N n a_n - 3 \sum_{k=2}^{N+1} (k-1) a_k + 3 \sum_{k=3}^{N+2} (k-2) a_k - \sum_{k=4}^{N+3} (k-3) a_k$.
We collect the coefficients for $a_k$ for $k=1, \dots, N+3$.
For $k=1$: $1 \cdot a_1$. Coefficient is $1$.
For $k=2$: $2 a_2 - 3(2-1)a_2 = 2a_2 - 3a_2 = -a_2$. Coefficient is $-1$.
For $k=3$: $3 a_3 - 3(3-1)a_3 + 3(3-2)a_3 = 3a_3 - 6a_3 + 3a_3 = 0$. Coefficient is $0$.
For $4 \leq k \leq N$: $k a_k - 3(k-1)a_k + 3(k-2)a_k - (k-3)a_k = (k - 3k + 3 + 3k - 6 - k + 3) a_k = 0$. Coefficient is $0$.
The terms collected so far sum to $a_1 - a_2$.

The remaining terms involve indices $k = N+1, N+2, N+3$.
Coefficient of $a_{N+1}$: from the second sum $-3(N+1-1)a_{N+1} = -3N a_{N+1}$, from the third sum $3(N+1-2)a_{N+1} = 3(N-1) a_{N+1}$, from the fourth sum $-(N+1-3)a_{N+1} = -(N-2) a_{N+1}$.
Total coefficient is $-3N + 3(N-1) - (N-2) = -3N + 3N - 3 - N + 2 = -N - 1$.
Coefficient of $a_{N+2}$: from the third sum $3(N+2-2)a_{N+2} = 3N a_{N+2}$, from the fourth sum $-(N+2-3)a_{N+2} = -(N-1) a_{N+2}$.
Total coefficient is $3N - (N-1) = 2N + 1$.
Coefficient of $a_{N+3}$: from the fourth sum $-(N+3-3)a_{N+3} = -N a_{N+3}$.
Total coefficient is $-N$.

So, $S_N = a_1 - a_2 - (N+1)a_{N+1} + (2N+1)a_{N+2} - N a_{N+3}$.
Let $T_N = -(N+1)a_{N+1} + (2N+1)a_{N+2} - N a_{N+3}$. We want to show $\lim_{N\to\infty} T_N = 0$.
We have $a_n \leq (\frac{1}{2})^n a_0$.
$|T_N| \leq (N+1)a_{N+1} + (2N+1)a_{N+2} + N a_{N+3}$
$ \leq (N+1) (\frac{1}{2})^{N+1} a_0 + (2N+1) (\frac{1}{2})^{N+2} a_0 + N (\frac{1}{2})^{N+3} a_0$
$ = a_0 \frac{1}{2^{N+3}} [ 4(N+1) + 2(2N+1) + N ]$
$ = a_0 \frac{1}{2^{N+3}} [ 4N+4 + 4N+2 + N ]$
$ = a_0 \frac{9N+6}{2^{N+3}}$.
Since $\lim_{N\to\infty} \frac{P(N)}{x^N} = 0$ for any polynomial $P(N)$ and $x > 1$, we have $\lim_{N\to\infty} \frac{9N+6}{2^{N+3}} = 0$.
Therefore, $\lim_{N\to\infty} T_N = 0$.
So, $\lim_{N\to\infty} S_N = a_1 - a_2$.

Final result: $\sum_{n=1}^\infty nb_n = a_1 - a_2$.

Final Answer: The final answer is $\boxed{a_1-a_2}$