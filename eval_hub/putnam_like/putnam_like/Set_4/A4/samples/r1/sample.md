

To show that any prime divisor \( p > 2 \) of \( a^{2^k} + b^{2^k} \) (with \( \gcd(a,b)=1 \)) is of the form \( p = 2^d m + 1 \), where \( d \geq k+1 \) and \( m \) is an odd positive integer, follow these steps:

**Step 1:** Since \( p \) divides \( a^{2^k} + b^{2^k} \), we have:
\[
a^{2^k} \equiv -b^{2^k} \pmod{p}.
\]

**Step 2:** Let \( c = a \cdot b^{-1} \pmod{p} \), which is well-defined because \( p \nmid b \) (as \( \gcd(a,b)=1 \)). Then:
\[
c^{2^k} \equiv -1 \pmod{p}.
\]

**Step 3:** Squaring both sides gives:
\[
c^{2^{k+1}} \equiv 1 \pmod{p}.
\]
The multiplicative order of \( c \) modulo \( p \) divides \( 2^{k+1} \). Since \( c^{2^k} \equiv -1 \neq 1 \pmod{p} \), the order of \( c \) is exactly \( 2^{k+1} \).

**Step 4:** By Fermat’s Little Theorem, \( c^{p-1} \equiv 1 \pmod{p} \). The order \( 2^{k+1} \) must divide \( p-1 \). Thus:
\[
2^{k+1} \mid (p-1).
\]

**Step 5:** Write \( p-1 = 2^d m \), where \( m \) is odd. Since \( 2^{k+1} \mid 2^d m \), and \( m \) is odd, it follows that \( d \geq k+1 \).

**Conclusion:** Therefore, \( p = 2^d m + 1 \), where \( d \geq k+1 \) and \( m \) is odd. This completes the proof.

```markdown
**Proof:**

Let \( p > 2 \) be a prime divisor of \( a^{2^k} + b^{2^k} \). Then:
1. \( a^{2^k} \equiv -b^{2^k} \pmod{p} \).
2. Let \( c = a \cdot b^{-1} \pmod{p} \). Then \( c^{2^k} \equiv -1 \pmod{p} \).
3. Squaring both sides: \( c^{2^{k+1}} \equiv 1 \pmod{p} \). The order of \( c \) modulo \( p \) is \( 2^{k+1} \).
4. By Fermat’s Little Theorem, \( 2^{k+1} \mid (p-1) \), so \( p \equiv 1 \pmod{2^{k+1}} \).
5. Write \( p-1 = 2^d m \) with \( m \) odd. Since \( 2^{k+1} \mid 2^d m \), we have \( d \geq k+1 \).

Thus, \( p = 2^d m + 1 \) with \( d \geq k+1 \) and \( m \) odd.
```