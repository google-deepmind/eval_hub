

To prove that the polynomial \( P(x) = a_nx^n + \ldots + a_1x + a_0 \) with integer coefficients has no rational roots under the given conditions, we proceed as follows:

**Given Conditions:**
1. \( a_n \) is a power of 5.
2. \( a_0 \) is a power of 3.
3. \( P(-1) \) is odd.

**Rational Root Theorem:** Any rational root \( \frac{p}{q} \) (in lowest terms) must satisfy \( p \mid a_0 \) and \( q \mid a_n \). Thus, possible roots are \( \pm \frac{3^k}{5^m} \), where \( k, m \geq 0 \).

### Key Steps:

1. **Parity Analysis of \( P(-1) \):**
   - \( P(-1) = a_n(-1)^n + a_{n-1}(-1)^{n-1} + \ldots + a_1(-1) + a_0 \).
   - Modulo 2, \( (-1)^i \equiv 1 \), so \( P(-1) \equiv a_n + a_{n-1} + \ldots + a_1 + a_0 \mod 2 \).
   - Since \( P(-1) \) is odd, this sum is \( \equiv 1 \mod 2 \).

2. **Contradiction via Rational Root Assumption:**
   - Assume \( \frac{p}{q} \) (in lowest terms) is a root. Then:
     \[
     a_n p^n + a_{n-1} p^{n-1}q + \ldots + a_1 p q^{n-1} + a_0 q^n = 0.
     \]
   - Modulo 2:
     - \( a_n, a_0 \) are odd (powers of 5 and 3, respectively).
     - \( p, q \) are odd (since \( p \) divides \( 3^k \), \( q \) divides \( 5^m \), both odd).
     - Simplifying:
       \[
       1 + \sum_{i=1}^{n-1} a_i + 1 \equiv 0 \mod 2 \implies \sum_{i=1}^{n-1} a_i \equiv 0 \mod 2.
       \]
   - From \( P(-1) \equiv 1 \mod 2 \):
     \[
     a_n + a_0 + \sum_{i=1}^{n-1} a_i \equiv 1 \mod 2 \implies 0 + \sum_{i=1}^{n-1} a_i \equiv 1 \mod 2.
     \]
   - Contradiction: \( \sum_{i=1}^{n-1} a_i \equiv 0 \mod 2 \) and \( \sum_{i=1}^{n-1} a_i \equiv 1 \mod 2 \).

Thus, no rational root exists for \( P(x) \).

```markdown
**Proof:**

Assume for contradiction that \( P(x) \) has a rational root \( \frac{p}{q} \) in lowest terms, where \( p \mid a_0 \) and \( q \mid a_n \). By the given conditions, \( p = \pm 3^k \) and \( q = 5^m \). Substituting \( \frac{p}{q} \) into \( P(x) \) and clearing denominators gives:

\[
a_n p^n + a_{n-1} p^{n-1}q + \ldots + a_1 p q^{n-1} + a_0 q^n = 0. \tag{1}
\]

**Modulo 2 Analysis:**
- \( a_n, a_0 \) are odd (powers of 5 and 3).
- \( p, q \) are odd (as \( 3^k, 5^m \) are odd).
- Each term \( a_i p^i q^{n-i} \equiv a_i \mod 2 \).

From Equation (1):
\[
\underbrace{a_n}_{1} + \underbrace{a_{n-1}}_{?} + \ldots + \underbrace{a_1}_{?} + \underbrace{a_0}_{1} \equiv 0 \mod 2.
\]
\[
1 + \sum_{i=1}^{n-1} a_i + 1 \equiv 0 \mod 2 \implies \sum_{i=1}^{n-1} a_i \equiv 0 \mod 2. \tag{2}
\]

From \( P(-1) \equiv 1 \mod 2 \):
\[
a_n + a_0 + \sum_{i=1}^{n-1} a_i \equiv 1 \mod 2 \implies \sum_{i=1}^{n-1} a_i \equiv 1 \mod 2. \tag{3}
\]

Equations (2) and (3) yield \( 0 \equiv 1 \mod 2 \), a contradiction. Hence, \( P(x) \) has no rational roots. ∎
```