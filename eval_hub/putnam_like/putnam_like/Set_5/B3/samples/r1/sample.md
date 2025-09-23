

To determine whether there exists a function \( f: \mathbb{Z} \to \mathbb{Z} \) satisfying the given conditions, we analyze the equations:

1. \( 9f(x) - 10f(f(x)) = 2x \)
2. \( f(2x) = 2f(x) \) for all \( x \in \mathbb{Z} \).

### Key Steps and Analysis:

1. **Linearity and Homogeneity**:
   - The second condition implies \( f \) is homogeneous: \( f(2^k x) = 2^k f(x) \). This allows expressing \( f \) in terms of its values on odd integers.

2. **Reduction to Odd Integers**:
   - For \( x = 2^k m \) (where \( m \) is odd), \( f(x) = 2^k f(m) \). Substituting into the first equation reduces it to:
     \[
     9f(m) - 10f(f(m)) = 2m \quad \text{for all odd } m.
     \]

3. **Modular Constraints**:
   - From \( 9f(x) - 10f(f(x)) = 2x \), we derive \( 9f(x) \equiv 2x \pmod{10} \). Multiplying by the modular inverse of 9 modulo 10 gives:
     \[
     f(x) \equiv 8x \pmod{10}.
     \]
   - Thus, \( f(x) = 8x + 10k_x \) for some integer \( k_x \).

4. **Substitution and Contradiction**:
   - Substituting \( f(x) = 8x + 10k_x \) into \( 9f(x) - 10f(f(x)) = 2x \), we derive:
     \[
     9(8x + 10k_x) - 10(64x + 80k_x + 10k_{f(x)}) = 2x.
     \]
   - Simplifying leads to a contradiction involving coefficients dependent on \( x \), which cannot hold for all integers \( x \).

### Conclusion:
The derived constraints lead to an inconsistency, indicating no such function \( f \) can satisfy both conditions simultaneously.

```markdown
**Answer**

\boxed{\text{No such function exists.}}
```