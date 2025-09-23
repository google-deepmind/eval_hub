```markdown
We begin by noting the composition of each box. For any positive integer \( m \), each box contains:

- \( 1 \) ball numbered \( 1 \),
- \( 2 \) balls numbered \( 2 \),
- \(\,\dots\,\)
- \( m \) balls numbered \( m \).

Thus, the total number of balls in a box is
\[
1 + 2 + \cdots + m = \frac{m(m+1)}{2},
\]
and the total of the numbers written on these balls is
\[
1^2 + 2^2 + \cdots + m^2 = \frac{m(m+1)(2m+1)}{6}.
\]
So if one draws a ball uniformly at random from a fresh box, the expected number on the ball is:
\[
\frac{\frac{m(m+1)(2m+1)}{6}}{\frac{m(m+1)}{2}} = \frac{2m+1}{3}.
\]

Now, consider the process of transferring balls:

1. A ball is drawn from the first box; its expected number is \(\frac{2m+1}{3}\).
2. This ball is added to the second box, whose original contents has the expected number \(\frac{2m+1}{3}\). When drawing from the augmented second box (which now contains one extra ball), the new expected value remains a weighted average of the original and the added ball. A short calculation shows that this expected value is also \(\frac{2m+1}{3}\).
3. The same reasoning applies inductively for each subsequent box.

Thus, the final ball drawn from the \( n \)th box also has the expected value
\[
\frac{2m+1}{3}.
\]

For this expected value to be an integer, the numerator \(2m+1\) must be divisible by \(3\). In other words, we require:
\[
\frac{2m+1}{3} \in \mathbb{Z} \quad \Longleftrightarrow \quad 2m+1 \equiv 0 \pmod{3}.
\]

To solve this congruence:
\[
2m + 1 \equiv 0 \pmod{3} \quad \Longrightarrow \quad 2m \equiv -1 \pmod{3}.
\]
Since \(-1 \equiv 2 \pmod{3}\), we have:
\[
2m \equiv 2 \pmod{3}.
\]
Multiplying both sides by the multiplicative inverse of \(2\) modulo \(3\) (note that \(2 \times 2 \equiv 1 \pmod{3}\)), we obtain:
\[
m \equiv 1 \pmod{3}.
\]

Thus, the expected value \(\frac{2m+1}{3}\) is an integer if and only if:
\[
m = 3k + 1 \quad \text{for some integer } k \ge 0.
\]

In summary, the final answer is:

The expected value of the written number is an integer if and only if \( m \equiv 1 \pmod{3} \), i.e. when \( m = 1, 4, 7, 10, \dots \).
```