# Solution

I need to prove the existence of a subgroup $H$ of $G$ with order $p^n$ that is both abelian and normal.

## Step 1: Identify a candidate subgroup

Let $P$ be a Sylow $p$-subgroup of $G$, so $|P| = p^n$. I will show that $P$ is the desired subgroup $H$.

## Step 2: Prove that $P$ is normal in $G$

By Sylow's theorem, the number $n_p$ of Sylow $p$-subgroups in $G$ satisfies:
- $n_p$ divides $|G|/|P| = q^2$
- $n_p \equiv 1 \pmod{p}$

The possible values for $n_p$ are 1, $q$, and $q^2$.

If $n_p = q$, then $q \equiv 1 \pmod{p}$. Since $p > q$, this is impossible.

If $n_p = q^2$, then $q^2 \equiv 1 \pmod{p}$. This means $p$ divides $q^2 - 1 = (q-1)(q+1)$.

Since $p$ is prime, it divides either $q-1$ or $q+1$:
- If $p$ divides $q-1$, then $q \equiv 1 \pmod{p}$. Since $p > q$, this is impossible.
- If $p$ divides $q+1$, then $q \equiv -1 \pmod{p}$. Since $p > q > 2$, both $p$ and $q$ are odd primes. If $q \equiv -1 \pmod{p}$, we would need $q = p-1$, which is even and thus cannot be a prime greater than 2.

Therefore, $n_p = 1$, which means there is a unique Sylow $p$-subgroup in $G$. This implies that $P$ is normal in $G$.

## Step 3: Prove that $P$ is abelian

For any $a, b \in P$, I need to show that their commutator $[a,b] = a^{-1}b^{-1}ab = e$.

The commutator $[a,b]$ belongs to $[G,G]$ (by definition of the commutator subgroup).
Additionally, since $P$ is a subgroup and $a,b \in P$, we also have $[a,b] \in P$.

Therefore, $[a,b] \in [G,G] \cap P$. Given that:
- $|[G,G]| = q^2$ (a power of $q$)
- $|P| = p^n$ (a power of $p$)
- $p$ and $q$ are distinct primes

The intersection $[G,G] \cap P$ must be trivial (by Lagrange's theorem). Hence, $[a,b] = e$ for all $a,b \in P$, which means $P$ is abelian.

## Conclusion

The Sylow $p$-subgroup $P$ is a subgroup of $G$ of order $p^n$ that is both abelian and normal, thus satisfying our requirements for the subgroup $H$.