

To solve the problem, we analyze the structure of \( G \) using properties of the commutator subgroup and Sylow theorems.

**Step-by-Step Explanation and Proof:**

1. **Commutator Subgroup and Abelian Quotient:**
   - The commutator subgroup \( [G, G] \) is normal in \( G \), and \( G/[G, G] \) is abelian.
   - Given \( |[G, G]| = q^2 \), the quotient \( G/[G, G] \) has order \( |G| / |[G, G]| = p^n \), hence is an abelian group of order \( p^n \).

2. **Sylow Subgroups:**
   - \( G \) has Sylow \( p \)-subgroups of order \( p^n \) and Sylow \( q \)-subgroups of order \( q^2 \).
   - Since \( [G, G] \) is a Sylow \( q \)-subgroup (order \( q^2 \)) and is normal (as commutator subgroups are always normal), there is exactly one Sylow \( q \)-subgroup, i.e., \( n_q = 1 \).

3. **Schur-Zassenhaus Theorem:**
   - \( [G, G] \) is a normal Hall subgroup (order \( q^2 \), coprime to \( p^n \)). By the Schur-Zassenhaus theorem, there exists a complement \( H \leq G \) such that \( G = [G, G] \rtimes H \), where \( |H| = p^n \).

4. **Trivial Action and Direct Product:**
   - The automorphism group \( \text{Aut}([G, G]) \) has order \( (q^2 - 1)(q - 1)q \), which is coprime to \( p \) (since \( p > q \)).
   - The homomorphism \( H \to \text{Aut}([G, G]) \) defining the semidirect product must be trivial. Thus, \( G \cong [G, G] \times H \), a direct product.

5. **Normality and Abelian Property of \( H \):**
   - \( H \) is a direct factor of \( G \), hence normal.
   - \( H \cong G/[G, G] \), which is abelian (as \( G/[G, G] \) is the abelianization of \( G \)). Therefore, \( H \) is abelian.

**Conclusion:**
There exists a subgroup \( H \) of \( G \) of order \( p^n \) that is both abelian and normal. The subgroup \( H \) arises as the complement guaranteed by the Schur-Zassenhaus theorem and is normal due to the trivial action in the semidirect product, which reduces to a direct product.

```markdown
**Final Answer**

\boxed{H \text{ is an abelian normal subgroup of } G \text{ of order } p^n}
```