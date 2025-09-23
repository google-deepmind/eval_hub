```markdown
We want to show that if one starts with
\[
(1, 2, \ldots, n),
\]
and in each move replaces every two consecutive numbers \(x_i\) and \(x_{i+1}\) by their geometric mean
\[
\sqrt{x_i x_{i+1}},
\]
then after \(n-1\) such moves the only remaining number – which we call the result – is strictly less than
\[
\frac{n+1}{2}.
\]

A key observation is that for any two positive numbers \(x\) and \(y\) the well-known inequality (the Arithmetic Mean–Geometric Mean inequality) holds:
\[
\sqrt{xy} \le \frac{x+y}{2},
\]
with equality if and only if \(x=y\). In our situation the numbers are all distinct (at least at the start), so the inequality is strict:
\[
\sqrt{xy} < \frac{x+y}{2}.
\]

We now formalize our idea by proving a stronger statement by induction.

Define the sequence after \(k\) moves as
\[
\bigl(a^{(k)}_1, a^{(k)}_2, \dots, a^{(k)}_{n-k}\bigr).
\]
Thus, the initial sequence is
\[
a^{(0)}_i = i\quad \text{for } i=1,2,\ldots,n.
\]
Our claim is that for each \(k=1,2,\dots,n-1\) and for each appropriate index \(i\) we have
\[
a^{(k)}_i < \frac{a^{(0)}_i + a^{(0)}_{i+k}}{2} = \frac{i + (i+k)}{2}.
\]

──────────────────────────────
Base Case (\(k=1\)):

For \(i=1,\ldots,n-1\),
\[
a^{(1)}_i = \sqrt{a^{(0)}_i \, a^{(0)}_{i+1}} = \sqrt{i (i+1)}.
\]
By the AM–GM inequality,
\[
\sqrt{i (i+1)} < \frac{i + (i+1)}{2} = \frac{2i+1}{2}.
\]
Thus, the claim holds for \(k=1\).

──────────────────────────────
Inductive Step:

Assume that for some \(k\) with \(1\le k < n-1\) the claim is true; that is, for all possible indices,
\[
a^{(k)}_i < \frac{a^{(0)}_i + a^{(0)}_{i+k}}{2} = \frac{i + (i+k)}{2}.
\]
Now, consider the next move. By the transformation rule,
\[
a^{(k+1)}_i = \sqrt{a^{(k)}_i \, a^{(k)}_{i+1}}.
\]
Using the inductive hypothesis, we obtain:
\[
a^{(k)}_i < \frac{i + (i+k)}{2}, \quad\text{and}\quad a^{(k)}_{i+1} < \frac{(i+1) + (i+k+1)}{2} = \frac{2i+k+2}{2}.
\]
Thus,
\[
a^{(k+1)}_i < \sqrt{ \frac{i + (i+k)}{2} \cdot \frac{(i+1) + (i+k+1)}{2} } = \frac{1}{2}\sqrt{(2i+k)(2i+k+2)}.
\]
It is now sufficient to show that
\[
\frac{1}{2}\sqrt{(2i+k)(2i+k+2)} \le \frac{i + (i+k+1)}{2} = \frac{2i+k+1}{2}.
\]
Multiplying both sides by 2 and then squaring, we need to verify
\[
(2i+k)(2i+k+2) \le (2i+k+1)^2.
\]
Let us expand both sides:

Left-hand side (LHS):
\[
(2i+k)(2i+k+2) = (2i+k)^2 + 2(2i+k).
\]
Right-hand side (RHS):
\[
(2i+k+1)^2 = (2i+k)^2 + 2(2i+k) + 1.
\]
Thus,
\[
(2i+k)(2i+k+2) = (2i+k+1)^2 - 1 < (2i+k+1)^2.
\]
Taking square roots (and noting all expressions are positive) gives:
\[
\sqrt{(2i+k)(2i+k+2)} < 2i+k+1,
\]
which shows that
\[
a^{(k+1)}_i < \frac{2i+k+1}{2}.
\]
This completes the inductive step.

──────────────────────────────
Conclusion:

After \(n-1\) moves the sequence reduces to a single number:
\[
\text{result} = a^{(n-1)}_1 < \frac{a^{(0)}_1 + a^{(0)}_n}{2} = \frac{1+n}{2}.
\]
Thus, the final result is strictly less than \(\frac{n+1}{2}\).

──────────────────────────────
Summary:

By applying the AM–GM inequality at each step and using induction to compare the terms of the evolving sequence with the averages of corresponding initial terms, we have shown that starting with \((1,2,\ldots, n)\), the final number obtained after \(n-1\) steps is always smaller than \(\frac{n+1}{2}\).
```