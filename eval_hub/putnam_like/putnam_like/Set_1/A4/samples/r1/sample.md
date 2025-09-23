

To prove that the group \( G = \langle x, y : x^n = e, y^2 = e, xyxy = e \rangle \) is non-abelian of order \( 2n \), we proceed as follows:

### Step 1: Rewriting the Relation \( xyxy = e \)
The relation \( xyxy = e \) can be rearranged as:
\[
xy = y^{-1}x^{-1} = yx^{-1} \quad (\text{since } y^2 = e \implies y^{-1} = y).
\]
Thus, we have:
\[
xy = yx^{n-1} \quad (\text{as } x^n = e \implies x^{-1} = x^{n-1}).
\]

### Step 2: Normal Form of Elements
Using the relation \( xy = yx^{n-1} \), any product of \( x \) and \( y \) can be rewritten to move all \( y \)-terms to the right. Specifically:
- If \( y \) precedes \( x \), we replace \( yx \) with \( x^{n-1}y \).
- Repeating this process reduces any word to the form \( x^k y^m \), where \( 0 \leq k < n \) and \( m \in \{0, 1\} \).

Thus, the elements of \( G \) are:
\[
G = \{ e, x, x^2, \dots, x^{n-1}, y, xy, x^2y, \dots, x^{n-1}y \}.
\]

### Step 3: Distinctness of Elements
Assume \( x^k y^m = x^l y^p \) for some \( 0 \leq k, l < n \) and \( m, p \in \{0, 1\} \). Then:
- If \( m = p \), then \( x^k = x^l \implies k = l \).
- If \( m \neq p \), assume \( m = 1 \), \( p = 0 \). Then \( x^k y = x^l \). Multiplying both sides by \( y \):
  \[
  x^k = x^l y \implies x^{k - l} = y.
  \]
  But \( y \notin \langle x \rangle \) (since \( y \) has order 2 and \( \langle x \rangle \) has order \( n \geq 3 \)), so no such equality exists. Hence, all elements are distinct, implying \( |G| = 2n \).

### Step 4: Non-Abelian Property
Suppose \( G \) is abelian. Then \( xy = yx \). From the relation \( xy = yx^{n-1} \), this implies:
\[
yx = yx^{n-1} \implies x = x^{n-1} \implies x^2 = e.
\]
But \( x^n = e \) and \( n \geq 3 \), so \( x^2 \neq e \). This contradiction shows \( G \) is non-abelian.

### Conclusion
The group \( G \) has exactly \( 2n \) distinct elements and is non-abelian. Hence, it is a non-abelian group of order \( 2n \).

```markdown
**Proof:**

1. **Relations imply conjugation:** From \( xyxy = e \), we derive \( xy = yx^{n-1} \).

2. **Normal form of elements:** Every element in \( G \) can be written uniquely as \( x^k y^m \) where \( 0 \leq k < n \) and \( m \in \{0, 1\} \). This gives \( 2n \) distinct elements.

3. **Non-abelian:** Assuming \( xy = yx \) leads to \( x^2 = e \), contradicting \( \text{ord}(x) = n \geq 3 \).

Thus, \( G \) is a non-abelian group of order \( 2n \). ∎
```