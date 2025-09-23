```markdown
We are given a finite group 
\[
G
\]
of order
\[
|G| = p^n q^2,
\]
where 
\[
p > q > 2
\]
are primes and \( n \ge 1 \). Moreover, the commutator subgroup (or derived subgroup) 
\[
[G, G]
\]
has order 
\[
q^2.
\]

Our goal is to show that there exists a subgroup \( H \) of \( G \) of order \( p^n \) which is both abelian and normal.

### Step 1. Show that the Sylow \( p \)-subgroup is unique and normal

Let \( H \) be a Sylow \( p \)-subgroup of \( G \). By Sylow's theorems, the number \( n_p \) of Sylow \( p \)-subgroups satisfies:
- \( n_p \equiv 1 \ (\text{mod } p) \),
- \( n_p \) divides \( q^2 \).

Since the divisors of \( q^2 \) are \(1\), \(q\), and \(q^2\), we have the possibilities
\[
n_p \in \{1, \; q, \; q^2\}.
\]
However, if \( n_p = q \) or \( n_p = q^2 \), then
\[
q \equiv 1 \ (\text{mod } p) \quad \text{or} \quad q^2 \equiv 1 \ (\text{mod } p),
\]
which is impossible because \( p > q \) (and if \( q \) is a prime greater than 2, these congruences cannot hold). Therefore, the only possibility is
\[
n_p = 1.
\]
Hence, \( H \) is the unique Sylow \( p \)-subgroup of \( G \) and must be normal:
\[
H \trianglelefteq G.
\]

### Step 2. Show that \( H \) is abelian

Since \( [G,G] \) is the commutator subgroup of \( G \), the quotient group
\[
G/[G,G]
\]
is abelian. The given order of \( [G,G] \) is \( q^2 \), so by Lagrange’s theorem, the order of the abelianization is
\[
|G/[G,G]| = \frac{|G|}{|[G,G]|} = \frac{p^n q^2}{q^2} = p^n.
\]

Now, consider the restriction of the natural projection 
\[
\pi : G \to G/[G,G]
\]
to the subgroup \( H \). Since
\[
|H| = p^n \quad \text{and} \quad |G/[G,G]| = p^n,
\]
it suffices to show that the kernel of the restriction, given by
\[
\ker(\pi|_H) = H \cap [G,G],
\]
is trivial.

Notice that \( H \) is a \( p \)-group and \( [G,G] \) is a \( q \)-group (since its order is \( q^2 \)). Because \( p \) and \( q \) are distinct primes, the intersection 
\[
H \cap [G,G]
\]
must be trivial:
\[
H \cap [G,G] = \{e\}.
\]
Hence, the restriction 
\[
\pi|_H: H \to G/[G,G]
\]
is an injective homomorphism between two groups of the same finite order. It follows that
\[
H \cong G/[G,G].
\]
Since \( G/[G,G] \) is abelian, we conclude that
\[
H \text{ is abelian}.
\]

### Conclusion

We have shown that the unique Sylow \( p \)-subgroup \( H \) of \( G \) is normal and, by the above argument, is abelian. This completes the proof that there exists an abelian and normal subgroup \( H \) of \( G \) of order \( p^n \).
```