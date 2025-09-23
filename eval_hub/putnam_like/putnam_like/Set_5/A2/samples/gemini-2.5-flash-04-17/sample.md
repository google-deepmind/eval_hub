Let $S_N = \sum_{n=1}^N nb_n$. Substituting the definition of $b_n$, we have
$$S_N = \sum_{n=1}^N n(a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3})$$
We can split this sum into four separate sums:
$$S_N = \sum_{n=1}^N n a_n - 3\sum_{n=1}^N n a_{n+1} + 3\sum_{n=1}^N n a_{n+2} - \sum_{n=1}^N n a_{n+3}$$
Let's re-index each sum so that the general term is $a_k$:
\begin{align*} \label{eq:1}\sum_{n=1}^N n a_n &= \sum_{k=1}^N k a_k \\ -3\sum_{n=1}^N n a_{n+1} &= -3\sum_{k=2}^{N+1} (k-1) a_k \quad &(\text{let } k=n+1, \text{ so } n=k-1) \\ 3\sum_{n=1}^N n a_{n+2} &= 3\sum_{k=3}^{N+2} (k-2) a_k \quad &(\text{let } k=n+2, \text{ so } n=k-2) \\ -\sum_{n=1}^N n a_{n+3} &= -\sum_{k=4}^{N+3} (k-3) a_k \quad &(\text{let } k=n+3, \text{ so } n=k-3)\end{align*}
Combining these sums, $S_N$ can be written as $\sum_{k=1}^{N+3} c_k a_k$ for some coefficients $c_k$. Let's find these coefficients:
For $k=1$: $c_1 = 1$ (from the first sum).
For $k=2$: $c_2 = 2$ (from the first sum) $-3(2-1)$ (from the second sum) $= 2 - 3 = -1$.
For $k=3$: $c_3 = 3$ (from the first) $-3(3-1)$ (from the second) $+3(3-2)$ (from the third) $= 3 - 6 + 3 = 0$.
For $4 \leq k \leq N$: $a_k$ appears in all four sums. The coefficient is $k - 3(k-1) + 3(k-2) - (k-3) = k - 3k + 3 + 3k - 6 - k + 3 = (k-3k+3k-k) + (3-6+3) = 0$.

So, terms $a_k$ for $3 \leq k \leq N$ have a coefficient of 0. $S_N$ simplifies to:
$$S_N = a_1 - a_2 + \sum_{k=N+1}^{N+3} c_k a_k$$
Now we compute the coefficients for $k=N+1, N+2, N+3$.
For $k=N+1$: $a_{N+1}$ appears in sums 2, 3, and 4 (if $N+1 \geq 4$).
$c_{N+1} = -3((N+1)-1) + 3((N+1)-2) - ((N+1)-3) = -3N + 3(N-1) - (N-2) = -3N + 3N - 3 - N + 2 = -N-1$.
For $k=N+2$: $a_{N+2}$ appears in sums 3 and 4 (if $N+2 \geq 4$).
$c_{N+2} = 3((N+2)-2) - ((N+2)-3) = 3N - (N-1) = 3N - N + 1 = 2N+1$.
For $k=N+3$: $a_{N+3}$ appears only in sum 4 (if $N+3 \geq 4$).
$c_{N+3} = -((N+3)-3) = -N$.

So, the partial sum is
$$S_N = a_1 - a_2 + (-N-1)a_{N+1} + (2N+1)a_{N+2} - Na_{N+3}$$
To find the value of the infinite sum $\sum_{n=1}^\infty nb_n$, we take the limit as $N \to \infty$:
$$\sum_{n=1}^\infty nb_n = \lim_{N\to\infty} S_N = a_1 - a_2 + \lim_{N\to\infty} [(-N-1)a_{N+1} + (2N+1)a_{N+2} - Na_{N+3}]$$
We need to evaluate the limit of the terms involving $N$. We are given $a_{n+1} \leq \frac{1}{2}a_n$ for all $n \geq 0$. Since $a_n > 0$, this implies $0 < a_n \leq (\frac{1}{2})^n a_0$ for all $n \geq 0$.
Consider the terms:
1. $\lim_{N\to\infty} (N+1)a_{N+1}$:
Since $a_{N+1} \leq (\frac{1}{2})^{N+1} a_0$, we have $0 < (N+1)a_{N+1} \leq (N+1)(\frac{1}{2})^{N+1} a_0$.
The limit $\lim_{N\to\infty} (N+1)(\frac{1}{2})^{N+1} = 0$ because exponential decay dominates polynomial growth. Thus, $\lim_{N\to\infty} (N+1)a_{N+1} = 0$.

2. $\lim_{N\to\infty} (2N+1)a_{N+2}$:
$0 < (2N+1)a_{N+2} \leq (2N+1)(\frac{1}{2})^{N+2} a_0$.
$\lim_{N\to\infty} (2N+1)(\frac{1}{2})^{N+2} = \lim_{N\to\infty} \frac{2N+1}{4 \cdot 2^N} = \frac{1}{4} \lim_{N\to\infty} \frac{2N+1}{2^N}$. By L'Hopital's rule, $\lim_{N\to\infty} \frac{2}{2^N \ln 2} = 0$. Thus, $\lim_{N\to\infty} (2N+1)a_{N+2} = 0$.

3. $\lim_{N\to\infty} Na_{N+3}$:
$0 < Na_{N+3} \leq N(\frac{1}{2})^{N+3} a_0$.
$\lim_{N\to\infty} N(\frac{1}{2})^{N+3} = \lim_{N\to\infty} \frac{N}{8 \cdot 2^N} = \frac{1}{8} \lim_{N\to\infty} \frac{N}{2^N}$. By L'Hopital's rule, $\lim_{N\to\infty} \frac{1}{2^N \ln 2} = 0$. Thus, $\lim_{N\to\infty} Na_{N+3} = 0$.

Since $\lim_{N\to\infty} (N+1)a_{N+1}=0$, $\lim_{N\to\infty} (2N+1)a_{N+2}=0$, and $\lim_{N\to\infty} Na_{N+3}=0$, we have:
$$\lim_{N\to\infty} [(-N-1)a_{N+1} + (2N+1)a_{N+2} - Na_{N+3}] = 0 + 0 - 0 = 0$$
Therefore,
$$\sum_{n=1}^\infty nb_n = a_1 - a_2 + 0 = a_1 - a_2$$

The final answer is $\boxed{\sum_{n=1}^\infty nb_n =a_1-a_2}$.