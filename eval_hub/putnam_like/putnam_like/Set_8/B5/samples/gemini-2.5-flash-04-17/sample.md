Let $N_0$ be the initial number of balls in each box.
The balls in each box $i$ ($1 \le i \le n$) are $k$ balls with number $k$ for $k=1, 2, \ldots, m$.
The total number of balls initially in each box is $N_0 = \sum_{k=1}^m k = \frac{m(m+1)}{2}$.

Let $X_i$ be the number on the ball drawn from box $i$. We are interested in $E[X_n]$.
Let $C_{i,k}$ be the number of balls with number $k$ in box $i$ just before drawing a ball from it.
The total number of balls in box $i$ just before drawing is $N_i = \sum_{k=1}^m C_{i,k}$.

For box 1, the counts are deterministic: $C_{1,k} = k$ for $k=1, \ldots, m$.
$N_1 = \sum_{k=1}^m k = N_0$.
The probability of drawing a ball with number $k$ from box 1 is $P(X_1=k) = \frac{C_{1,k}}{N_1} = \frac{k}{N_0}$.
The expected value of $X_1$ is $E[X_1] = \sum_{k=1}^m k P(X_1=k) = \sum_{k=1}^m k \frac{k}{N_0} = \frac{1}{N_0} \sum_{k=1}^m k^2$.
Let $S_2 = \sum_{k=1}^m k^2 = \frac{m(m+1)(2m+1)}{6}$.
$E[X_1] = \frac{S_2}{N_0} = \frac{m(m+1)(2m+1)/6}{m(m+1)/2} = \frac{m(m+1)(2m+1)}{6} \cdot \frac{2}{m(m+1)} = \frac{2m+1}{3}$.

Now consider box $i$ for $i \ge 2$. Box $i$ initially contains $k$ balls of number $k$ for each $k$. Then, the ball $X_{i-1}$ drawn from box $i-1$ is added to box $i$.
So, the number of balls of type $k$ in box $i$ just before drawing $X_i$ is $C_{i,k} = k + \mathbb{I}(X_{i-1}=k)$, where $\mathbb{I}(X_{i-1}=k)$ is an indicator variable which is 1 if $X_{i-1}=k$ and 0 otherwise.
The total number of balls in box $i$ for $i \ge 2$ is $N_i = N_0 + 1$. This is because we add one ball to the initial $N_0$ balls.
The expected number of balls of type $k$ in box $i$ before drawing $X_i$ is $E[C_{i,k}] = E[k + \mathbb{I}(X_{i-1}=k)] = k + E[\mathbb{I}(X_{i-1}=k)] = k + P(X_{i-1}=k)$.

The expected value of $X_i$ is $E[X_i] = E\left[\sum_{k=1}^m k \frac{C_{i,k}}{N_i}\right]$.
For $i \ge 2$, $N_i=N_0+1$, which is not a random variable.
$E[X_i] = \frac{1}{N_0+1} E\left[\sum_{k=1}^m k C_{i,k}\right] = \frac{1}{N_0+1} \sum_{k=1}^m k E[C_{i,k}]$.
Substituting $E[C_{i,k}] = k + P(X_{i-1}=k)$:
$E[X_i] = \frac{1}{N_0+1} \sum_{k=1}^m k (k + P(X_{i-1}=k)) = \frac{1}{N_0+1} \left(\sum_{k=1}^m k^2 + \sum_{k=1}^m k P(X_{i-1}=k)\right)$.
The first sum is $S_2$. The second sum is the definition of the expected value of $X_{i-1}$, $E[X_{i-1}]$.
So, for $i \ge 2$, we have the recurrence relation $E[X_i] = \frac{S_2 + E[X_{i-1}]}{N_0+1}$.

Let $E_i = E[X_i]$. We have $E_i = \frac{S_2}{N_0+1} + \frac{1}{N_0+1} E_{i-1}$ for $i \ge 2$, and $E_1 = \frac{S_2}{N_0}$.
This is a linear recurrence relation $E_i = a + b E_{i-1}$ with $a = \frac{S_2}{N_0+1}$ and $b = \frac{1}{N_0+1}$.
The fixed point of this recurrence is $E$ such that $E = a + bE$, which gives $E(1-b)=a$, so $E = \frac{a}{1-b}$.
$E = \frac{S_2/(N_0+1)}{1 - 1/(N_0+1)} = \frac{S_2/(N_0+1)}{N_0/(N_0+1)} = \frac{S_2}{N_0}$.
Since the initial value $E_1 = S_2/N_0$ is equal to the fixed point, the sequence $E_i$ is constant: $E_i = S_2/N_0$ for all $i=1, \ldots, n$.
This means $E[X_n] = S_2/N_0 = \frac{2m+1}{3}$.

We are given that $m$ is a positive integer, and we want $E[X_n]$ to be an integer.
Thus, $\frac{2m+1}{3}$ must be an integer.
This requires $2m+1$ to be divisible by 3.
$2m+1 \equiv 0 \pmod 3$.
$2m \equiv -1 \pmod 3$.
$2m \equiv 2 \pmod 3$.
Since $\gcd(2, 3)=1$, we can divide by 2:
$m \equiv 1 \pmod 3$.

Since $m$ is a positive integer, $m$ must be of the form $3k+1$ for some integer $k \ge 0$.
The possible values for $m$ are $1, 4, 7, 10, \ldots$.

The final answer is $\boxed{m \equiv 1 \pmod 3}$.