Let $B_j$ denote the contents of box $j$ for $j=1, \dots, n$.
According to the problem statement, initially, each box $j$ contains $k$ balls with the number $k$ for each $k \in \{1, 2, \dots, m\}$.
Let $N_{j,k}$ be the number of balls with the number $k$ in box $j$. Initially, for any $j \in \{1, \dots, n\}$, $N_{j,k}^{(0)} = k$ for $k=1, \dots, m$.
The total number of balls in each box initially is $N = \sum_{k=1}^m k = \frac{m(m+1)}{2}$.

Let $X_j$ be the random variable representing the number on the ball drawn from box $j$.
The process consists of $n$ steps:
1. Draw a ball from box 1. Its number is $X_1$. Put this ball into box 2.
2. Draw a ball from box 2. Its number is $X_2$. Put this ball into box 3.
...
j. Draw a ball from box $j$. Its number is $X_j$. Put this ball into box $j+1$ (if $j<n$).
...
n. Draw a ball from box $n$. Its number is $X_n$. Record this number.

We want to find the expected value $E[X_n]$. Let $E_j = E[X_j]$.

First, let's calculate $E_1$. The balls in box 1 are $\{k^k\}_{k=1}^m$. Total number of balls is $N$.
The probability of drawing a ball with number $k$ is $P(X_1 = k) = \frac{N_{1,k}^{(0)}}{N} = \frac{k}{N}$.
$E_1 = \sum_{k=1}^m k P(X_1 = k) = \sum_{k=1}^m k \frac{k}{N} = \frac{1}{N} \sum_{k=1}^m k^2$.
Let $S_2 = \sum_{k=1}^m k^2$. We know $S_2 = \frac{m(m+1)(2m+1)}{6}$.
$E_1 = \frac{S_2}{N} = \frac{m(m+1)(2m+1)/6}{m(m+1)/2} = \frac{2m+1}{3}$.

Now, let's consider the step from box $j$ to box $j+1$.
Suppose we have drawn $X_j$ from box $j$ and put it into box $j+1$.
Box $j+1$ initially contains $N$ balls $\{k^k\}_{k=1}^m$. After adding the ball with number $X_j$, box $j+1$ contains $N+1$ balls.
Let's compute $E[X_{j+1} | X_j=k_j]$ for a fixed value $k_j$ of $X_j$.
When $X_j = k_j$, box $j+1$ contains $k$ balls of number $k$ for $k \neq k_j$, and $k_j+1$ balls of number $k_j$. Total $N+1$ balls.
The probability of drawing a ball with number $k$ from box $j+1$, given $X_j=k_j$, is:
$P(X_{j+1}=k | X_j=k_j) = \begin{cases} \frac{k}{N+1} & \text{if } k \neq k_j \\ \frac{k_j+1}{N+1} & \text{if } k = k_j \end{cases}$.
The conditional expectation is:
$E[X_{j+1} | X_j=k_j] = \sum_{k=1}^m k P(X_{j+1}=k | X_j=k_j)$
$E[X_{j+1} | X_j=k_j] = \sum_{k \neq k_j} k \frac{k}{N+1} + k_j \frac{k_j+1}{N+1}$
$E[X_{j+1} | X_j=k_j] = \frac{1}{N+1} \left( \sum_{k \neq k_j} k^2 + k_j(k_j+1) \right)$
$E[X_{j+1} | X_j=k_j] = \frac{1}{N+1} \left( \sum_{k \neq k_j} k^2 + k_j^2 + k_j \right)$
$E[X_{j+1} | X_j=k_j] = \frac{1}{N+1} \left( \sum_{k=1}^m k^2 + k_j \right) = \frac{S_2 + k_j}{N+1}$.

Now we use the Law of Total Expectation to find $E_{j+1}$:
$E_{j+1} = E[X_{j+1}] = E[E[X_{j+1} | X_j]]$
$E_{j+1} = E\left[ \frac{S_2 + X_j}{N+1} \right]$.
Since expectation is linear:
$E_{j+1} = \frac{1}{N+1} E[S_2 + X_j] = \frac{1}{N+1} (S_2 + E[X_j]) = \frac{S_2 + E_j}{N+1}$.

We have a recurrence relation $E_{j+1} = \frac{S_2 + E_j}{N+1}$ for $j \ge 1$.
Let's check if $E_j$ is constant. We know $E_1 = S_2/N$.
$E_2 = \frac{S_2 + E_1}{N+1} = \frac{S_2 + S_2/N}{N+1} = \frac{S_2(1 + 1/N)}{N+1} = \frac{S_2((N+1)/N)}{N+1} = \frac{S_2}{N}$.
So $E_2 = E_1$.
Let's assume $E_j = S_2/N$ for some $j \ge 1$. Then $E_{j+1} = \frac{S_2 + E_j}{N+1} = \frac{S_2 + S_2/N}{N+1} = \frac{S_2}{N}$.
By induction, $E_j = S_2/N$ for all $j=1, \dots, n$.
Therefore, $E[X_n] = E_n = \frac{S_2}{N}$.

We already calculated $E_1 = S_2/N = \frac{2m+1}{3}$.
So, $E[X_n] = \frac{2m+1}{3}$.

The problem asks for which positive integers $m$ the expected value $E[X_n]$ is an integer.
We need $\frac{2m+1}{3}$ to be an integer. This means that $2m+1$ must be divisible by 3.
$2m+1 \equiv 0 \pmod 3$.
$2m \equiv -1 \pmod 3$.
Since $-1 \equiv 2 \pmod 3$, we have $2m \equiv 2 \pmod 3$.
Since $\gcd(2, 3) = 1$, we can divide both sides by 2:
$m \equiv 1 \pmod 3$.

So, the expected value $E[X_n]$ is an integer if and only if $m$ is a positive integer such that $m \equiv 1 \pmod 3$.
The set of such integers $m$ is $\{1, 4, 7, 10, \dots\}$. This can be written as the set $\{ m \in \mathbb{Z}^+ \mid m = 3k+1 \text{ for some integer } k \ge 0 \}$.

Final Answer: The final answer is $\boxed{m \equiv 1 \pmod 3}$