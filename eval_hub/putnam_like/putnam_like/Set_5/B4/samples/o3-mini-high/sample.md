```markdown
We wish to show that for every \(a,b\in R\) there exists an element \(d\in R\) with
\[
aba+bab = d^3.
\]
The proof splits naturally into two cases.

---

### Case 1. When \(a=b\)

If \(a=b\) then
\[
aba+bab = a^3+a^3 = 2a^3.
\]
Since the hypothesis (1) tells us that for any two elements of \(R\) the sum of their cubes is itself a cube, there exists some \(d\in R\) such that
\[
a^3+a^3 = d^3.
\]
Thus, the conclusion holds in this case.

---

### Case 2. When \(a\neq b\)

In this case we shall use both given properties.

1. **Using the second property.**  
   By hypothesis (2), for any two distinct elements \(a\) and \(b\) we have
   \[
   a^2b=-ba^2.
   \]
   A similar argument (by interchanging \(a\) and \(b\)) shows that
   \[
   ab^2=-b^2a.
   \]

2. **Expanding \((a+b)^3\).**  
   In any ring (even if not commutative) the cube of a sum expands as
   \[
   (a+b)^3 = a^3 + a^2b + aba + ab^2 + ba^2 + bab + b^2a + b^3.
   \]
   Group the terms as follows:
   \[
   (a+b)^3 = \bigl(a^3+b^3\bigr) +
   \bigl(a^2b+ba^2\bigr) +
   \bigl(ab^2+b^2a\bigr) + (aba+bab).
   \]
   By the relations obtained above,
   \[
   a^2b+ba^2 = 0 \quad \text{and} \quad ab^2+b^2a=0.
   \]
   Hence, the expansion simplifies to
   \[
   (a+b)^3 = a^3+b^3+ (aba+bab).
   \]
   Rearranging gives the identity
   \[
   aba+bab = (a+b)^3 - a^3 - b^3.
   \]

3. **Expressing \(aba+bab\) as a cube.**  
   Notice that
   \[
   (a+b)^3 - a^3 - b^3 = (a+b)^3 + \Bigl(-a^3-b^3\Bigr).
   \]
   It is a standard fact in any ring that
   \[
   (-x)^3 = -x^3
   \]
   (since \((-x)^3=(-1)^3x^3=-x^3\)). Thus the expression on the right is the sum of two cubes.  
   Now, hypothesis (1) tells us that for any two elements of \(R\) (here, \((a+b)\) and an element whose cube is \(-a^3-b^3\)) the sum of their cubes is itself a cube. Therefore, there exists some \(d\in R\) such that
   \[
   (a+b)^3 + \Bigl(-a^3-b^3\Bigr) = d^3.
   \]
   That is,
   \[
   aba+bab = d^3.
   \]

---

### Conclusion

In either case—whether \(a=b\) or \(a\neq b\)—we have demonstrated the existence of an element \(d\in R\) such that
\[
aba+bab = d^3.
\]
This completes the proof.

\(\Box\)
```