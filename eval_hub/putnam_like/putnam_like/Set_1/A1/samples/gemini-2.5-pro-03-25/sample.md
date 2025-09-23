Let $\mathbb{P}$ denote the set of all prime numbers. The set $\mathcal{D}$ is defined as
$$
\mathcal{D} := \{ pq \ : \ p,q \in \mathbb{P} \}.
$$
This means $\mathcal{D}$ is the set of integers that are the product of exactly two primes, counting multiplicity. Such numbers are often called semiprimes. The set $\mathcal{D}$ includes squares of primes, such as $4=2^2$, $9=3^2$, $25=5^2$, etc.

We are looking for the maximal length $k$ of a sequence of consecutive integers $n, n+1, \dots, n+k-1$ such that all integers in the sequence belong to $\mathcal{D}$.

Let's list the first few elements of $\mathcal{D}$:
$4 = 2^2$
$6 = 2 \times 3$
$9 = 3^2$
$10 = 2 \times 5$
$14 = 2 \times 7$
$15 = 3 \times 5$
$21 = 3 \times 7$
$22 = 2 \times 11$
$25 = 5^2$
$26 = 2 \times 13$
$33 = 3 \times 11$
$34 = 2 \times 17$
$35 = 5 \times 7$

We can observe some sequences of consecutive integers in $\mathcal{D}$.
- $(14, 15)$: length 2. $14=2 \times 7$, $15=3 \times 5$.
- $(21, 22)$: length 2. $21=3 \times 7$, $22=2 \times 11$.
- $(33, 34, 35)$: length 3. $33=3 \times 11$, $34=2 \times 17$, $35=5 \times 7$.
- $(85, 86, 87)$: length 3. $85=5 \times 17$, $86=2 \times 43$, $87=3 \times 29$.
- $(93, 94, 95)$: length 3. $93=3 \times 31$, $94=2 \times 47$, $95=5 \times 19$.

We have found sequences of length 3. This implies that the maximal length $k$ must be at least 3. $k \ge 3$.

Now let's consider if a sequence of length 4 is possible. Let $(n, n+1, n+2, n+3)$ be a sequence of 4 consecutive integers such that all of them are in $\mathcal{D}$.
In any sequence of 4 consecutive integers, exactly one of them must be divisible by 4. Let this integer be $m$.
Since $m$ must be in $\mathcal{D}$, $m$ must be of the form $pq$ for some primes $p$ and $q$.
We have $4 \mid m$, so $4 \mid pq$.
Let's consider the prime factorization of $m = pq$.
If $p=2$, then $m = 2q$. Since $4 \mid 2q$, this implies $2 \mid q$. As $q$ is prime, we must have $q=2$. Therefore, $m = 2 \times 2 = 4$.
If $p$ is an odd prime, then $p \ne 2$. Since $4 \mid pq$, and $p$ has no factors of 2, $q$ must contain the factor $2^2=4$. But $q$ is prime, so this is impossible unless $q=2$. If $q=2$, then $m=2p$. Since $4 \mid 2p$, we must have $2 \mid p$. As $p$ is prime, $p=2$. This contradicts the assumption that $p$ is odd.
If both $p$ and $q$ are odd primes, then their product $pq$ is odd. But $m$ is divisible by 4, so $m$ must be even. This is a contradiction.

The only possibility is $m=4$.
So, any sequence of 4 consecutive integers, all belonging to $\mathcal{D}$, must contain the number 4.
Let's examine all possible sequences of length 4 that contain 4:
1. $(1, 2, 3, 4)$: The integers 1, 2, 3 are not in $\mathcal{D}$. $1$ is not a product of two primes. $2$ and $3$ are prime numbers, so they are products of only one prime.
2. $(2, 3, 4, 5)$: The integers 2, 3, 5 are not in $\mathcal{D}$.
3. $(3, 4, 5, 6)$: The integers 3, 5 are not in $\mathcal{D}$. $4 = 2^2 \in \mathcal{D}$ and $6 = 2 \times 3 \in \mathcal{D}$.
4. $(4, 5, 6, 7)$: The integers 5, 7 are not in $\mathcal{D}$. $4 = 2^2 \in \mathcal{D}$ and $6 = 2 \times 3 \in \mathcal{D}$.

None of these sequences consist entirely of integers from $\mathcal{D}$.
Therefore, there cannot be a sequence of length 4. The maximal length $k$ must be strictly less than 4. $k < 4$.

Since we know $k \ge 3$ and $k < 4$, the maximal length $k$ must be 3.

Final check:
We established that the maximal length $k$ satisfies $k \le 3$.
We provided examples of sequences of length 3, such as (33, 34, 35).
$33 = 3 \times 11$. Both 3 and 11 are primes. $33 \in \mathcal{D}$.
$34 = 2 \times 17$. Both 2 and 17 are primes. $34 \in \mathcal{D}$.
$35 = 5 \times 7$. Both 5 and 7 are primes. $35 \in \mathcal{D}$.
Thus, a sequence of length 3 exists.

The maximal length of a sequence of consecutive integers in $\mathcal{D}$ is 3.

Final Answer: The final answer is $\boxed{3}$