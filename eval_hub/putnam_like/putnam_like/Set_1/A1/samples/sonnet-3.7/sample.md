# Solution: Maximal Length of Consecutive Integers in $\mathcal{D}$

I'll show that the maximal length of a sequence of consecutive integers in $\mathcal{D}$ is 3.

## Step 1: Understanding the set $\mathcal{D}$

The set $\mathcal{D} = \{pq : p,q \in \mathbb{P}\}$ consists of products of two primes. These numbers are called semiprimes. The primes $p$ and $q$ may be equal (like $2^2 = 4$) or different (like $2 \cdot 3 = 6$).

## Step 2: Finding examples of consecutive integers in $\mathcal{D}$

Let's verify some examples of consecutive integers in $\mathcal{D}$:

- $33 = 3 \cdot 11$, $34 = 2 \cdot 17$, and $35 = 5 \cdot 7$ are three consecutive semiprimes.
- $85 = 5 \cdot 17$, $86 = 2 \cdot 43$, and $87 = 3 \cdot 29$ are three consecutive semiprimes.

So the maximal length is at least 3.

## Step 3: Proving there can't be 4 consecutive integers in $\mathcal{D}$

I'll prove that we cannot have 4 consecutive integers all belonging to $\mathcal{D}$.

In any sequence of 4 consecutive integers, exactly one of them is divisible by 4 (i.e., is a multiple of $2^2$).

Case 1: If that multiple of 4 is 4 itself, then our sequence must contain at least one of these sequences: $\{1,2,3,4\}$, $\{2,3,4,5\}$, $\{3,4,5,6\}$, or $\{4,5,6,7\}$. However, each of these contains at least one prime number (2, 3, 5, or 7), and prime numbers are not in $\mathcal{D}$ since they're not products of two primes.

Case 2: If the multiple of 4 is $4k$ where $k > 1$, then $4k = 2^2 \cdot k$. For this to be in $\mathcal{D}$, it must have exactly two prime factors. However:
- If $k$ is not a prime, then $4k$ has at least three prime factors.
- If $k$ is a prime, then $4k = 2 \cdot 2 \cdot k$ has three prime factors.

In either case, $4k$ (with $k > 1$) cannot be in $\mathcal{D}$.

Therefore, in any sequence of 4 consecutive integers, at least one is not in $\mathcal{D}$, which means the maximal length is at most 3.

Since we've found examples of 3 consecutive integers in $\mathcal{D}$ and proved that 4 consecutive integers is impossible, the answer is 3.