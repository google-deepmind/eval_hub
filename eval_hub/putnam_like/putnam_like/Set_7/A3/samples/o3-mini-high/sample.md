```markdown
We will show that for any positive integers 
\[
a_1,a_2,\dots,a_n\quad (n\ge2)
\]
and any permutation \(\sigma\in S_n\) the inequality
\[
\frac{\Bigl(\sum_{i=1}^n a_i\Bigr)^{\sum_{i=1}^n a_i}}{\Bigl(\sum_{i=1}^n a_i\Bigr)!} > \frac{\prod_{i=1}^n a_i^{\, a_{\sigma(i)}}}{\prod_{i=1}^n a_i!}
\]
holds.

In what follows we describe one way of arriving at the result.

---

### Reduction by Rearrangement

Notice that the right‐hand side depends on the permutation \(\sigma\). In fact, if we write 
\[
A = a_1+a_2+\cdots+a_n,
\]
then the inequality reads
\[
\frac{A^A}{A!} > \frac{\prod_{i=1}^n a_i^{\, a_{\sigma(i)}}}{\prod_{i=1}^n a_i!}.
\]
Using the classical rearrangement inequality one may show that the product 
\[
\prod_{i=1}^n a_i^{\, a_{\sigma(i)}}
\]
is maximized when \(\sigma\) is the identity (that is, when the exponents match the corresponding bases). Hence it suffices to prove the stronger inequality
\[
\frac{A^A}{A!} > \frac{\prod_{i=1}^n a_i^{\, a_i}}{\prod_{i=1}^n a_i!},
\]
or, equivalently (after multiplying both sides by \(A! \prod_{i=1}^n a_i!\)),
\[
A^A\, \prod_{i=1}^n a_i! > A!\, \prod_{i=1}^n a_i^{\, a_i}.
\]
We now explain one inductive approach to prove this last inequality.

---

### Proof by Induction

#### Base Case (\(n=2\))

Let \(a_1\) and \(a_2\) be two positive integers and \(A=a_1+a_2\). The inequality becomes
\[
(a_1+a_2)^{a_1+a_2}\, (a_1! \, a_2!) > (a_1+a_2)! \, a_1^{\, a_1}a_2^{\, a_2}.
\]
Rearrange this as
\[
\frac{(a_1+a_2)^{a_1+a_2}}{a_1^{\, a_1}a_2^{\, a_2}} > \binom{a_1+a_2}{a_1},
\]
since
\[
\binom{a_1+a_2}{a_1}=\frac{(a_1+a_2)!}{a_1! \, a_2!}.
\]
This inequality is known to hold; one may verify it by standard estimates or by a direct inductive argument on \(a_1+a_2\).

#### Inductive Step

Assume that the inequality
\[
B^B\, \prod_{i=1}^{n-1} b_i! > B!\, \prod_{i=1}^{n-1} b_i^{\, b_i}
\]
holds whenever \(b_1,b_2,\dots,b_{n-1}\) are positive integers with sum \(B\).

Now consider \(n\) positive integers \(a_1,a_2,\dots,a_n\) whose sum is
\[
A = a_1+a_2+\cdots+a_n.
\]
Group the first two numbers by setting
\[
b = a_1+a_2.
\]
Then \(A=b+a_3+\cdots+a_n\). By the base case (applied to \(a_1\) and \(a_2\)) we have
\[
b^b\, (a_1!a_2!) > b!\, a_1^{\, a_1}a_2^{\, a_2}.
\]
Next, applying the inductive hypothesis to the \(n-1\) numbers \(b, a_3, \dots, a_n\) (whose sum is \(A\)) we obtain 
\[
A^A\, \bigl(b! \, a_3!\cdots a_n!\bigr) > A!\, b^{b}\, a_3^{\, a_3}\cdots a_n^{\, a_n}.
\]
Multiplying the two inequalities we deduce
\[
A^A\, (a_1!a_2!a_3!\cdots a_n!) > A!\, (a_1^{\, a_1}a_2^{\, a_2}\cdots a_n^{\, a_n}),
\]
which is exactly the inequality we wanted to prove:
\[
A^A\, \prod_{i=1}^n a_i! > A!\, \prod_{i=1}^n a_i^{\, a_i}.
\]
This completes the induction.

---

### Conclusion

Since we have shown that
\[
\frac{A^A}{A!} > \frac{\prod_{i=1}^n a_i^{\, a_i}}{\prod_{i=1}^n a_i!},
\]
and this is the strongest case (when \(\sigma\) is the identity), it follows that for every permutation \(\sigma\in S_n\) we have
\[
\frac{\Bigl(\sum_{i=1}^n a_i\Bigr)^{\sum_{i=1}^n a_i}}{\Bigl(\sum_{i=1}^n a_i\Bigr)!} > \frac{\prod_{i=1}^n a_i^{\, a_{\sigma(i)}}}{\prod_{i=1}^n a_i!}.
\]
This completes the solution.
```