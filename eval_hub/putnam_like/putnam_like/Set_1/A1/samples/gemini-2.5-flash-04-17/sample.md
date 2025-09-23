Let $\mathbb{P}$ denote the set of prime numbers. The set $\mathcal{D}$ is defined as
$$ \mathcal{D} := \{ pq \ : \ p,q \in \mathbb{P} \}. $$
We are looking for the maximal length $L$ of a sequence of consecutive integers $n, n+1, \dots, n+L-1$ such that all elements of the sequence are in $\mathcal{D}$.

The elements of $\mathcal{D}$ are integers that are products of two prime factors, counted with multiplicity. These are also known as 2-almost primes. For example, $4 = 2 \times 2 \in \mathcal{D}$, $6 = 2 \times 3 \in \mathcal{D}$, $9 = 3 \times 3 \in \mathcal{D}$, $10 = 2 \times 5 \in \mathcal{D}$, etc. Prime numbers $p$ are not in $\mathcal{D}$ because if $p = pq$ for $p,q \in \mathbb{P}$, then $q$ must be 1, and 1 is not a prime number.

Consider any integer $m$ that is a multiple of 4. So $m=4k$ for some integer $k \ge 1$.
If $m \in \mathcal{D}$, then $m = pq$ for some primes $p,q \in \mathbb{P}$.
Since $m=4k$, $m$ is even, so at least one of the prime factors $p$ or $q$ must be 2. Let $p=2$.
Then $m = 2q$. Since $m$ is a multiple of 4, $m=4k$, so $4k = 2q$, which simplifies to $2k=q$.
For $q$ to be a prime number, $2k$ must be a prime number. The only prime number that is twice an integer is 2 itself (when $k=1$). So $q=2$ and $k=1$.
This means $m = 4 \times 1 = 4$.
So, if an integer $m$ is a multiple of 4 and $m \in \mathcal{D}$, then $m$ must be equal to 4.

Now consider a sequence of $L$ consecutive integers: $n, n+1, \dots, n+L-1$.
If $L \ge 4$, this sequence must contain a multiple of 4. This is because in any four consecutive integers, exactly one is divisible by 4. Let this multiple of 4 be $m$.
If all integers in the sequence $n, n+1, \dots, n+L-1$ are in $\mathcal{D}$, then $m$ must also be in $\mathcal{D}$.
According to the argument above, if $m \in \mathcal{D}$ and $m$ is a multiple of 4, then $m$ must be equal to 4.
So, any sequence of $L \ge 4$ consecutive integers consisting entirely of elements from $\mathcal{D}$ must contain the number 4.

Let's examine sequences of length 4 that contain the number 4. A sequence of 4 consecutive integers is of the form $k, k+1, k+2, k+3$. For this sequence to contain 4, one of its elements must be 4.
There are four such sequences:
1. $1, 2, 3, 4$: $1$ is not in $\mathcal{D}$. $2, 3$ are primes, so not in $\mathcal{D}$. $4=2^2 \in \mathcal{D}$. This sequence is not entirely in $\mathcal{D}$.
2. $2, 3, 4, 5$: $2, 3, 5$ are primes, so not in $\mathcal{D}$. $4=2^2 \in \mathcal{D}$. This sequence is not entirely in $\mathcal{D}$.
3. $3, 4, 5, 6$: $3, 5$ are primes, so not in $\mathcal{D}$. $4=2^2 \in \mathcal{D}$, $6=2 \times 3 \in \mathcal{D}$. This sequence is not entirely in $\mathcal{D}$.
4. $4, 5, 6, 7$: $5, 7$ are primes, so not in $\mathcal{D}$. $4=2^2 \in \mathcal{D}$, $6=2 \times 3 \in \mathcal{D}$. This sequence is not entirely in $\mathcal{D}$.

Since none of the sequences of length 4 containing 4 consist entirely of elements from $\mathcal{D}$, there is no sequence of 4 consecutive integers in $\mathcal{D}$.
This means the maximal length $L$ must be less than 4, i.e., $L \le 3$.

Now we need to check if there exists a sequence of length 3 in $\mathcal{D}$.
Let's test small numbers:
$4, 5, 6$: $4 \in \mathcal{D}$, $5 \notin \mathcal{D}$, $6 \in \mathcal{D}$. No.
$6, 7, 8$: $6 \in \mathcal{D}$, $7 \notin \mathcal{D}$, $8=2^3 \notin \mathcal{D}$. No.
$14, 15, 16$: $14=2 \times 7 \in \mathcal{D}$, $15=3 \times 5 \in \mathcal{D}$, $16=2^4 \notin \mathcal{D}$. No.
$33, 34, 35$: $33 = 3 \times 11$. $3, 11 \in \mathbb{P}$, so $33 \in \mathcal{D}$.
$34 = 2 \times 17$. $2, 17 \in \mathbb{P}$, so $34 \in \mathcal{D}$.
$35 = 5 \times 7$. $5, 7 \in \mathbb{P}$, so $35 \in \mathcal{D}$.
The sequence $33, 34, 35$ is a sequence of 3 consecutive integers, and all three are in $\mathcal{D}$.
This shows that there exists a sequence of length 3 in $\mathcal{D}$. Thus, the maximal length $L$ must be at least 3, i.e., $L \ge 3$.

Combining the results $L \le 3$ and $L \ge 3$, we conclude that the maximal length is 3.

The final answer is $\boxed{3}$.